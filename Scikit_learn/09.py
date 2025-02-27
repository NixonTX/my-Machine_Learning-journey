## Hyperparameter Tuning - the process of finding the best parameters for a model to improve its performance

# GridSearchCV to find the best hyperparameters for K-Nearest Neighbors (KNN).

from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define Hyperparameter Grid
param_grid = {
    'n_neighbors': [3, 5, 7],
    'weights': ['uniform', 'distance']
}

knn = KNeighborsClassifier()

grid_search = GridSearchCV(knn, param_grid, cv=5)   # cross-validation
grid_search.fit(X_train, y_train)

print("Best Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)

print("Test Accuracy:", grid_search.score(X_test, y_test))

"""
What does cv=5 do?
It splits the training data into 5 parts (folds) and trains the model 5 times, each time using:

4 folds for training
1 fold for validation (rotating through all 5 folds)
Then, it averages the accuracy across all 5 runs to give a more reliable estimate of performance.

Why use cross-validation?
Prevents overfitting by testing on different subsets.
Ensures hyperparameter tuning is unbiased (not just lucky on one split).
Gives a more generalizable model for real-world data.
"""