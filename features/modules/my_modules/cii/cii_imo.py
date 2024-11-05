from pandas import DataFrame

class CIIIMO:
    """Object responsible for the calculation of the CII IMO.
    
    Use the dataframe containing the information of attained and required CII and calculate the
    CII IMO.

    Attributes:
        df (DataFrame): A dataframe containing the data used in the calculation."""

    def __init__(self, df: DataFrame) -> None:
        self.df = df

    def get_cii_imo(self, cii_prefix):
        """Calculate the CII IMO and returns the dataframe with a new CII IMO column

        Args:
            cii_prefix: String with one of the prefixes 'min', 'mean' or 'max.
        
        Return:
            The received dataframe with a new column containing the calculated CII IMO.
        """
        df = self.df
        df[f'{cii_prefix}_cii_imo'] = df['attained_cii'] / df[f'{cii_prefix}_required_cii']
        return df

