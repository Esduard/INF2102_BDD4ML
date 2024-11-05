Feature: testing a classification model performance 
    Scenario: run a performance test on a classification model
        Given We obtain a model from the file KNN-orig
        And We evaluate the test as a classification problem
        And We obtain test data from the file test_data.csv
        When We process the data

        # Recall
        Then the model will reach a value of 70 on the metric recall on a macro average
        And the model identifies 70 percent of the correct cases of all classes with a macro average
        And the model identifies 70 percent of the correct cases of all classes with a weighted average
        And the model identifies 70 percent of the correct cases of all classes
        And the model identifies 70 percent of the correct cases of class 'False'
        
        # Precision 
        And the model will reach a value of 70 on the metric precision on class 'False'
        And the model correctly classifies positives of class 'False' 70 percent of the time
        And the model correctly classifies positives of all classes with a macro average 70 percent of the time
        And the model correctly classifies positives of all classes with a weighted average 70 percent of the time
        And the model correctly classifies positives of all classes 70 percent of the time

        # Accuracy
        And the model will reach a value of 70 on the metric accuracy
        And the model correctly classifies class 'False' 70 percent of the time
        And the model correctly classifies all classes 70 percent of the time

        # F1 Score
        And the model will reach a value of 70 on the metric f1_score
        And the model will reach a value of 70 on the metric f1_score on a macro average
        And the model will reach a value of 70 on the metric f1_score on a weighted average
        And the model will reach a value of 70 on the metric f1_score on class 'False'