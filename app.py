import streamlit as st
from twin import Profile, Lifestyle, compare, risk_band

st.set_page_config(page_title="Health Digital Twin", layout="wide")
st.title("Personal Health Digital Twin")
st.caption("Illustrative what-if simulator. Not medical advice.")

with st.sidebar:
    st.header("Your profile")
    age = st.slider("Age", 18, 80, 35)
    sex = st.selectbox("Sex", ["male", "female"])
    h = st.number_input("Height (cm)", 140.0, 210.0, 172.0)
    w = st.number_input("Weight (kg)", 40.0, 200.0, 82.0)
    bp = st.number_input("Systolic BP (mmHg)", 90.0, 200.0, 128.0)
    glu = st.number_input("Fasting glucose (mg/dL)", 60.0, 250.0, 102.0)
    hr = st.number_input("Resting HR (bpm)", 40.0, 120.0, 72.0)
    days = st.slider("Horizon (days)", 30, 365, 90)


def lifestyle_inputs(label, d):
    st.subheader(label)
    return Lifestyle(
        steps=st.slider("Steps/day", 1000, 20000, int(d.steps), 500, key=label + "s"),
        sleep_h=st.slider("Sleep (h)", 4.0, 10.0, float(d.sleep_h), 0.5, key=label + "sl"),
        calories=st.slider("Calories", 1200, 4000, int(d.calories), 50, key=label + "c"),
        sodium_g=st.slider("Sodium (g)", 1.0, 8.0, float(d.sodium_g), 0.1, key=label + "na"),
        stress=st.slider("Stress (0-10)", 0.0, 10.0, float(d.stress), 0.5, key=label + "st"),
    )


c1, c2 = st.columns(2)
with c1:
    base = lifestyle_inputs("Current habits", Lifestyle())
with c2:
    plan = lifestyle_inputs("What-if plan", Lifestyle(9000, 7.5, 2200, 2.3, 3))

p = Profile(age, sex, h, w, bp, glu, hr)
a, b, d = compare(p, base, plan, days)

metrics = [("Weight", "weight_kg", "kg"), ("Systolic BP", "systolic_bp", "mmHg"),
           ("Glucose", "fasting_glucose", "mg/dL"), ("Resting HR", "resting_hr", "bpm"),
           ("Risk", "risk", "/100")]
for col, (name, key, unit) in zip(st.columns(5), metrics):
    col.metric(name, f"{b[key].iloc[-1]:.1f} {unit}", f"{d[key]:+.1f} vs current habits",
               delta_color="inverse")
st.write(f"Risk band: **{risk_band(a.risk.iloc[-1])}** -> **{risk_band(b.risk.iloc[-1])}**")

for _, key, _ in metrics:
    chart = a[[key]].rename(columns={key: "current"}).join(b[[key]].rename(columns={key: "plan"}))
    st.line_chart(chart, height=180)
