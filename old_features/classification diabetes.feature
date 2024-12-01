Feature: testing a classification model performance 
    Scenario: run a performance test on a classification model
        Given We obtain a model from the file KNN-orig
        Given We evaluate the test as a classification problem
        Given We obtain test data from the file test_data.csv
        When We process the data

        # Recall
        Then the model correctly classifies real positives of all classes 70 percent of the time
        Then the model correctly classifies real positives of all classes with a macro average 70 percent of the time
        Then the model correctly classifies real positives of all classes with a weighted average 70 percent of the time
        Then the model correctly classifies real positives of class 'False' 70 percent of the time
        
        # Precision 
        Then the model will reach a value of 70 on the metric precision on class 'False'
        Then the model correctly classifies predicted positives of class 'False' 70 percent of the time
        Then the model correctly classifies predicted positives of all classes 70 percent of the time
        Then the model correctly classifies predicted positives of all classes with a macro average 70 percent of the time
        Then the model correctly classifies predicted positives of all classes with a weighted average 70 percent of the time
        

        
        # Accuracy
        Then the model will reach a value of 70 on the metric accuracy
        Then the model correctly classifies all classes 70 percent of the time

        # F1 Score
        Then the model will reach a value of 70 on the metric f1_score
        Then the model will reach a value of 70 on the metric f1_score on a macro average
        Then the model will reach a value of 70 on the metric f1_score on a weighted average
        Then the model will reach a value of 70 on the metric f1_score on class 'False'