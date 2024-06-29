

from features.modules.data_loader import DataLoader
from features.modules.model_config_loader import ModelConfigLoader
from features.modules.model_loader import ModelLoader
from features.modules.evaluator import Evaluator
from features.modules.pre_processor import PreProcessor

class Controller():

    def __init__(self,dataLoader: DataLoader, preProcessor: PreProcessor,
                 modelLoader: ModelLoader, evaluator : Evaluator):
        self.__dataloader = dataLoader
        self.__modelLoader = modelLoader
        self.__evaluator = evaluator
        self.__preProcessor = preProcessor


    def __processTests(self,model_name,model, X_test, y_test):
        #Model Predict
        print('\nPredicting {}...'.format(model_name))
        predictions = model.predict(X_test)

        #Evaluation
        print('\nEstimating {}...'.format(model_name))
        return self.__evaluator.evaluate(y_test,predictions)

    
    def run(self):
        # Load Dataset
        dataset = self.__dataloader.dataset()
        # Preprocessing
        x_test, y_test = self.__preProcessor.preprocess(dataset)


        return self.__processTests(self.__modelLoader.get_name(),self.__modelLoader.get_model(), x_test, y_test)
        