# Marketing Campaign Optimization: A/B Testing & Predictive Insights
> **Business Case:** Evaluating Bidding Strategies to Maximize ROAS and Conversion Efficiency.

## 📌 Project Overview
This project performs a deep-dive A/B test analysis between two marketing bidding strategies: **Campaign A (Control)** and **Campaign B (Test)**. Beyond basic conversion metrics, this analysis implements rigorous statistical "guardrails"—including **Power Analysis** and **Sample Ratio Mismatch (SRM)** detection—to ensure data-driven recommendations are mathematically sound and business-ready.

## 🛠️ The Technical Toolkit
- **Analysis:** Python (Pandas, NumPy)
- **Statistics:** Statsmodels (Z-Test, Power Analysis), SciPy (Chi-Square, Pearson Correlation)
- **Visualization:** Seaborn, Matplotlib

---

## 🛡️ Data Integrity & Experiment Audit
*Before analyzing performance, I audited the experiment's health to prevent "False Positives."*

1. **Power Analysis:** Confirmed the experiment was "Overpowered" with **340k+ total interactions**, far exceeding the required sample size of ~12.5k for a 5% effect size.
2. **SRM Detection (The Critical Catch):** - A Chi-Square test revealed a severe **Sample Ratio Mismatch (p < 0.01)**. 
   - Traffic was unevenly split (159k vs 180k), suggesting potential bias in the randomization engine.
3. **Mitigation:** I implemented **Proportional Downsampling** to equalize group sizes, ensuring that Campaign B's "win" in raw volume didn't mask a failure in conversion efficiency.

---

## 🔍 Key Business Questions & Findings

### Q1: Which campaign has the highest conversion efficiency?
* **Result:** **Campaign A** (Control).
* **Stats:** After balancing samples, Campaign A achieved a superior conversion rate. The **Z-statistic of 11.56 (p=0.0000)** proves this isn't random.
* **Metric:** Campaign B showed a **-12.06% Relative Lift** compared to A.

### Q2: Which campaign is more cost-effective (ROAS)?
* **Result:** **Campaign A**.
* **Finding:** Campaign A generated **$11.42 per $1 spent**, while Campaign B generated only $10.17. 
* **Impact:** Using Campaign A saves the company nearly $1.25 in ad spend for every dollar of revenue generated.

### Q3: Do "Clicky" ads lead to more sales? (CTR vs. Purchase Rate)
* **Finding:** **No.** Both campaigns showed a **negative correlation** (A: -0.62, B: -0.35).
* **Analysis:** High Click-Through Rates (CTR) are actually correlating with *lower* purchase rates. This suggests the ads may be "clickbait," attracting low-intent users who bounce upon reaching the landing page.

---

## 🚀 Final Strategic Recommendation
**Action: Terminate Test Campaign (B) and scale Control Campaign (A).**

While Campaign B drives higher raw traffic, it is less efficient. 
1. **Prioritize Quality over Quantity:** Campaign A’s bidding strategy attracts higher-intent users with a 12% better conversion lift.
2. **Optimize the Funnel:** The negative CTR/Purchase correlation indicates a "Leaky Funnel." I recommend a UX audit of the landing page to better align ad messaging with the checkout experience.

---

## 📂 Project Structure
```text
├── data/
│   ├── Control_group.csv  # Campaign A Data
│   └── Test_group.csv     # Campaign B Data
├── notebooks/
│   └── ab_test_analysis.ipynb # Full Python Workflow & Statistical Audit
├── visuals/               # Data Visualizations & Z-Distributions
└── README.md              # Executive Summary
