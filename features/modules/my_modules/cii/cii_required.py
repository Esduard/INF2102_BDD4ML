from pandas import DataFrame

class CIIRequired:
    """Object responsible for the calculation of the required CII.
    
    Use the dataframe containing the information of year and reference cii and calculate the
    required CII.

    Attributes:
        df: A dataframe containing the data used in the calculation.
    """

    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.z_20 = 1  # reduction factor for the year of 2020
        self.z_21 = 2  # reduction factor for the year of 2021
        self.z_22 = 3  # reduction factor for the year of 2022
        self.z_23 = 5  # reduction factor for the year of 2023
        self.z_24 = 7  # reduction factor for the year of 2024
        self.z_25 = 9  # reduction factor for the year of 2025
        self.z_26 = 11  # reduction factor for the year of 2026

    def get_cii_required(self, cii_prefix: str) -> DataFrame:
        """Calculate the required CII and return a dataframe containing calculated required CII.
        
        Args:
            year: String with the 'year' column name.

        Returns:
            The received dataframe with a new column containing the calculated required CII.
        """

        df = self.df
        df.loc[df['year'] == 2020, f'{cii_prefix}_required_cii'] = ((100 - self.z_20) / 100) * df['cii_reference']
        df.loc[df['year'] == 2021, f'{cii_prefix}_required_cii'] = ((100 - self.z_21) / 100) * df['cii_reference']
        df.loc[df['year'] == 2022, f'{cii_prefix}_required_cii'] = ((100 - self.z_22) / 100) * df['cii_reference']
        df.loc[df['year'] == 2023, f'{cii_prefix}_required_cii'] = ((100 - self.z_23) / 100) * df['cii_reference']
        df.loc[df['year'] == 2024, f'{cii_prefix}_required_cii'] = ((100 - self.z_24) / 100) * df['cii_reference']
        df.loc[df['year'] == 2025, f'{cii_prefix}_required_cii'] = ((100 - self.z_25) / 100) * df['cii_reference']
        df.loc[df['year'] == 2026, f'{cii_prefix}_required_cii'] = ((100 - self.z_26) / 100) * df['cii_reference']
        df.loc[df['year'] > 2026, f'{cii_prefix}_required_cii'] = ((100 - self.z_26) / 100) * df['cii_reference']

        return df
