import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import (
    mean_squared_error,
    r2_score,
    explained_variance_score
)



#--
# loading the dataset
#--

DATA_URL = "https://raw.githubusercontent.com/Santosh-1845/CS-4375---Assignment1/refs/heads/main/student-mat.csv"

data = pd.read_csv(DATA_URL, sep=";")

print("Dataset loaded successfully.")
print("Original dataset shape:", data.shape)



#--
# doing the preprocessing
#--


# getting rid of missing values and duplicate rows
data = data.dropna()
data = data.drop_duplicates()

# seperating X from Y, features from target variable
X = data.drop(columns=["G3"])
y = data["G3"]

# converting categorical variables into numerical variables
X = pd.get_dummies(X, drop_first=True, dtype=int)

feature_names = X.columns

print("Dataset shape after preprocessing:", data.shape)
print("Number of features after encoding:", X.shape[1])


#--
# training / testing split
#--

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


#--
# standardizing features
#--


scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

y_train = y_train.to_numpy()
y_test = y_test.to_numpy()



#--
# performing linear regression using Scikit-Learn SGREGRESSOR
#--

learning_rate = 0.0065
iterations = 2000

model = SGDRegressor(
    loss="squared_error",
    penalty=None,
    alpha=0.0,
    max_iter=iterations,
    tol=None,
    learning_rate="constant",
    eta0=learning_rate,
    random_state=42
)



#--
# training the model
#--

model.fit(X_train, y_train)



#--
# making predictions
#--

train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)



#--
# evaluating the model
#--

train_mse = mean_squared_error(y_train, train_predictions)
test_mse = mean_squared_error(y_test, test_predictions)

test_r2 = r2_score(y_test, test_predictions)

test_explained_variance = explained_variance_score(
    y_test,
    test_predictions
)



#--
# displaying the results
#--

print("\n================ MODEL RESULTS ================")

print("Learning rate:", learning_rate)
print("Iterations:", iterations)

print("\nTraining MSE:", train_mse)
print("Testing MSE:", test_mse)

print("Testing R2:", test_r2)
print(
    "Testing Explained Variance:",
    test_explained_variance
)

print("\nBias:")
print(model.intercept_[0])

print("\nWeight coefficients:")

for feature, weight in zip(feature_names, model.coef_):
    print(feature, ":", weight)



#--
# displaying the trial table
#--

trial_table = pd.DataFrame({
    "Learning Rate": [learning_rate],
    "Iterations": [iterations],
    "Training MSE": [train_mse],
    "Testing MSE": [test_mse]
})

print("\n================ TRIAL RESULTS ================")
print(trial_table.to_string(index=False))