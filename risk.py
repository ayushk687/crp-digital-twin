"""Transparent composite risk indicator (0-100). Illustrative only."""

def _band(x, lo, hi):
    """0 at/below lo, 1 at/above hi, linear between."""
    return float(min(1.0, max(0.0, (x - lo) / (hi - lo))))


def risk_score(age: int, s: dict) -> float:
    parts = {
        "bp": 0.30 * _band(s["systolic_bp"], 115, 160),
        "glucose": 0.30 * _band(s["fasting_glucose"], 90, 126),
        "bmi": 0.25 * _band(s["bmi"], 23, 35),
        "hr": 0.10 * _band(s["resting_hr"], 60, 90),
        "age": 0.05 * _band(age, 25, 70),
    }
    return round(100 * sum(parts.values()), 1)


def risk_band(score: float) -> str:
    return "Low" if score < 25 else "Moderate" if score < 50 else "High" if score < 75 else "Very high"
