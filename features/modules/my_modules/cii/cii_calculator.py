from pandas import DataFrame
from . import CIIAttained
from . import CIIIMO
from . import CIIRating
from . import CIIReference
from . import CIIRequired


class CIICalculator:
    """Operator responsible for generating all the necessary CII information.
    
    Attributes:
        df: DataFrame containing the emissions information.
    """

    def __init__(self, df: DataFrame) -> None:
        self.df = df

    def calculate_cii(self, co2_emissions_with_exclusions: str, dwt: str, distance: str,
                      ship_type: str, cii_prefix: str) -> DataFrame:
        """Create all CII columns and return dataframe with new columns.
        
        Args:
            year: String with the 'Year' column name.
            co2_emissions_with_exclusions: String with the 'DWT' column name.
            dwt: String with the 'DWT' column name.
            distance: String with the 'DWT' column name.
            cii_prefix: String with one of the prefixes 'min', 'mean' or 'max.

        Returns:
            The received dataframe with the new CII columns.
        """
        df = self.df

        df = CIIAttained(df).get_attained_cii(co2_emissions_with_exclusions, dwt, distance)
        df = CIIReference(df).get_cii_reference(ship_type, dwt)
        df = CIIRequired(df).get_cii_required(cii_prefix=cii_prefix)

        df = CIIIMO(df).get_cii_imo(cii_prefix=cii_prefix)
        df = CIIRating(df).get_cii_rating(dwt, cii_prefix=cii_prefix)

        return df
