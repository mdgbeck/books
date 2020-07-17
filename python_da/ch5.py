import numpy as np
import pandas as pd

obj = pd.Series([4, 7, 5, -3])
obj
obj.values
obj.index

obj2 = pd.Series([4, -7, -5, 3], index = ['d', 'b', 'a', 'c'])
obj2
obj.index
obj2['a']
obj2['a'] = 99
obj2

obj2[obj2 > 0]
'b' in obj2

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index = states)
obj4
pd.isnull(obj4)
obj4.isnull()
pd.notnull(obj4)

# can use indexs to sort of join operations
obj3 + obj4

# give names to index and values (series ess. 1 col data with rownames)
obj4.name = 'population'
obj4.index.name = 'state'
obj4

obj
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
obj

# DataFrames
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
frame
pd.DataFrame(data, columns = ['year', 'state', 'pop'])
frame2 = pd.DataFrame(data, columns = ['year', 'state', 'pop', 'debt'],
        index = ['one', 'two', 'three', 'four', 'five', 'six'])
frame2.columns
frame2['state']
frame2.state # same as line above but will only work when names are valid variable name
frame2.loc['three']
frame2.debt = 165
frame2
frame2['debt'] = np.arange(6.)
frame2
frame2.debt = range(6)

# can use series to "join" value over index
val = pd.Series([-1.2, -1.5, -1.7], index = ['two', 'three', 'five'])
frame2['debt'] = val
frame2
frame2['eastern'] = frame2.state == 'Ohio'
# frame2.eastern = '' # this doesn't work, save separate attr
frame2['western'] = True
frame2['test'] = 23
del frame2['test']

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
        'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
frame3

# reindexing
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index = ['d', 'b', 'a', 'c'])
obj
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj2

obj3 = pd.Series(['blue', 'purple', 'yellow'], index = [0, 2, 4])
obj3 = pd.Series(['blue', 'purple', 'yellow'], index = np.arange(0, 5, 2))
obj3
obj3.reindex(range(6), method='ffill') # foward fill to add missing indexes

# reoder DateFrame, will use rows default but can do columns as well
f = pd.DataFrame(np.arange(9).reshape((3, 3)),
        index = ['a', 'd', 'c'],
        columns = ['Ohio', 'Texas', 'California'])
f
f2 = f.reindex(['a', 'b', 'c', 'd'])
f2
states = ['Texas', 'Utah', 'California']
f.reindex(columns=states)

# dropping entries
obj = pd.Series(np.arange(5.), index = ['a', 'b', 'c', 'd', 'e'])
obj
obj.drop('c')
obj # still exists, need to save this one
new_obj = obj.drop('c')
new_obj
obj.drop(['d', 'c'])

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
        index = ['Ohio', 'California', 'Utah', 'New York'],
        columns = ['one', 'two', 'three', 'four'])
data
data.drop(['Ohio', 'Utah'])
data.drop(['one', 'two'], axis = 1, inplace = True) # the inplace saves
data

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
        index = ['Ohio', 'California', 'Utah', 'New York'],
        columns = ['one', 'two', 'three', 'four'])
data['two']
data[['three', 'one']]
data[data['three'] > 5]
data[data < 5] = 0
data

data.loc['California', ['two', 'three']]
data.iloc[2, [3, 0, 1]]
data.iloc[2]

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index = ['a', 'c', 'e', 'f', 'g'])
s1
s2
s1 + s2 # sort auto outerjoin

df1 = pd.DataFrame(np.arange(9).reshape((3, 3)), columns=list('bcd'),
        index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12).reshape((4, 3)), columns=list('bde'),
        index=['Utah', 'Ohio', 'Texas', 'Oregon'])
df1
df2
df1 + df2

df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
df2
df2.loc[1, 'b'] = np.nan
df2
df1 + df2
df1
df1.add(df2, fill_value = 0) # puts 0 where NA before adding essentially

# operations between dataframes and series
arr = np.arange(12.).reshape((3, 4))
arr
arr[0]
arr - arr[0]

frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
        columns = list('bde'),
        index = ['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]
series
frame
frame - series
series2 = pd.Series(range(3), index=['b', 'e', 'f'])
frame + series2

frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
        index = ['Utah', 'Ohio', 'Texas', 'Oregon'])
frame
np.abs(frame)

f = lambda x: x.max() - x.min()
frame
frame.apply(f)
frame.apply(f, axis='columns')
frame.apply(f, axis=1) # same as above

def f(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])
frame
frame.apply(f)

format = lambda x: '%.2f' % x
frame.applymap(format) # applymap is for element line functions
frame['e'].map(format)

# sorting and ranking
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
obj
obj.sort_index()

frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
            index=['three', 'one'],
            columns=['d', 'a', 'b', 'c'])
    frame.sort_index()
    frame.sort_index(axis=1)
    frame.sort_index(axis=1, ascending=False)

obj = pd.Series([4, 7, -3, 2])
obj.sort_values()

obj = pd.Series([4, 7, -3, 2])
obj.sort_values()
obj = pd.Series([4, np.nan, 7, -3])
obj.sort_values()

frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
frame
frame.sort_values(by='b')
frame.sort_values(by=['a', 'b'])

obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
obj.rank() # gives a value to the order they are sorted, taking mean of same values
obj.rand(method='first') # same values ordered by which is first

frame = pd.DataFrame({'b': [4.3, 7, -3, 2],
                    'a': [0, 1, 0, 1],
                    'c': [-2, 5, 8, -2.5]})
frame.rank(axis=1)

# duplicate axis labels
obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
obj
obj.index.is_unique


# summarizing and computing descriptive statistics
df = pd.DataFrame([[1.4, np.nan],
                    [7.1, -4.5],
                    [np.nan, np.nan],
                    [0.75, -1.3],],
                index=list('abcd'),
                columns=['one', 'two'])

df
df.sum()
df.sum(axis='columns')
df.sum(axis=1, skipna=False)
df.cumsum()
df.describe()
obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
obj.describe()

# correlation and covariance
import pandas_datareader.data as web
all_data = {ticker: web.get_data_yahoo(ticker)
        for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG', 'KO']}

price = pd.DataFrame({ticker: data['Adj Close']
    for ticker, data in all_data.items()})
volume = pd.DataFrame({ticker: data['Volume']
    for ticker, data in all_data.items()})
returns = price.pct_change() # time series operation
returns.tail()
returns['MSFT'].corr(returns['IBM'])
returns.MSFT.corr(returns.IBM)
returns['MSFT'].cov(returns['IBM'])
# on full df gets matrix
returns.corr()
returns.cov()

# unique values, counts, membership
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
obj.unique()
obj.value_counts()
obj.isin(['b', 'c'])
obj[obj.isin(['b', 'c'])]
all_data

