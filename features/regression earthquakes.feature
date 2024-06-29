Feature: testing a regression model performance 
    Scenario: run a performance test on a regression model
        Given We obtain a regression model from the file earthquakeKNNRegressor-orig.pkl
        And We obtain test data from the file test_data_earthquake.csv
        When We process the data

        #MSE
        Then the model will reach a Mean Squared Error below 30

        #R2 score
        And the model will reach an R2 Score above 0.1

        #MAE
        And the model will reach a Mean Absolute Error below 3


        #RMSE
        And the model will reach a Root Mean Squared Error below 5

        #Median Absolute Error
        And the model will reach a Median Absolute Error below 2