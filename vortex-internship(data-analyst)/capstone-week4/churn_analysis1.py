import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set style
plt.style.use("seaborn-v0_8-whitegrid")

# Load Dataset & Clean
df = pd.read_csv("customer_churn_dataset-testing-master.csv")
df.drop_duplicates(inplace=True)
df = df.ffill()

# -------------------------------------------------------------
# ALL CHARTS ON A SINGLE PAGE (Dashboard Layout)
# -------------------------------------------------------------
fig, axes = plt.subplots(3, 2, figsize=(15, 18))
fig.suptitle(
    "Customer Churn End-to-End Analysis Dashboard",
    fontsize=18,
    fontweight="bold",
)

# 1. Churn Count Overview
sns.countplot(
    data=df,
    x="Churn",
    hue="Churn",
    palette=["#2ecc71", "#e74c3c"],
    ax=axes[0, 0],
)
axes[0, 0].set_title("Overall Customer Churn Distribution", fontweight="bold")
axes[0, 0].set_xlabel("Churn Status (0 = Retained, 1 = Churned)")
axes[0, 0].set_ylabel("Number of Customers")

# 2. Churn by Subscription Type
sns.countplot(
    data=df,
    x="Subscription Type",
    hue="Churn",
    palette=["#3498db", "#e74c3c"],
    ax=axes[0, 1],
)
axes[0, 1].set_title("Churn by Subscription Type", fontweight="bold")
axes[0, 1].set_xlabel("Subscription Type")
axes[0, 1].set_ylabel("Customer Count")

# 3. Support Calls vs Churn
sns.boxplot(
    data=df,
    x="Churn",
    y="Support Calls",
    palette=["#2ecc71", "#e74c3c"],
    ax=axes[1, 0],
)
axes[1, 0].set_title("Impact of Support Calls on Churn", fontweight="bold")
axes[1, 0].set_xlabel("Churn Status")
axes[1, 0].set_ylabel("Number of Support Calls")

# 4. Tenure vs Churn
sns.boxplot(
    data=df,
    x="Churn",
    y="Tenure",
    palette=["#3498db", "#f1c40f"],
    ax=axes[1, 1],
)
axes[1, 1].set_title("Customer Tenure Length vs Churn", fontweight="bold")
axes[1, 1].set_xlabel("Churn Status")
axes[1, 1].set_ylabel("Tenure (Months)")

# 5. Total Spend vs Churn
sns.histplot(
    data=df,
    x="Total Spend",
    hue="Churn",
    multiple="stack",
    palette="Set2",
    ax=axes[2, 0],
)
axes[2, 0].set_title("Spending Distribution Across Churn", fontweight="bold")
axes[2, 0].set_xlabel("Total Spend ($)")
axes[2, 0].set_ylabel("Customer Count")

# Hide the unused 6th subplot grid space
axes[2, 1].axis("off")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Save the dashboard image to folder
plt.savefig("customer_churn_dashboard.png", dpi=300)
print("Dashboard saved successfully as 'customer_churn_dashboard.png'!")

# Show all charts together on one single page
plt.show()