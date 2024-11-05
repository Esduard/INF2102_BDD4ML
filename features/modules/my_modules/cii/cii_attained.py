import numpy as np
from pandas import DataFrame


class CIIAttained:
    """Object responsible for the calculation of the attained CII.
    
    Use the dataframe containing the information of fuel consumption and calculate the attained
    CII.

    Attributes:
        df (DataFrame): A dataframe containing the data used in the calculation.
    """

    def __init__(self, df: DataFrame) -> None:
        self.df = df

    def get_attained_cii(self, co2_emissions_with_exclusions: str, dwt: str, distance: str
                         ) -> DataFrame:
        """Calculate the attained CII and return a dataframe containing calculated attained CII.
        
        Args:
            co2_emissions_with_exclusions: String with the 'CO2 emissions with exclusions' column
            name.
            dwt: String with the 'DWT' column name.
            distance: String with the 'Distance' column name.

        Returns:
            The received dataframe with a new column containing the calculated attained CII.
        """
        df = self.df
        df['attained_cii'] = (df[co2_emissions_with_exclusions] / (df[distance] * df[dwt])
                                      ) * (10 ** 6)
        df['attained_cii'].replace([np.inf, -np.inf], 0, inplace=True)

        return df
