import pandera as pa

# From $PROJECT_ROOT/exploratory/describe_raw_data.py
# Excluding Id: 'Id': {'min': 1.0, 'max': 150.0},
model_features_description = {'SepalLengthCm': {'min': 4.3, 'max': 7.9}, 'SepalWidthCm': {'min': 2.0, 'max': 4.4},
                              'PetalLengthCm': {'min': 1.0, 'max': 6.9}, 'PetalWidthCm': {'min': 0.1, 'max': 2.5}}


class Transformer:
    # define schema, set limits based on the data the model was "trained on"
    InputSchema = pa.DataFrameSchema({
        col: pa.Column(float, checks=[
            pa.Check.ge(conf["min"]),
            pa.Check.le(conf["max"])
        ])
        for col, conf in model_features_description.items()
    })

    # No real transformations for now, but this could be an
    # entirely new schema based on the real model
    OutputSchema = InputSchema

    @staticmethod
    @pa.check_input(InputSchema, "df")
    @pa.check_output(OutputSchema)
    def apply(df):
        """Validates input as `InputSchema`, transforms input to `OutputSchema`

        :param df: InputSchema
        :return: OutputSchema
        """
        # do all the fancy transformations here
        return df
