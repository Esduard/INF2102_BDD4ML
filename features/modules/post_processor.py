from abc import ABC, abstractmethod
from features.modules.my_modules.cii.cii_calculator import CIICalculator


class PostProcessor(ABC):
    '''Classe abstrata que contém operaçoes de um pos processador de dados. '''
    @abstractmethod
    def postprocess(self,dataset):
        pass

class CarbonPostProcessor(PostProcessor):
    def __init__(self, features, label, ship_type_column='ship_type_name', ship_type = None):
        print("Setting Up CarbonPostProcessor")
        self.features = features
        self.label = label
        self.ship_type_column = ship_type_column
        self.ship_type = ship_type

    def __filter_by_ship_type(self, dataset, ship_type):
        """Filter the dataset by the ship type."""
        return dataset[dataset[self.ship_type_column].isin([ship_type])]
    
    def postprocess(self,dataset, y_test, predictions):
        dataset = self.__filter_by_ship_type(dataset, self.ship_type)

        dataset['y_test'] = y_test
        dataset['predictions'] = predictions

        y_values_column = 'y_test'
        predictions_column = 'predictions'



        # Calculate CII for y_test values
        dataset = CIICalculator(dataset).calculate_cii(
            co2_emissions_with_exclusions=y_values_column, dwt='dwt', distance='distance',
            ship_type='ship_type_name', cii_prefix=y_values_column
        )
        print('---------------------------')
        print(dataset.columns)
        print(dataset['y_test_cii'].head(5))

        # Calculate CII for predictions
        dataset = CIICalculator(dataset).calculate_cii(
            co2_emissions_with_exclusions=predictions_column, dwt='dwt', distance='distance',
            ship_type='ship_type_name', cii_prefix=predictions_column
        )
        print('---------------------------')
        print(dataset.columns)
        print(dataset['predictions_cii'].head(5))

        # Replace NaN values in 'predictions_cii' and 'y_test_cii' with 'E'
        dataset['predictions_cii'] = dataset['predictions_cii'].fillna('E')
        dataset['y_test_cii'] = dataset['y_test_cii'].fillna('E')
        ''' 
        # Filter rows where 'predictions_cii' is NaN
        nan_rows = dataset[dataset['predictions_cii'].isna()]

        # Reduce to specific columns
        columns_to_keep = [
            "distance",
            "dwt",
            "harbor_time",
            "fo_per_distance",
            "PETROLEIRO",
            "is_platform",
            "Cabotagem",
            "Exportação",
            "Importação",
            "Internacional",
            "distance_restricted",
            'predictions_cii',
            'y_test_cii',
            'predictions',
            'y_test'
        ]

        # Filter columns
        nan_rows_reduced = nan_rows[columns_to_keep]

        # Print the reduced DataFrame
        print(nan_rows_reduced)

        # Export the reduced DataFrame to a CSV file
        #nan_rows_reduced.to_csv('nan_rows_reduced.csv', index=False)
        '''
        

    
        return dataset, y_values_column + "_cii", predictions_column + "_cii"