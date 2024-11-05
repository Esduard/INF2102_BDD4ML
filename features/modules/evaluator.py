from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.metrics import root_mean_squared_error, median_absolute_error
from sklearn.metrics import classification_report
import pandas as pd


from abc import ABC, abstractmethod

class Evaluator(ABC):
    """Classe abstrata que contém opreações de um Avaliador"""

    @abstractmethod
    def evaluate(self,y_test,predictions):
        pass

 
class RegressionEvaluator(Evaluator):

    def __init__(self, target_names=None):
        self.best_results = {'name' : 'none', 'r2_score' : 1.00, 'mse' : 1.00, 'mae' : 1.00, 'rmse' : 1.00, 'median_ae' : 1.00}

    def calculate_mean_squared_error(self,y_test,predictions):
        return mean_squared_error(y_test, predictions)
    
    def calculate_mean_absolute_error(self,y_test,predictions):
        return mean_absolute_error(y_test, predictions)
    
    def calculate_root_mean_squared_error(self,y_test,predictions):
        return root_mean_squared_error(y_test, predictions)
    
    def calculate_median_absolute_error(self,y_test,predictions):
        return median_absolute_error(y_test, predictions)


    def calculate_r2_score(self,y_test, predictions):
        return r2_score(y_test, predictions)

    def evaluate(self,y_test,predictions):
        mse = self.calculate_mean_squared_error(y_test,predictions)
        r2_score = self.calculate_r2_score(y_test,predictions)
        mae = self.calculate_mean_absolute_error(y_test,predictions)
        rmse = self.calculate_root_mean_squared_error(y_test,predictions)
        median_ae = self.calculate_median_absolute_error(y_test,predictions)
        print("Mean Squared Error:", mse)
        print("R2 score:", r2_score)
        print("Mean Absolute Error:", mae)
        print("Root Mean Squared Error", rmse)
        print("Median Absolute Error", median_ae)

        return {'mse': mse, 'r2_score': r2_score, 'mae' : mae, 'rmse' : rmse, 'median_ae' : median_ae}



class ClassificationEvaluator(Evaluator):

    def __init__(self, target_names=None):
        print("Setting Up ClassificationEvaluator")
        self.target_names = target_names
    
    def evaluate(self,y_test,predictions):
        #print("\nConfusion Matrix:")
        #cm = confusion_matrix(y_test, predictions)
        #print(cm)
        print("\nClassification Report:")

        cr_dict = classification_report(y_test, predictions, output_dict=True)
        self.results = cr_dict
        print(cr_dict)
        return cr_dict
