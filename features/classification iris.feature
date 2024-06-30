Feature: testing a classification model performance 
    Scenario: run a performance test on a classification model
        Given We obtain a classification model from the file irisCART-orig.pkl
        And We obtain test data from the file test_data_iris.csv
        When We process the data

        # Recall
        Then the model will reach a value of 70 on the metric recall on a macro average
        And the model identifies 70 percent of the correct cases of all classes with a macro average
        And the model identifies 70 percent of the correct cases of class 'virginica'
        
        # Precision 
        And the model will reach a value of 70 on the metric precision on class 'virginica'
        And the model correctly classifies positives of class 'virginica' 70 percent of the time
        And the model correctly classifies positives of all classes with a macro average 70 percent of the time

        # Accuracy
        And the model will reach a value of 70 on the metric accuracy
        And the model correctly classifies class 'virginica' 70 percent of the time
        And the model correctly classifies all classes 70 percent of the time

        # F1-Score

        And the model will reach a value of 70 on the metric f1_score on a weighted average

        # F1 Score
        And the model will reach a value of 70 on the metric f1_score
        And the model will reach a value of 70 on the metric f1_score on a macro average
        And the model will reach a value of 70 on the metric f1_score on a weighted average
        And the model will reach a value of 70 on the metric f1_score on class 'setosa'