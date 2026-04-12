import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time
from datetime import datetime
import pytz
import os
from joblib import dump, load
from disease_info import get_disease_info   # ← our knowledge base module

# ─────────────────────────────────────────────────────────
# 1. PAGE CONFIG
# ─────────────────────────────────────────────────────────
st.set_page_config(page_title="MedAI Predictor", page_icon="🩺", layout="wide")

# ─────────────────────────────────────────────────────────
# 2. CSS
# ─────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

/* ── BACKGROUND ── */
body, .stApp {
    font-family: 'DM Sans', sans-serif;
    background: #04080f;
    color: #c9daea;
}
.stApp::before {
    content: '';
    position: fixed; inset: 0; pointer-events: none; z-index: 0;
    background:
        radial-gradient(ellipse 70% 50% at 10% 15%, rgba(6,182,212,0.09) 0%, transparent 55%),
        radial-gradient(ellipse 50% 40% at 90% 85%, rgba(99,102,241,0.08) 0%, transparent 55%),
        radial-gradient(ellipse 90% 70% at 50% 50%, rgba(0,20,50,0.6) 0%, transparent 80%);
}
.stApp::after {
    content: '';
    position: fixed; inset: 0; pointer-events: none; z-index: 0;
    background-image:
        linear-gradient(rgba(6,182,212,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(6,182,212,0.03) 1px, transparent 1px);
    background-size: 60px 60px;
}
.stApp > * { position: relative; z-index: 1; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1.5rem 2.5rem 4rem; max-width: 1280px; }

/* ── TYPE ── */
h1 {
    font-family: 'Syne', sans-serif;
    font-weight: 800; font-size: clamp(1.8rem, 4vw, 3rem);
    color: #f0f9ff; text-align: center; letter-spacing: -1.5px; line-height: 1.1;
}
h2, h3 { font-family: 'Syne', sans-serif; color: #bdd8f0; }

/* ── PILL BADGE ── */
.pill-badge {
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(6,182,212,0.07);
    border: 1px solid rgba(6,182,212,0.22);
    border-radius: 100px; padding: 5px 18px;
    font-size: 0.72rem; font-weight: 600; color: #22d3ee;
    letter-spacing: 3px; text-transform: uppercase;
}
.pill-badge::before {
    content: ''; width: 7px; height: 7px; border-radius: 50%;
    background: #22d3ee;
    box-shadow: 0 0 6px #22d3ee, 0 0 14px #22d3ee;
    animation: blink 2.2s ease-in-out infinite;
}
@keyframes blink {
    0%, 100% { opacity: 1; } 50% { opacity: 0.3; }
}

/* ── LOGIN CARD ── */
.login-card {
    background: rgba(6,14,28,0.82);
    border: 1px solid rgba(6,182,212,0.15);
    border-radius: 28px; padding: 2.8rem 3rem;
    backdrop-filter: blur(24px);
    box-shadow: 0 0 0 1px rgba(6,182,212,0.04),
                0 40px 80px rgba(0,0,0,0.6),
                inset 0 1px 0 rgba(255,255,255,0.05);
    animation: float 7s ease-in-out infinite;
}
@keyframes float {
    0%, 100% { transform: translateY(0); }
    50%       { transform: translateY(-8px); }
}

/* ── PATIENT BAR ── */
.patient-bar {
    display: flex; align-items: center; gap: 20px; flex-wrap: wrap;
    background: rgba(6,182,212,0.04);
    border: 1px solid rgba(6,182,212,0.1);
    border-radius: 14px; padding: 12px 22px; margin-bottom: 20px;
    font-size: 0.88rem;
}
.patient-bar b   { color: #64748b; font-weight: 400; margin-right: 3px; }
.patient-bar span { color: #22d3ee; font-weight: 600; }

/* ── MAIN PRED CARD ── */
.pred-hero {
    position: relative; overflow: hidden;
    background: linear-gradient(135deg, rgba(6,20,50,0.9) 0%, rgba(2,8,20,0.95) 100%);
    border: 1px solid rgba(6,182,212,0.18);
    border-radius: 28px; padding: 3rem 2.5rem 2.5rem;
    text-align: center; margin: 20px 0 28px;
    transition: all 0.5s ease;
}
.pred-hero::before {
    content: '';
    position: absolute; top: -100px; left: 50%; transform: translateX(-50%);
    width: 500px; height: 300px;
    background: radial-gradient(ellipse, rgba(6,182,212,0.1) 0%, transparent 70%);
    pointer-events: none;
}
.pred-hero:hover {
    border-color: rgba(6,182,212,0.5);
    box-shadow: 0 0 80px rgba(6,182,212,0.12),
                0 0 160px rgba(6,182,212,0.05),
                inset 0 0 60px rgba(6,182,212,0.03);
    transform: translateY(-3px);
}
.pred-hero:hover .pred-name { color: #67e8f9; }
.pred-eyebrow {
    font-size: 0.68rem; letter-spacing: 4px; text-transform: uppercase;
    color: rgba(34,211,238,0.5); font-weight: 600; margin-bottom: 14px;
}
.pred-name {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2rem, 4.5vw, 3.2rem); font-weight: 800;
    color: #f0f9ff; letter-spacing: -1px; margin-bottom: 14px;
    transition: color 0.4s ease;
}
.pred-reason-text {
    font-size: 0.83rem; color: #4a7a9b; font-style: italic; margin-bottom: 18px;
}
.pred-syms {
    font-size: 0.78rem; color: #2a4a68; margin-top: 10px;
}
.conf-pill {
    display: inline-block; padding: 5px 20px;
    background: rgba(6,182,212,0.08); border: 1px solid rgba(6,182,212,0.22);
    border-radius: 100px; font-size: 0.82rem; font-weight: 700; color: #22d3ee;
}

/* ── METRIC TRIO ── */
.metric-card {
    background: rgba(6,14,30,0.75);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 18px; padding: 1.4rem 1.6rem;
    transition: all 0.35s ease;
    height: 100%;
}
.metric-card:hover {
    border-color: rgba(6,182,212,0.28);
    box-shadow: 0 0 24px rgba(6,182,212,0.08), 0 12px 32px rgba(0,0,0,0.35);
    transform: translateY(-3px);
}
.metric-label {
    font-size: 0.68rem; letter-spacing: 2.5px; text-transform: uppercase;
    color: #334e68; font-weight: 700; margin-bottom: 10px;
    display: flex; align-items: center; gap: 6px;
}
.metric-value {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem; font-weight: 700; color: #e0f2fe;
}
.badge-low    { display: inline-block; padding: 4px 14px; border-radius: 100px; font-size: 0.8rem; font-weight: 700; background: rgba(16,185,129,0.12); border: 1px solid rgba(16,185,129,0.3); color: #34d399; }
.badge-medium { display: inline-block; padding: 4px 14px; border-radius: 100px; font-size: 0.8rem; font-weight: 700; background: rgba(245,158,11,0.12); border: 1px solid rgba(245,158,11,0.3); color: #fbbf24; }
.badge-high   { display: inline-block; padding: 4px 14px; border-radius: 100px; font-size: 0.8rem; font-weight: 700; background: rgba(239,68,68,0.12);  border: 1px solid rgba(239,68,68,0.3);  color: #f87171; }

/* ── INFO CARDS ── */
.info-card {
    background: rgba(6,14,30,0.72);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 18px; padding: 1.6rem;
    margin-bottom: 16px; transition: all 0.3s ease; height: 100%;
}
.info-card:hover {
    border-color: rgba(6,182,212,0.2);
    box-shadow: 0 0 22px rgba(6,182,212,0.07);
    transform: translateY(-2px);
}
.info-card-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.72rem; letter-spacing: 2.5px; text-transform: uppercase;
    color: #0891b2; font-weight: 700; margin-bottom: 14px;
    display: flex; align-items: center; gap: 7px;
}
.info-card p, .info-card li {
    color: #7a9ab8; font-size: 0.91rem; line-height: 1.8;
}
.info-card ul { padding-left: 18px; }
.info-card li { margin-bottom: 5px; }
.info-card li::marker { color: #0891b2; }

/* ── DIVIDER LABEL ── */
.divider-label {
    display: flex; align-items: center; gap: 12px;
    margin: 28px 0 18px; color: #1e3a52;
    font-size: 0.68rem; letter-spacing: 3px; text-transform: uppercase; font-weight: 700;
}
.divider-label::before, .divider-label::after {
    content: ''; flex: 1; height: 1px;
    background: linear-gradient(90deg, transparent, rgba(6,182,212,0.18), transparent);
}

/* ── MODEL CARDS ── */
.model-card {
    background: rgba(6,14,30,0.65);
    border: 1px solid rgba(255,255,255,0.04);
    border-radius: 16px; padding: 1.3rem; text-align: center;
    transition: all 0.35s ease;
}
.model-card:hover {
    border-color: rgba(6,182,212,0.3);
    box-shadow: 0 0 22px rgba(6,182,212,0.1);
    transform: translateY(-5px) scale(1.02);
}
.mc-name {
    font-size: 0.72rem; letter-spacing: 1.5px; text-transform: uppercase;
    color: #1d6a8a; font-weight: 700; margin-bottom: 10px;
}
.mc-disease {
    font-family: 'Syne', sans-serif;
    font-size: 1rem; font-weight: 700; color: #bde0f5; margin-bottom: 10px;
}
.mc-conf { font-size: 0.78rem; color: #1d6a8a; margin-bottom: 6px; }
.mc-bar-bg { background: rgba(0,0,0,0.5); border-radius: 10px; height: 5px; overflow: hidden; }
.mc-bar { height: 5px; border-radius: 10px; background: linear-gradient(90deg, #0369a1, #22d3ee); }
.mc-acc { font-size: 0.72rem; color: #0f3a50; margin-top: 8px; }

/* ── BUTTONS ── */
.stButton > button {
    font-family: 'DM Sans', sans-serif; font-weight: 600;
    border-radius: 12px; border: 1px solid rgba(6,182,212,0.18);
    background: rgba(6,182,212,0.06); color: #90c4d8;
    letter-spacing: 0.3px; transition: all 0.3s ease;
}
.stButton > button:hover {
    background: rgba(6,182,212,0.16) !important;
    border-color: rgba(6,182,212,0.5) !important; color: #fff !important;
    box-shadow: 0 0 20px rgba(6,182,212,0.22) !important;
    transform: translateY(-2px);
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #075985, #0891b2) !important;
    border: none !important; color: #fff !important; font-size: 0.95rem;
}
.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #0369a1, #06b6d4) !important;
    box-shadow: 0 0 28px rgba(6,182,212,0.32), 0 6px 18px rgba(0,0,0,0.3) !important;
    transform: translateY(-3px);
}

/* ── INPUTS ── */
[data-testid="stTextInput"] input, [data-testid="stNumberInput"] input {
    background: rgba(4,10,22,0.9) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 10px !important; color: #c8e6f5 !important;
    font-family: 'DM Sans', sans-serif !important;
}
[data-testid="stTextInput"] input:focus, [data-testid="stNumberInput"] input:focus {
    border-color: rgba(6,182,212,0.5) !important;
    box-shadow: 0 0 0 3px rgba(6,182,212,0.1) !important;
}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(4,10,22,0.8); border-radius: 12px; padding: 4px; gap: 4px;
    border: 1px solid rgba(255,255,255,0.05);
}
.stTabs [data-baseweb="tab"] {
    border-radius: 9px; color: #3d6a80; font-weight: 600;
    font-family: 'DM Sans', sans-serif; transition: all 0.3s;
}
.stTabs [aria-selected="true"] {
    background: rgba(6,182,212,0.14) !important;
    color: #22d3ee !important;
    box-shadow: 0 0 14px rgba(6,182,212,0.14) !important;
}

/* ── MULTISELECT TAGS ── */
[data-baseweb="tag"] {
    background: rgba(6,100,140,0.35) !important;
    border: 1px solid rgba(6,182,212,0.28) !important;
    border-radius: 7px !important;
}

/* ── EXPANDER ── */
.streamlit-expanderHeader {
    background: rgba(6,14,30,0.7) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.05) !important;
    color: #3d7a96 !important; font-family: 'DM Sans', sans-serif !important; font-weight: 600 !important;
}
.streamlit-expanderHeader:hover {
    border-color: rgba(6,182,212,0.25) !important;
    box-shadow: 0 0 14px rgba(6,182,212,0.08) !important;
    color: #22d3ee !important;
}

/* ── HR ── */
hr { border: none; height: 1px; background: linear-gradient(90deg, transparent, rgba(6,182,212,0.18), transparent); margin: 2rem 0; }

/* ── DISCLAIMER ── */
.disclaimer {
    background: rgba(160,120,0,0.05); border: 1px solid rgba(250,180,0,0.1);
    border-radius: 12px; padding: 1rem 1.4rem;
    font-size: 0.8rem; color: #607080; line-height: 1.7;
}
.disclaimer strong { color: #d4a520; }

/* ── FOOTER ── */
.footer {
    text-align: center; padding: 2.5rem 0 1rem;
    font-size: 0.75rem; letter-spacing: 1.5px; color: #1e3a52;
}
.footer span { color: #0891b2; }

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #04080f; }
::-webkit-scrollbar-thumb { background: rgba(6,182,212,0.3); border-radius: 3px; }

/* ── ALERTS ── */
[data-testid="stAlert"] {
    background: rgba(6,14,30,0.8) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(250,180,0,0.15) !important;
}

/* ── STATS POPOVER ── */
[data-testid="stPopover"] {
    background: rgba(6,14,30,0.95) !important;
    border: 1px solid rgba(6,182,212,0.15) !important;
    border-radius: 14px !important;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────
# 3. ML SYSTEM INIT
# ─────────────────────────────────────────────────────────
CACHE_FILE = "medai_v3_cache.joblib"

@st.cache_resource(show_spinner="⚕️  Initialising MedAI — loading models…")
def initialize_system():
    if os.path.exists(CACHE_FILE):
        try:
            cached = load(CACHE_FILE)
            if len(cached) == 6:
                cached[5].append("⚡ Loaded from compressed disk cache.")
                return cached
        except Exception:
            pass

    logs = []
    t0 = time.time()
    try:
        df = pd.read_csv("Disease and symptoms dataset.csv", low_memory=False).copy()
        df.columns = (df.columns.str.strip().str.lower()
                      .str.replace(' ', '_').str.replace('[^a-z0-9_]', '', regex=True))

        disease_col = 'disease' if 'disease' in df.columns else df.select_dtypes(include='object').columns[0]
        y_raw = df[disease_col].astype(str).str.strip()
        feat_cols = [c for c in df.columns if c != disease_col]

        X_bin = (df[feat_cols].fillna(0).values > 0).astype(np.int8)
        X_df  = pd.DataFrame(X_bin, columns=feat_cols)

        mask = X_df.sum(axis=1) > 0
        X_df, y_raw = X_df[mask].reset_index(drop=True), y_raw[mask].reset_index(drop=True)

        valid_cls = y_raw.value_counts()[lambda s: s >= 2].index
        m = y_raw.isin(valid_cls)
        X_df, y_raw = X_df[m].reset_index(drop=True), y_raw[m].reset_index(drop=True)

        # Build disease→symptom profile map
        dsm = {}
        for d in y_raw.unique():
            rows = X_df[y_raw == d]
            freq = rows.mean(axis=0)
            dsm[d] = set(freq[freq >= 0.3].index.tolist())

        stratify = y_raw if not (y_raw.value_counts() < 2).any() else None
        X_tr, X_te, y_tr, y_te = train_test_split(
            X_df, y_raw, test_size=0.2, stratify=stratify, random_state=42)

        models = {
            "Decision Tree": DecisionTreeClassifier(max_depth=22, min_samples_split=8, min_samples_leaf=4, random_state=42),
            "Random Forest": RandomForestClassifier(n_estimators=30, max_depth=22, min_samples_split=8, min_samples_leaf=4, n_jobs=-1, random_state=42),
            "Naïve Bayes":   GaussianNB()
        }
        accs = {}
        for name, mdl in models.items():
            mdl.fit(X_tr, y_tr)
            accs[name] = accuracy_score(y_te, mdl.predict(X_te))

        logs.append(
            f"✅ Training complete in {time.time()-t0:.1f}s | "
            f"DT: {accs['Decision Tree']:.2%}  RF: {accs['Random Forest']:.2%}  NB: {accs['Naïve Bayes']:.2%}"
        )

        data = (models, accs, feat_cols, list(y_raw.unique()), dsm, logs)
        dump(data, CACHE_FILE, compress=3)
        return data

    except FileNotFoundError:
        st.error("❌  'Disease and symptoms dataset.csv' not found."); st.stop()
    except Exception as e:
        st.error(f"❌  Init error: {e}"); st.stop()


# ─────────────────────────────────────────────────────────
# 4. ENSEMBLE ALGORITHM
# ─────────────────────────────────────────────────────────
def _overlap(disease, sel_syms, dsm):
    profile = dsm.get(disease, set())
    if not profile: return 0.0
    sel = set(sel_syms)
    u = profile | sel
    return len(profile & sel) / len(u) if u else 0.0


def smart_ensemble(iv, sel_syms, models, accs, dsm):
    candidates, per_model, per_probs = {}, {}, {}

    for name, mdl in models.items():
        w = accs.get(name, 0.5)
        pred = mdl.predict(iv)[0].strip()
        per_model[name] = pred

        if hasattr(mdl, "predict_proba"):
            proba = mdl.predict_proba(iv)[0]
            cls   = mdl.classes_
            for idx in np.argsort(proba)[::-1][:3]:
                d = cls[idx].strip()
                candidates[d] = candidates.get(d, 0.0) + proba[idx] * w
            conf = float(proba[np.where(cls == pred)[0][0]]) if pred in cls else float(np.max(proba))
        else:
            candidates[pred] = candidates.get(pred, 0.0) + w
            conf = 1.0
        per_probs[name] = conf

    ws = sum(accs.values())
    scores = {
        d: 0.4*(s/ws) + 0.6*_overlap(d, sel_syms, dsm)
        for d, s in candidates.items()
    }
    if not scores:
        return "Inconclusive", "No patterns found", per_model, per_probs, 0.0

    best = max(scores, key=scores.get)
    agr  = sum(1 for p in per_model.values() if p == best)
    ov   = _overlap(best, sel_syms, dsm) * 100

    if agr == 3:
        reason = "Unanimous agreement across all 3 models"
    elif agr == 2:
        reason = f"Majority consensus (2/3 models) · {ov:.0f}% symptom match"
    else:
        reason = f"Symptom-weighted selection · {ov:.0f}% symptom match"

    return best, reason, per_model, per_probs, min(scores[best] * 1.5, 1.0)


# ─────────────────────────────────────────────────────────
# 5. REPORT GENERATOR
# ─────────────────────────────────────────────────────────
def generate_report(ai: dict) -> str:
    p  = st.session_state.patient
    d  = st.session_state.pred
    ts = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S %Z")

    def fl(s):
        return "\n".join(f"  • {x.strip()}" for x in str(s).split(';') if x.strip())

    return f"""
╔══════════════════════════════════════════════════════════════╗
║          MedAI — AI-GENERATED CLINICAL PREDICTION REPORT     ║
╚══════════════════════════════════════════════════════════════╝
  Generated   : {ts}

── PATIENT DETAILS ──────────────────────────────────────────────
  Name        : {p.get('name','')} {p.get('surname','')}
  Age         : {p.get('age','N/A')}  |  Gender: {p.get('gender','N/A')}

── PREDICTION ────────────────────────────────────────────────────
  Condition   : {d.get('disease','N/A')}
  Confidence  : {d.get('confidence',0)*100:.1f}%
  Risk Level  : {ai.get('risk_level','N/A')}
  Specialist  : {ai.get('specialist','General Physician')}
  Recovery    : {ai.get('recovery_time','N/A')}
  Symptoms    : {d.get('symptoms','N/A')}

── OVERVIEW ──────────────────────────────────────────────────────
  {ai.get('overview','')}

── CAUSES & RISK FACTORS ─────────────────────────────────────────
{fl(ai.get('causes','N/A'))}

── KEY SYMPTOMS OF THIS CONDITION ────────────────────────────────
{fl(ai.get('symptoms_detail','N/A'))}

── PRECAUTIONS ───────────────────────────────────────────────────
{fl(ai.get('precautions','N/A'))}

── MEDICATIONS & TREATMENTS ──────────────────────────────────────
{fl(ai.get('medications','N/A'))}

── HOME CARE TIPS ────────────────────────────────────────────────
{fl(ai.get('home_remedies','N/A'))}

── WHEN TO SEE A DOCTOR IMMEDIATELY ─────────────────────────────
{fl(ai.get('when_to_see_doctor','N/A'))}

──────────────────────────────────────────────────────────────────
  ⚠ DISCLAIMER: Academic demonstration tool only.
    NOT a substitute for professional medical advice.
──────────────────────────────────────────────────────────────────
  Developed by THAKUR & TRIPATHI  ·  B.Tech Final Year Project
"""


# ─────────────────────────────────────────────────────────
# 6. RESULT DISPLAY
# ─────────────────────────────────────────────────────────
def display_results(disease, reason, per_model, per_probs, conf, sel_syms, models, accs):
    syms_str = ", ".join(s.replace('_', ' ').title() for s in sel_syms)

    st.session_state.pred = {
        'disease':    disease,
        'confidence': conf,
        'symptoms':   syms_str
    }

    # ── HERO CARD ──────────────────────────────────────────
    st.markdown(f"""
    <div class="pred-hero">
        <div class="pred-eyebrow">Predicted Condition</div>
        <div class="pred-name">{disease}</div>
        <div class="pred-reason-text">{reason}</div>
        <span class="conf-pill">Confidence  {conf*100:.1f}%</span>
        <div class="pred-syms">Symptoms analysed: {syms_str}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── FETCH FROM KNOWLEDGE BASE ────────────────────────
    ai = get_disease_info(disease)
    st.session_state.ai_info = ai

    # ── METRIC TRIO ──────────────────────────────────────
    risk     = ai.get("risk_level", "Medium")
    spec     = ai.get("specialist", "General Physician")
    recovery = ai.get("recovery_time", "Varies")
    risk_badge_cls = {"Low": "badge-low", "Medium": "badge-medium", "High": "badge-high"}.get(risk, "badge-medium")

    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(f"""
        <div class="metric-card" style="text-align:center">
            <div class="metric-label">⚠&nbsp; Risk Level</div>
            <div style="margin-top:8px">
                <span class="{risk_badge_cls}">{risk}</span>
            </div>
        </div>""", unsafe_allow_html=True)
    with m2:
        st.markdown(f"""
        <div class="metric-card" style="text-align:center">
            <div class="metric-label">👨‍⚕️&nbsp; Recommended Specialist</div>
            <div class="metric-value" style="font-size:0.95rem; margin-top:8px">{spec}</div>
        </div>""", unsafe_allow_html=True)
    with m3:
        st.markdown(f"""
        <div class="metric-card" style="text-align:center">
            <div class="metric-label">🕐&nbsp; Typical Recovery</div>
            <div class="metric-value" style="font-size:0.9rem; margin-top:8px">{recovery}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<div class='divider-label'>Medical Intelligence</div>", unsafe_allow_html=True)

    # ── OVERVIEW ─────────────────────────────────────────
    st.markdown(f"""
    <div class="info-card">
        <div class="info-card-title">📋 &nbsp;Overview</div>
        <p>{ai.get('overview','')}</p>
    </div>""", unsafe_allow_html=True)

    # ── SYMPTOMS | CAUSES ─────────────────────────────────
    c1, c2 = st.columns(2)
    with c1:
        items = "".join(f"<li>{x.strip()}</li>" for x in ai.get('symptoms_detail','').split(';') if x.strip())
        st.markdown(f"""
        <div class="info-card">
            <div class="info-card-title">🩺 &nbsp;Key Symptoms of This Condition</div>
            <ul>{items}</ul>
        </div>""", unsafe_allow_html=True)
    with c2:
        items = "".join(f"<li>{x.strip()}</li>" for x in ai.get('causes','').split(';') if x.strip())
        st.markdown(f"""
        <div class="info-card">
            <div class="info-card-title">🔬 &nbsp;Causes & Risk Factors</div>
            <ul>{items}</ul>
        </div>""", unsafe_allow_html=True)

    # ── PRECAUTIONS | MEDICATIONS ─────────────────────────
    c3, c4 = st.columns(2)
    with c3:
        items = "".join(f"<li>{x.strip()}</li>" for x in ai.get('precautions','').split(';') if x.strip())
        st.markdown(f"""
        <div class="info-card">
            <div class="info-card-title">🛡 &nbsp;Recommended Precautions</div>
            <ul>{items}</ul>
        </div>""", unsafe_allow_html=True)
    with c4:
        items = "".join(f"<li>{x.strip()}</li>" for x in ai.get('medications','').split(';') if x.strip())
        st.markdown(f"""
        <div class="info-card">
            <div class="info-card-title">💊 &nbsp;Medications & Treatments</div>
            <ul>{items}</ul>
        </div>""", unsafe_allow_html=True)

    # ── HOME CARE | WHEN TO SEE DOCTOR ──────────────────
    c5, c6 = st.columns(2)
    with c5:
        items = "".join(f"<li>{x.strip()}</li>" for x in ai.get('home_remedies','').split(';') if x.strip())
        st.markdown(f"""
        <div class="info-card">
            <div class="info-card-title">🏠 &nbsp;Home Care Tips</div>
            <ul>{items}</ul>
        </div>""", unsafe_allow_html=True)
    with c6:
        items = "".join(f"<li>{x.strip()}</li>" for x in ai.get('when_to_see_doctor','').split(';') if x.strip())
        st.markdown(f"""
        <div class="info-card">
            <div class="info-card-title">🚨 &nbsp;See a Doctor Immediately If…</div>
            <ul>{items}</ul>
        </div>""", unsafe_allow_html=True)

    # ── MODEL BREAKDOWN ──────────────────────────────────
    st.markdown("<div class='divider-label'>Individual Model Decisions</div>",
                unsafe_allow_html=True)
    with st.expander("🔬  View per-model predictions & confidence"):
        c_a, c_b, c_c = st.columns(3)
        for col, (name, pred_d), icon in zip([c_a, c_b, c_c], per_model.items(), ["🌳","🌲","🧮"]):
            cv = per_probs.get(name, 0.0)
            with col:
                st.markdown(f"""
                <div class="model-card">
                    <div class="mc-name">{icon}&nbsp; {name}</div>
                    <div class="mc-disease">{pred_d}</div>
                    <div class="mc-conf">Confidence: {cv*100:.1f}%</div>
                    <div class="mc-bar-bg"><div class="mc-bar" style="width:{int(cv*100)}%"></div></div>
                    <div class="mc-acc">Model Accuracy: {accs[name]*100:.1f}%</div>
                </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────
# 7. SESSION STATE
# ─────────────────────────────────────────────────────────
models, model_accs, symptoms_list, all_diseases, dsm, sys_logs = initialize_system()

for k, v in [('page','home'), ('patient',{}), ('pred',None), ('ai_info',{}), ('logs', sys_logs)]:
    if k not in st.session_state:
        st.session_state[k] = v


# ─────────────────────────────────────────────────────────
# 8. HOME PAGE
# ─────────────────────────────────────────────────────────
if st.session_state.page == 'home':
    st.markdown("<br><br>", unsafe_allow_html=True)

    _, cc, _ = st.columns([1, 1.5, 1])
    with cc:
        st.markdown("""
        <div style="text-align:center; margin-bottom:20px">
            <div class="pill-badge">MedAI · B.Tech Final Year Project</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<h1>AI Disease Predictor</h1>", unsafe_allow_html=True)
        st.markdown("""
        <p style="text-align:center; color:#1e4060; font-size:0.92rem; margin: 10px 0 32px; line-height:1.6">
            Three ML models · Symptom-weighted ensemble · Comprehensive medical database
        </p>
        """, unsafe_allow_html=True)

        st.markdown("<div class='login-card'>", unsafe_allow_html=True)
        with st.form("pf"):
            name    = st.text_input("First Name",  placeholder="e.g. Arjun")
            surname = st.text_input("Last Name",   placeholder="e.g. Sharma")
            age     = st.number_input("Age", min_value=1, max_value=120, step=1, value=22)
            gender  = st.radio("Gender", ["Male", "Female", "Other"], horizontal=True)
            st.markdown("<br>", unsafe_allow_html=True)
            if st.form_submit_button("Begin Diagnostic Session  →", use_container_width=True):
                if name.strip() and surname.strip():
                    st.session_state.patient = {
                        'name': name.strip(), 'surname': surname.strip(),
                        'age': age, 'gender': gender
                    }
                    st.session_state.page = 'app'
                    st.rerun()
                else:
                    st.error("Please enter both first and last name.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        Developed by <span>THAKUR &amp; TRIPATHI</span>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────
# 9. MAIN APP
# ─────────────────────────────────────────────────────────
elif st.session_state.page == 'app':
    p = st.session_state.patient

    # Top bar
    lc, tc, rc = st.columns([0.13, 0.74, 0.13])
    with lc:
        with st.popover("📊"):
            st.markdown("**Model Accuracies**")
            for n, a in model_accs.items():
                st.metric(n, f"{a*100:.1f}%")
    with tc:
        st.markdown("<h1 style='font-size:2rem'>🩺 MedAI Disease Predictor</h1>",
                    unsafe_allow_html=True)
    with rc:
        with st.popover("📋"):
            for l in st.session_state.logs:
                st.caption(l)

    # Patient bar
    st.markdown(
        f"<div class='patient-bar'>👤 "
        f"<b>Patient:</b><span>{p.get('name')} {p.get('surname')}</span>"
        f"<b>Age:</b><span>{p.get('age')}</span>"
        f"<b>Gender:</b><span>{p.get('gender')}</span>"
        f"</div>",
        unsafe_allow_html=True)

    if st.button("⬅  New Session"):
        st.session_state.page    = 'home'
        st.session_state.patient = {}
        st.session_state.pred    = None
        st.session_state.ai_info = {}
        st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["  🔍 Predict by Symptoms  ", "  📂 Predict from File  "])

    # ── TAB 1 ─────────────────────────────────────────────
    with tab1:
        with st.container(border=True):
            st.subheader("Select Patient Symptoms")
            selected = st.multiselect(
                "syms", options=sorted(symptoms_list),
                label_visibility="collapsed",
                placeholder="Type to search symptoms…"
            )

        if st.button("🔬  Analyse & Predict", type="primary", use_container_width=True):
            if selected:
                with st.spinner("Analysing symptom pattern…"):
                    time.sleep(0.3)
                iv = np.array([1 if s in selected else 0
                               for s in symptoms_list]).reshape(1, -1)
                disease, reason, pm, pp, conf = smart_ensemble(
                    iv, selected, models, model_accs, dsm)
                display_results(disease, reason, pm, pp, conf, selected, models, model_accs)
            else:
                st.warning("⚠  Please select at least one symptom.")

    # ── TAB 2 ─────────────────────────────────────────────
    with tab2:
        with st.container(border=True):
            st.subheader("Upload Patient CSV")
            st.caption("CSV columns should match symptom names from the training dataset.")
            uploaded = st.file_uploader("csv", type=["csv"], label_visibility="collapsed")

        if uploaded and st.button("📊  Run Batch Prediction", type="primary", use_container_width=True):
            try:
                df_up = pd.read_csv(uploaded)
                df_up.columns = df_up.columns.str.strip()
                for dc in ['prognosis', 'disease']:
                    if dc in df_up.columns:
                        df_up = df_up.drop(columns=[dc])

                X_up = df_up.reindex(columns=symptoms_list, fill_value=0)
                preds_out = []
                for i in range(len(X_up)):
                    row = X_up.iloc[[i]].values
                    ss  = [symptoms_list[j] for j, v in enumerate(row[0]) if v > 0]
                    dis, _, _, _, _ = smart_ensemble(row, ss, models, model_accs, dsm)
                    preds_out.append(dis)

                df_up['AI_Prediction'] = preds_out
                st.success(f"✅  Predicted {len(preds_out)} record(s) successfully.")
                st.dataframe(df_up, use_container_width=True)

                if len(df_up) == 1:
                    row = X_up.iloc[[0]].values
                    ss  = [symptoms_list[j] for j, v in enumerate(row[0]) if v > 0]
                    d, r, pm, pp, c = smart_ensemble(row, ss, models, model_accs, dsm)
                    display_results(d, r, pm, pp, c, ss, models, model_accs)

            except Exception as e:
                st.error(f"File error: {e}")

    # ── DOWNLOAD ──────────────────────────────────────────
    if st.session_state.pred and st.session_state.get('ai_info'):
        st.markdown("<hr>", unsafe_allow_html=True)
        st.download_button(
            label="📄  Download Full Clinical Report",
            data=generate_report(st.session_state.ai_info),
            file_name=f"MedAI_{p.get('surname','patient')}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
            mime="text/plain",
            use_container_width=True
        )

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
    <div class="disclaimer">
        <strong>⚠ Disclaimer:</strong> This is an academic B.Tech final year demonstration project.
        It is <strong>NOT</strong> a substitute for professional medical diagnosis, advice, or treatment.
        Always consult a qualified and licensed healthcare professional for any medical concerns.
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        Developed by <span>THAKUR &amp; TRIPATHI</span> &nbsp;·&nbsp; B.Tech Final Year
    </div>""", unsafe_allow_html=True)
