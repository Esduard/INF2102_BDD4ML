from abc import ABC, abstractmethod
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import sys
import joblib
import os
#sys.modules['model'] = sys.modules['features.modules.model']


class ModelScaler(ABC):
    """Abstract class that loads and applies transformations using a model scaler"""

    def __init__(self, scaler_name, scaler_path=None):
        """
        Initialize the ModelScaler with a name and optional path to the scaler.
        
        Args:
            scaler_name (str): The name of the scaler.
            scaler_path (str, optional): Path to the scaler file.
        """
        self.scaler_path = scaler_path
        self._scaler = None
        self._name = scaler_name

    @abstractmethod
    def load_scaler(self):
        """Load a scaler from a specified source."""
        pass

    @abstractmethod
    def apply_scaling(self, features):
        """Apply transformation or prediction based on the provided features.
        
        Args:
            features (array-like): Input features to be transformed or predicted.
            
        Returns:
            array-like: Transformed or predicted output.
        """
        pass

    def get_name(self):
        """Get the name of the scaler."""
        return self._name

    def get_scaler(self):
        """Return the loaded scaler instance."""
        return self._scaler

    def clear(self):
        """Clear the scaler, resetting it to None."""
        self._scaler = None

class ScalerLoaderFromFile(ModelScaler):
    """Class that loads a scaler from a .pkl file"""

    def __init__(self, model_name, model_dir='estimators'):
        """
        Initialize the ScalerLoaderFromFile class.

        Args:
            model_name (str): Name of the scaler model.
            model_dir (str): Directory where the scaler .pkl file is stored.
        """
        self.scaler_path = os.path.join(model_dir, f"{model_name}")
        self._scaler = self.load_scaler()

        if self._scaler is None:
            return None

        print("Scaler type:", type(self._scaler))

        # Optional: Display feature names and types if applicable
        try:
            output_feature_names, output_feature_types = self.get_feature_names_and_types(self._scaler)
            print("Feature names:", output_feature_names)
            print("Feature types:", output_feature_types)
        except Exception as e:
            print("Error retrieving feature names/types:", str(e))

        self._name = model_name

    def get_feature_names_and_types(self, model):
        # Check if the model is a pipeline
        if hasattr(model, 'steps'):
            first_step = model.steps[0][1]
        else:
            first_step = model

        output_feature_names = []
        output_feature_types = []

        if hasattr(first_step, 'get_feature_names_out'):
            output_feature_names = first_step.get_feature_names_out()
        elif hasattr(first_step, 'feature_names_in_'):
            output_feature_names = first_step.feature_names_in_
        else:
            print("Could not find feature names")

        if hasattr(first_step, 'transformers'):
            for name, transformer, columns in first_step.transformers:
                for col in columns:
                    if isinstance(transformer, (StandardScaler, OneHotEncoder)):
                        output_feature_types.append(type(transformer).__name__)
                    else:
                        output_feature_types.append('unknown')
        else:
            output_feature_types = ['unknown' for _ in output_feature_names]

        return output_feature_names, output_feature_types

    def load_scaler(self):
        """Load a scaler from a .pkl file specified by the scaler_path."""
        try:
            with open(self.scaler_path, 'rb') as file:
                scaler = joblib.load(file)
                self._scaler = scaler
                return scaler
        except FileNotFoundError:
            print(f"Scaler file {self.scaler_path} not found.")
            return None
        except Exception as e:
            raise ValueError(f"An error occurred while loading the scaler: {e}")

    def apply_scaling(self, features):
        """
        Apply the scaling or transformation to the input features.

        Args:
            features: An array-like structure containing the input features.
        
        Returns:
            The transformed features.
        """
        if self._scaler is not None:
            try:
                if hasattr(self._scaler, 'transform'):
                    return self._scaler.transform(features)
                else:
                    raise ValueError("Loaded scaler does not have a transform method.")
            except Exception as e:
                print(f"An error occurred while applying scaling: {e}")
                return None
        else:
            raise ValueError("Scaler is not loaded.")