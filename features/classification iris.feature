Feature: testing a classification model performance 
    Scenario: run a performance test on a classification model
        Given We obtain a classification model from the file irisCART-orig.pkl
        And We obtain test data from the file test_data_iris.csv
        When We process the data
        Then the model will reach 70 percent accuracy
        And the model will reach 70 percent f1_score

        # Recall
        And the model will reach 70 percent recall on a macro average
        And the model identifies 70 percent of the correct cases of all classes with a macro average
        And the model identifies 70 percent of the correct cases of class 'virginica'
        
        # Precision 
        And the model will reach 70 percent precision on class 'virginica'
        And the model classifies positives of class 'virginica' correctly 70 percent of the time
        And the model classifies positives of all classes with a macro average correctly 70 percent of the time

        # Accuracy
        And the model will reach 70 percent accuracy
        And the model classifies class 'virginica' correctly 70 percent of the time
        And the model classifies all classes correctly 70 percent of the time

        And the model will reach 70 percent f1_score on a weighted average
        
        And the model will reach 70 percent support on class 'virginica'
        And the model will reach 50 percent recall on class 'setosa'