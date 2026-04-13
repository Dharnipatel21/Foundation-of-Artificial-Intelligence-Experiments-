# 11 k-means clusturing
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
# Create sample customer dataset
data = {
"Age": [25, 34, 22, 45, 52, 23, 40, 60, 48, 33, 27, 38, 50, 29, 41],
"Annual_Income": [40000, 60000, 25000, 80000, 90000, 27000, 75000, 100000, 85000, 62000, 48000, 72000, 95000, 52000, 78000]
"Spending_Score": [60, 65, 45, 80, 85, 50, 78, 90, 88, 70, 55, 75, 92, 58, 82]
}
df = pd.DataFrame(data)
# Select relevant features for segmentation
X = df[["Age", "Annual_Income", "Spending_Score"]]
# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Apply K-Means
kmeans = KMeans(n_clusters=5, random_state=42)
df["Cluster"] = kmeans.fit_predict(X_scaled)
# View segmented customers
print(df.head())
# Visualize (Income vs Spending Score)
plt.figure(figsize=(6,5))
plt.scatter(df["Annual_Income"], df["Spending_Score"],
c=df["Cluster"], cmap="viridis", s=60)
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation (K-Means)")
plt.show()
