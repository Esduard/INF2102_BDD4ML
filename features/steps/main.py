import numpy as np
from features.modules.controller import Controller
from features.modules.model_config_loader import ModelConfigLoader
from features.modules.model_loader import ModelLoaderFromEndpoint, ModelLoaderFromFile
from features.modules.data_loader import DataLoaderFromLocal
from features.modules.evaluator import ClassificationEvaluator, RegressionEvaluator
from features.modules.pre_processor import BasePreProcessor
from features.modules.compatibility_checker import CompatibilityChecker
import sys
import debugpy

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")


from behave import *
from behave import given, when, then, use_step_matcher


# Allow VS Code to attach to the debugger
#debugpy.listen(("localhost", 5678))
#print("Waiting for debugger to attach...")
#debugpy.wait_for_client()



@given('We obtain a {model_type} model from the file {filename}')
def step_obtain_model(context,model_type, filename):
    
    modelLoader = ModelLoaderFromFile(filename)

    context.modelLoader = modelLoader
    context.model_filename = filename

    context.model_dataConfigLoader = ModelConfigLoader(context.model_filename)

    if model_type == 'classification':
        evaluator = ClassificationEvaluator()
    else:
        evaluator = RegressionEvaluator()
    context.evaluator = evaluator

@given('We obtain test data from the file {filename}')
def step_obtain_test_data(context, filename):
    context.test_dataLoader = DataLoaderFromLocal(filename)

    
    


# separate the test and train data in a preprocess class
@when('We process the data')
def step_impl(context):

    # create a configuration file that tells:
    # reason: depeding on which scaler was used on the model we need to apply it to the data if necessary
    CompatibilityChecker(context.modelLoader, context.test_dataLoader.dataset(),context.model_dataConfigLoader)

    context.preprocessor = BasePreProcessor(context.model_dataConfigLoader.get_feature_names(),context.model_dataConfigLoader.get_target_names())

    context.controller = Controller(context.test_dataLoader, context.preprocessor, context.modelLoader, context.evaluator)
    context.results_dict = context.controller.run()