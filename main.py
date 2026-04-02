import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.power import NormalIndPower
from scipy.stats import norm, chisquare

# 1. Data Loading
A_df = pd.read_csv(r"D:\DEVELOPMENT\PROJECTS\AB Testing\data\control_group.csv", sep=';') 
B_df = pd.read_csv(r"D:\DEVELOPMENT\PROJECTS\AB Testing\data\test_group.csv", sep=';') 

# Handling missing values
A_df = A_df.fillna(A_df.mean(numeric_only=True))
B_df = B_df.fillna(B_df.mean(numeric_only=True))

# core metrics
total_purchases_A = A_df['# of Purchase'].sum()
total_clicks_A = A_df['# of Website Clicks'].sum()
total_purchases_B = B_df['# of Purchase'].sum()
total_clicks_B = B_df['# of Website Clicks'].sum()

# --- 2. EXPERIMENT AUDIT  ---
# Check Sample Ratio Mismatch (SRM)
observed_traffic = [total_clicks_A, total_clicks_B]
total_traffic = sum(observed_traffic)
expected_traffic = [total_traffic / 2, total_traffic / 2]
_, srm_p_value = chisquare(f_obs=observed_traffic, f_exp=expected_traffic)

print("--- STEP 1: DATA INTEGRITY AUDIT ---")
if srm_p_value < 0.01:
    print(f"CRITICAL WARNING: SRM Detected (p={srm_p_value:.4f}).")
    print("The traffic split is severely biased. In a live environment, we would stop here.")
else:
    print(f"PASSED: No SRM detected (p={srm_p_value:.4f}).")

# --- 3. MITIGATION & BALANCED Z-TEST ---
# Proportional downsampling to mitigate bias
scaling_factor = total_clicks_A / total_clicks_B
balanced_purchases_B = round(total_purchases_B * scaling_factor)
balanced_clicks_B = round(total_clicks_A) 

# Running the Balanced Z-Test
successes = np.array([round(total_purchases_A), balanced_purchases_B])
trials = np.array([round(total_clicks_A), balanced_clicks_B])
z_stat, p_value = proportions_ztest(successes, trials, alternative='two-sided')

# Calculating Relative Lift based on balanced numbers
conv_A = successes[0] / trials[0]
conv_B = successes[1] / trials[1]
relative_lift = (conv_B - conv_A) / conv_A

print("\n--- STEP 2: MITIGATION & BALANCED RESULTS (Q1) ---")
print(f"Mitigation: Proportional downsampling to {total_clicks_A:.0f} users per group.")
print(f"Balanced Z-statistic: {z_stat:.4f} | Balanced P-value: {p_value:.4f}")
print(f"Relative Lift: {relative_lift:.2%}")

# Visuals: Balanced Conversion Rate comparison
# plt.figure(figsize=(6,4))
# sns.barplot(x=['A', 'B'], y=[conv_A*100, conv_B*100],hue=['A', 'B'], palette='Blues',legend=False)
# plt.title('Balanced Conversion Rate Comparison (%)')
# plt.ylabel('Conversion Rate (%)')
# plt.show()

# --- 4. FINANCIAL ANALYSIS (Q2: ROAS) ---
AOV = 50 # Assumed Average Order Value
A_total_revenue = total_purchases_A * AOV
B_total_revenue = total_purchases_B * AOV

A_roas = A_total_revenue / A_df['Spend [USD]'].sum()
B_roas = B_total_revenue / B_df['Spend [USD]'].sum()

print("\n--- Q2 Results: Financial Impact ---")
print(f"Campaign A ROAS: {A_roas:.2f} | Campaign B ROAS: {B_roas:.2f}")

# Visuals: ROAS Comparison
# plt.figure(figsize=(6,4))
# sns.barplot(x=['A', 'B'], y=[A_roas, B_roas],hue=['A', 'B'], palette='Greens',legend=False)
# plt.title('Return on Ad Spend (ROAS) Comparison')
# plt.ylabel('ROAS ($)')
# plt.show()

# --- 5. ENGAGEMENT CORRELATIONS (Q3: Impressions vs Purchases) ---
A_corr = A_df['# of Impressions'].corr(A_df['# of Purchase'])
B_corr = B_df['# of Impressions'].corr(B_df['# of Purchase'])

print("\n--- Q3 Results: Impression Correlation ---")
print(f"Correlation (Impression vs Purchase) -> A: {A_corr:.2f}, B: {B_corr:.2f}")

# Visuals: Regression Analysis for Impressions
# fig, axes = plt.subplots(1, 2, figsize=(12, 5))
# sns.regplot(x='# of Impressions', y='# of Purchase', data=A_df, ax=axes[0], line_kws={'color':'red'})
# axes[0].set_title(f'A (Corr: {A_corr:.2f})')
# sns.regplot(x='# of Impressions', y='# of Purchase', data=B_df, ax=axes[1], line_kws={'color':'red'})
# axes[1].set_title(f'B (Corr: {B_corr:.2f})')
# plt.suptitle('Correlation: Impressions vs Purchases')
# plt.show()

# --- 6. BEHAVIORAL CORRELATIONS (Q4: CTR vs Purchase Rate) ---
A_df['CTR'] = (A_df['# of Website Clicks'] / A_df['# of Impressions']) * 100
B_df['CTR'] = (B_df['# of Website Clicks'] / B_df['# of Impressions']) * 100
A_df['PR'] = (A_df['# of Purchase'] / A_df['# of Website Clicks']) * 100
B_df['PR'] = (B_df['# of Purchase'] / B_df['# of Website Clicks']) * 100

A_corr_ctr = A_df['CTR'].corr(A_df['PR'])
B_corr_ctr = B_df['CTR'].corr(B_df['PR'])

print("\n--- Q4 Results: CTR vs Purchase Rate ---")
print(f"Correlation (CTR vs PR) -> A: {A_corr_ctr:.2f}, B: {B_corr_ctr:.2f}")

# Visuals: Regression Analysis for CTR
# fig, axes = plt.subplots(1, 2, figsize=(12, 5))
# sns.regplot(x='CTR', y='PR', data=A_df, ax=axes[0], color='darkgreen')
# axes[0].set_title(f'A (Corr: {A_corr_ctr:.2f})')
# sns.regplot(x='CTR', y='PR', data=B_df, ax=axes[1], color='darkblue')
# axes[1].set_title(f'B (Corr: {B_corr_ctr:.2f})')
# plt.suptitle('Correlation: CTR vs Purchase Rate')
# plt.show()

# --- 7. FINAL STATISTICAL PROOF ---
# Visuals: Final Hypothesis Test Distribution
# x_axis = np.linspace(-4, 4, 1000)
# plt.figure(figsize=(10, 5))
# plt.plot(x_axis, norm.pdf(x_axis, 0, 1), label='Standard Normal Distribution', color='gray')
# plt.fill_between(x_axis, norm.pdf(x_axis, 0, 1), where=(x_axis <= -1.96) | (x_axis >= 1.96), color='red', alpha=0.3, label='Rejection Region (0.05)')
# plt.axvline(z_stat, color='darkred', linestyle='--', label=f'Actual Z-stat: {z_stat:.2f}')
# plt.title('Z-Distribution & Hypothesis Test Verdict')
# plt.legend()
# plt.show()
