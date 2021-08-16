# Iris Model Training
Simple package for training a model around the classification of iris flowers.

## Getting Started

### Installation

```bash
python -m pip install IrisModelTraining
```
or..
```
python -m pip install git+https://github.com/taylorperkins/ARTTECH-iris-model-training.git@master
```

### Some setup
`IrisModelTraining` will try to save/load data into an `artifacts` folder.
By default, this folder is inside the project itself @ `iris-model-training/artifacts`.
If you want this to be somewhere else, overwrite the `ARTIFACTS_DIRECTORY` environment variable.

For example:
```bash
export ARTIFACTS_DIRECTORY=$HOME/.iris_artifacts
```

Once set, you will want to finish building out the artifacts folder like so:
```
/artifacts
    /data
        /raw
        /processed
    /models
```

Once set, the package should know what to do.


### Training
Found in `iris_model_training.train`.
Just run it as a script.
Dumps a model to your `artifacts/models` folder.
Relies on `artifacts/data/raw/Iris.csv`.
Feel free to grab the dataset [from Kaggle](https://www.kaggle.com/uciml/iris).

### Using the model!

Once you have the model loaded (see helpers section), you will want to feed it data it knows how to work with.
So, use the feature engineering class for some sanity checks.

```python
import pandas as pd

from iris_model_training.feature_engineering import Transformer
from iris_model_training.helpers import ModelIO


raw_features = pd.DataFrame({
    "SepalLengthCm": [5.0],
    "SepalWidthCm": [2.3],
    "PetalLengthCm": [4.7],
    "PetalWidthCm": [1.0]
})

clf = ModelIO.load()
transformed_features = Transformer.apply(raw_features)

predictions = clf.predict(transformed_features)
```



