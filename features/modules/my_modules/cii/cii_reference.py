from pandas import DataFrame

class CIIReference:
    """Object responsible for the calculation of the reference CII.
    
    Use the dataframe containing the information of ship class.

    Attributes:
        df: A dataframe containing the data used in the calculation.
    """

    def __init__(self, df: DataFrame) -> None:
        self.df = df

        self.tanker = ['AFRAMAX-DP', 'AFRAMAX', 'HANDY 1', 'HANDY 2', 'MR 1', 'MR 2', 'PANAMAX-DP', 'PANAMAX',
                       'SUEZ-DP', 'SUEZMAX', 'VLCC']
        self.gas_carrier = ['PRESS.', 'MGC', 'SEMI REFR.', 'VLGC', 'SMALL PRESS.']

    def __calculate_cii_reference(self, row, dwt):

        if row['class_imo'] == 'tanker':
            row['cii_reference'] = 5247 * row[dwt] ** (-0.610)

        elif row['class_imo'] == 'gas_carrier':
            if row[dwt] >= 65000:
                row['cii_reference'] = 14405e+7 * row[dwt] ** (-2.071)
            else:
                row['cii_reference'] = 8104 * row[dwt] ** (-0.639)

        return row

    def get_cii_reference(self, ship_type: str, dwt: str) -> DataFrame:
        """Calculate the reference CII and return a dataframe containing calculated reference CII.
        
        Args:
            ship_type: String with the 'ship type' column
            name.
            dwt: String with the 'DWT' column name.

        Returns:
            The received dataframe with a new column containing the calculated reference CII."""

        df = self.df
        df['cii_reference'] = ''
        df['class_imo'] = ''

        df.loc[df[ship_type].isin(self.tanker), 'class_imo'] = 'tanker'
        df.loc[df[ship_type].isin(self.gas_carrier), 'class_imo'] = 'gas_carrier'

        df = df.apply(self.__calculate_cii_reference, axis=1, dwt=dwt)
        return df
