from joblib import dump, load
from pathlib import Path

from sklearn.neighbors import KNeighborsClassifier

import iris_model_training.config as conf


class ModelIO:
    """
    Simple class for consistent saving / loading methods
    of the model itself.
    """

    @staticmethod
    def save(clf: KNeighborsClassifier, fp: Path = conf.MODEL_FP):
        dump(clf, fp)

    @staticmethod
    def load(fp: Path = conf.MODEL_FP) -> KNeighborsClassifier:
        return load(fp)
