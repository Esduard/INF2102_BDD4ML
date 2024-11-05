import numpy as np
from pandas import DataFrame, Series
from sklearn.linear_model import LinearRegression


class CIIRating:
    """Object responsible for the calculation of the CII ratind.
    
    Use the dataframe containing the information of CII IMO and ship class.

    Attributes:
        df: A dataframe containing the data used in the calculation.
    """

    def __init__(self, df: DataFrame) -> None:
        self.df = df

    def get_cii_rating(self, dwt: str, cii_prefix: str) -> DataFrame:
        """Calculate the CII rating and return a dataframe containing calculated CII ratings.
        
        Args:
            dwt: String with the 'DWT' column name.
            cii_prefix: String with one of the prefixes 'min', 'mean' or 'max.

        Returns:
            The received dataframe with a new column containing the calculated CII ratings.
        """
        df = self.df
        df = df.apply(self.__get_cii_letter, target_imo=f'{cii_prefix}_cii_imo',
                    target_rating=f'{cii_prefix}_cii',
                    target_expanded_rating=f'{cii_prefix}_cii_expanded', dwt=dwt, axis=1)

        return df

    @staticmethod
    def __calculate_new_rating_boundaries(d1: float, d2: float, d3: float, d4: float) -> dict:

        # Define initial rating boundaries
        initial_boundaries = [0, d1, d2, d3, d4]

        # Calculate differences between boundaries
        differences = [round(d2 - d1, 2), round(d3 - d2, 2), round(d4 - d3, 2)]

        # Fit a linear regression model
        x_train = np.array([2, 3, 4]).reshape([-1, 1])
        y_train = np.array(differences)
        model = LinearRegression().fit(x_train, y_train)

        # Predict new boundaries
        boundaries_positions = np.array([1, 2, 3, 4, 5]).reshape((-1, 1))
        y_predicted = model.predict(boundaries_positions)

        # Create a dictionary to hold these boundaries with their indices
        rating_boundaries = {i * 3: boundary for i, boundary in enumerate(initial_boundaries)}

        # Initialize the dictionary for new rating boundaries
        new_rating_boundaries = {}

        # Define a percentage to calculate the new rating variables
        scaling_factor = 0.2

        # Calculate the new rating boundaries
        for index in range(0, 13, 3):
            if index == 0:
                new_rating_boundaries[index] = rating_boundaries[index + 3] - y_predicted[index]
                new_rating_boundaries[index + 1] = rating_boundaries[index + 3] - (
                    scaling_factor * y_predicted[index])
                new_rating_boundaries[index + 2] = rating_boundaries[index + 3]

            elif (index > 2) and (index < 10):
                new_rating_boundaries[index] = rating_boundaries[index] + scaling_factor * (
                    rating_boundaries[index + 3] - rating_boundaries[index])
                new_rating_boundaries[index + 1] = rating_boundaries[index] + (
                    1 - scaling_factor) * (rating_boundaries[index + 3] - rating_boundaries[index])
                new_rating_boundaries[index + 2] = rating_boundaries[index + 3]
            else:
                new_rating_boundaries[index] = rating_boundaries[index] + (scaling_factor
                                                                           * y_predicted[4])
                new_rating_boundaries[index + 1] = rating_boundaries[index] + (
                    1 - scaling_factor) * y_predicted[4]
                new_rating_boundaries[index + 2] = float('inf')

        # Apply rounding to the new rating boundaries dictionary
        new_rating_boundaries = {k: round(v, 3) for k, v in new_rating_boundaries.items()}

        return new_rating_boundaries

    def __get_cii_letter(self, row: Series, target_imo: str, target_rating: str,
                        target_expanded_rating: str, dwt: str):

        # Define default boundary values
        d1 = d2 = d3 = d4 = 0

        # Set boundary values based on class_imo
        if row['class_imo'] == 'tanker':
            d1, d2, d3, d4 = 0.82, 0.93, 1.08, 1.28
        elif row['class_imo'] == 'gas_carrier':
            if row[dwt] >= 65000:
                d1, d2, d3, d4 = 0.81, 0.91, 1.12, 1.44
            else:
                d1, d2, d3, d4 = 0.85, 0.95, 1.06, 1.25

        # Define rating boundaries
        rating_boundaries = [(d1, 'A'), (d2, 'B'), (d3, 'C'), (d4, 'D'), (float('inf'), 'E')]
        expanded_rating_boundaries = self.__calculate_new_rating_boundaries(d1, d2, d3, d4)
        expanded_ratings = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-',
                            'D+', 'D', 'D-', 'E+', 'E', 'E-']

        # Assign ratings
        try:
            for boundary, rating in rating_boundaries:
                if (row[target_imo] < boundary) and (row[target_imo] > 0):
                    row[target_rating] = rating
                    break
        except:
            row[target_rating] = None

        # Assign expanded ratings
        try:
            for i in range(len(expanded_ratings)):
                if (row[target_imo] < expanded_rating_boundaries[i]) and (row[target_imo] > 0):
                    row[target_expanded_rating] = expanded_ratings[i]
                    break
        except:
            row[target_expanded_rating] = None

        return row
