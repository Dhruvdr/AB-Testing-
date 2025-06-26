import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import norm

# Loading the Data
A_df = pd.read_csv(r"D:\DEVELOPMENT\PROJECTS\AB Testing\data\control_group.csv",sep=';') 
B_df = pd.read_csv(r"D:\DEVELOPMENT\PROJECTS\AB Testing\data\test_group.csv",sep=';') 

# print(A_df.head())
# print(B_df.head())
# print(A_df.columns)           #'Campaign Name', 'Date', 'Spend [USD]', '# of Impressions', 'Reach','# of Website Clicks', '# of Searches', '# of View Content','# of Add to Cart', '# of Purchase'],

#                               QUESTION 1
# Calculating Conversion Rate 
A_df['Purchase_Conversion_rate'] = (A_df['# of Purchase'] / A_df['# of Website Clicks'])*100
B_df['Purchase_Conversion_rate'] = (B_df['# of Purchase'] / B_df['# of Website Clicks'])*100

# Calculating the Average Conversion rate
A_avg_conv_rate = A_df['Purchase_Conversion_rate'].mean()
B_avg_conv_rate = B_df['Purchase_Conversion_rate'].mean()

# Output the conversion rates for both campaigns
# print(f"Average Purchase Conversion Rate for Campaign A: {A_avg_conv_rate:.2f}%")
# print(f"Average Purchase Conversion Rate for Campaign B: {B_avg_conv_rate:.2f}%")

# # Visualization 
# conv_data = pd.DataFrame({
#     'Campaign' : ['A' , 'B'],
#     'Conversion Rate': [A_avg_conv_rate,B_avg_conv_rate]
# })

# plt.figure(figsize=(8,6))
# sns.barplot(x='Campaign', y='Conversion Rate', data = conv_data , palette='Blues')
# plt.title('Comparison of Conversion Rates Between Campaign A and B')
# plt.ylabel('Conversion Rate(%)')
# plt.show()

# Calculate the total number of purchases and website clicks for both campaigns
total_purchases_A = A_df['# of Purchase'].sum()
total_clicks_A = A_df['# of Website Clicks'].sum()

total_purchases_B = B_df['# of Purchase'].sum()
total_clicks_B = B_df['# of Website Clicks'].sum()

# Conversion rate (proportion of purchases to clicks) for both campaigns
conversion_rate_A = total_purchases_A / total_clicks_A
conversion_rate_B = total_purchases_B / total_clicks_B


# print(f"Conversion Rate for Campaign A: {conversion_rate_A:.4f}")
# print(f"Conversion Rate for Campaign B: {conversion_rate_B:.4f}")

# Perform Z-test for proportions

# Number of successes (purchases) and number of trials (clicks)
successes = np.array([total_purchases_A, total_purchases_B])
trials = np.array([total_clicks_A, total_clicks_B])

# Run the proportions z-test
z_stat, p_value = proportions_ztest(successes, trials, alternative='two-sided')

# Output the Z-statistic and p-value
# print(f"Z-statistic: {z_stat:.4f}")
# print(f"P-value: {p_value:.4f}")

# Interpretation of p-value
# if p_value < 0.05:
#     print("There is a statistically significant difference in conversion rates between Campaign A and Campaign B.")
# else:
#     print("There is no statistically significant difference in conversion rates between Campaign A and Campaign B.")

# Visualising 
# Plot the Z-distribution (standard normal distribution)
# x = np.linspace(-4, 4, 1000)
# y = norm.pdf(x,0,1)

# z_critical = 1.96

# plt.figure(figsize=(10, 6))
# plt.plot(x, y, label="Standard Normal Distribution", color='gray')

# # Shade rejection regions (two-tailed)
# plt.fill_between(x, y, where=(x <= -z_critical) | (x >= z_critical), color='lightcoral', alpha=0.5, label='Rejection Region (α = 0.05)')

# # Highlight the Z-statistic value
# plt.axvline(z_stat, color='darkred', linestyle='--', linewidth=2, label=f'Z-statistic = {z_stat:.2f}')
# plt.axvline(-z_critical, color='black', linestyle=':', label='Critical Z = ±1.96')
# plt.axvline(z_critical, color='black', linestyle=':')

# # Add labels and legend
# plt.title('Z-Test for Conversion Rate Difference')
# plt.xlabel('Z value')
# plt.ylabel('Probability Density')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()

#                               QUESTION 2

# Average Order Value 
AOV = 50        # for a general ecommerce product

# Making Revenue Column
A_df['Revenue'] = A_df['# of Purchase'] * AOV
B_df['Revenue'] = B_df['# of Purchase'] * AOV

# Calculating total values 

A_total_revenue = A_df['Revenue'].sum()
B_total_revenue = B_df['Revenue'].sum()

A_total_spend = A_df['Spend [USD]'].sum()
B_total_spend = B_df['Spend [USD]'].sum()

# Calculating ROAS
A_roas = A_total_revenue/A_total_spend
B_roas = B_total_revenue/B_total_spend

# Results
# print(f"Campaign A -> ROAS: {A_roas:.2f}")
# print(f"Campaign B -> ROAS: {B_roas:.2f}")

# Interpretation:
# Campaign A generates $11.04 in revenue for every $1 spent.
# Campaign B generates $10.17 in revenue per $1 spent.
# Therefore, Campaign A is more cost-effective.

# Visualising
# creating dataframe
# roas_data = pd.DataFrame({
#     'Campaign' : ['A','B'],
#     'ROAS': [A_roas,B_roas]
# })
# # plotting
# plt.figure(figsize=(8,6))
# sns.barplot(x='Campaign',y='ROAS',data=roas_data, palette='Greens')
# plt.title("Return on Ad Spend(RAOS) Comparison")
# plt.ylabel("ROAS")
# plt.xlabel("Campaign")
# plt.grid(True, axis='y', linestyle='--',alpha=0.7)
# plt.tight_layout()
# plt.show()

#                       QUESTION 3

# Calculate Pearson correlation 

A_corr = A_df['# of Impressions'].corr(A_df['# of Purchase'])
B_corr = B_df['# of Impressions'].corr(B_df['# of Purchase'])

# Print correlation results
# print(f"Campaign A - Correlation bw Impression and Purchases: {A_corr:.2f}")
# print(f"Campaign B - Correlation bw Impression and Purchases: {B_corr:.2f}")

# # Visualisation

# # plot style
# sns.set_theme(style='whitegrid')
# # two subplots 
# fig, axes = plt.subplots(1,2, figsize= (14,6))

# # Campaign A
# sns.regplot(
#     x='# of Impressions', y="# of Purchase",
#     data=A_df, ax= axes[0],
#     scatter_kws = {'alpha':0.6}, line_kws={'color':'red'}
# )
# axes[0].set_title(f'Campaign A\n Correlation: {A_corr:.2f}')

# # Campaign B
# sns.regplot(
#     x="# of Impressions", y="# of Purchase",
#     data= B_df, ax =axes[1],
#     scatter_kws={'alpha':0.6}, line_kws={'color':'red'}
# )
# axes[1].set_title(f"Campaign B\n Correlation: {B_corr:.2f}")

# # Layout 
# for ax in axes:
#     ax.set_xlabel('Number of Impressions')
#     ax.set_ylabel('Number of Purchases')

# plt.suptitle('Correlation Between Impressions and Purchases', fontsize=16)
# plt.tight_layout(rect=[0, 0, 1, 0.95])
# plt.show()

# "We analyzed the relationship between the number of impressions and number of purchases for Campaign A and B. Campaign A showed a negative correlation (r = -0.02), suggesting impressions does not influence purchases. Campaign B had a low correlation (r = 0.10), indicating a weaker link between impressions and purchases. This suggests that Campaign B’s creative or targeting may be more effective at converting impressions into sales."

#                           QUESTION 4

# Calculate CTR and Purchase Rate
for df in [A_df, B_df]:
    df["CTR"] = (df["# of Website Clicks"] / df["# of Impressions"])*100
    df["Purchase Rate"] = (df['# of Purchase'] / df["# of Website Clicks"])*100

# Calculating correlation 
A_corr2 = A_df["CTR"].corr(A_df["Purchase Rate"])
B_corr2 = B_df["CTR"].corr(B_df["Purchase Rate"])

print(f"Campaign A - Correlation between CTR and Purchase Rate: {A_corr2:.2f}")
print(f"Campaign B - Correlation between CTR and Purchase Rate: {B_corr2:.2f}")

# # Visualisation

# # Sub plots
# fig, axes = plt.subplots(1,2,figsize=(14,6))

# # Campaign A
# sns.regplot(
#     x="CTR" , y="Purchase Rate",
#     data=A_df , ax = axes[0],
#     scatter_kws={'alpha':0.6}, line_kws={'color': 'darkgreen'} 
# )
# axes[0].set_title(f'Campaign A\n Correlation: {A_corr2:.2f}')

# # Campaign B
# sns.regplot(
#     x="CTR" , y= "Purchase Rate",
#     data=B_df, ax = axes[1],
#     scatter_kws={'alpha':0.6}, line_kws={'color': "darkblue"}
# )
# axes[1].set_title(f"Campaign B \n Correlation: {B_corr2:.2f}")

# for ax in axes:
#     ax.set_xlabel("Click-Through Rate")
#     ax.set_ylabel("Purchase Rate")

# plt.suptitle('CTR vs Purchase Rate Across Campaigns', fontsize=16)
# plt.tight_layout(rect=[0,0,1,0.95])
# plt.show()

# "We analyzed the relationship between click-through rate (CTR) and purchase behavior for both campaigns. Campaign A showed a moderate negative correlation (r = -0.63), suggesting that higher CTR is not related to more purchases. Campaign B showed a weak negative correlation (r = -0.35), indicating that although users clicked on the ad, it didn’t strongly predict conversions. This may suggest issues in the post-click experience for both Campaigns."
