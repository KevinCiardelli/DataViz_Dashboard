import pandas as pd

class DataLoader:
    @staticmethod
    def load_csv(file_path):
        return pd.read_csv(file_path)
    
    @staticmethod
    def load_excel(file_path):
        return pd.read_excel(file_path)