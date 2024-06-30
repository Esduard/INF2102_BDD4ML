import json
import os


class ModelConfigLoader():

    def __init__(self, model_file_name) -> None:
        try:
            # Check if the model has feature names attribute
            model_name_no_ext = model_file_name.split('.')[0]
            json_name =  model_name_no_ext + '.json'
            config_dict =  self.load_features_from_config(json_name)

            self.feature_names   = config_dict["feature_names"]
            self.feature_types   = config_dict["feature_types"]
            self.target_names    = config_dict["target_names"]
            self.target_types    = config_dict["target_types"]
        except Exception as e:
            raise ValueError("Error loading model configurations: " + str(e))
        
    def load_features_from_config(self, config_filename):
        # print the current execution path
        full_path = os.path.join('model_configs', config_filename)
        with open(full_path, 'r') as file:
            config = json.load(file)
            return config

    def get_feature_names(self):
        return self.feature_names

    def get_feature_types(self):
        return self.feature_types

    def get_target_names(self):
        return self.target_names

    def get_target_types(self):
        return self.target_types
        