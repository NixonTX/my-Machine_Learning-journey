from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

log_reg = LogisticRegression(max_iter=200)
log_reg.fit(X_train, y_train)

sample = [[3, 5, 4, 2], [2, 3, 5, 4]]

preds = log_reg.predict(sample)
pred_species = [iris.target_names[p] for p in preds]

print("Predictions:", pred_species)