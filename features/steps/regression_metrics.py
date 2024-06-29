# make a class that evaluates the results from the 'predictions' array

# enhance the evaluator class so that can use reflect to get results from sk learn

from behave import *
from behave import given, when, then, use_step_matcher

use_step_matcher("re")

@then('the model will reach a (Mean Squared Error|Mean Absolute Error|Root Mean Squared Error|Median Absolute Error) below (\d+(?:\.\d+)?)')
def step_impl(context,metric, number):

    regression_evaluate(context.results_dict,metric,'below',number)

@then('the model will reach an R2 Score above (\d+(?:\.\d+)?)')
def step_impl(context, number):

    regression_evaluate(context.results_dict,'R2 Score','above',number)


def regression_evaluate(results_dict,full_metric,reference,number):

    conversion_metric = {
        'Mean Squared Error': 'mse',
        'R2 Score': 'r2_score',
        'Mean Absolute Error': 'mae',
        'Root Mean Squared Error': 'rmse',
        'Median Absolute Error': 'median_ae'
    }

    if full_metric in conversion_metric:
        metric = conversion_metric[full_metric]


    print(f"Metric: {metric}, Number: {number}")

    try:
        if reference == 'above':
            assert results_dict[metric] >= float(number)
        else:
            assert results_dict[metric] <= float(number)
    except AssertionError as e:
        raise ValueError(f"The metric \'{full_metric}\' failed to reach the desired value: Should be {reference} {number}, but was {results_dict[metric]}")

    # For demonstration, just printing the values:
    print(results_dict)
