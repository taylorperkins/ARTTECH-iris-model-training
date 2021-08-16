from pathlib import Path

from joblib import dump, load

import iris_model_training.config as conf


class ModelIO:
    """
    Simple class for consistent saving / loading methods
    of the model itself.
    """

    @staticmethod
    def save(clf, fp: Path = conf.MODEL_FP):
        dump(clf, fp)

    @staticmethod
    def load(fp: Path = conf.MODEL_FP):
        return load(fp)
