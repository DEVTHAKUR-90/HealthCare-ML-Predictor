# disease_info.py
# ─────────────────────────────────────────────────────────────────────────────
# Comprehensive medical knowledge base for the MedAI Disease Predictor.
# Each entry contains: overview, causes, symptoms_detail, precautions,
# medications, home_remedies, when_to_see_doctor, specialist,
# risk_level ("Low" | "Medium" | "High"), recovery_time
# ─────────────────────────────────────────────────────────────────────────────

DISEASE_DB = {

    # ── INFECTIOUS / RESPIRATORY ─────────────────────────────────────────────
    "fungal infection": {
        "overview": "A fungal infection occurs when a harmful fungus invades the body and the immune system cannot fight it off. Fungal infections can affect the skin, nails, lungs, and other organs. They range from mild superficial infections to life-threatening systemic ones.",
        "causes": "Exposure to environmental fungi (mold, yeast); Weakened immune system; Prolonged antibiotic use; Humid or sweaty skin conditions; Contact with infected person or animal",
        "symptoms_detail": "Itchy, red, or scaly skin patches; Thickened or discoloured nails; White patches inside the mouth (oral thrush); Persistent cough or chest pain (lung infection); Redness and burning in affected areas; Discharge with unusual odour",
        "precautions": "Keep skin clean and dry, especially in skin folds; Wear breathable, loose-fitting clothing; Avoid walking barefoot in public areas; Change socks and underwear daily; Do not share personal items like towels or nail clippers; Maintain good hygiene after gym or swimming",
        "medications": "Topical antifungals: Clotrimazole or Miconazole for skin infections; Oral antifungals: Fluconazole for systemic or persistent infections; Terbinafine for nail fungal infections; Nystatin for oral thrush; Itraconazole for more resistant strains",
        "home_remedies": "Apply diluted tea tree oil to affected skin areas; Use coconut oil as a natural antifungal topical; Keep affected area aired out and dry; Consume probiotics (yogurt) to restore gut flora",
        "when_to_see_doctor": "Infection spreading rapidly or not improving after 2 weeks of OTC treatment; Fever or chills accompanying skin infection; Infection in or around the eyes, mouth, or genitals; Signs of secondary bacterial infection (pus, increasing redness)",
        "specialist": "Dermatologist (skin/nail) or Infectious Disease Specialist (systemic)",
        "risk_level": "Low",
        "recovery_time": "2–4 weeks with proper antifungal treatment"
    },

    "allergy": {
        "overview": "An allergy is an exaggerated immune response to a substance (allergen) that is harmless to most people. The immune system mistakenly identifies it as a threat and releases chemicals like histamine, causing a range of symptoms.",
        "causes": "Pollen, dust mites, or pet dander; Food allergens (nuts, dairy, shellfish, gluten); Insect stings or bites; Medications (penicillin, aspirin, NSAIDs); Latex or chemical contact; Mold spores",
        "symptoms_detail": "Sneezing, runny or congested nose; Itchy, watery, or red eyes; Skin hives, rash, or eczema flare; Swelling of lips, tongue, or face; Shortness of breath or wheezing; Stomach cramps, nausea, or vomiting (food allergy)",
        "precautions": "Identify and strictly avoid known allergens; Use air purifiers with HEPA filters indoors; Wear a medical alert bracelet if you have severe allergies; Keep antihistamines readily available; Wash hands and face after outdoor exposure; Check food labels carefully",
        "medications": "Antihistamines: Cetirizine or Loratadine for mild-moderate symptoms; Corticosteroid nasal sprays: Fluticasone for nasal allergies; Epinephrine auto-injector (EpiPen) for anaphylaxis; Leukotriene inhibitors: Montelukast; Allergen immunotherapy (allergy shots) for long-term desensitisation",
        "home_remedies": "Rinse nasal passages with saline spray; Apply cool wet cloth to itchy skin areas; Stay indoors during high pollen count days; Use hypoallergenic bedding covers",
        "when_to_see_doctor": "Sudden severe swelling of throat or difficulty swallowing; Anaphylactic reaction (drop in blood pressure, loss of consciousness); Symptoms significantly impacting daily life or sleep; Worsening asthma triggered by allergens",
        "specialist": "Allergist / Immunologist",
        "risk_level": "Medium",
        "recovery_time": "Symptoms resolve in hours to days with treatment; chronic management ongoing"
    },

    "gerd": {
        "overview": "Gastroesophageal Reflux Disease (GERD) is a chronic digestive condition where stomach acid frequently flows back into the oesophagus, irritating its lining. It is more than occasional heartburn and can cause long-term complications if untreated.",
        "causes": "Weakened or abnormal lower oesophageal sphincter; Obesity or excess abdominal pressure; Hiatal hernia; Spicy, fatty, or acidic foods; Smoking and alcohol use; Pregnancy; Certain medications (aspirin, ibuprofen)",
        "symptoms_detail": "Burning sensation in chest (heartburn) after meals; Regurgitation of food or sour liquid; Difficulty swallowing (dysphagia); Chronic cough or hoarseness; Feeling of lump in throat; Disrupted sleep due to acid reflux",
        "precautions": "Eat smaller, more frequent meals; Avoid lying down within 2–3 hours after eating; Elevate head of bed by 15–20 cm; Avoid trigger foods: spicy, oily, coffee, citrus, chocolate; Maintain a healthy weight; Quit smoking and reduce alcohol intake",
        "medications": "Proton pump inhibitors (PPIs): Omeprazole or Pantoprazole (most effective); H2 blockers: Ranitidine or Famotidine; Antacids: Gelusil or Eno for immediate relief; Prokinetics: Domperidone to improve gastric emptying; Surgery (Nissen fundoplication) for severe refractory GERD",
        "home_remedies": "Chew sugar-free gum after meals to stimulate saliva; Drink aloe vera juice before meals; Ginger tea may soothe the oesophagus; Avoid tight-fitting clothes around abdomen",
        "when_to_see_doctor": "Difficulty swallowing or painful swallowing; Vomiting blood or black tarry stools; Unexplained weight loss alongside symptoms; Symptoms not responding to 2 weeks of PPI therapy",
        "specialist": "Gastroenterologist",
        "risk_level": "Medium",
        "recovery_time": "Symptom control within days of medication; long-term management required"
    },

    "chronic cholestasis": {
        "overview": "Chronic cholestasis is a condition where bile flow from the liver is reduced or blocked over a prolonged period, leading to accumulation of bile acids in the liver and bloodstream. It can cause liver damage if left untreated.",
        "causes": "Primary biliary cholangitis (autoimmune); Primary sclerosing cholangitis; Intrahepatic causes (drug-induced, pregnancy-related); Biliary obstruction from gallstones or tumours; Chronic hepatitis B or C; Certain medications (anabolic steroids, antibiotics)",
        "symptoms_detail": "Persistent itching (pruritus) all over the body; Jaundice (yellow skin and eyes); Dark urine and pale-coloured stools; Fatigue and general weakness; Right upper abdominal discomfort; Fat malabsorption and vitamin deficiencies",
        "precautions": "Follow a low-fat diet to reduce liver workload; Avoid alcohol completely; Avoid hepatotoxic medications without doctor's approval; Regular liver function monitoring; Take fat-soluble vitamin supplements (A, D, E, K) as prescribed; Stay well hydrated",
        "medications": "Ursodeoxycholic acid (UDCA): Primary treatment for primary biliary cholangitis; Cholestyramine: To relieve pruritus by binding bile acids; Rifampicin: For refractory pruritus; Vitamin supplementation (fat-soluble vitamins); Immunosuppressants for autoimmune causes; Liver transplant in advanced cases",
        "home_remedies": "Cool baths or cool compresses to relieve itching; Wear loose cotton clothing; Avoid hot showers which worsen itching; Keep skin well moisturised with fragrance-free lotion",
        "when_to_see_doctor": "Progressive worsening of jaundice; Confusion or altered mental state (hepatic encephalopathy); Uncontrollable bleeding; Severe abdominal pain; Rapid weight loss",
        "specialist": "Hepatologist / Gastroenterologist",
        "risk_level": "High",
        "recovery_time": "Managed long-term; underlying cause determines prognosis"
    },

    "drug reaction": {
        "overview": "An adverse drug reaction (ADR) is an unintended, harmful response to a medication taken at normal doses. It can range from mild side effects to severe life-threatening reactions such as anaphylaxis or Steven-Johnson syndrome.",
        "causes": "Allergic immune response to a drug (penicillin, sulfa drugs); Overdose or incorrect dosing; Drug-drug interactions; Genetic predisposition to drug metabolism issues; Cumulative toxicity from long-term use; Idiosyncratic reactions (unpredictable)",
        "symptoms_detail": "Skin rash, hives, or blistering; Itching, swelling, or redness; Fever; Difficulty breathing or wheezing; Nausea, vomiting, or diarrhoea; Dizziness, confusion, or liver/kidney abnormalities",
        "precautions": "Always inform doctors of known drug allergies; Never self-medicate or exceed prescribed doses; Review all medications with pharmacist for interactions; Carry a medical alert ID if you have serious drug allergies; Read drug information leaflets carefully; Do not share prescription medicines",
        "medications": "Discontinue the offending drug immediately (under doctor guidance); Antihistamines: Diphenhydramine or Cetirizine for mild reactions; Corticosteroids: Prednisolone to reduce severe inflammation; Epinephrine (EpiPen) for anaphylaxis; Supportive IV fluids if required; Specific antidotes where available",
        "home_remedies": "Cool compresses on skin rashes; Stay well hydrated; Rest and monitor symptoms closely; Calamine lotion for localised mild skin reactions",
        "when_to_see_doctor": "Any sign of breathing difficulty or throat swelling; Widespread blistering of skin or mouth (SJS/TEN); High fever with rash; Rapid worsening of symptoms; Suspected internal organ involvement",
        "specialist": "Allergist / Clinical Pharmacologist / Emergency Physician",
        "risk_level": "High",
        "recovery_time": "Mild reactions: 3–7 days after stopping drug; Severe reactions: weeks with treatment"
    },

    "peptic ulcer disease": {
        "overview": "Peptic ulcer disease involves open sores (ulcers) in the lining of the stomach, upper small intestine, or oesophagus. They form when the protective mucous layer is eroded by stomach acid.",
        "causes": "Helicobacter pylori (H. pylori) bacterial infection; Long-term use of NSAIDs (ibuprofen, aspirin); Excessive alcohol consumption; Smoking; Rare tumours (Zollinger-Ellison syndrome); Severe physiological stress",
        "symptoms_detail": "Burning or gnawing stomach pain, often between meals; Nausea and vomiting; Bloating or belching; Feeling of fullness; Dark or tar-like stools (bleeding ulcer); Vomiting blood in severe cases",
        "precautions": "Avoid NSAIDs; take with food if essential; Eliminate H. pylori with full antibiotic course; Avoid smoking and alcohol; Eat regular small meals; Reduce stress through relaxation techniques; Avoid spicy and acidic foods",
        "medications": "Proton pump inhibitors: Omeprazole or Esomeprazole; H. pylori eradication: Triple therapy (Amoxicillin + Clarithromycin + PPI) for 14 days; Bismuth subsalicylate; H2 blockers: Famotidine; Sucralfate for mucosal protection; Endoscopy with cauterisation for bleeding ulcers",
        "home_remedies": "Eat smaller, more frequent meals; Drink licorice root tea (deglycyrrhizinated); Cabbage juice has traditional mucosal protective properties; Probiotics help restore gut bacteria balance",
        "when_to_see_doctor": "Black or bloody stools; Vomiting blood; Sudden severe abdominal pain (perforation); Unexplained weight loss; Symptoms not improving after 2 weeks of treatment",
        "specialist": "Gastroenterologist",
        "risk_level": "Medium",
        "recovery_time": "4–8 weeks with proper PPI therapy; H. pylori eradication prevents recurrence"
    },

    "aids": {
        "overview": "Acquired Immunodeficiency Syndrome (AIDS) is the late stage of HIV infection, where the immune system is severely damaged. Without treatment, HIV progressively destroys CD4 T-cells, making the body vulnerable to opportunistic infections.",
        "causes": "HIV infection through unprotected sexual contact; Sharing contaminated needles; Mother-to-child transmission during pregnancy, birth, or breastfeeding; Blood transfusions with infected blood (rare in screened blood banks); No casual contact transmission",
        "symptoms_detail": "Rapid unexplained weight loss; Recurring fever, night sweats, and chills; Extreme fatigue; Swollen lymph nodes; Diarrhoea lasting more than a week; Sores in mouth, genitals, or anus; Pneumonia; Memory loss or neurological symptoms",
        "precautions": "Practice safe sex with consistent condom use; Never share needles or syringes; Get tested for HIV regularly if at risk; PrEP (pre-exposure prophylaxis) for high-risk individuals; Adhere strictly to antiretroviral therapy (ART); Avoid raw or undercooked food to prevent opportunistic infections",
        "medications": "Antiretroviral therapy (ART): Multiple drug combinations (HAART); Nucleoside reverse transcriptase inhibitors: Tenofovir + Emtricitabine; Integrase inhibitors: Dolutegravir; Prophylactic antibiotics for opportunistic infections; Antifungals, antivirals as needed for comorbidities",
        "home_remedies": "Maintain a nutritious well-balanced diet; Regular light exercise to support immunity; Adequate sleep and stress management; Avoid smoking and alcohol; Join support groups for mental health",
        "when_to_see_doctor": "Any new or worsening infection; CD4 count falling below 200 cells/mm³; Neurological symptoms (confusion, vision changes); New skin lesions or persistent fever; Missed doses of ART — contact clinic immediately",
        "specialist": "Infectious Disease Specialist / HIV Specialist",
        "risk_level": "High",
        "recovery_time": "Lifelong management with ART; life expectancy near-normal with adherence"
    },

    "diabetes": {
        "overview": "Diabetes mellitus is a chronic metabolic disease characterised by elevated blood glucose levels due to insufficient insulin production (Type 1), insulin resistance (Type 2), or both. Uncontrolled diabetes damages blood vessels and nerves throughout the body.",
        "causes": "Type 1: Autoimmune destruction of pancreatic beta cells; Type 2: Insulin resistance from obesity, sedentary lifestyle, genetic factors; Gestational diabetes during pregnancy; Polycystic ovary syndrome (PCOS); Chronic pancreatitis; Certain medications (steroids)",
        "symptoms_detail": "Frequent urination (polyuria); Excessive thirst (polydipsia); Unexplained weight loss; Extreme hunger; Blurred vision; Slow-healing wounds and sores; Tingling or numbness in hands and feet; Fatigue and weakness",
        "precautions": "Monitor blood glucose levels regularly; Follow a low-glycaemic, balanced diet; Exercise at least 150 minutes per week; Maintain healthy body weight; Inspect feet daily for cuts or sores; Avoid smoking and alcohol; Annual eye and kidney function check-ups",
        "medications": "Type 1: Insulin therapy (multiple daily injections or pump); Type 2: Metformin (first-line oral); SGLT2 inhibitors: Empagliflozin or Dapagliflozin; GLP-1 agonists: Semaglutide or Liraglutide; DPP-4 inhibitors: Sitagliptin; Sulphonylureas: Glimepiride; Insulin when oral agents insufficient",
        "home_remedies": "Bitter melon juice may help lower blood sugar; Fenugreek seeds soaked overnight improve insulin sensitivity; Cinnamon in food may modestly reduce fasting glucose; Regular brisk walking after meals",
        "when_to_see_doctor": "Blood glucose above 300 mg/dL or below 70 mg/dL; Signs of diabetic ketoacidosis (vomiting, abdominal pain, fruity breath); Foot ulcer that is not healing; Sudden vision changes; Chest pain or stroke symptoms",
        "specialist": "Endocrinologist / Diabetologist",
        "risk_level": "High",
        "recovery_time": "Lifelong management; good control prevents complications"
    },

    "gastroenteritis": {
        "overview": "Gastroenteritis, commonly called stomach flu, is inflammation of the stomach and intestines usually caused by a viral or bacterial infection. It typically causes sudden onset of vomiting and diarrhoea and is highly contagious.",
        "causes": "Norovirus or Rotavirus (most common viral causes); Bacterial: Salmonella, E. coli, Campylobacter, Shigella; Parasitic: Giardia or Cryptosporidium; Contaminated food or water; Poor hand hygiene; Close contact with infected individuals",
        "symptoms_detail": "Sudden watery diarrhoea; Nausea and vomiting; Abdominal cramps and pain; Fever (usually low-grade); Headache and muscle aches; Dehydration signs: dry mouth, dark urine, dizziness",
        "precautions": "Wash hands thoroughly with soap before eating and after using toilet; Drink only safe, clean water; Avoid raw or undercooked meats and seafood; Isolate from others while symptomatic; Disinfect contaminated surfaces; Do not prepare food for others while ill",
        "medications": "Oral rehydration salts (ORS) — most critical treatment; Antiemetics: Ondansetron for severe vomiting; Loperamide for diarrhoea in adults (not if fever or bloody stools); Antibiotics only for confirmed bacterial causes (Azithromycin or Ciprofloxacin); Zinc supplements for children with diarrhoea",
        "home_remedies": "Sip clear fluids and electrolyte drinks frequently; Eat bland BRAT diet (bananas, rice, applesauce, toast); Avoid dairy, caffeine, and fatty foods until recovery; Ginger tea to ease nausea",
        "when_to_see_doctor": "Signs of severe dehydration; Bloody or black stools; Vomiting lasting more than 48 hours; High fever above 39°C; Symptoms in infants, elderly, or immunocompromised patients",
        "specialist": "General Physician / Gastroenterologist (if prolonged)",
        "risk_level": "Low",
        "recovery_time": "1–3 days for viral; up to 1 week for bacterial gastroenteritis"
    },

    "bronchial asthma": {
        "overview": "Bronchial asthma is a chronic inflammatory disease of the airways that causes recurring episodes of wheezing, breathlessness, chest tightness, and coughing, particularly at night or early morning. Inflammation makes the airways narrower and more reactive to triggers.",
        "causes": "Allergens: Dust mites, pollen, pet dander, mould; Respiratory infections (viral); Air pollution and tobacco smoke; Physical exercise (exercise-induced asthma); Cold air or weather changes; Emotional stress; Occupational exposures (chemicals, dust)",
        "symptoms_detail": "Recurrent wheezing (whistling sound while breathing); Shortness of breath, especially at night; Chest tightness or pressure; Chronic dry cough, worse at night; Breathing difficulty triggered by specific factors; Reduced exercise tolerance",
        "precautions": "Identify and avoid personal triggers; Keep home dust-free with regular cleaning; Use hypoallergenic pillowcases and mattress covers; Never smoke and avoid secondhand smoke; Keep a reliever inhaler accessible at all times; Follow your personalised Asthma Action Plan",
        "medications": "Short-acting bronchodilators (reliever): Salbutamol (Ventolin) inhaler; Inhaled corticosteroids (controller): Budesonide or Fluticasone; Long-acting beta agonists: Formoterol or Salmeterol; Leukotriene modifiers: Montelukast; Systemic corticosteroids for severe exacerbations; Biologic agents: Omalizumab for severe allergic asthma",
        "home_remedies": "Practice breathing exercises (Buteyko or diaphragmatic breathing); Steam inhalation may loosen mucus; Ginger and turmeric have anti-inflammatory properties; Maintain indoor humidity between 40–50%",
        "when_to_see_doctor": "Severe breathlessness not relieved by reliever inhaler; Blue tinge to lips or fingertips (cyanosis); Can't complete sentences due to breathlessness; Peak flow below 50% of personal best; Nighttime attacks increasing in frequency",
        "specialist": "Pulmonologist / Respiratory Physician",
        "risk_level": "Medium",
        "recovery_time": "Acute attacks resolve in minutes to hours; chronic management ongoing"
    },

    "hypertension": {
        "overview": "Hypertension (high blood pressure) is a chronic condition where the force of blood against artery walls is consistently too high (≥140/90 mmHg). Often called the 'silent killer', it has no obvious symptoms but significantly raises the risk of heart attack, stroke, and kidney disease.",
        "causes": "Primary (essential) hypertension: Genetic predisposition, sedentary lifestyle, high sodium diet, obesity; Secondary: Kidney disease, sleep apnoea, thyroid disorders, certain medications (NSAIDs, contraceptive pills); Chronic stress; Excessive alcohol and tobacco use",
        "symptoms_detail": "Usually asymptomatic (silent); Severe hypertension: Headache, especially in the morning; Nosebleeds; Visual disturbances or blurred vision; Dizziness or lightheadedness; Chest pain (in hypertensive crisis); Shortness of breath",
        "precautions": "Monitor blood pressure regularly at home; Adopt DASH diet (low sodium, high potassium — fruits, vegetables, whole grains); Exercise at least 30 minutes most days; Maintain healthy weight (BMI 18.5–24.9); Limit alcohol to ≤1 drink/day; Quit smoking; Manage chronic stress",
        "medications": "ACE inhibitors: Enalapril or Ramipril; Angiotensin receptor blockers: Losartan or Telmisartan; Calcium channel blockers: Amlodipine; Thiazide diuretics: Hydrochlorothiazide; Beta blockers: Metoprolol or Atenolol; Combination therapy often required",
        "home_remedies": "Reduce salt intake to less than 5g/day; Practice yoga and deep breathing daily; Hibiscus tea may modestly lower blood pressure; Regular aerobic exercise (walking, swimming)",
        "when_to_see_doctor": "Blood pressure above 180/120 mmHg; Severe headache with confusion or vision changes; Chest pain or shortness of breath; Sudden weakness or speech difficulty (stroke signs); Blood pressure not controlled on current medications",
        "specialist": "Cardiologist / Nephrologist",
        "risk_level": "High",
        "recovery_time": "Requires lifelong management; BP controlled within weeks of medication"
    },

    "migraine": {
        "overview": "Migraine is a neurological disorder characterised by recurring, intense headaches often accompanied by nausea, vomiting, and extreme sensitivity to light and sound. Attacks can last from 4 to 72 hours and can significantly impair daily functioning.",
        "causes": "Hormonal changes (menstrual cycle); Specific food triggers (red wine, aged cheese, chocolate, caffeine); Stress and anxiety; Disrupted sleep patterns; Strong sensory stimuli (bright light, loud noise, strong smells); Skipping meals or dehydration; Genetic predisposition",
        "symptoms_detail": "Intense, throbbing or pulsating headache (usually one-sided); Nausea and vomiting; Sensitivity to light (photophobia) and sound (phonophobia); Visual aura (flashing lights, zigzag lines) before headache; Dizziness or feeling faint; Neck stiffness; Difficulty concentrating",
        "precautions": "Keep a migraine diary to identify personal triggers; Maintain regular sleep schedule; Stay well hydrated throughout the day; Do not skip meals; Manage stress with relaxation techniques; Wear sunglasses in bright light; Limit screen time",
        "medications": "Acute/abortive: Triptans (Sumatriptan or Rizatriptan) — most effective; NSAIDs: Ibuprofen or Naproxen for mild-moderate attacks; Anti-nausea: Metoclopramide or Ondansetron; Preventive (if >4 attacks/month): Topiramate, Propranolol, Amitriptyline, or CGRP inhibitors (Erenumab)",
        "home_remedies": "Apply ice pack to forehead or neck; Rest in a dark, quiet room; Peppermint oil applied to temples may relieve pain; Ginger tea helps reduce nausea; Caffeine in small amounts can boost pain relief",
        "when_to_see_doctor": "Sudden 'thunderclap' headache (worst headache of your life); Headache with fever, stiff neck, or rash (meningitis risk); New headache after age 50; Aura lasting more than 1 hour; Headaches increasing in frequency or severity",
        "specialist": "Neurologist",
        "risk_level": "Medium",
        "recovery_time": "Individual attacks: 4–72 hours; preventive therapy reduces frequency over months"
    },

    "cervical spondylosis": {
        "overview": "Cervical spondylosis is age-related wear and tear of the spinal discs in the neck (cervical spine). As discs dehydrate and shrink, bone spurs form, often causing neck pain and stiffness. It is extremely common and affects more than 85% of people over age 60.",
        "causes": "Age-related disc degeneration; Prolonged poor posture (especially desk or phone use); Past neck injuries; Repetitive neck movements (occupational); Genetic predisposition; Sedentary lifestyle; Overweight",
        "symptoms_detail": "Neck pain and stiffness, worse in the morning; Headache at the back of the skull; Tingling or numbness in arms, hands, or fingers; Weakness in arms or legs; Grinding or popping sensation when turning neck; Dizziness; Balance difficulty in severe cases",
        "precautions": "Maintain correct ergonomic posture at workstation; Take regular breaks from screens (every 30–45 min); Use a firm, supportive pillow; Avoid holding phone between shoulder and ear; Strengthen neck muscles with regular physiotherapy exercises; Avoid smoking (accelerates disc degeneration)",
        "medications": "NSAIDs: Ibuprofen or Diclofenac for pain and inflammation; Muscle relaxants: Cyclobenzaprine or Tizanidine for spasm; Nerve pain medication: Pregabalin or Gabapentin; Corticosteroid injections for severe nerve compression; Physiotherapy is cornerstone of treatment; Surgery for severe myelopathy or radiculopathy",
        "home_remedies": "Apply warm compress or heating pad to neck 15–20 min; Gentle neck stretching and range-of-motion exercises; Hot shower directed at neck in the morning; Turmeric milk for anti-inflammatory benefit",
        "when_to_see_doctor": "Progressive weakness in arms or legs; Loss of bladder or bowel control; Sudden severe increase in neck pain after injury; Balance problems or difficulty walking; Symptoms not improving after 6 weeks of conservative treatment",
        "specialist": "Orthopaedic Surgeon / Neurologist / Spine Specialist",
        "risk_level": "Medium",
        "recovery_time": "Symptoms improve with physiotherapy over weeks to months; chronic management"
    },

    "jaundice": {
        "overview": "Jaundice is a yellowing of the skin and whites of the eyes caused by elevated bilirubin levels in the blood. It is a symptom of an underlying condition affecting the liver, bile ducts, or red blood cells, rather than a disease itself.",
        "causes": "Liver diseases: Hepatitis, cirrhosis, alcoholic liver disease; Bile duct obstruction from gallstones or tumours; Haemolytic anaemia (excessive red blood cell breakdown); Newborn jaundice (physiological); Drug-induced liver injury; Gilbert syndrome (benign genetic condition); Pancreatic cancer",
        "symptoms_detail": "Yellowing of skin, eyes, and mucous membranes; Dark yellow or brown urine; Pale or clay-coloured stools; Generalised itching; Fatigue and weakness; Abdominal pain especially in right upper quadrant; Fever if infectious cause",
        "precautions": "Avoid alcohol completely; Do not take hepatotoxic medications without supervision; Practise safe sex and avoid sharing needles (Hepatitis B/C prevention); Eat a low-fat, nutritious diet; Get vaccinated against Hepatitis A and B; Maintain good hygiene and drink clean water",
        "medications": "Treatment targets the underlying cause; Antiviral therapy for viral hepatitis; Ursodeoxycholic acid for cholestatic jaundice; Cholestyramine for itch relief; Phototherapy for neonatal jaundice; Surgery or ERCP for bile duct obstruction; Liver transplant for end-stage liver disease",
        "home_remedies": "Increase hydration with water and coconut water; Eat easily digestible, low-fat foods; Sugarcane juice is a traditional remedy; Turmeric in warm water may support liver function",
        "when_to_see_doctor": "Rapid worsening of jaundice; Confusion or altered consciousness (hepatic encephalopathy); Fever with chills (infected bile duct — cholangitis); Severe abdominal pain; Vomiting blood",
        "specialist": "Hepatologist / Gastroenterologist",
        "risk_level": "High",
        "recovery_time": "Depends on underlying cause; infectious hepatitis: 4–8 weeks; obstruction: after procedure"
    },

    "malaria": {
        "overview": "Malaria is a life-threatening infectious disease caused by Plasmodium parasites transmitted through the bites of infected female Anopheles mosquitoes. It is characterised by cyclical fever, chills, and flu-like symptoms and can be fatal if untreated.",
        "causes": "Plasmodium falciparum (most dangerous), P. vivax, P. malariae, P. ovale; Transmission via infected Anopheles mosquito bites; Rarely: blood transfusion, shared needles, or mother to foetus; Travel to endemic areas (sub-Saharan Africa, South Asia, Southeast Asia)",
        "symptoms_detail": "High fever with cyclical pattern (every 48–72 hours); Chills and rigors; Profuse sweating; Severe headache; Nausea, vomiting, and body aches; Anaemia (pallor, fatigue); Splenomegaly (enlarged spleen); Severe malaria: confusion, seizures, respiratory distress",
        "precautions": "Use insecticide-treated mosquito nets while sleeping; Apply DEET-based mosquito repellent on exposed skin; Wear long-sleeved clothing in endemic areas; Take prophylactic antimalarials before travel; Eliminate standing water around home; Use indoor insecticide sprays",
        "medications": "Artemisinin-based combination therapies (ACTs): Artemether-Lumefantrine or Artesunate-Amodiaquine (first-line); Chloroquine for sensitive P. vivax strains; IV Artesunate for severe malaria; Primaquine to prevent relapse (P. vivax and P. ovale); Antipyretics: Paracetamol for fever management",
        "home_remedies": "Stay well hydrated with water, coconut water, ORS; Rest in a cool environment; Cold sponging for high fever; Ensure adequate nutrition during recovery",
        "when_to_see_doctor": "Any suspected malaria — seek same-day medical care; Convulsions or loss of consciousness; Difficulty breathing; Dark coloured urine; Jaundice; Not improving within 24 hours of starting treatment",
        "specialist": "Infectious Disease Specialist / Internal Medicine Physician",
        "risk_level": "High",
        "recovery_time": "Uncomplicated malaria: 3–7 days with ACT; Severe malaria: hospitalisation required"
    },

    "chicken pox": {
        "overview": "Chickenpox (varicella) is a highly contagious viral infection caused by the varicella-zoster virus (VZV). It causes an itchy blister rash that spreads over the body. It is usually mild in children but can be severe in adults and immunocompromised individuals.",
        "causes": "Varicella-zoster virus (VZV) transmitted by direct contact with blisters; Airborne transmission via respiratory droplets; Contact with Shingles blisters; Highly contagious 1–2 days before rash until all blisters crust over; No prior vaccination or infection",
        "symptoms_detail": "Itchy red spots progressing to fluid-filled blisters; Rash appearing in waves on face, scalp, trunk, then limbs; Low-grade fever; Fatigue and loss of appetite; Headache; Spots can appear in mouth, eyelids, and genitals; Blisters eventually crust over within 7–10 days",
        "precautions": "Isolate infected person until all blisters have crusted over; Do not scratch blisters to prevent secondary infection and scarring; Vaccination (Varivax) is the best prevention; Avoid contact with pregnant women, newborns, and immunocompromised individuals; Wash hands frequently; Change bed linens daily",
        "medications": "Acyclovir antiviral: Started within 24 hours of rash in adults and high-risk patients; Antihistamines: Diphenhydramine to relieve itch; Calamine lotion for topical itch relief; Paracetamol for fever (avoid aspirin — Reye syndrome risk); Varicella immunoglobulin (VZIG) for high-risk exposures; VZV vaccine for prevention",
        "home_remedies": "Oatmeal baths to soothe itching; Trim fingernails and wear cotton mittens (especially children); Dab calamine lotion on blisters; Use baking soda paste on itchy spots; Wear loose, cool cotton clothing",
        "when_to_see_doctor": "Bacterial superinfection of blisters (increasing redness, pus, warmth); Difficulty breathing or chest pain (varicella pneumonia); Severe headache, confusion, or stiff neck (encephalitis); Rash near eyes; Immunocompromised patients or pregnant women",
        "specialist": "General Physician / Infectious Disease Specialist for complicated cases",
        "risk_level": "Low",
        "recovery_time": "7–14 days; blisters crust over within 10 days in healthy individuals"
    },

    "typhoid": {
        "overview": "Typhoid fever is a serious bacterial infection caused by Salmonella typhi, typically spread through contaminated food and water. It can cause a prolonged high fever, abdominal pain, and can be life-threatening if untreated with antibiotics.",
        "causes": "Salmonella typhi bacteria in contaminated water or food; Faecal-oral route of transmission; Poor sanitation and hygiene practices; Eating street food in endemic areas; Travel to developing countries without vaccination; Carrier individuals who shed bacteria",
        "symptoms_detail": "Sustained high fever (39–40°C) gradually rising over days; Severe headache; Abdominal pain and tenderness; Constipation (early) or diarrhoea (later); Rose-coloured spots on trunk; Weakness and fatigue; Loss of appetite; Enlarged liver or spleen",
        "precautions": "Drink only safe boiled or bottled water; Avoid raw vegetables, unpeeled fruits, and street food in endemic areas; Practise strict handwashing with soap; Get vaccinated before travel to endemic regions; Use proper sanitation facilities; Avoid consuming food prepared by known typhoid carriers",
        "medications": "Fluoroquinolones: Ciprofloxacin or Ofloxacin (first-line where sensitive); Cephalosporins: Ceftriaxone IV for hospitalised patients; Azithromycin for multidrug-resistant strains; Paracetamol for fever control; Dexamethasone for severe cases with altered consciousness; Full course (7–14 days) is essential to prevent relapse",
        "home_remedies": "Strict bed rest; Consume easily digestible soft foods; Maintain hydration with ORS and coconut water; Cold sponging for high fever; Avoid solid, spicy, or difficult-to-digest foods during illness",
        "when_to_see_doctor": "Fever not reducing after 2–3 days of antibiotics; Severe abdominal pain (intestinal perforation risk); Blood in stools; Confusion or altered consciousness; Any signs of relapse after completing treatment",
        "specialist": "Infectious Disease Specialist / Internal Medicine Physician",
        "risk_level": "High",
        "recovery_time": "7–14 days with effective antibiotic treatment"
    },

    "hepatitis a": {
        "overview": "Hepatitis A is a highly contagious liver infection caused by the Hepatitis A virus (HAV). It is transmitted through contaminated food and water and typically causes a self-limiting illness, though it can occasionally be severe.",
        "causes": "HAV in contaminated water or food (shellfish, raw produce); Poor sanitation and handwashing; Travel to endemic areas; Close contact with infected person; Anal-oral sexual contact; Sharing food or utensils with infected person",
        "symptoms_detail": "Fatigue and weakness; Nausea, vomiting, and abdominal pain; Loss of appetite; Low-grade fever; Jaundice (yellow skin and eyes); Dark urine and pale stools; Intense itching; Joint pain",
        "precautions": "Vaccination (2 doses) provides lifelong protection; Wash hands thoroughly after using toilet and before eating; Drink only safe, treated water; Avoid raw shellfish; Follow safe food handling practices; Maintain good personal hygiene",
        "medications": "No specific antiviral treatment; supportive care is the mainstay; Adequate rest; IV fluids if unable to maintain hydration; Anti-emetics for nausea; Avoid all alcohol and hepatotoxic drugs; Vaccination of close contacts within 2 weeks of exposure",
        "home_remedies": "Rest and avoid strenuous activity; Eat small, frequent, bland meals; Increase fluid intake; Avoid fatty, spicy foods and alcohol; Coconut water for hydration",
        "when_to_see_doctor": "Symptoms not improving after 2 weeks; Severe jaundice; Inability to keep fluids down; Confusion or extreme drowsiness; Known liver disease or immunocompromised status",
        "specialist": "Hepatologist / Gastroenterologist / Infectious Disease Specialist",
        "risk_level": "Medium",
        "recovery_time": "Most recover fully within 2 months; fulminant hepatitis is rare"
    },

    "hepatitis b": {
        "overview": "Hepatitis B is a potentially life-threatening liver infection caused by the Hepatitis B virus (HBV). It can become chronic, leading to cirrhosis, liver failure, or hepatocellular carcinoma. Safe and effective vaccines are available.",
        "causes": "Sexual contact with infected person; Sharing needles or syringes; Mother-to-child transmission during birth; Blood transfusion with unscreened blood; Needle-stick injuries in healthcare workers; Sharing personal items (razors, toothbrushes) with infected person",
        "symptoms_detail": "Fatigue, weakness; Jaundice; Abdominal pain, especially right upper quadrant; Dark urine; Nausea and vomiting; Joint pain; Loss of appetite; Fever (acute phase)",
        "precautions": "Vaccination (3-dose series) is the most effective prevention; Practice safe sex and use condoms; Never share needles, syringes, or personal hygiene items; Ensure blood transfusions use screened blood; Healthcare workers: follow universal precautions; Vaccinate newborns of HBsAg-positive mothers within 12 hours of birth",
        "medications": "Acute HBV: Supportive care; most adults clear it naturally; Chronic HBV antivirals: Tenofovir disoproxil fumarate (TDF) or Entecavir — suppress viral replication; Pegylated interferon-alpha; Regular monitoring of liver function and HBV DNA levels; Liver transplant for end-stage liver disease",
        "home_remedies": "Strict alcohol avoidance; Rest and nutritious diet; Increase fresh vegetables and fruits; Reduce processed foods and fatty meals; Regular light exercise if tolerated",
        "when_to_see_doctor": "Progressive jaundice; Confusion or personality changes (hepatic encephalopathy); Ascites (abdominal fluid accumulation); Unexplained weight loss; Vomiting blood",
        "specialist": "Hepatologist / Infectious Disease Specialist",
        "risk_level": "High",
        "recovery_time": "Acute: resolves in 1–4 months; Chronic: managed long-term with antivirals"
    },

    "hepatitis c": {
        "overview": "Hepatitis C is a bloodborne viral infection causing liver inflammation, often leading to serious liver damage. Unlike Hepatitis B, there is no vaccine, but it is now curable with direct-acting antiviral medications in over 95% of cases.",
        "causes": "Sharing needles or drug equipment; Blood transfusions before routine screening (pre-1992); Needlestick injuries in healthcare settings; Organ transplant from infected donor; Mother-to-child transmission (less common); Unregulated tattooing or piercing",
        "symptoms_detail": "Often asymptomatic for decades (silent disease); Fatigue; Jaundice; Dark urine; Abdominal pain; Nausea; Joint pain; Cirrhosis signs in advanced disease: ascites, spider angiomas, bleeding",
        "precautions": "Never share needles, syringes, or drug paraphernalia; Ensure tattooing and body piercing use sterile equipment; Healthcare workers: follow strict needle-stick prevention protocols; Avoid sharing razors or toothbrushes; Limit alcohol; Screen all adults born between 1945–1965 (high-prevalence cohort)",
        "medications": "Direct-acting antivirals (DAAs): Sofosbuvir-based regimens (Harvoni, Epclusa, Mavyret); 8–12 week course achieves >95% cure rate; Treatment tailored to HCV genotype; Regular liver function and HCV RNA monitoring; Management of cirrhosis complications if present",
        "home_remedies": "Complete alcohol abstinence; Healthy balanced diet low in processed foods; Regular moderate exercise; Adequate sleep; Avoid herbal supplements that may be hepatotoxic",
        "when_to_see_doctor": "All confirmed HCV-positive individuals should see a specialist; Signs of decompensated cirrhosis; Liver cancer surveillance if cirrhosis present; Mental health support as chronic illness affects wellbeing",
        "specialist": "Hepatologist / Gastroenterologist",
        "risk_level": "High",
        "recovery_time": "Curable in 8–12 weeks with DAA therapy in most patients"
    },

    "hepatitis d": {
        "overview": "Hepatitis D (delta hepatitis) is a serious liver disease caused by the Hepatitis D virus (HDV), which only infects people who also have Hepatitis B. Co-infection leads to more severe disease and faster progression to cirrhosis.",
        "causes": "HDV requires HBV for replication — only occurs in HBV-infected individuals; Shared needles or drug equipment; Sexual transmission (less efficient than HBV); Blood-to-blood contact; Mother-to-child transmission (rare)",
        "symptoms_detail": "Severe fatigue; Jaundice; Abdominal pain; Dark urine and pale stools; Nausea and vomiting; Rapid progression of liver disease compared to HBV alone; Signs of fulminant hepatic failure in severe cases",
        "precautions": "Prevention of HBV infection effectively prevents HDV (HBV vaccination); Never share needles; Practice safe sex; Avoid sharing personal hygiene items; HBV-positive patients: avoid co-infection through same precautions",
        "medications": "Pegylated interferon-alpha for 48 weeks (currently most effective treatment); Bulevirtide (entry inhibitor) — newer approved treatment in Europe; Manage HBV with Tenofovir or Entecavir; Liver transplant for decompensated HDV cirrhosis; No specific vaccine for HDV; HBV vaccination prevents HDV",
        "home_remedies": "Complete alcohol abstinence; Nutritious balanced diet; Adequate rest; Regular monitoring as directed by specialist",
        "when_to_see_doctor": "Any HBV patient with worsening liver function; Jaundice worsening rapidly; Signs of liver failure (ascites, confusion); All HDV-positive patients need specialist care",
        "specialist": "Hepatologist / Infectious Disease Specialist",
        "risk_level": "High",
        "recovery_time": "Chronic in most cases; managed long-term; cure difficult to achieve"
    },

    "hepatitis e": {
        "overview": "Hepatitis E is a liver infection caused by the Hepatitis E virus (HEV), primarily transmitted through contaminated water. It is usually self-limiting, but can be severe in pregnant women and immunocompromised patients.",
        "causes": "Contaminated drinking water (main route in developing countries); Consumption of undercooked pork or game meat (zoonotic, in developed countries); Person-to-person contact (less common); Blood transfusions; Vertical mother-to-child transmission",
        "symptoms_detail": "Jaundice; Fatigue and malaise; Loss of appetite; Nausea and vomiting; Abdominal pain (right upper quadrant); Dark urine and pale stools; Low-grade fever; Itching (cholestatic form)",
        "precautions": "Drink only boiled or treated water; Avoid raw or undercooked pork, shellfish, or game meat; Practise good hand hygiene; Ensure clean water sanitation in communities; Pregnant women should avoid endemic areas; HEV vaccine (HEV 239) available in China",
        "medications": "Primarily supportive treatment; most cases self-resolve in 4–6 weeks; Ribavirin for severe or chronic HEV in immunocompromised patients; Pegylated interferon in some chronic cases; Hospitalisation for severe or fulminant cases; IV fluids and nutritional support",
        "home_remedies": "Complete rest; Adequate hydration; Light, easily digestible meals; Avoid alcohol completely; Avoid hepatotoxic drugs",
        "when_to_see_doctor": "Pregnant women with any symptoms — immediate medical attention; Rapidly worsening jaundice; Confusion or altered mental state; Immunocompromised patients with confirmed HEV; Inability to maintain hydration",
        "specialist": "Hepatologist / Infectious Disease Specialist",
        "risk_level": "Medium",
        "recovery_time": "Self-limiting: 4–6 weeks; severe cases (pregnant women) may need hospitalisation"
    },

    "alcoholic hepatitis": {
        "overview": "Alcoholic hepatitis is inflammation of the liver caused by heavy, prolonged alcohol consumption. It represents a spectrum from mild, reversible disease to severe, life-threatening liver failure. Even after diagnosis, continued drinking dramatically worsens outcomes.",
        "causes": "Chronic heavy alcohol consumption (>3–4 drinks/day); Binge drinking; Duration of heavy drinking (>10–20 years is higher risk); Malnutrition; Female sex (increased susceptibility); Genetic variants in alcohol-metabolising enzymes; Pre-existing liver disease",
        "symptoms_detail": "Jaundice; Abdominal pain and tenderness (right upper quadrant); Nausea and vomiting; Fever; Fatigue and weakness; Ascites (abdominal fluid); Loss of appetite; Bleeding tendencies; Confusion (encephalopathy) in severe cases",
        "precautions": "Complete and permanent alcohol cessation — the most critical step; Nutritional rehabilitation with vitamin supplements (thiamine, folate); Regular liver function monitoring; Treat co-existing infections promptly; Attend alcohol cessation programmes or counselling; Hepatitis A and B vaccination",
        "medications": "Prednisolone (corticosteroids) for severe alcoholic hepatitis (Maddrey score ≥32); Pentoxifylline as alternative if steroids contraindicated; Thiamine (B1) supplementation to prevent Wernicke encephalopathy; Nutritional support (enteral feeding if needed); Manage complications (diuretics for ascites, lactulose for encephalopathy); Liver transplant in carefully selected patients",
        "home_remedies": "Complete alcohol abstinence (non-negotiable); High-protein, high-calorie diet; Multivitamin supplementation; Seek psychological support for alcohol dependency",
        "when_to_see_doctor": "Any suspected alcoholic hepatitis — immediate medical care; Jaundice with fever; Confusion or behavioural changes; Vomiting blood; Abdominal swelling; Poor response to initial treatment",
        "specialist": "Hepatologist / Gastroenterologist / Addiction Medicine Specialist",
        "risk_level": "High",
        "recovery_time": "Mild: months with abstinence; Severe: 30-day mortality up to 30% without treatment"
    },

    "tuberculosis": {
        "overview": "Tuberculosis (TB) is a serious infectious disease caused by Mycobacterium tuberculosis bacteria, primarily affecting the lungs. It spreads through the air when an infected person coughs or sneezes. It remains one of the leading infectious disease killers globally.",
        "causes": "Mycobacterium tuberculosis airborne transmission; Close contact with active TB patient; Weakened immunity (HIV, diabetes, malnutrition, immunosuppressants); Overcrowded living conditions; Healthcare worker exposure; Travel to high-prevalence regions",
        "symptoms_detail": "Persistent cough lasting more than 3 weeks (may be blood-stained); Low-grade fever, especially in evenings; Night sweats; Unexplained weight loss; Fatigue and weakness; Chest pain; Shortness of breath; Loss of appetite",
        "precautions": "Complete full TB treatment course — never stop early; Wear mask in high-risk settings; Ensure good ventilation in living spaces; BCG vaccination for newborns in endemic areas; Regular TB screening for high-risk populations; Contact tracing and treatment of latent TB; HIV testing for all TB patients",
        "medications": "Standard DOTS regimen: HRZE (Isoniazid, Rifampicin, Pyrazinamide, Ethambutol) for 2 months, then HR for 4 months (total 6 months); Drug-resistant TB: Bedaquiline, Linezolid, Cycloserine-based regimens; Pyridoxine (B6) supplementation with Isoniazid; Corticosteroids for TB meningitis or pericarditis",
        "home_remedies": "Adequate nutritious diet rich in protein and calories; Sufficient rest during intensive treatment phase; Good ventilation in bedroom; Avoid smoking and alcohol; Sunlight exposure for mood and Vitamin D",
        "when_to_see_doctor": "Cough lasting more than 3 weeks; Coughing up blood; Unexplained weight loss with fever; Any contact with confirmed TB patient; Missed doses — contact healthcare provider immediately; Side effects of anti-TB drugs (yellowing of eyes, vision changes)",
        "specialist": "Pulmonologist / Infectious Disease Specialist",
        "risk_level": "High",
        "recovery_time": "6 months for drug-sensitive TB; 18–24 months for drug-resistant TB"
    },

    "common cold": {
        "overview": "The common cold is a mild viral infection of the upper respiratory tract, most commonly caused by rhinoviruses. It is the most frequent infectious disease in humans and is usually self-limiting, resolving within 7–10 days.",
        "causes": "Rhinoviruses (most common — over 100 types); Coronavirus, parainfluenza, and respiratory syncytial viruses; Direct contact with infected person; Touching contaminated surfaces then touching face; Cold weather and low humidity (facilitates viral spread); Weakened immune system",
        "symptoms_detail": "Runny or stuffy nose; Sneezing; Sore throat; Mild cough; Low-grade fever (more common in children); Watery eyes; Mild headache; Mild fatigue; Loss of taste or smell",
        "precautions": "Wash hands frequently for at least 20 seconds; Avoid touching face with unwashed hands; Cover mouth and nose when coughing or sneezing; Avoid close contact with symptomatic individuals; Disinfect frequently touched surfaces; Stay home when sick to avoid spreading; Maintain good nutrition and adequate sleep",
        "medications": "No curative antiviral treatment; Symptomatic relief: Paracetamol or Ibuprofen for fever and headache; Decongestants: Pseudoephedrine or Oxymetazoline nasal spray; Antihistamines: Diphenhydramine for runny nose; Throat lozenges or gargling with warm salt water; Cough suppressants: Dextromethorphan; Zinc lozenges within 24 hours may shorten duration",
        "home_remedies": "Honey and lemon in warm water for sore throat and cough; Warm chicken soup — proven anti-inflammatory effects; Steam inhalation with eucalyptus oil; Ginger and tulsi tea; Adequate rest and warm fluids; Gargling with warm salt water twice daily",
        "when_to_see_doctor": "High fever above 39.4°C (103°F); Symptoms lasting more than 10 days without improvement; Difficulty breathing or chest pain; Ear pain or symptoms of secondary bacterial sinusitis; Wheezing in known asthmatic patients",
        "specialist": "General Physician",
        "risk_level": "Low",
        "recovery_time": "7–10 days; symptoms peak at days 2–3"
    },

    "pneumonia": {
        "overview": "Pneumonia is an infection of the lungs that inflames air sacs (alveoli), filling them with fluid or pus. It can be caused by bacteria, viruses, or fungi and ranges from mild 'walking pneumonia' to severe, life-threatening illness requiring hospitalisation.",
        "causes": "Bacteria: Streptococcus pneumoniae (most common), Haemophilus influenzae, Mycoplasma pneumoniae; Viruses: Influenza, SARS-CoV-2, RSV; Fungi: Pneumocystis jirovecii (in immunocompromised); Aspiration of food or liquids; Weakened immunity; Advanced age or chronic illness",
        "symptoms_detail": "Cough producing greenish, yellow, or bloody mucus; High fever with chills and sweating; Shortness of breath, even at rest; Sharp chest pain worsening with breathing; Fatigue and loss of appetite; Rapid breathing and heart rate; Confusion or altered consciousness (in elderly); Blue-tinged lips (severe hypoxia)",
        "precautions": "Pneumococcal and influenza vaccinations; Avoid smoking — severely damages lung defence mechanisms; Practise good hand hygiene; Avoid close contact with sick individuals; Treat respiratory infections promptly; Aspiration precautions in bedridden or neurologically impaired patients",
        "medications": "Bacterial pneumonia: Amoxicillin-Clavulanate or Azithromycin (outpatient); Ceftriaxone + Azithromycin (inpatient); Respiratory fluoroquinolones: Levofloxacin; Antiviral: Oseltamivir for influenza pneumonia; Antifungal: TMP-SMX for PCP pneumonia; Supplemental oxygen and IV fluids as needed; Hospitalisation for severe cases",
        "home_remedies": "Complete bed rest; Stay well hydrated; Warm steam inhalation to loosen mucus; Prop up on pillows to ease breathing; Warm ginger and honey tea; Avoid cold air and smoking",
        "when_to_see_doctor": "Any suspected pneumonia — do not delay seeking care; Oxygen saturation below 94%; Breathing rate above 30/minute; Confusion or altered mental status; Failure to improve after 48 hours of antibiotics; Elderly, infants, or immunocompromised individuals",
        "specialist": "Pulmonologist / Infectious Disease Specialist",
        "risk_level": "High",
        "recovery_time": "Mild outpatient: 1–3 weeks; Severe hospitalised: 4–6 weeks"
    },

    "dengue": {
        "overview": "Dengue fever is a mosquito-borne viral disease caused by any of four dengue virus serotypes (DENV 1–4), transmitted by Aedes aegypti and Aedes albopictus mosquitoes. Severe dengue (dengue haemorrhagic fever) can be life-threatening.",
        "causes": "Dengue virus transmitted through bite of infected Aedes mosquito; Aedes mosquitoes breed in clean stagnant water (flower pots, containers, tyres); Four serotypes exist — infection with one does not protect against others; Subsequent infection with a different serotype increases risk of severe dengue; No person-to-person transmission",
        "symptoms_detail": "Sudden high fever (39–40°C); Severe headache, especially behind eyes; Intense muscle and joint pain ('breakbone fever'); Skin rash appearing 3–5 days after fever; Nausea, vomiting, and abdominal pain; Mild bleeding (nose, gums); Fatigue; Dengue haemorrhagic fever: severe bleeding, plasma leakage, shock",
        "precautions": "Eliminate Aedes mosquito breeding sites (empty standing water containers regularly); Use mosquito repellents containing DEET or Picaridin; Use mosquito nets and window screens; Wear full-sleeved clothing; Aedes mosquitoes bite primarily during daytime; Dengvaxia vaccine available for those with prior dengue infection",
        "medications": "No specific antiviral treatment; Paracetamol for fever — AVOID aspirin and NSAIDs (bleeding risk); Adequate oral hydration with ORS and fluids; IV fluid resuscitation in severe dengue with plasma leakage; Platelet transfusion only in severe haemorrhagic dengue; Careful monitoring of platelet count and haematocrit",
        "home_remedies": "Drink plenty of fluids including coconut water, ORS, papaya leaf juice (may help platelet count); Complete rest; Cool sponging for high fever; Monitor for warning signs daily; Papaya leaf extract is traditionally used to raise platelet count",
        "when_to_see_doctor": "Warning signs: severe abdominal pain, persistent vomiting, rapid breathing, bleeding gums, blood in urine or stools; Platelet count below 100,000/mm³; Signs of shock: cold clammy skin, rapid weak pulse; Confusion or altered consciousness; Any dengue with underlying medical conditions",
        "specialist": "Infectious Disease Specialist / Internal Medicine Physician",
        "risk_level": "High",
        "recovery_time": "7–10 days for uncomplicated dengue; severe dengue requires hospitalisation"
    },

    "heart attack": {
        "overview": "A heart attack (myocardial infarction) occurs when blood flow to a part of the heart muscle is blocked, usually by a blood clot in a coronary artery. Without prompt treatment, the affected heart muscle begins to die. It is a medical emergency.",
        "causes": "Coronary artery disease (atherosclerosis — plaque buildup); Coronary artery spasm; Hypertension; Diabetes mellitus; Smoking; High cholesterol (LDL); Obesity and sedentary lifestyle; Family history of heart disease; Stress and psychological factors",
        "symptoms_detail": "Chest pain or pressure radiating to left arm, jaw, neck, or back; Shortness of breath; Cold sweats; Nausea and vomiting; Lightheadedness or sudden dizziness; Palpitations; Fatigue (especially in women); Sense of impending doom; Women may have atypical symptoms (fatigue, jaw pain) without classic chest pain",
        "precautions": "CALL EMERGENCY SERVICES IMMEDIATELY if heart attack is suspected; Control blood pressure, diabetes, and cholesterol; Quit smoking; Follow a heart-healthy diet; Exercise regularly; Maintain healthy weight; Take prescribed medications consistently (antiplatelet, statins); Attend cardiac rehabilitation after a heart attack",
        "medications": "Acute: Aspirin 300mg immediately (chew and swallow); Clopidogrel or Ticagrelor (antiplatelet); Thrombolytics: Alteplase if PCI not available within 120 min; Primary PCI (coronary angioplasty with stent) is gold standard; Beta-blockers: Metoprolol; ACE inhibitors: Ramipril; Statins: Atorvastatin at high dose; Anticoagulants: Heparin or Enoxaparin",
        "home_remedies": "This is a medical emergency — NO home remedies replace emergency care; While waiting for ambulance: Rest in comfortable position; Chew aspirin if not allergic and not contraindicated; Loosen tight clothing; Do not eat or drink anything; Keep patient calm",
        "when_to_see_doctor": "CALL EMERGENCY SERVICES (ambulance) IMMEDIATELY; Do not drive yourself to the hospital; Time is muscle — every minute matters; Do not wait to see if symptoms improve on their own",
        "specialist": "Cardiologist / Emergency Medicine Physician",
        "risk_level": "High",
        "recovery_time": "6–8 weeks for physical recovery; cardiac rehabilitation 3–6 months; lifelong management"
    },

    "urinary tract infection": {
        "overview": "A urinary tract infection (UTI) is an infection in any part of the urinary system — kidneys, ureters, bladder, and urethra. Most infections involve the lower urinary tract (bladder and urethra). UTIs are far more common in women.",
        "causes": "Escherichia coli bacteria (80% of UTIs); Staphylococcus saprophyticus (young sexually active women); Klebsiella, Proteus species; Sexual activity; Female anatomy (shorter urethra); Urinary catheter use; Kidney stones; Diabetes or immunosuppression; Menopause (reduced oestrogen)",
        "symptoms_detail": "Burning sensation or pain during urination (dysuria); Frequent, urgent need to urinate; Passing small amounts of urine frequently; Cloudy, strong-smelling, or bloody urine; Pelvic pain or discomfort (women); Lower back or flank pain (kidney infection); Fever, chills (upper UTI/pyelonephritis)",
        "precautions": "Drink at least 2–2.5 litres of water daily; Urinate after sexual intercourse; Wipe front to back after using the toilet; Avoid feminine hygiene sprays and douches; Wear cotton underwear; Change underwear daily; Empty bladder fully when urinating; Do not hold urine for long periods",
        "medications": "Uncomplicated UTI: Nitrofurantoin 5 days or Trimethoprim-Sulfamethoxazole 3 days or Fosfomycin single dose; Pyelonephritis: Ciprofloxacin or Ceftriaxone 7–14 days; Culture-guided antibiotic selection; Phenazopyridine for urinary pain relief (not antibiotic); Recurrent UTIs: Low-dose prophylactic antibiotics or post-coital antibiotics",
        "home_remedies": "Increase water intake significantly; Unsweetened cranberry juice (may reduce adherence of bacteria); D-Mannose supplements; Avoid caffeine, alcohol, and spicy foods during infection; Apply warm heating pad to abdomen for comfort",
        "when_to_see_doctor": "Fever with back pain (possible kidney infection — pyelonephritis); Symptoms not improving after 48 hours of antibiotics; Recurrent UTIs (3 or more per year); UTI in men (always warrants investigation); UTI in pregnancy; Blood in urine",
        "specialist": "Urologist / Gynaecologist (for recurrent UTIs in women)",
        "risk_level": "Medium",
        "recovery_time": "Simple UTI: 3–7 days with antibiotics; pyelonephritis: 10–14 days"
    },

    "psoriasis": {
        "overview": "Psoriasis is a chronic autoimmune skin condition that causes the rapid buildup of skin cells, resulting in scaling on the skin surface. It is characterised by red, itchy, scaly patches and follows a relapsing-remitting course triggered by various factors.",
        "causes": "Autoimmune dysregulation (T-cell mediated); Genetic predisposition (30–40% have family history); Triggers: stress, infections (Streptococcal sore throat), skin injury (Koebner phenomenon), certain medications (lithium, beta-blockers), alcohol, smoking; Cold weather; Obesity",
        "symptoms_detail": "Red raised plaques with silvery-white scales; Most common on elbows, knees, scalp, and lower back; Dry, cracked skin that may bleed; Itching, burning, or soreness; Thickened, pitted, or ridged nails (nail psoriasis); Joint pain and swelling (psoriatic arthritis in 30%); Scalp scaling and flaking",
        "precautions": "Identify and avoid personal triggers; Moisturise skin daily with thick emollients; Avoid scratching or picking at plaques; Protect skin from cuts and injuries; Limit alcohol and quit smoking; Manage stress with relaxation techniques; Sun exposure in moderation may help (avoid sunburn)",
        "medications": "Topical: Corticosteroid creams (Betamethasone); Vitamin D analogues: Calcipotriol; Calcineurin inhibitors: Tacrolimus; Coal tar preparations; Phototherapy: Narrowband UVB (very effective); Systemic: Methotrexate, Cyclosporine, Acitretin; Biologics: Adalimumab, Secukinumab, Ixekizumab for moderate-severe disease",
        "home_remedies": "Daily moisturising with fragrance-free emollients; Oatmeal baths to soothe inflammation; Dead Sea salt baths; Aloe vera gel applied topically; Omega-3 fatty acids (fish oil) may reduce inflammation; Turmeric supplementation",
        "when_to_see_doctor": "Psoriasis covering large areas of the body; Significant joint pain (psoriatic arthritis); Not responding to topical treatments; Significant psychological impact; Pustular or erythrodermic psoriasis (urgent)",
        "specialist": "Dermatologist / Rheumatologist (for psoriatic arthritis)",
        "risk_level": "Medium",
        "recovery_time": "Chronic lifelong condition; treatment achieves remission in weeks to months"
    },

    "impetigo": {
        "overview": "Impetigo is a highly contagious, superficial bacterial skin infection most common in children. It causes sores that quickly rupture, ooze for a few days, and then form a yellowish-brown crust. It is usually not serious but spreads easily.",
        "causes": "Staphylococcus aureus (most common); Group A Streptococcus; Enters through cuts, insect bites, or compromised skin; Direct contact with infected person's sores or contaminated items; Hot, humid environments; Poor hygiene; Crowded settings (schools, daycare)",
        "symptoms_detail": "Red sores, usually around nose and mouth (non-bullous); Honey-coloured crusts after sores rupture; Itching; Bullous impetigo: larger fluid-filled blisters; Swollen lymph nodes near infection site; Sores on hands and feet also common; Rarely painful",
        "precautions": "Wash hands frequently; Keep child's nails cut short to prevent spreading by scratching; Cover sores with loose gauze or bandage; Do not share towels, bedding, or clothing; Keep infected child home from school until non-contagious (24 hours of antibiotics); Wash contaminated items in hot water",
        "medications": "Topical: Mupirocin ointment (Bactroban) for localised disease — 5 days; Fusidic acid cream; Oral antibiotics for extensive disease: Flucloxacillin or Cefalexin 5–7 days; Amoxicillin-Clavulanate for mixed infections; MRSA-directed therapy if resistant",
        "home_remedies": "Gently clean sores with warm soapy water and remove crusts; Apply antibacterial soap; Loose cotton clothing to avoid irritation; Do not lance or pop blisters",
        "when_to_see_doctor": "Sores spreading rapidly or not responding to topical treatment after 3 days; Fever accompanying skin infection; Deeply painful sores; Suspected MRSA infection; Recurrent impetigo",
        "specialist": "Dermatologist / Paediatrician for children",
        "risk_level": "Low",
        "recovery_time": "7–10 days with appropriate antibiotic treatment"
    },

    "dimorphic hemorrhoids": {
        "overview": "Haemorrhoids (piles) are swollen veins in the rectum or anus. Dimorphic haemorrhoids refer to a combination of both internal and external haemorrhoids. They cause rectal bleeding, pain, and discomfort and are extremely common.",
        "causes": "Chronic straining during bowel movements; Constipation or chronic diarrhoea; Low-fibre diet; Prolonged sitting (especially on toilet); Pregnancy (increased pressure on pelvic veins); Obesity; Heavy lifting; Genetic predisposition; Ageing",
        "symptoms_detail": "Bright red blood during bowel movements (on tissue or in bowl); Itching and irritation in the anal region; Pain or discomfort, especially while sitting; Swelling around anus; Feeling of incomplete bowel emptying; Mucus discharge; Prolapsed haemorrhoid felt as lump at anus",
        "precautions": "Eat a high-fibre diet (25–38g/day); Drink at least 2 litres of water daily; Do not strain during bowel movements; Avoid sitting on toilet for prolonged periods; Exercise regularly to prevent constipation; Lose weight if overweight; Avoid heavy lifting",
        "medications": "Topical agents: Hydrocortisone creams, Lidocaine gels for pain relief; Oral pain relief: Ibuprofen or Paracetamol; Fibre supplements: Ispaghula husk (Metamucil); Stool softeners: Docusate sodium or Lactulose; Procedures for persistent haemorrhoids: Rubber band ligation, Sclerotherapy, Haemorrhoidectomy",
        "home_remedies": "Warm sitz baths (sitting in warm water) 3–4 times daily; Cold ice pack for 15 minutes for external swelling; Witch hazel applied topically with cotton pad; Aloe vera gel applied to external haemorrhoids; Psyllium husk supplementation daily",
        "when_to_see_doctor": "Significant rectal bleeding (always needs evaluation to rule out other causes); Severe pain not relieved by simple measures; Prolapsed haemorrhoid that cannot be pushed back; Thrombosed external haemorrhoid; Symptoms persisting beyond 1 week of conservative treatment",
        "specialist": "Colorectal Surgeon / Gastroenterologist",
        "risk_level": "Medium",
        "recovery_time": "Mild cases: 1–2 weeks with conservative care; surgical: 2–4 weeks recovery"
    },

    "hypothyroidism": {
        "overview": "Hypothyroidism is a condition where the thyroid gland does not produce enough thyroid hormone (T3 and T4), slowing down many of the body's functions. It is more common in women and the elderly.",
        "causes": "Hashimoto's thyroiditis (autoimmune — most common cause); Thyroid surgery or radioiodine treatment; Iodine deficiency; Certain medications (Lithium, Amiodarone); Pituitary gland disorders; Congenital hypothyroidism; Postpartum thyroiditis",
        "symptoms_detail": "Fatigue and sluggishness; Weight gain despite no change in diet; Cold intolerance; Constipation; Dry skin and hair; Hair loss; Slowed heart rate; Puffy face (myxoedema); Depression; Impaired memory; Muscle weakness and aches; Irregular or heavy menstrual periods",
        "precautions": "Take levothyroxine at the same time daily, on empty stomach; Avoid calcium, iron supplements, or antacids within 4 hours of thyroid medication; Regular TSH level monitoring every 6–12 months; Inform all doctors about thyroid condition; Maintain iodine-adequate diet; Do not stop medication without medical guidance",
        "medications": "Levothyroxine (LT4): Synthetic thyroid hormone — gold standard treatment; Liothyronine (LT3) in select patients; Dose adjusted based on TSH levels; Combination T4/T3 therapy in some patients; Regular monitoring of TSH, Free T4, and T3 levels",
        "home_remedies": "Ensure adequate iodine intake (iodised salt, seafood); Selenium-rich foods (Brazil nuts) support thyroid function; Regular moderate exercise; Reduce stress; Ashwagandha (with doctor approval) may support thyroid function",
        "when_to_see_doctor": "Symptoms persisting despite being on levothyroxine; Myxoedema coma (severe hypothyroidism — emergency); Planning pregnancy (requires dose adjustment); Chest pain or heart rate changes; Significant weight changes or mood disturbances",
        "specialist": "Endocrinologist",
        "risk_level": "Medium",
        "recovery_time": "Symptoms improve within 2–3 months of correct dosing; lifelong treatment required"
    },

    "hyperthyroidism": {
        "overview": "Hyperthyroidism is a condition where the thyroid gland produces too much thyroid hormone, accelerating the body's metabolism. Graves' disease is the most common cause. Without treatment, it can cause serious heart problems.",
        "causes": "Graves' disease (autoimmune — most common); Toxic thyroid nodules or multinodular goitre; Thyroiditis (subacute or postpartum); Excessive iodine intake; Overtreatment with thyroid medication; TSH-secreting pituitary tumour (rare)",
        "symptoms_detail": "Unexplained weight loss despite increased appetite; Rapid or irregular heartbeat (palpitations); Anxiety, nervousness, and irritability; Increased sweating and heat intolerance; Tremor in hands and fingers; Enlarged thyroid (goitre); Changes in menstrual cycle; Fatigue and muscle weakness; Difficulty sleeping; Bulging eyes (Graves' ophthalmopathy)",
        "precautions": "Avoid excess iodine (iodine-rich foods, contrast dyes, supplements); Avoid stimulants: caffeine, nicotine; Monitor heart rate and report irregularities; Protect eyes from sunlight in Graves' ophthalmopathy (sunglasses); Regular thyroid function monitoring; Do not skip medications",
        "medications": "Antithyroid drugs: Methimazole (first-line) or Propylthiouracil (PTU in pregnancy); Beta-blockers: Propranolol for symptomatic relief (palpitations, tremor); Radioactive iodine (RAI) therapy for definitive treatment; Surgery (thyroidectomy) for large goitre or failure of other treatments; Thyroid eye disease: Selenium, corticosteroids, or orbital decompression",
        "home_remedies": "Avoid iodine-rich foods (excess seaweed, kelp); Yoga and meditation to reduce anxiety; Cooling foods and clothing in heat intolerance; Adequate rest; Anti-inflammatory diet",
        "when_to_see_doctor": "Rapid irregular heartbeat (atrial fibrillation risk); Thyroid storm (emergency): high fever, extreme agitation, heart failure; Eye pain or protruding eyes; Significant weight loss; Any new or worsening symptoms",
        "specialist": "Endocrinologist",
        "risk_level": "Medium",
        "recovery_time": "Symptom control within weeks; definitive treatment: months; lifelong monitoring"
    },

    "hypoglycaemia": {
        "overview": "Hypoglycaemia (low blood sugar, <70 mg/dL) occurs when blood glucose drops below the level needed for normal body function. It is most common in people with diabetes on insulin or certain oral medications but can occur in non-diabetics.",
        "causes": "Excessive insulin or antidiabetic medication dose; Missed or delayed meal; Unusual physical activity; Alcohol consumption without eating; Insulinoma (rare insulin-producing tumour); Severe liver or kidney disease; Prolonged fasting; Post-bariatric surgery reactive hypoglycaemia",
        "symptoms_detail": "Shakiness, trembling, and sweating; Rapid heartbeat and palpitations; Hunger; Anxiety and irritability; Pale skin; Dizziness or lightheadedness; Weakness and fatigue; Difficulty concentrating; Confusion or unusual behaviour; Severe: loss of consciousness or seizures",
        "precautions": "Never skip meals, especially when on insulin or antidiabetic drugs; Carry fast-acting sugar (glucose tablets, sweets, juice) at all times; Monitor blood glucose regularly; Wear medical alert identification; Inform family members how to respond to severe hypoglycaemia; Adjust medication before unusual physical activity (consult doctor)",
        "medications": "Mild-moderate: 15–20g fast-acting glucose — 4 glucose tablets, 150ml fruit juice, or 3–4 sweets; Retest after 15 minutes (Rule of 15); Severe: Glucagon injection (GlucaGen) by bystander if unconscious; IV Dextrose 50% in hospital setting; Review and adjust antidiabetic medication doses to prevent recurrence",
        "home_remedies": "Immediately consume fast-acting sugar; Follow with complex carbohydrate snack (biscuits, toast); Rest until symptoms fully resolve; Record episode in glucose diary to share with doctor; If recurrent, identify triggers with help of dietitian",
        "when_to_see_doctor": "Loss of consciousness or seizure (call emergency services immediately); Hypoglycaemia unresponsive to oral glucose after two attempts; Recurrent unexplained hypoglycaemia in non-diabetic; Hypoglycaemia occurring at night or during sleep; Medication dose review needed",
        "specialist": "Endocrinologist / Diabetologist",
        "risk_level": "High",
        "recovery_time": "Blood sugar normalises within 15–20 minutes of treatment; underlying cause needs addressing"
    },

    "osteoarthritis": {
        "overview": "Osteoarthritis (OA) is the most common form of arthritis, involving the gradual breakdown of joint cartilage and underlying bone. It most often affects the knees, hips, hands, and spine, causing pain and reduced mobility.",
        "causes": "Age-related cartilage degeneration; Obesity (excess load on weight-bearing joints); Previous joint injuries; Repetitive joint stress (occupational or sports); Genetic predisposition; Weak supporting muscles; Female sex (especially post-menopause); Metabolic conditions",
        "symptoms_detail": "Joint pain worsening with activity and improving with rest; Stiffness, especially in the morning (usually less than 30 minutes); Swelling or tenderness around the joint; Grating sensation (crepitus) on movement; Reduced range of motion; Bone spurs (osteophytes) visible on X-ray; Muscle weakness around affected joint",
        "precautions": "Maintain healthy body weight to reduce joint load; Regular low-impact exercise (swimming, cycling, walking); Strengthen muscles around joints with physiotherapy; Avoid repetitive high-impact activities; Use supportive footwear; Joint protection techniques in daily activities; Avoid prolonged static postures",
        "medications": "Paracetamol for mild pain; Topical NSAIDs: Diclofenac gel (preferred for knee OA); Oral NSAIDs: Ibuprofen or Naproxen (with PPI protection); Intra-articular corticosteroid injections for flares; Intra-articular hyaluronic acid (viscosupplementation); Duloxetine for centralised pain; Joint replacement surgery for end-stage OA",
        "home_remedies": "Hot/cold therapy on affected joints; Weight loss — 10% body weight reduction halves knee OA pain; Turmeric with black pepper (curcumin) supplementation; Omega-3 fatty acids; Epsom salt baths; Tai chi and yoga improve balance and reduce pain",
        "when_to_see_doctor": "Severe or rapidly worsening joint pain; Joint swelling with redness and warmth (infection or gout flare); Night pain disrupting sleep; Significant functional limitation in daily activities; Falls or instability due to joint weakness; Considering joint replacement surgery",
        "specialist": "Rheumatologist / Orthopaedic Surgeon",
        "risk_level": "Medium",
        "recovery_time": "Chronic condition; symptoms managed, not cured; surgery recovery: 3–6 months"
    },

    "arthritis": {
        "overview": "Arthritis is an umbrella term for over 100 conditions causing joint inflammation, pain, stiffness, and damage. The two most common types are osteoarthritis (degenerative) and rheumatoid arthritis (autoimmune).",
        "causes": "Osteoarthritis: Age and wear; Rheumatoid arthritis: Autoimmune; Gout: Uric acid crystal deposition; Psoriatic arthritis: Associated with psoriasis; Infectious arthritis: Bacterial or viral joint infection; Lupus arthritis; Reactive arthritis; Ankylosing spondylitis",
        "symptoms_detail": "Joint pain, tenderness, and swelling; Morning stiffness (especially prolonged in RA); Warmth and redness over joints; Reduced range of motion; Fatigue (in inflammatory arthritis); Joint deformity in advanced disease; Systemic symptoms in RA: fever, weight loss",
        "precautions": "Regular appropriate exercise to maintain joint mobility; Maintain healthy body weight; Physical and occupational therapy; Joint protection techniques; Regular monitoring of disease activity; Annual cardiovascular and bone density assessment in RA; Vaccinations (flu, pneumococcal) before starting immunosuppressants",
        "medications": "RA: DMARDs (Methotrexate first-line); Biologic agents (TNF inhibitors: Adalimumab, Etanercept; IL-6 inhibitors: Tocilizumab); JAK inhibitors: Baricitinib; Corticosteroids: Prednisolone for flares; NSAIDs for symptomatic relief; Gout: Allopurinol for prevention, Colchicine or NSAIDs for acute attacks",
        "home_remedies": "Warm bath or heat application for stiffness; Cold packs for swollen joints; Anti-inflammatory diet (omega-3 rich foods); Turmeric and ginger supplementation; Regular gentle exercise (yoga, swimming); Adequate rest during flares",
        "when_to_see_doctor": "Persistent joint swelling and pain lasting more than 6 weeks; New joint swelling with fever (infectious arthritis — emergency); Unable to perform daily activities; Starting or changing DMARD or biologic therapy; Joint deformity progressing",
        "specialist": "Rheumatologist",
        "risk_level": "Medium",
        "recovery_time": "Chronic; symptoms controlled with treatment; flares managed acutely"
    },

    "paroymsal positional vertigo": {
        "overview": "Benign Paroxysmal Positional Vertigo (BPPV) is one of the most common causes of vertigo — a sudden, brief sensation that the room is spinning. It occurs when small calcium crystals in the inner ear dislodge and enter the semicircular canals.",
        "causes": "Dislodged otoconia (calcium carbonate crystals) in semicircular canals; Head injury or trauma; Inner ear disorders (labyrinthitis, Meniere's disease); Prolonged bed rest or inactivity; Ageing (most common after 50); Sometimes no identifiable cause (idiopathic)",
        "symptoms_detail": "Brief episodes of intense vertigo triggered by head position changes; Spinning or rolling sensation lasting seconds to minutes; Nausea and sometimes vomiting; Unsteadiness or loss of balance; Nystagmus (involuntary eye movements during episode); No hearing loss or tinnitus in typical BPPV",
        "precautions": "Move slowly when changing head positions; Avoid positions that trigger vertigo; Sleep with head slightly elevated; Hold onto stable surfaces when standing up; Use handrails on stairs; Avoid driving during active episodes; Inform employer if vertigo affects work safety",
        "medications": "BPPV is primarily treated with repositioning manoeuvres, not medication; Epley manoeuvre (canalith repositioning) is 80–90% effective; Semont manoeuvre as alternative; Vestibular suppressants (Meclizine, Dimenhydrinate) for nausea only — short-term; Vestibular rehabilitation therapy; Surgery (canal plugging) is a last resort",
        "home_remedies": "Brandt-Daroff exercises at home (self-treatment vestibular exercises); Rise slowly from lying or sitting; Avoid neck extension positions; Stay well hydrated; Reduce caffeine and alcohol which can worsen vestibular symptoms",
        "when_to_see_doctor": "Vertigo not resolving after Epley manoeuvre; Vertigo with hearing loss or ear fullness (Meniere's disease); Vertigo with double vision, weakness, or numbness (central cause — urgent); Recurrent episodes over weeks; Falls or injury due to vertigo",
        "specialist": "ENT (Otolaryngologist) / Neurologist / Vestibular Physiotherapist",
        "risk_level": "Low",
        "recovery_time": "Most resolve with 1–3 Epley manoeuvres within days to weeks; may recur"
    },

    "acne": {
        "overview": "Acne vulgaris is a common chronic skin condition that occurs when hair follicles become plugged with oil (sebum) and dead skin cells. It leads to blackheads, whiteheads, pimples, and cysts, primarily on the face, chest, and back.",
        "causes": "Excess sebum production (androgenic influence); Clogged hair follicles; Proliferation of Cutibacterium acnes (C. acnes) bacteria; Hormonal changes (puberty, menstrual cycle, PCOS, pregnancy); Certain medications (steroids, lithium); Stress; High-glycaemic diet; Genetic predisposition",
        "symptoms_detail": "Whiteheads and blackheads (comedones); Papules (small red, tender bumps); Pustules (pimples with pus); Nodules (large, solid, painful lumps); Cysts (painful, pus-filled lumps causing scarring); Oily skin; Post-inflammatory hyperpigmentation; Acne scars",
        "precautions": "Wash face twice daily with gentle, non-comedogenic cleanser; Do not pick, squeeze, or pop pimples; Use oil-free, non-comedogenic moisturisers and makeup; Remove makeup before sleeping; Change pillowcase frequently; Avoid touching face; Manage stress; Reduce high-glycaemic foods and dairy",
        "medications": "Topical: Benzoyl peroxide; Retinoids (Tretinoin, Adapalene); Topical antibiotics (Clindamycin); Azelaic acid; Oral: Antibiotics (Doxycycline or Minocycline) for moderate-severe; Oral contraceptives (hormonal acne in women); Spironolactone; Isotretinoin (Accutane) for severe nodular acne — highly effective",
        "home_remedies": "Apply tea tree oil diluted with carrier oil; Aloe vera gel as soothing topical; Zinc supplementation may reduce inflammation; Green tea extract topically; Ice wrapped in cloth to reduce inflamed pimples; Honey and cinnamon mask (antibacterial properties)",
        "when_to_see_doctor": "Severe nodular or cystic acne causing significant scarring; Acne significantly impacting mental health or self-esteem; No improvement with 3 months of OTC treatments; Acne in adults with suspected hormonal cause (PCOS); Starting isotretinoin (requires monitoring)",
        "specialist": "Dermatologist",
        "risk_level": "Low",
        "recovery_time": "Significant improvement in 8–12 weeks with treatment; Isotretinoin: 4–6 month course"
    },

    "urticaria": {
        "overview": "Urticaria (hives) is a skin reaction characterised by raised, itchy welts (wheals) on the skin surface that appear and disappear within hours. It can be acute (less than 6 weeks) or chronic (more than 6 weeks) and is often allergic in origin.",
        "causes": "Allergic: Foods (nuts, shellfish, eggs), medications (penicillin, aspirin), insect stings; Non-allergic: Infections, stress, cold or heat exposure, pressure, sun; Idiopathic (cause unknown in >50% of chronic cases); Autoimmune (autoimmune urticaria); Underlying conditions (thyroid disease, lupus)",
        "symptoms_detail": "Raised, red or skin-coloured itchy welts of varying sizes; Welts appear suddenly and move around the body; Burning or stinging sensation; Individual wheals typically resolve within 24 hours; Angioedema: deeper swelling of lips, eyes, hands, or genitals; Anaphylaxis: throat swelling, breathing difficulty (emergency)",
        "precautions": "Identify and strictly avoid triggers; Keep antihistamines readily available; Wear cool, loose-fitting cotton clothing; Avoid NSAIDs, which can worsen urticaria; Avoid excessive heat, tight clothing, or scratching; Carry EpiPen if history of anaphylaxis; Keep a symptom and food diary to identify triggers",
        "medications": "Second-generation antihistamines: Cetirizine, Loratadine, or Fexofenadine (first-line); Higher doses or multiple antihistamines for chronic urticaria; Omalizumab (anti-IgE biologic) for refractory chronic urticaria; Short course oral corticosteroids for severe acute urticaria; Epinephrine for anaphylaxis",
        "home_remedies": "Cool compresses or ice packs on welts; Cool oatmeal bath; Calamine lotion for itch relief; Avoid scratching; Wear loose cool clothing; Aloe vera gel application",
        "when_to_see_doctor": "Throat or tongue swelling with difficulty swallowing or breathing (anaphylaxis — call emergency services); Urticaria persisting more than 6 weeks (chronic urticaria needs investigation); Not responding to antihistamines after 48 hours; Associated joint pain or fever; First-time severe episode",
        "specialist": "Allergist / Immunologist / Dermatologist",
        "risk_level": "Medium",
        "recovery_time": "Acute: resolves in hours to days; Chronic: months to years; majority resolve within 5 years"
    },

}

# ─────────────────────────────────────────────────────────────────────────────
# LOOKUP FUNCTION
# Returns disease info or a generic structured placeholder.
# Performs fuzzy-ish matching (lowercase, strip) for robustness.
# ─────────────────────────────────────────────────────────────────────────────
def get_disease_info(disease_name: str) -> dict:
    key = disease_name.strip().lower()
    # Exact match first
    if key in DISEASE_DB:
        return DISEASE_DB[key]
    # Partial / substring match
    for db_key, info in DISEASE_DB.items():
        if db_key in key or key in db_key:
            return info
    # Generic fallback — still has proper structure
    return {
        "overview": (
            f"{disease_name.title()} is a medical condition that requires clinical evaluation "
            f"by a qualified healthcare professional for accurate diagnosis and treatment planning."
        ),
        "causes": (
            "Specific causes vary and require clinical investigation; "
            "Genetic predisposition may play a role; "
            "Environmental or lifestyle factors; "
            "Underlying comorbidities"
        ),
        "symptoms_detail": (
            "Symptoms depend on the specific presentation; "
            "General malaise and fatigue; "
            "Discomfort in affected area; "
            "Please consult a doctor for a full symptom assessment"
        ),
        "precautions": (
            "Do not self-diagnose or self-medicate; "
            "Consult a licensed medical professional promptly; "
            "Maintain good general health — balanced diet, hydration, sleep; "
            "Rest and avoid strenuous activity until evaluated; "
            "Keep a record of symptoms, onset, and severity to share with your doctor"
        ),
        "medications": (
            "Treatment must be prescribed by a qualified physician after proper examination; "
            "Do not take over-the-counter medications without professional guidance; "
            "Follow prescribed dosing schedule completely"
        ),
        "home_remedies": (
            "Adequate rest; "
            "Stay well hydrated with water and clear fluids; "
            "Eat light, nutritious, easily digestible meals; "
            "Monitor symptoms and document any changes"
        ),
        "when_to_see_doctor": (
            "Symptoms are severe, sudden, or rapidly worsening; "
            "High fever persists beyond 48 hours; "
            "Difficulty breathing, chest pain, or altered consciousness; "
            "Any symptom causing significant distress or limiting daily function"
        ),
        "specialist": "General Physician (refer to specialist after initial evaluation)",
        "risk_level": "Medium",
        "recovery_time": "Varies — determined by diagnosis and treatment"
    }
