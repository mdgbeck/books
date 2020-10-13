import numpy as np
import pandas as pd
from numpy import nan as NA

df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
    'key2' : ['one', 'two', 'one', 'two', 'one'],
    'data1' : np.random.randn(5),
    'data2' : np.random.randn(5)})

grouped = df['data1'].groupby(df['key1'])
grouped
grouped.mean()

means = df['data1'].groupby([df['key1'], df['key2']]).mean()
means

means.unstack()

# can group data with other unralted arrays if right length
states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])

df['data1'].groupby([states, years]).mean()

df.groupby('key1').mean() # auto drops key2 since not numeric data
df.groupby(['key1', 'key2']).mean()
df.groupby(['key1', 'key2']).size()

for name, group in df.groupby('key1'):
    print(name)
    print(group)

for (k1, k2), group in df.groupby(['key1', 'key2']):
    print((k1, k2))
    print(group)

pieces = dict(list(df.groupby('key1')))

df.dtypes
grouped = df.groupby(df.dtypes, axis=1)

for dtype, group in grouped:
    print(dtype)
    print(group)

df.groupby('key1')['data1']
df.groupby('key1')[['data2']]
# top equivalent to bottom# top equivalent to bottom# top equivalent to bottom
df['data1'].groupby(df['key1'])
df[['data2']].groupby(df['key1'])

df.groupby(['key1'])[['data2']].mean()
df.groupby(['key1', 'key2'])[['data2']].mean()
df.groupby(['key1', 'key2'])['data2'].mean()

people = pd.DataFrame(np.random.rand(5, 5),
        columns = ['a', 'b', 'c', 'd', 'd'],
        index = ['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
people.iloc[2:3, [1, 2]] = NA
people

mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
        'd': 'blue', 'e': 'red', 'f': 'orange'}

by_column = people.groupby(mapping, axis=1)
by_column.sum()

map_series = pd.Series(mapping)
map_series

people.groupby(map_series, axis=1).count()

people.groupby(len).sum()

key_list =['one', 'one', 'one', 'two', 'two']
people.groupby([len, key_list]).min()

# data aggregation
grouped = df.groupby('key1')
grouped['data1'].quantile(0.9)

def peak_to_peak(arr):
    return arr.max() - arr.min()

grouped.agg(peak_to_peak)
grouped.describe()

tips = pd.read_csv('examples/tips.csv')

tips['tip_pct'] = tips.tip / tips.total_bill
tips[:6]
grouped = tips.groupby(['day', 'smoker'])
grouped_pct = grouped.tip_pct
grouped_pct.agg('mean')
grouped_pct.agg(['mean', 'std', 'max', 'min', peak_to_peak])
# name agg functions
grouped_pct.agg([('MeAn', 'mean'), ('sTd', np.std)])

functions = ['count', 'min', 'max']
results = grouped['tip_pct', 'total_bill'].agg(functions)
results

grouped.agg({'tip_pct': ['min', 'max', 'mean', 'std'],
    'size': 'sum'})

# make groups columns not indexes
x = tips.groupby(['day', 'smoker'], as_index=False).mean()

def top(df, n=5, column='tip_pct'):
    return df.sort_values(by=column)[-n:]
top(tips, n=6)

tips.groupby('smoker').apply(top)
tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill')

# Random sampling and permutation
