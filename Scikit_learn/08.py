## Preprocessing - prepares data for ML
"""
Scaling: Normalize or standardize features.

Encoding: Convert categorical data into numerical data.

Handling Missing Values: Fill or drop missing data.
"""

# Handling Missing Values
from sklearn.impute import SimpleImputer
import numpy as np

X = np.array([[1, 2], [np.nan, 3], [7, 6]])

imputer = SimpleImputer(strategy='mean') # fill missing values with mean
X_filled = imputer.fit_transform(X)
# print("Filled:\n", X_filled)


## Pipelines - combine preprocessing and modeling steps into a single workflow.
"""
Cleaner code.

Avoidance of data leakage (e.g., scaling test data with stats from training data).
"""
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create pipeline:Scale → Logistic Regression
pipeline = make_pipeline(
    StandardScaler(),
    LogisticRegression()
)   # Pipelines combine preprocessing (like StandardScaler) and model training (like LogisticRegression) into a single workflow.

pipeline.fit(X_train, y_train)
print("Accuracy:", pipeline.score(X_test, y_test))