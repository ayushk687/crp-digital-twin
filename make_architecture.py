"""Generates docs/architecture.pdf (and .png). Run: python docs/make_architecture.py"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(13, 7.5))
ax.set_xlim(0, 13); ax.set_ylim(0, 7.5); ax.axis("off")

def box(x, y, w, h, title, lines, fc, ec):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04,rounding_size=0.12",
                                fc=fc, ec=ec, lw=1.6))
    ax.text(x + w / 2, y + h - 0.28, title, ha="center", va="center", fontsize=11, fontweight="bold", color="#12263a")
    for i, t in enumerate(lines):
        ax.text(x + w / 2, y + h - 0.7 - i * 0.3, t, ha="center", va="center", fontsize=8.5, color="#2b3a4a")

def arrow(x1, y1, x2, y2, label=""):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="-|>", lw=1.6, color="#37506b"))
    if label:
        ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.17, label, ha="center", fontsize=8, color="#37506b", style="italic")

ax.text(6.5, 7.15, "Personal Health Digital Twin - System Architecture", ha="center", fontsize=16, fontweight="bold", color="#12263a")

# Inputs
box(0.3, 4.35, 2.7, 2.1, "1. Data Inputs", ["Profile: age, sex, height, weight", "Vitals: BP, glucose, resting HR", "Lifestyle: steps, sleep, kcal,", "sodium, stress","CSV / wearable: roadmap"], "#e8f1fb", "#3b7dd8")
# Twin core
box(4.0, 4.35, 3.2, 2.1, "2. Twin Core", ["twin/model.py", "Daily state-space simulation", "Energy balance -> weight", "First-order relaxation (tau = 30 d)", "-> BP, glucose, resting HR"], "#e9f7ef", "#2e9d62")
# Risk
box(8.2, 4.35, 2.2, 2.1, "3. Risk Engine", ["twin/risk.py", "Banded composite", "score 0-100", "-> Low / Moderate / High"], "#fff4e0", "#e69a1f")
# Scenario
box(4.0, 2.1, 3.2, 1.6, "4. Scenario Comparison", ["compare(baseline, plan)", "Current habits vs what-if plan", "Deltas at horizon (30-365 d)"], "#f3e9fb", "#8a4fd0")
# UI
box(8.2, 2.1, 4.5, 1.6, "5. User Interfaces", ["Streamlit dashboard (app.py)", "CLI demo (python -m twin.demo)", "Metric cards + trend charts"], "#fdeaea", "#d04f4f")
# Roadmap
box(0.3, 2.1, 2.7, 1.6, "Roadmap: AI/ML layer", ["Per-user calibration of coefficients", "Monte Carlo uncertainty bands", "Learned targets() from data"], "#f2f2f2", "#8c8c8c")
# Governance
box(0.3, 0.3, 12.4, 1.2, "Privacy, Safety & Governance", ["No PII stored; all computation local to the session  |  Consent-first design for wearable data  |  Educational prototype - not a medical device, not medical advice"], "#eef3f7", "#5b7083")

arrow(3.0, 5.5, 4.0, 5.5, "inputs")
arrow(7.2, 5.5, 8.2, 5.5, "biomarkers")
arrow(5.6, 4.35, 5.6, 3.7, "simulate x2")
arrow(7.2, 2.9, 8.2, 2.9, "results")
arrow(9.3, 4.35, 9.3, 3.7, "risk")
ax.annotate("", xy=(4.0, 2.9), xytext=(3.0, 2.9), arrowprops=dict(arrowstyle="-|>", lw=1.2, color="#8c8c8c", ls="--"))

fig.savefig("docs/architecture.pdf", bbox_inches="tight")
fig.savefig("docs/architecture.png", dpi=170, bbox_inches="tight")
