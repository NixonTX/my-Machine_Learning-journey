## Training the Model  using an algorithm (here, Using Logistic Regression).
from sklearn.linear_model import LogisticRegression
from a01 import X_train, y_train, X_test, y_test
from sklearn import metrics

log_reg = LogisticRegression(max_iter=200)
log_reg.fit(X_train, y_train)

y_pred = log_reg.predict(X_test)

# print("Tested data:", y_test)
# print("Predicted data:", y_pred)

print("Logistic Regression model accuracy:", metrics.accuracy_score(y_test, y_pred))