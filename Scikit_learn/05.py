# Classification model
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1. Load data
iris = load_iris()
X = iris.data
y = iris.target

# 2. split data into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test) 
"""
During training, the model learns from X_train and y_train.

Now, we need to check how well it generalizes to new data.

X_test contains feature values that the model has never seen before.

how well the model performs on new, unseen data and to check if it can generalize beyond the training set.
###
we use X_test instead of y_test is because we need features to make predictions.

X_test: This contains the features (sepal length, sepal width, petal length, petal width) of test data.
knn.predict(X_test): The model uses these features to predict class labels.
y_pred: The predicted labels for X_test.

y_test contains actual class labels (setosa, versicolor, virginica).
We do not pass it to predict() because the model is supposed to predict labels, not use them.
Instead, we compare y_pred with y_test to check accuracy

### - We pass X_test to predict() because the model needs feature values to make predictions. y_test is only used after prediction to check accuracy.
"""
print(y_pred)

pred_species = [iris.target_names[p] for p in y_pred]
print("Predicted Species:", pred_species)

print("Accuracy:", accuracy_score(y_test, y_pred))
"""
Classification Predicts categories- Uses accuracy_score, which tells us how many predictions were correct.
"""