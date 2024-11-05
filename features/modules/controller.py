

from features.modules.data_loader import DataLoader
from features.modules.model_config_loader import ModelConfigLoader
from features.modules.model_loader import ModelLoader
from features.modules.evaluator import Evaluator
from features.modules.post_processor import PostProcessor
from features.modules.pre_processor import PreProcessor

class Controller():

    def __init__(self,dataLoader: DataLoader, preProcessor: PreProcessor, 
                 postProcessor: PostProcessor,
                 modelLoader: ModelLoader, evaluator : Evaluator):
        self.__dataloader = dataLoader
        self.__modelLoader = modelLoader
        self.__evaluator = evaluator
        self.__preProcessor = preProcessor
        self.__postProcessor = postProcessor


    def __processTests(self,model_name,model, X_test, y_test):
        #Model Predict
        print('\nPredicting {}...'.format(model_name))
        predictions = model.predict(X_test)

        #Evaluation
        print('\nEstimating {}...'.format(model_name))
        return self.__evaluator.evaluate(y_test,predictions)
    
    def __process(self,model_name,model, X_test, y_test):
        #Model Predict
        print('\nPredicting {}...'.format(model_name))
        try:
            predictions = model.predict(X_test)
        except:
            raise ValueError(
    "Error making the predictions. This is most likely an issue related to "
    "compatibility issues between the input dataset and the model. Make sure "
    "you are using the correct preprocessing steps."
)

        return predictions

        

    
    def run(self):
        model_name = self.__modelLoader.get_name(),

        # Load Dataset
        dataset = self.__dataloader.dataset()
        
        # Preprocessing
        #'xtest' and 'ytest' do not have the column names
        x_test, y_test = self.__preProcessor.preprocess(dataset)

        predictions = self.__process(model_name,self.__modelLoader.get_model(), x_test, y_test)


        if not self.__postProcessor:
            #Evaluation
            print('\nEstimating {}...'.format(model_name))
            return self.__evaluator.evaluate(y_test,predictions)
        else:
            # I need to send the dataset and 'predictions' values
            # and create two new columns with
            # the 'ytest' values and 'predictions' values postprocessed

             # Post-processing: add columns with 'y_test' and 'predictions'
            
            # Post-process the dataset
            postprocessed_dataset, y_test_column, predictions_column = self.__postProcessor.postprocess(dataset, y_test, predictions)
            
            # Extract the postprocessed y_test and predictions
            y_test_postprocessed = postprocessed_dataset[y_test_column].values
            predictions_postprocessed = postprocessed_dataset[predictions_column].values

            # Evaluation
            print('\nEstimating {} with post-processing...'.format(model_name))
            return self.__evaluator.evaluate(y_test_postprocessed, predictions_postprocessed)