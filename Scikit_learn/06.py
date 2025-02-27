## Regression (Diabetes Dataset)
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target   # features, target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)   # random_state=42 - ensures reproducibility(same split every time)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Mean Square Error:", mean_squared_error(y_test, y_pred))
print("R2 score:", r2_score(y_test, y_pred))
"""
Regression Predicts continuous values- Uses mean_squared_error (MSE) and R² score to measure how far predictions are from actual values.
###

Why Not Use Accuracy for Regression?
    Accuracy_score works only for classification, where predictions are exact categories.
    In regression, predictions are continuous numbers, not discrete classes.
    Example: A true value is 150, but the model predicts 148.5.
    There's no way to say "correct" or "incorrect", only how close the prediction is.
###
    
Use accuracy_score for classification (discrete labels).
Use MSE and R² score for regression (continuous values).
Accuracy can't measure errors in continuous predictions, so it's not useful in regression.
"""