# make a class that evaluates the results from the 'predictions' array

# enhance the evaluator class so that can use reflect to get results from sk learn

from behave import *
from behave import given, when, then, use_step_matcher

use_step_matcher("re")

#recall
@then('the model identifies (100|[1-9]?\\d) percent of the correct cases of(?: all classes with (a macro average|a weighted average)| class \'([\\w\\s-]+)\')?')
def step_impl(context, percent, average_type=None, class_name=None):
    # percent: string capturing the percentage match
    # average_type: captures 'a macro average' or 'a weighted average' if provided
    # class_name: captures the class name if provided


    classification_evaluate(context.results_dict,percent,'recall',average_type,class_name)

#precision
#The model classifies positives of ... correctly <number> percent of the time
@then('the model classifies positives of(?: all classes with (a macro average|a weighted average)| class \'([\\w\\s-]+)\')? correctly (100|[1-9]?\\d) percent of the time')
def step_impl(context,average_type=None,class_name=None, percent=None):
    # percent: string capturing the percentage match
    # average_type: captures 'a macro average' or 'a weighted average' if provided
    # class_name: captures the class name if provided

    classification_evaluate(context.results_dict,percent,'precision',average_type,class_name)

#accuracy
#The model classifies of ... correctly <number> percent of the time
@then('the model classifies(?: all classes| class \'([\\w\\s-]+)\')? correctly (100|[1-9]?\\d) percent of the time')
def step_impl(context,class_name=None, percent=None):
    # percent: string capturing the percentage match
    # average_type: captures 'a macro average' or 'a weighted average' if provided
    # class_name: captures the class name if provided

    classification_evaluate(context.results_dict,percent,'accuracy',None,class_name)

#explicit
@then('the model will reach (100|[1-9]?\\d) percent (recall|f1_score|precision|support|accuracy)(?: on (a macro average|a weighted average|class \'([\\w\\s-]+)\'))?')
def step_impl(context, percent, metric, average_type=None, class_name=None):
    # percent: the percentage value captured
    # metric: the metric type (recall, f1_score, precision, support, accuracy)
    # average_type: captures 'a macro average' or 'a weighted average' if provided
    # class_name: captures the class name if provided
    
    print(f"Percentage: {percent}, Metric: {metric}, Average Type : {average_type}{average_type if average_type else 'N/A'}, Class Name: {class_name if class_name else 'N/A'}")

    if average_type:
        if 'class' in average_type:
            average_type = None

    classification_evaluate(context.results_dict,percent,metric,average_type,class_name)


def classification_evaluate(results_dict,percent,metric,average_type,class_name):
    # Print statement to display the parameters. Conditionally display 'N/A' if average_type or class_name are None
    print(f"Percentage: {percent}, Metric: {metric}, Average Type: {average_type if average_type else 'N/A'}, Class Name: {class_name if class_name else 'N/A'}")

    # Dictionary to map the metric parameters from function to those used in results_dict
    conversion_metric = {
        'recall': 'recall',
        'f1_score': 'f1-score',
        'precision': 'precision',
        'support': 'support',
        'accuracy': 'accuracy'
    }

    # Dictionary to convert average_type to the format used in results_dict
    conversion_condition = {
        'a macro average': 'macro avg',
        'a weighted average': 'weighted avg'
    }

    # Convert the metric using the dictionary
    if metric in conversion_metric:
        metric = conversion_metric[metric]

    # Handle the accuracy case separately, as it doesn't depend on average_type or class_name
    if metric == 'accuracy':
        assert results_dict[metric] >= float(percent) / 100, f"Accuracy is below {percent}%"
        return

    # Determine the key in the results dictionary based on average_type or class_name
    condition_key = None
    if average_type:
        condition_key = conversion_condition.get(average_type)  # Convert average_type using the dictionary
    elif class_name:
        condition_key = class_name.strip()  # Directly use class_name if provided

    # Assert the condition based on the extracted key and metric
    if condition_key:
        assert results_dict[condition_key][metric] >= float(percent) / 100, f"{condition_key} {metric} is below {percent}%"
    else:
        # If no specific condition is given, fall back to 'macro avg' as a default
        assert results_dict['macro avg'][metric] >= float(percent) / 100, f"Macro average {metric} is below {percent}%"