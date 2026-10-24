# Architecture

```
Profile + Lifestyle inputs --> HealthTwin (daily state-space model) --> time series --> risk_score --> band
Streamlit UI (app.py) <-- compare(baseline, plan) --> deltas at horizon
```

- **Twin state:** weight, systolic BP, fasting glucose, resting HR (BMI derived).
- **Dynamics:** weight follows energy balance (7700 kcal/kg, Mifflin-St Jeor BMR + steps).
  Other biomarkers relax toward lifestyle-dependent targets with a 30-day time constant.
- **Risk:** transparent weighted composite of banded biomarkers (0-100).
- **Diagram:** see `architecture.pdf`.
- **Extending:** replace `targets()` with a learned model; calibrate per user from wearable data;
  add uncertainty bands via Monte Carlo over inputs.

## Limitations
Coefficients are illustrative, not clinically validated. Not a medical device.
