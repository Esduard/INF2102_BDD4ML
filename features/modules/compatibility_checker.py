import pandas as pd
import pickle
import json
import os

class CompatibilityChecker:
    def __init__(self, modelLoader, test_data, test_model_config):
        # Load the model
        self.model = modelLoader.get_model()
        self.model_name = modelLoader.get_name()
        # Load the test data
        self.test_data = test_data
        # Load model features from the model or a configuration file
        self.model_features =   test_model_config.get_feature_names()
        self.feature_types  =   test_model_config.get_feature_types()
        self.target_names   =   test_model_config.get_target_names()
        self.target_types   =   test_model_config.get_target_types()

        # Perform checks
        self.check_features_exist()
        self.check_target_exists()
        self.check_data_types()


    def check_target_exists(self):
        missing_targets = [target for target in self.target_names if target not in self.test_data.columns]

        if missing_targets:
            print("Missing targets: " + str(missing_targets))
            raise ValueError("The following target columns are missing from the test data: " + ", ".join(missing_targets))

    def check_features_exist(self):
        missing_features = [f for f in self.model_features if f not in self.test_data.columns]
        if missing_features:
            raise ValueError(f"The following features are missing in the test data: {missing_features}")

    def check_data_types(self):
        # Assume that the data types should match the training data exactly (this might need to be adjusted based on real scenarios)
        expected_feature_dtypes = self.feature_types  # Replace with actual data types used in training
        actual_feature_dtypes = [str(self.test_data[col].dtype) for col in self.model_features]

        expected_target_dtypes = self.target_types  # Replace with actual data types used in training
        actual_target_dtypes = [str(self.test_data[col].dtype) for col in self.target_names]

        
        if expected_feature_dtypes != actual_feature_dtypes:
            print("expected feature data types: " + str(expected_feature_dtypes))

            print("actual feature data types:" + str(actual_feature_dtypes))
            raise ValueError("Data types of the test data do not match expected types from training.")
        
        if expected_target_dtypes != actual_target_dtypes:
            print("expected target data types: " + str(expected_target_dtypes))

            print("actual target data types:" + str(actual_target_dtypes))
            raise ValueError("Data types of the test data do not match expected types from training.")
