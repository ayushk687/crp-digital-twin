"""Personal health digital twin: a simple, transparent daily state-space model.

State (per day): weight, systolic BP, fasting glucose, resting HR.
Inputs: Lifestyle (steps, sleep, calories, sodium, stress).
Each biomarker relaxes toward a lifestyle-dependent target (first-order dynamics),
so changes appear gradually, like real physiology.

NOT a medical device. Coefficients are illustrative, not clinically validated.
"""
from __future__ import annotations
from dataclasses import dataclass
import pandas as pd


@dataclass(frozen=True)
class Profile:
    age: int = 35
    sex: str = "male"            # "male" | "female"
    height_cm: float = 172.0
    weight_kg: float = 82.0
    systolic_bp: float = 128.0
    fasting_glucose: float = 102.0   # mg/dL
    resting_hr: float = 72.0

    @property
    def bmi(self) -> float:
        return self.weight_kg / (self.height_cm / 100) ** 2


@dataclass(frozen=True)
class Lifestyle:
    steps: float = 5000.0        # per day
    sleep_h: float = 6.0
    calories: float = 2500.0     # kcal intake per day
    sodium_g: float = 4.0        # per day
    stress: float = 6.0          # 0 (calm) .. 10 (very high)


def bmr(p: Profile, weight: float) -> float:
    """Mifflin-St Jeor basal metabolic rate (kcal/day)."""
    s = 5 if p.sex == "male" else -161
    return 10 * weight + 6.25 * p.height_cm - 5 * p.age + s


def energy_expenditure(p: Profile, weight: float, l: Lifestyle) -> float:
    return bmr(p, weight) * 1.2 + l.steps * 0.04 * (weight / 70.0)


def _bmi(p: Profile, weight: float) -> float:
    return weight / (p.height_cm / 100) ** 2


def targets(p: Profile, weight: float, l: Lifestyle) -> dict:
    bmi = _bmi(p, weight)
    sleep_debt = max(0.0, 7.5 - l.sleep_h)
    activity = min(l.steps, 12000) / 1000.0
    bp = (108 + 0.9 * max(0, bmi - 22) + 1.5 * max(0, l.sodium_g - 2.3)
          + 0.8 * l.stress + 1.0 * sleep_debt - 0.6 * activity + 0.15 * (p.age - 30))
    glu = (82 + 1.4 * max(0, bmi - 22) + 1.5 * sleep_debt + 0.6 * l.stress
           - 0.9 * activity + 0.1 * (p.age - 30))
    hr = 78 - 1.6 * activity + 0.9 * l.stress + 1.2 * sleep_debt + 0.2 * max(0, bmi - 25)
    return {"systolic_bp": bp, "fasting_glucose": glu, "resting_hr": hr}


class HealthTwin:
    def __init__(self, profile: Profile, tau_days: float = 30.0):
        self.p = profile
        self.k = 1.0 / tau_days
        self.state = {
            "weight_kg": profile.weight_kg,
            "systolic_bp": profile.systolic_bp,
            "fasting_glucose": profile.fasting_glucose,
            "resting_hr": profile.resting_hr,
        }

    def step(self, l: Lifestyle) -> dict:
        s = self.state
        s["weight_kg"] += (l.calories - energy_expenditure(self.p, s["weight_kg"], l)) / 7700.0
        for key, tgt in targets(self.p, s["weight_kg"], l).items():
            s[key] += self.k * (tgt - s[key])
        return dict(s)


def simulate(profile: Profile, lifestyle: Lifestyle, days: int = 90) -> pd.DataFrame:
    from .risk import risk_score
    twin = HealthTwin(profile)
    rows = []
    for d in range(days + 1):
        st = dict(twin.state)
        st["bmi"] = _bmi(profile, st["weight_kg"])
        st["day"] = d
        st["risk"] = risk_score(profile.age, st)
        rows.append(st)
        twin.step(lifestyle)
    return pd.DataFrame(rows).set_index("day")


def compare(profile: Profile, baseline: Lifestyle, plan: Lifestyle, days: int = 90):
    a, b = simulate(profile, baseline, days), simulate(profile, plan, days)
    return a, b, (b.iloc[-1] - a.iloc[-1])
