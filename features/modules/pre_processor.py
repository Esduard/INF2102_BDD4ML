from sklearn.model_selection import train_test_split
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import SelectKBest # para a Seleção Univariada

from abc import ABC, abstractmethod

class PreProcessor(ABC):
    '''Classe abstrata que contém operaçoes de um preprocessador de dados. '''
    @abstractmethod
    def preprocess(self,dataset):
        pass
    
class BasePreProcessor(PreProcessor):
    def __init__(self,features, label,model_scaler = None):
        print("Setting Up BasePreProcessor")
        self.features = features
        self.label = label
        self.model_scaler = model_scaler

    def __separate_feature_and_label(self,dataset):
        dataframe = dataset
        dataframe.sort_index(inplace=True)
        x = dataframe[self.features].values
        y = dataframe[self.label].values
        return x,y

    def preprocess(self, dataset):
        X_test, y_test = self.__separate_feature_and_label(dataset)

        # Apply scaling if a model_scaler is provided
        if self.model_scaler.get_scaler():
            X_test = self.model_scaler.apply_scaling(X_test)
        else:
            print("No model_scaler provided, proceeding without scaling.")

        return X_test, y_test