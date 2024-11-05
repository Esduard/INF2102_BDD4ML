import numpy as np
from features.modules.controller import Controller
from features.modules.model_config_loader import ModelConfigLoader
from features.modules.model_loader import ModelLoaderFromFile
from features.modules.model_scaler_loader import ScalerLoaderFromFile
from features.modules.data_loader import DataLoaderFromLocal
from features.modules.evaluator import ClassificationEvaluator, RegressionEvaluator
from features.modules.post_processor import CarbonPostProcessor
from features.modules.pre_processor import BasePreProcessor
from features.modules.my_modules.cii.cii_preprocessor import XGBoostPreProcessor
from features.modules.compatibility_checker import CompatibilityChecker
import sys
import debugpy

#print(f"Python version: {sys.version}")
#print(f"Python executable: {sys.executable}")


from behave import *
from behave import given, when, then, use_step_matcher

# Configuração para não exibir os warnings
import warnings

warnings.filterwarnings("ignore")

# Allow VS Code to attach to the debugger
#debugpy.listen(("localhost", 5678))
#print("Waiting for debugger to attach...")
#debugpy.wait_for_client()



@given('We obtain a model from the file {model_filename}')
def step_obtain_model(context, model_filename):

    if not hasattr(context, 'used_identifiers'):
        context.used_identifiers = set()
    else:
        # if this is already initalized it means some othe clause started it before
        raise AssertionError(f"Wrong order of execution of steps, read the manual for the correct order")

    if 'obtain_model' in context.used_identifiers:
        raise AssertionError(f"Model has already been obtained. 'Given' And 'When' Clauses cannot be reused")
    
    context.model_loader = ModelLoaderFromFile(model_filename + "_model.pkl")

    context.model_dataConfigLoader = ModelConfigLoader(model_filename)

    context.model_scaler = ScalerLoaderFromFile(model_filename + "_scaler.pkl")

    context.preprocessor = BasePreProcessor(context.model_dataConfigLoader.get_feature_names(),context.model_dataConfigLoader.get_target_names(),context.model_scaler)

    context.postprocessor = None

    # Mark the identifier as used
    context.used_identifiers.add('obtain_model')


@given('We evaluate the test as a {eval_type} problem')
def step_obtain_evaluator(context, eval_type):

    if not hasattr(context, 'used_identifiers'):
        raise AssertionError(f"Wrong order of execution of steps, read the manual for the correct order")

        

    if 'define_evaluator' in context.used_identifiers:
        raise AssertionError(f"Evaluator has already been defined. 'Given' and 'When' clauses cannot be reused")

    if eval_type == 'classification':
        evaluator = ClassificationEvaluator()
    elif eval_type == 'regression' :
        evaluator = RegressionEvaluator()
    else:
        raise ValueError(f'{eval_type} type evaluator not implemented')
    context.evaluator = evaluator

    # Mark the identifier as used
    context.used_identifiers.add('define_evaluator')

@given('We obtain test data from the file {filename}')
def step_obtain_test_data(context, filename):

    if not hasattr(context, 'used_identifiers'):
        raise AssertionError(f"Wrong order of execution of steps, read the manual for the correct order")

    if 'obtain_data' in context.used_identifiers:
        raise AssertionError(f"Test data has already been obtained. 'Given' and 'When' clauses cannot be reused")

    context.test_dataLoader = DataLoaderFromLocal(filename)

    # Mark the identifier as used
    context.used_identifiers.add('obtain_data')

    
@given('We use a custom preprocessor to transform the data')
def use_custom_preprocessor(context):

    if not hasattr(context, 'used_identifiers'):
        raise AssertionError(f"Wrong order of execution of steps, read the manual for the correct order")

    if 'define_preprocessor' in context.used_identifiers:
        raise AssertionError(f"Custom preprocessor has already been defined. 'Given' and 'When' clauses cannot be reused")

    # insert your preprocessor here
    context.preprocessor = XGBoostPreProcessor(context.model_dataConfigLoader.get_feature_names(),context.model_dataConfigLoader.get_target_names(),'ship_type_name',context.model_scaler,'AFRAMAX')

    # Mark the identifier as used
    context.used_identifiers.add('define_preprocessor')

@given('We use a custom postprocessor to transform the data')
def use_custom_postprocessor(context):

    if not hasattr(context, 'used_identifiers'):
        raise AssertionError(f"Wrong order of execution of steps, read the manual for the correct order")
    
    if 'define_postprocessor' in context.used_identifiers:
        raise AssertionError(f"Custom postprocessor has already been defined. 'Given' and 'When' clauses cannot be reused")

    # insert your postprocessor here
    context.postprocessor = CarbonPostProcessor(context.model_dataConfigLoader.get_feature_names(),context.model_dataConfigLoader.get_target_names(),'ship_type_name','AFRAMAX')

    # Mark the identifier as used
    context.used_identifiers.add('define_postprocessor')


@when('We process the data')
def perform_test(context):

    if not hasattr(context, 'used_identifiers'):
        raise AssertionError(f"Wrong order of execution of steps, read the manual for the correct order")

    if 'run_test' in context.used_identifiers:
        raise AssertionError(f"Test already ran. 'Given' and 'When' clauses cannot be reused")

    CompatibilityChecker(context.model_loader, context.test_dataLoader.dataset(),context.model_dataConfigLoader)

    context.controller = Controller(context.test_dataLoader, context.preprocessor, context.postprocessor, context.model_loader, context.evaluator)
    context.results_dict = context.controller.run()

    # Mark the identifier as used
    context.used_identifiers.add('run_test')