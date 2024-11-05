Feature: testing a regression model performance 
    Scenario: run a performance test on a regression model
        Given We obtain a model from the file KNNRegressor-orig
        And We evaluate the test as a regression problem
        And We obtain test data from the file test_data_regression.csv
        When We process the data

        #MSE
        Then the model will reach a Mean Squared Error below 30

        #R2 score
        And the model will reach an R2 Score above 0.2