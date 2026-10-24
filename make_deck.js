const pptxgen = require("pptxgenjs");
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.title = "Personal Health Digital Twin";
const NAVY = "12263A", TEAL = "1F9D8A", LIGHT = "F4F8FA", GREY = "4A5B6B";
const F = "Calibri";

function base(title) {
  const s = pres.addSlide();
  s.background = { color: "FFFFFF" };
  s.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 10, h: 0.9, fill: { color: NAVY }, line: { color: NAVY } });
  s.addText(title, { x: 0.5, y: 0.1, w: 9, h: 0.7, fontFace: F, fontSize: 26, bold: true, color: "FFFFFF", margin: 0, isTextBox: true });
  s.addText("CRP Digital Twin Challenge 2026 | Ayush Kakulte, IIIT Jabalpur", { x: 0.5, y: 5.25, w: 9, h: 0.3, fontFace: F, fontSize: 10, color: GREY, margin: 0, isTextBox: true });
  return s;
}
function bullets(s, items, opt = {}) {
  s.addText(items.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < items.length - 1 } })),
    Object.assign({ x: 0.6, y: 1.2, w: 8.8, h: 3.8, fontFace: F, fontSize: 18, color: NAVY, paraSpaceAfter: 10, valign: "top", isTextBox: true }, opt));
}

// 1 Title
let s = pres.addSlide();
s.background = { color: NAVY };
s.addText("Personal Health Digital Twin", { x: 0.7, y: 1.5, w: 8.6, h: 1, fontFace: F, fontSize: 40, bold: true, color: "FFFFFF", isTextBox: true });
s.addText("Simulate lifestyle changes before you commit to them", { x: 0.7, y: 2.5, w: 8.6, h: 0.6, fontFace: F, fontSize: 20, color: "8FD6C9", isTextBox: true });
s.addText("CRP Digital Twin Challenge 2026 (Happiest Health)\nAyush Kakulte  |  IIIT Jabalpur", { x: 0.7, y: 3.7, w: 8.6, h: 1, fontFace: F, fontSize: 14, color: "D5DEE6", isTextBox: true });

// 2 Problem
s = base("Problem");
bullets(s, [
  "Chronic lifestyle conditions (hypertension, prediabetes, obesity) build up silently over months",
  "People get generic advice and cannot see how their own habits change their own numbers",
  "Check-ups are snapshots; there is no way to test 'what if I sleep more and walk daily?'",
  "Our question: how can people see in advance how their own habits will change their own health markers?",
]);

// 3 Use case
s = base("Healthcare Use Case: Preventive Care");
bullets(s, [
  "Individual: enter profile and habits, see projected BP, glucose, heart rate, weight and risk",
  "Compare 'current habits' vs a 'what-if plan' side by side over 30-365 days",
  "Coach / clinician: use the twin to motivate and personalise lifestyle plans",
  "Focus: prevention and early behaviour change, not diagnosis",
]);

// 4 Solution
s = base("Our Solution");
bullets(s, [
  "A virtual copy of the user's key health markers that evolves day by day",
  "Inputs: steps, sleep, calories, sodium, stress",
  "Outputs: weight, systolic BP, fasting glucose, resting HR and a 0-100 risk score",
  "Transparent, explainable model: every coefficient is readable and editable",
  "Delivered as a Streamlit dashboard and a CLI demo, with unit tests",
]);

// 5 Architecture
s = base("Architecture");
s.addImage({ path: "architecture.png", x: 0.9, y: 1.0, w: 8.2, h: 4.15 });

// 6 Model
s = base("Model and AI/ML Framework");
bullets(s, [
  "Mechanistic state-space model: weight from energy balance (Mifflin-St Jeor BMR + activity, 7700 kcal/kg)",
  "BP, glucose and heart rate relax toward lifestyle-dependent targets (30-day time constant)",
  "Composite risk score from banded biomarkers (BP, glucose, BMI, HR, age)",
  "Stack: Python, NumPy, pandas, Streamlit, pytest",
  "Honest status: coefficients are illustrative, not yet clinically validated; ML calibration is on the roadmap",
], { fontSize: 16 });

// 7 Results (native chart)
s = base("Outcome: Day-90 Simulation");
s.addChart(pres.charts.BAR, [
  { name: "Current habits", labels: ["Systolic BP", "Glucose", "Resting HR", "Risk score"], values: [120.6, 93.0, 77.6, 24.5] },
  { name: "What-if plan", labels: ["Systolic BP", "Glucose", "Resting HR", "Risk score"], values: [111.0, 84.0, 66.9, 11.1] },
], { x: 0.5, y: 1.1, w: 5.6, h: 3.9, barDir: "col", chartColors: ["B0BEC5", TEAL], showLegend: true, legendPos: "b", legendFontFace: F,
     showValue: true, dataLabelFontSize: 10, dataLabelPosition: "outEnd", catAxisLabelFontFace: F, valAxisLabelFontFace: F,
     valGridLine: { color: "E3E8EC", size: 0.5 }, catGridLine: { style: "none" }, showTitle: true, title: "Default profile, 90 days", titleFontFace: F, titleFontSize: 12 });
s.addText([
  { text: "Healthier plan vs current habits", options: { bold: true, breakLine: true } },
  { text: "9,000 steps, 7.5 h sleep, 2,200 kcal, 2.3 g sodium, low stress", options: { breakLine: true } },
  { text: " ", options: { breakLine: true } },
  { text: "Weight -5.2 kg", options: { breakLine: true } },
  { text: "Systolic BP -9.5 mmHg", options: { breakLine: true } },
  { text: "Glucose -9.0 mg/dL", options: { breakLine: true } },
  { text: "Risk score -13.4 points" },
], { x: 6.3, y: 1.3, w: 3.3, h: 3.5, fontFace: F, fontSize: 14, color: NAVY, valign: "top", isTextBox: true });

// 8 Roadmap
s = base("Roadmap, Privacy and Impact");
bullets(s, [
  "Calibrate to real wearable and lab data per user; add uncertainty bands (Monte Carlo)",
  "Learn target functions from public datasets; clinician and coaching views",
  "Privacy by design: no PII stored, computation local, consent-first data connection",
  "Educational prototype; not a medical device and not medical advice",
  "Impact: earlier, more motivated prevention at low cost",
], { fontSize: 16 });

pres.writeFile({ fileName: "presentation.pptx" }).then(() => console.log("done"));
