from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

def train_classifier(file):
    # Load the data
    cars = pd.read_csv(file)

    # Convert 'mpg' to boolean values: 1 if mpg > 23.45, 0 otherwise
    cars['is_efficient'] = (cars['mpg'] > 23.45).astype(int)

    features = cars[['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration','model year']]
    target = cars['is_efficient']

    # Split the data into a training set and a test set
    features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.2, random_state=52)

    classifier = DecisionTreeClassifier(random_state=52)
    classifier.fit(features_train, target_train)

    return classifier

def predict_efficiency(clf, car_data):
    # Convert the list to a DataFrame
    test_case_df = pd.DataFrame([car_data], columns=['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration','model year'])
    prediction = clf.predict(test_case_df)
    return prediction[0]