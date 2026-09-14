import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score

import matplotlib.pyplot as plt

#--
# loading dataset
#--

DATA_URL = "https://raw.githubusercontent.com/Santosh-1845/CS-4375---Assignment1/refs/heads/main/student-mat.csv"

data = pd.read_csv(DATA_URL, sep=";")

print("Dataset loaded successfully.")
print("Original dataset shape:", data.shape)

#--
# preprocessing
#--

# removing rows with missing values and duplicates
data = data.dropna()
data = data.drop_duplicates()

# seperating features (X) and target variable G3, which is final grade  (y)
X = data.drop(columns=["G3"])
y = data["G3"]

# converting categorical variables into numerical variables
X = pd.get_dummies(X, drop_first=True, dtype=int)

# saving feature names before standardization
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
# linear regression using gradient descent
#--

class LinearRegressionGD:

    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate = learning_rate
        self.iterations = iterations

        self.weights = None
        self.bias = 0

        # storing MSE after every iteration for later plotting
        self.mse_history = []


    def fit(self, X, y):

        # storing # of training examples and # of features
        m, n = X.shape

        self.weights = np.zeros(n)
        self.bias = 0

        # performing gradient descent
        for _ in range(self.iterations):

            # making predictions
            predictions = X @ self.weights + self.bias

            # calculating prediction errors
            errors = predictions - y

            # calculating gradients
            dw = (2 / m) * (X.T @ errors)
            db = (2 / m) * np.sum(errors)

            # updating weights and bias
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            # calculating & daving MSE for this iteration
            mse = np.mean(errors ** 2)
            self.mse_history.append(mse)


    def predict(self, X):

        return X @ self.weights + self.bias



#--
# training model
#--


learning_rate = 0.2
iterations = 500

model = LinearRegressionGD(
    learning_rate=learning_rate,
    iterations=iterations
)

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
# displaying results
#--

print("\n================ MODEL RESULTS ================")

print("Learning rate:", learning_rate)
print("Iterations:", iterations)

print("\nTraining MSE:", train_mse)
print("Testing MSE:", test_mse)

print("Testing R2:", test_r2)
print("Testing Explained Variance:", test_explained_variance)

print("\nBias:")
print(model.bias)

print("\nWeight coefficients:")

for feature, weight in zip(feature_names, model.weights):
    print(feature, ":", weight)


#--
# displaying trial table
#--

trial_table = pd.DataFrame({
    "Learning Rate": [learning_rate],
    "Iterations": [iterations],
    "Training MSE": [train_mse],
    "Testing MSE": [test_mse]
})

print("\n================ TRIAL RESULTS ================")
print(trial_table.to_string(index=False))





# G1 vs G3
plt.figure()
plt.scatter(data["G1"], data["G3"], alpha=0.6)
plt.xlabel("G1 - First Period Grade")
plt.ylabel("G3 - Final Grade")
plt.title("G1 vs G3")
plt.grid(True)
plt.show()

# G2 vs G3
plt.figure()
plt.scatter(data["G2"], data["G3"], alpha=0.6)
plt.xlabel("G2 - Second Period Grade")
plt.ylabel("G3 - Final Grade")
plt.title("G2 vs G3")
plt.grid(True)
plt.show()