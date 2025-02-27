## e-commerce website wants to group customers based on their purchasing behavior

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Customer data
np.random.seed(42)
customers = pd.DataFrame({
    "Annual Income": np.random.randint(15000, 100000, 200),
    "Spending Score": np.random.randint(1, 100, 200)
})

# scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(customers)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

# Add cluster labels to Data
customers["Cluster"] = clusters

# Visualize
plt.figure(figsize=(8, 6))
for cluster in range(4):
    cluster_data = customers[customers["Cluster"] == cluster]
    plt.scatter(cluster_data["Annual Income"], cluster_data["Spending Score"], label=f"Cluster {cluster}")

plt.xlabel("Annual Income($)")
plt.ylabel("Spending Score")
plt.title("Customer Segments Based on Spending Behavior")
plt.legend()
plt.show()