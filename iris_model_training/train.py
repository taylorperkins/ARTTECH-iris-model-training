import pandas
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from joblib import dump

import iris_model_training.config as conf
from iris_model_training.feature_engineering import Transformer
from iris_model_training.helpers import ModelIO


def train():
    raw_data = pandas.read_csv(conf.ARTIFACTS_DIRECTORY / "data" / "raw" / "Iris.csv") \
        .set_index("Id")

    features, labels = raw_data.drop("Species", axis=1), raw_data["Species"]
    features = Transformer.apply(features)

    X_train, X_test, y_train, y_test = train_test_split(
        features, labels,
        test_size=0.3, random_state=42)

    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(X_train, y_train)

    pred = clf.predict(X_test)
    print(f"Accuracy of model: {metrics.accuracy_score(pred, y_test)}")

    ModelIO.save(clf)


if __name__ == '__main__':
    train()
