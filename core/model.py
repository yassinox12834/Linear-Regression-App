from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np


class Analyser:
    def __init__(self):
        self.model = LinearRegression()

    def training(self, X , Y, test_size=0.2, x_column_2=None):
        """
        X = features
        Y = target
        test_size = from the interface
        """

        if x_column_2 is not None:
            X = [[a, b] for a, b in zip(X, x_column_2)]
        else:
            X = X.reshape(-1, 1)
        
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            Y,
            test_size=test_size,
            random_state=42
        )

        self.model.fit(X_train, y_train)
        y_predictions = self.model.predict(X_test)

        report = {
            "MSE" : mean_squared_error(y_test, y_predictions),
            "R2"  : r2_score(y_test, y_predictions),
            "y_train" : y_train,
            "y_test"  : y_test,
            "x_train" : X_train,
            "x_test"  : X_test,
            "y_pred"  : y_predictions,
            "coef1"       : self.model.coef_[0],
            "coef2"       : self.model.coef_[1] if x_column_2 is not None else None,  #None if list is 1-dimensional
            "intercept"   : self.model.intercept_,



        }
        return report
    
    def predict(self, value):
        """"This method is for predicting values you insert yourself, which are not in the CSV"""
        value = np.array(value).reshape(1, -1)
        return self.model.predict(value)[0]
