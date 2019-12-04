import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class ts_generator():
    def f(self, x):
        y = np.random.randint(0, 100)
        result = []
        for _ in x:
            result.append(y)
            y += np.random.normal(scale=1)
        return np.array(result)

    def generate(self, ts_number, length, plot=True):
        timeseries_data = []
        columns = []
        for i in range(0, 20):
            x = np.linspace(0, 1000, length)
            timeseries_data.append(self.f(x))
            columns.append('TS_'+str(i))

        ts_df = pd.DataFrame(timeseries_data).T
        ts_df.columns = columns
        if plot:
            ts_df.plot(legend=False, figsize=(16, 8))
        return ts_df
