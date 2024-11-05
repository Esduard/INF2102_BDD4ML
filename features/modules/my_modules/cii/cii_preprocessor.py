import xgboost as xgb
from features.modules.pre_processor import PreProcessor
from features.modules.my_modules.cii.cii_calculator import CIICalculator

class XGBoostPreProcessor(PreProcessor):
    def __init__(self, features, label, ship_type_column='ship_type_name', model_scaler=None, ship_type = None):
        """
        Initialize the XGBoostPreProcessor.

        Args:
            features (list): List of feature column names.
            label (str): Name of the target column.
            ship_type_column (str): Column name for ship type filtering.
            model_scaler (ModelScaler, optional): Scaler to apply to features.
        """
        print("Setting Up XGBoostPreProcessor")
        #features.sort()
        self.features = features
        #label.sort()
        self.label = label
        self.ship_type_column = ship_type_column
        self.ship_type = ship_type
        self.model_scaler = model_scaler

    def __separate_feature_and_label(self, dataset):
        """Separate features and label from the dataset."""
        dataframe = dataset
        dataframe.sort_index(inplace=True)
        x = dataframe[self.features].values
        y = dataframe[self.label].values
        return x, y

    def __filter_by_ship_type(self, dataset, ship_type):
        """Filter the dataset by the ship type."""
        return dataset[dataset[self.ship_type_column].isin([ship_type])]

    def preprocess(self, df_test):
        """
        Preprocess the data by filtering by ship type and scaling.

        Args:
            df_train (DataFrame): Training dataset.
            df_test (DataFrame): Test dataset.
            ship_type (str): Ship type to filter the datasets.

        Returns:
            DMatrix: XGBoost DMatrix for test set.
            numpy array: Target values for test set.
        """
        # Filter train and test sets by ship type
        df_test_type = self.__filter_by_ship_type(df_test, self.ship_type)
        #print(df_test_type.columns.tolist())

        # Separate features and labels for the test set
        X_test, y_test = self.__separate_feature_and_label(df_test_type)

        # Apply scaling to the test set if a scaler is provided
        if self.model_scaler is not None:
            X_test = self.model_scaler.apply_scaling(X_test)
        else:
            print("No model_scaler provided, proceeding without scaling.")

        # Create DMatrix for XGBoost with categorical feature handling
        dtest_reg = xgb.DMatrix(X_test, label=y_test, enable_categorical=True, feature_names=self.features)

        #print(dtest_reg.feature_names)

        return dtest_reg, y_test