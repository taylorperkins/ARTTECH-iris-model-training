import os
from pathlib import Path

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARTIFACTS_DIRECTORY = Path(os.environ.get("ARTIFACTS_DIRECTORY", f"{PROJECT_ROOT}/artifacts"))

MODEL_FP = ARTIFACTS_DIRECTORY / "models" / "iris_clf.joblib"
