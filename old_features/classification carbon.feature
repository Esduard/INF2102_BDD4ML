Feature: testing a regression model performance 
    Scenario: run a performance test on a regression model
        Given We obtain a model from the file aframax_2023
        And We evaluate the test as a classification problem
        And We obtain test data from the file carbon_aframax_2023.csv
        And We use a custom preprocessor to transform the data
        And We use a custom postprocessor to transform the data

        When We process the data
        # Recall
        Then the model will reach a value of 50 on the metric recall on a macro average
        And the model identifies 50 percent of the correct cases of all classes with a macro average
        And the model identifies 40 percent of the correct cases of class 'D'

        # Precision
        And the model will reach a value of 40 on the metric precision on class 'C'
        And the model correctly classifies positives of class 'C' 40 percent of the time
        And the model correctly classifies positives of all classes with a macro average 40 percent of the time

        # Accuracy
        And the model will reach a value of 50 on the metric accuracy
        And the model correctly classifies class 'B' 50 percent of the time
        And the model correctly classifies all classes 50 percent of the time

        # F1 Score
        And the model will reach a value of 50 on the metric f1_score
        And the model will reach a value of 50 on the metric f1_score on a macro average
        And the model will reach a value of 50 on the metric f1_score on a weighted average
        And the model will reach a value of 50 on the metric f1_score on class 'A'