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
        self.target_names   =   test_model_config.get_target_names()

        # Perform checks
        self.check_features_exist()
        self.check_target_exists()


    def check_target_exists(self):
        missing_targets = [target for target in self.target_names if target not in self.test_data.columns]

        if missing_targets:
            print("Missing targets: " + str(missing_targets))
            raise ValueError("The following target columns are missing from the test data: " + ", ".join(missing_targets))

    def check_features_exist(self):
        missing_features = [f for f in self.model_features if f not in self.test_data.columns]
        if missing_features:
            raise ValueError(f"The following features are missing in the test data: {missing_features}")
