from twin import Profile, Lifestyle, simulate, compare


def test_healthier_plan_improves_outcomes():
    a, b, d = compare(Profile(), Lifestyle(), Lifestyle(9000, 7.5, 2200, 2.3, 3), 90)
    assert d["weight_kg"] < 0 and d["systolic_bp"] < 0
    assert d["fasting_glucose"] < 0 and d["risk"] < 0


def test_length_and_bounds():
    df = simulate(Profile(), Lifestyle(), 30)
    assert len(df) == 31 and df.risk.between(0, 100).all()


def test_weight_changes_with_surplus():
    df = simulate(Profile(), Lifestyle(calories=4000), 30)
    assert df.weight_kg.iloc[-1] > df.weight_kg.iloc[0]
