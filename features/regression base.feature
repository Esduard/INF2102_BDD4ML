Feature: testing a regression model performance 
    Scenario: run a performance test on a regression model
        Given We obtain a model from the file {}
        And We evaluate the test as a regression problem
        And We obtain test data from the file {}
        When We process the data  