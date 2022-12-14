from statsmodels.tsa.stattools import adfuller, kpss
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, mean_squared_log_error
import numpy as np

# tests to check stationarity
def adf_test(timeseries, print_only_result=True):
    """"Augmented Dickey-Fuller test""" 
    # run test
    results = adfuller(timeseries)
    print('\nADF Test Results')
    print('-----------------')
    # display all results
    if print_only_result is False:
        print(f'ADF Statistic: {results[0]}')
        print(f'p-value: {results[1]}')
        print(f'num lags: {results[2]}')
        print('Critical Values:')
        for key, value in results[4].items():
            print(f'\t{key} : {value}')
    # conclusion
    print(f'Result: The timeseries is {"not " if results[1] > 0.05 else ""}stationary')

def kpss_test(timeseries, print_only_result=True):
    """KPSS test"""
    # run test
    statistic, p_value, n_lags, critical_values = kpss(timeseries)
    print('\nKPSS Test Results')
    print('-----------------')
    # display all results
    if print_only_result is False:
        print(f'KPSS Statistic: {statistic}')
        print(f'p-value: {p_value}')
        print(f'num lags: {n_lags}')
        print('Critical Values:')
        for key, value in critical_values.items():
            print(f'\t{key} : {value}')
    # conclusion:
    print(f'Result: The timeseries is {"not " if p_value < 0.05 else ""}stationary')


# =========METRICS================================================================================================
# evaluation related functions
def RMSLE(y_true:np.ndarray, y_pred:np.ndarray) -> np.float64:
    """
        Root Mean Squared Log Error (RMSLE) metric 
        Args:        
            y_true: real values
            y_pred: predicted values
            
        Returns:   
            RMSLE score
    """
    return np.sqrt(mean_squared_log_error(y_true, y_pred))

def RMSE(y_true:np.ndarray, y_pred:np.ndarray) -> np.float64:
    """
        Root Mean Squared Error (RMSE) metric
        Args:
            y_true: real values
            y_pred: predicted values
            
        Returns:
            RMSE score
    """
    return np.sqrt(mean_squared_error(y_true, y_pred))


metrics = {'RMSLE': RMSLE, 'MAE': mean_absolute_error, 'RMSE': RMSE, 'MAPE': mean_absolute_percentage_error}
