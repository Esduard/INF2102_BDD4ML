from abc import ABC, abstractmethod
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import sys
import joblib
import os
#sys.modules['model'] = sys.modules['features.modules.model']


class ModelLoader(ABC):
    """Abstract class that loads a model"""

    def __init__(self, model_name):
        self.model_path = None
        self._model = None
        self._name = model_name

    @abstractmethod
    def load_model(self):
        """Load a model from a specified source."""
        pass

    @abstractmethod
    def predict(self, features):
        """Make a prediction based on the provided features."""
        pass

    def get_name(self):
        return self._name

    def get_model(self):
        return self._model


class ModelLoaderFromFile(ModelLoader):
    """class that loads a model from a file"""

    def get_feature_names_and_types(self,model):
        # Check if the model is a pipeline
        if hasattr(model, 'steps'):
            # Get the first step of the pipeline
            first_step = model.steps[0][1]
        else:
            # The model itself is the estimator
            first_step = model

        # Initialize lists to store feature names and types
        output_feature_names = []
        output_feature_types = []

        # Check if the first step has the get_feature_names_out method
        if hasattr(first_step, 'get_feature_names_out'):
            output_feature_names = first_step.get_feature_names_out()
        elif hasattr(first_step, 'feature_names_in_'):
            output_feature_names = first_step.feature_names_in_
        else:
            print("could not find feature names")

        # Determine the types of the features
        if hasattr(first_step, 'transformers'):
            # If the first step is a ColumnTransformer
            for name, transformer, columns in first_step.transformers:
                for col in columns:
                    if isinstance(transformer, (StandardScaler, OneHotEncoder)):
                        output_feature_types.append(type(transformer).__name__)
                    else:
                        output_feature_types.append('unknown')
        else:
            # For other types of estimators
            output_feature_types = ['unknown' for _ in output_feature_names]

        return output_feature_names, output_feature_types

    def __init__(self, model_name):
        # Save the path to the model file
        self.model_path = os.path.join('estimators',model_name)
        # Load the model from the specified file
        self._model = self.load_model()

        print("model type")
        print(type(self._model))

        try:
            print("get_feature_names_out")
            output_feature_names, output_feature_types = self.get_feature_names_and_types(self._model)
            print("Feature names:", output_feature_names)
            print("Feature types:", output_feature_types)
        except Exception as e:
            print("problem with feature_names_in_:", str(e))

        self._name = model_name

    def get_name(self):
        return self._name

    def get_model(self):
        return self._model

    def load_model(self):
        """Load a model from a file specified by the model path."""
        try:
            with open(self.model_path, 'rb') as file:
                model = joblib.load(file)
                self._model = model
                return model
        except Exception as e:
            raise ValueError(f"An error occurred while loading the model: {e}")

    def predict(self, features):
        """Make a prediction based on the provided features.
        
        Args:
            features: An array-like structure containing the input features.
            
        Returns:
            The predicted values based on the model.
        """
        if self._model is not None:
            try:
                return self._model.predict(features)
            except Exception as e:
                print(f"An error occurred while making predictions: {e}")
                return None
        else:
            raise ValueError("Model is not loaded.")