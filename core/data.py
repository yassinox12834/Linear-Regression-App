import pandas as pd


class DataHandler:
    """Class used for handling dataset loading and column extraction"""

    def __init__(self, path: str):
        self.path = path
        self.df = None

    def load_data(self):
        """Loads the data"""
        self.df = pd.read_csv(self.path)
        if self.df.empty:
            raise ValueError("Dataset is empty")
        return self.df
    
    def missing_values(self): 
        """Checks and deletes the lines with missing values, returns the number of dropped lines"""
        before = len(self.df)
        self.df = self.df.dropna()
        dropped = before - len(self.df)
        return dropped

    def get_columns(self, y: str, x: str, x_2: str = None):
        """
        Return target (y) and feature(s) (x, optional x_2)
        """

        if self.df is None:
            raise ValueError("You must call load_data() first")


        for col in [y, x, x_2]:
            if col is not None and col not in self.df.columns:
                raise ValueError(f"Column '{col}' not found in dataset")

        y_column = self.df[y].to_numpy()
        x_column = self.df[x].to_numpy()

        if x_2 is not None:
            x_column2 = self.df[x_2].to_numpy()
            return y_column, x_column, x_column2

        return y_column, x_column  





    def check_string_columns(self):
        """Returns the list of columns that contain string (object) values, excluding the header"""
        if self.df is None:
            raise ValueError("You must call load_data() first")
        return self.df.select_dtypes(include="object").columns.tolist()  




