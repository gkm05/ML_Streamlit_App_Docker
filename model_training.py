import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pickle

# Load the iris dataset from a CSV file (assuming it's in the same directory)
data = pd.read_csv("iris.csv")
# Separate features and target
X = data.drop("species", axis=1)
y = data["species"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create and train a K-Nearest Neighbors classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Save the trained model to a pickle file
with open("iris_model.pkl", "wb") as f:
    pickle.dump(knn, f)