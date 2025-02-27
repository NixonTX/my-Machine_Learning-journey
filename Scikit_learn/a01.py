from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=1)

# X_train, y_train : features and target values used for training the model.
# X_test, y_test : features and target values used for testing the model after it has been trained.

# test_size=0.4: 40% of the data is allocated to the testing set while the remaining 60% is used for training.

# random_state=1: This ensures that the split is consistent, meaning you’ll get the same random split every time you run the code.


# Check split
print("X_train Shape:", X_train.shape)
print("X_test Shape:", X_test.shape)
print("Y_train Shape:", y_train.shape)
print("Y_test Shape:", y_test.shape)