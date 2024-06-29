from abc import ABC, abstractmethod
from sklearn.neighbors import KNeighborsClassifier
import sys
import joblib
import os
#sys.modules['model'] = sys.modules['features.modules.model']


class ModelLoader(ABC):
    """abstract class that loads a model"""

    @abstractmethod
    def predict(self):
        pass


class ModelLoaderFromEndpoint(ModelLoader):
    """class that establishes a connection to an endpoint
    and runs inferences from here
    """

    def __init__(self, model_name):
        self.model_name = model_name

    def predict(self):
        return self.model_name
    

class ModelLoaderFromFile(ModelLoader):
    """class that loads a model from a file"""

    def __init__(self, model_name):
        # Save the path to the model file
        self.model_path = os.path.join('estimators',model_name)
        # Load the model from the specified file
        self._model = self.load_model()

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