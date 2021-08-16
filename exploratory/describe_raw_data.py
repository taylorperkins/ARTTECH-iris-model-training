import pandas as pd


def main():
    data: pd.DataFrame = pd.read_csv("../../artifacts/data/raw/Iris.csv")

    # note that this excludes the label (categorical, Species)
    description = data.describe()
    print(description.columns)

    conf = {}
    for col in description.columns:
        conf[col] = {
            "min": description.loc["min", col],
            "max": description.loc["max", col],
        }

    print(conf)


if __name__ == '__main__':
    main()
