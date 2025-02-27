# Loading dataset - iris
from sklearn.datasets import load_iris
iris = load_iris()

# store feature matrix(x) and response vector (y)
X = iris.data
y = iris.target

# store feature and target names
feature_names = iris.feature_names
target_names = iris.target_names

print("Feature names:", feature_names)
print("Target namesa:", target_names)

print("\nType of X is:", type(X))

print("\nFirst 5 rows of X:\n", X[:5])