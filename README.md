# Personal Health Digital Twin

**CRP Digital Twin Challenge 2026 (Happiest Health)** – Prototype & Code Submission

## 1. Team Details
| Field | Details |
|---|---|
| Team name | `<TEAM NAME, if any>` |
| Team leader | Ayush Kakulte, ayushkakulte818@gmail.com |
| Members | Ayush Kakulte (Team Leader) |
| Unstop registration / team ID | `<ID>` |

## 2. College / Incubator Information
- Institution / incubator: IIIT Jabalpur
- Department / program: `<DEPARTMENT / YEAR>`
- City, State: Jabalpur, Madhya Pradesh

## 3. Project Title
**Personal Health Digital Twin: a what-if simulator for preventive lifestyle care**

## 4. Problem Statement
**How can individuals see, in advance, how their own daily habits will change their own health markers,
so that preventive lifestyle changes become concrete and motivating instead of generic?**

Lifestyle-driven conditions (hypertension, prediabetes, obesity) develop silently over months. People receive
generic advice, and check-ups are snapshots in time, so nobody can see how *their* sleep, activity, diet,
salt intake and stress will change *their* blood pressure, glucose, heart rate and weight. There is no
low-cost way to test "what if I change my habits?" before committing to the change.

**Challenge theme:** Digital Twin (CRP Digital Twin Challenge 2026, Happiest Health). We build a personal
health digital twin that answers this question.

## 5. Healthcare Use Case
**Preventive care and lifestyle-medicine decision support.**
- An individual enters a profile (age, sex, height, weight, BP, fasting glucose, resting HR) and habits
  (steps, sleep, calories, sodium, stress).
- The twin projects weight, systolic BP, glucose, resting HR and a 0-100 risk score over 30-365 days.
- The user compares **current habits** vs a **what-if plan** before committing to a change.
- Health coaches / clinicians can use it to personalise and motivate lifestyle plans.
- Scope: prevention and behaviour change. Not diagnosis or treatment.

## 6. Technical Stack
| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Numerics / data | NumPy, pandas |
| UI | Streamlit (dashboard), CLI demo |
| Testing | pytest |
| Docs / diagrams | matplotlib (architecture), pptxgenjs (deck) |

## 7. AI/ML Model or Framework Details
- **Framework:** hybrid-ready digital twin. The current prototype is a *mechanistic state-space model*
  (transparent and explainable), designed so the target functions can be replaced by learned models.
- **Dynamics (`twin/model.py`):**
  - Weight follows energy balance: Mifflin-St Jeor BMR x 1.2 + step expenditure vs intake, 7700 kcal/kg.
  - Systolic BP, fasting glucose and resting HR relax toward lifestyle-dependent targets
    (first-order, 30-day time constant).
- **Risk (`twin/risk.py`):** weighted, banded composite of BP, glucose, BMI, HR and age (0-100).
- **Validation status:** coefficients are illustrative and **not clinically validated**.
- **AI/ML roadmap:** per-user calibration from wearable/lab data, learned target functions trained on public
  datasets, Monte Carlo uncertainty bands.
- Architecture detail: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)

## 8. Demo Video (15-20 minutes, Unlisted YouTube)
**Link:** `<PASTE UNLISTED YOUTUBE URL HERE>`

## 9. Open-source License Details
Released under the **MIT License**. See [`LICENSE`](LICENSE).

## 10. Architecture Diagram (PDF)
[`docs/architecture.pdf`](docs/architecture.pdf)  (preview: `docs/architecture.png`)

![Architecture](docs/architecture.png)

## 11. Presentation (PDF/PPT)
- PDF: [`docs/presentation.pdf`](docs/presentation.pdf)
- PPT: [`docs/presentation.pptx`](docs/presentation.pptx)

## 12. Public Accessibility
This repository, the demo video (unlisted link) and every file linked above are publicly accessible
without additional permissions.

---

## Quick Start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m twin.demo        # CLI demo
streamlit run app.py       # dashboard
pytest                     # tests
```

### Sample output (default profile, 90 days, current habits -> healthier plan)
```
weight_kg           84.1 ->    78.9  (-5.2)
systolic_bp        120.6 ->   111.0  (-9.5)
fasting_glucose     93.0 ->    84.0  (-9.0)
resting_hr          77.6 ->    66.9  (-10.6)
risk                24.5 ->    11.1  (-13.4)
```

## Repository Layout
```
twin/model.py        twin dynamics and simulation
twin/risk.py         risk score and bands
twin/demo.py         CLI demo
app.py               Streamlit dashboard
tests/               unit tests
docs/architecture.*  architecture diagram (PDF/PNG) + generator script
docs/presentation.*  project presentation (PDF/PPTX) + generator script
```

## Disclaimer
Educational prototype. Not a medical device and not medical advice. Consult a qualified clinician for health decisions.
