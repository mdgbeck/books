import numpy as np
import pandas as pd
from numpy import nan as NA

data = pd.Series(np.random.randn(9),
        index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
        [1, 2, 3, 1, 3, 1, 2, 2, 3]])
data
data.index
data['b']
data['b':'c']
data.loc[['b', 'd']]
data.loc[:, 2]
data.unstack()
data.unstack().stack()

frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
            index=[['a', 'a', 'b' ,'b'], [1, 2, 1, 2]],
            columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
frame
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
frame
frame['Ohio']
frame.Ohio
pd.MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']],
        names=['state', 'color'])
frame
frame.swaplevel('key1', 'key2')
frame.sort_index(level=1)
frame.swaplevel(0, 1).sort_index(level=0)

frame.sum(level='key2')

frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
    'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
    'd': [0, 1, 2, 0, 1, 2, 3]})
frame
frame2 = frame.set_index(['c', 'd'])
frame2
frame2.reset_index()

# combining and merging datasets
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})

pd.merge(df1, df2)
pd.merge(df1, df2, on='key')
pd.merge(df1, df2, left_on='data1', right_on='data2')
pd.merge(df1, df2, on='key', how='outer')
pd.merge(df1, df2, left_on='data1', right_on='data2', suffixes=('_l', '_r'))

# concatenating along an axis
arr = np.arange(12).reshape((3, 4))
np.concatenate([arr, arr])
np.concatenate([arr, arr], axis=1)

s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])

pd.concat([s1, s2, s3])
pd.concat([s1, s2, s3], axis=1) # basically an outer join of them since no overlap

s4 = pd.concat([s1, s3])
pd.concat([s1, s4], axis=1)

result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
result

pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three'])

df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
        columns=['one', 'two'])
df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],
        columns=['three', 'four'])
pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])

# overlap
a = pd.Series([NA, 2.5, 0, 3.5, 4.5, NA],
        index=['f', 'e', 'd', 'c', 'b', 'a'])
b = pd.Series([0., NA, 2, NA, NA, 5],
        index=['a', 'b', 'c', 'd', 'e', 'f'])
np.where(pd.isnull(a), b, a)
b.combine_first(a)


# reshaping
data = pd.DataFrame(np.arange(6).reshape((2, 3)),
        index=pd.Index(['Ohio', 'Colorado'], name='state'),
        columns=pd.Index(['one', 'two', 'three'], name='number'))
data
data.stack()

data = pd.read_csv('examples/macrodata.csv')
periods = pd.PeriodIndex(year=data.year, quarter=data.quarter, name='date')
columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')
data = data.reindex(columns = columns)
data.index = periods.to_timestamp('D', 'end')
ldata = data.stack().reset_index().rename(columns={0: 'value'})
