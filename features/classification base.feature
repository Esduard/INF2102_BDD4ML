Feature: testing a classification model performance 
    Scenario: run a performance test on a classification model
        Given We obtain a model from the file {}
        And We evaluate the test as a classification problem
        And We obtain test data from the file {}
        When We process the data  