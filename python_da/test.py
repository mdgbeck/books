import pandas as pd
import numpy as np

def test_single(n):
    df = pd.DataFrame(np.random.randn(n, 1))
    df2 = df.sample(2, replace=True)
    return df2.iloc[0,] == df2.iloc[1,]

dist = 10
n_tests = 10000
x = pd.DataFrame(np.arange(1, dist).reshape((1, ( dist-1 ))))
y = x.append(x.iloc[[-1]*(n_tests-1)])
y.columns = range(1, dist)


for i in range(1, dist):
    y[i] = y[i].apply(test_single)
