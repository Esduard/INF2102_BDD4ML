from abc import ABC, abstractmethod
import os

import pandas as pd

from sklearn.datasets import load_diabetes # para importar o dataset diabetes

class DataLoader(ABC):
    '''Classe abstrata que contém operacées de um carregador de dados.'''

    @abstractmethod
    def dataset(self):
        '''Método que retorna um dataset.'''
        pass
    
class DataLoaderFromLocal(DataLoader):
    def __init__(self,filename):
        print("Loading Data Locally")
        full_path = os.path.join('test_data', filename)
        dataset = pd.read_csv(full_path, delimiter=',')
        self.__dataset = dataset
        self.__columns = dataset.columns

    def columns(self):
        return self.__columns

    def dataset(self):
        return self.__dataset