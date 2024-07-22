import pandas as pd

class DataProcessor:
    @staticmethod
    def filter_data(data: pd.DataFrame, condition):
        return data.query(condition)
    
    @staticmethod
    def sort_data(data: pd.DataFrame, column_name):
        return data.sort_values(by=column_name)
    
    