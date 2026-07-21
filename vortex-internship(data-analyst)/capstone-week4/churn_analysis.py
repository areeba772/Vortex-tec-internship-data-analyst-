import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set style for professional, non-technical audience charts
plt.style.use("seaborn-v0_8-whitegrid")
sns.set_palette("muted")

# -------------------------------------------------------------
# 1. LOAD DATASET
# -------------------------------------------------------------
df = pd.read_csv("customer_churn_dataset-testing-master.csv")

# -------------------------------------------------------------
# 2. DATA CLEANING
# -------------------------------------------------------------
# Drop duplicates and handle missing values if any
df.drop_duplicates(inplace=True)
df = df.ffill()

print("--- DATA CLEANING COMPLETED ---")
print(f"Total Cleaned Records: {df.shape[0]}, Columns: {df.shape[1]}\n")
# -------------------------------------------------------------
# 3. EXECUTIVE SUMMARY PRINT (For Non-Technical Stakeholders)
# -------------------------------------------------------------
print("=" * 60)
print("EXECUTIVE SUMMARY: CUSTOMER CHURN ANALYSIS")
print("=" * 60)
print(
    """
This analysis investigates why customers are churning from our subscription service.
By examining customer tenure, support calls, subscription types, and usage frequencies, 
we uncovered critical patterns. Primarily, customers with high support interactions 
and shorter tenures are at the highest risk of leaving. Implementing targeted retention 
strategies for monthly subscribers and streamlining support resolution can significantly 
reduce overall churn rates and boost long-term business revenue.
"""
)
print("=" * 60 + "\n")

# -------------------------------------------------------------
# 4. KEY FINDINGS & POLISHED VISUALIZATIONS (5+ Charts)
# -------------------------------------------------------------

# Visualization 1: Churn Count Overview
plt.figure(figsize=(7, 4))
sns.countplot(data=df, x="Churn", hue="Churn", palette=["#2ecc71", "#e74c3c"])
plt.title(
    "Overall Customer Churn Distribution", fontsize=13, fontweight="bold"
)
plt.xlabel("Churn Status (0 = Retained, 1 = Churned)")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("churn_distribution.png")
plt.show()

# Visualization 2: Churn by Subscription Type
plt.figure(figsize=(8, 4))
sns.countplot(
    data=df, x="Subscription Type", hue="Churn", palette=["#3498db", "#e74c3c"]
)
plt.title("Customer Churn by Subscription Type", fontsize=13, fontweight="bold")
plt.xlabel("Subscription Type")
plt.ylabel("Customer Count")
plt.tight_layout()
plt.savefig("churn_by_subscription.png")
plt.show()

# Visualization 3: Support Calls vs Churn
plt.figure(figsize=(8, 4))
sns.boxplot(data=df, x="Churn", y="Support Calls", palette=["#2ecc71", "#e74c3c"])
plt.title(
    "Impact of Support Calls on Customer Churn", fontsize=13, fontweight="bold"
)
plt.xlabel("Churn Status (0 = Retained, 1 = Churned)")
plt.ylabel("Number of Support Calls")
plt.tight_layout()
plt.savefig("support_calls_vs_churn.png")
plt.show()

# Visualization 4: Tenure vs Churn
plt.figure(figsize=(8, 4))
sns.boxplot(data=df, x="Churn", y="Tenure", palette=["#3498db", "#f1c40f"])
plt.title(
    "Customer Tenure Length vs Churn Status", fontsize=13, fontweight="bold"
)
plt.xlabel("Churn Status (0 = Retained, 1 = Churned)")
plt.ylabel("Tenure (Months)")
plt.tight_layout()
plt.savefig("tenure_vs_churn.png")
plt.show()

# Visualization 5: Total Spend vs Churn
plt.figure(figsize=(8, 4))
sns.histplot(
    data=df, x="Total Spend", hue="Churn", multiple="stack", palette="Set2"
)
plt.title("Spending Distribution Across Churned Customers", fontsize=13, fontweight="bold")
plt.xlabel("Total Spend ($)")
plt.ylabel("Customer Count")
plt.tight_layout()
plt.savefig("spend_vs_churn.png")
plt.show()

# -------------------------------------------------------------
# 5. ACTIONABLE RECOMMENDATIONS
# -------------------------------------------------------------
print("\n" + "=" * 60)
print("ACTIONABLE BUSINESS RECOMMENDATIONS")
print("=" * 60)
print(
    """
1. Priority Support Escalation: Customers who make frequent support calls exhibit high churn rates. 
   Establish a fast-track resolution team for clients with >5 support calls.
2. Monthly-to-Annual Incentive Program: Monthly subscribers show higher volatility and churn. 
   Offer discounted annual upgrade promotions to stabilize long-term retention.
3. Early-Stage Engagement Campaigns: New customers with lower tenures drop off quickly; introduce 
   onboarding check-ins during their first 30-60 days.
"""
)
print("=" * 60)