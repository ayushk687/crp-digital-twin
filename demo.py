"""CLI demo: python -m twin.demo"""
from .model import Profile, Lifestyle, compare
from .risk import risk_band


def main():
    p = Profile()
    base = Lifestyle()
    plan = Lifestyle(steps=9000, sleep_h=7.5, calories=2200, sodium_g=2.3, stress=3)
    a, b, d = compare(p, base, plan, 90)
    print("Day-90 outcome (current habits -> healthier plan)")
    for col in ["weight_kg", "systolic_bp", "fasting_glucose", "resting_hr", "risk"]:
        print(f"{col:16s} {a[col].iloc[-1]:7.1f} -> {b[col].iloc[-1]:7.1f}  ({d[col]:+.1f})")
    print("Risk band:", risk_band(a.risk.iloc[-1]), "->", risk_band(b.risk.iloc[-1]))
    print("\nIllustrative model, not medical advice.")


if __name__ == "__main__":
    main()
