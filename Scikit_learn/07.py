## Clustering (Digits Dataset)
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
import numpy as np

# Load data
digits = load_digits()
X = digits.data

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Cluster into 10 groups (digits 0-9)
kmeans = KMeans(n_clusters=10, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

print(confusion_matrix(digits.target, clusters))

# Assign actual digit labels to each cluster based on majority voting
true_labels = np.argmax(confusion_matrix(digits.target, clusters), axis=1)

for i, label in enumerate(true_labels):
    print(f"Custer {i} is mostly digit {label}")