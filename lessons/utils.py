from statsmodels.tsa.stattools import adfuller, kpss

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