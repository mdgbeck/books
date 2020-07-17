import numpy as np
import pandas as pd
from numpy import nan as NA

string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
string_data.isnull()

string_data[0] = None
string_data.isnull()

data = pd.Series([1, NA, 3.5, NA, 7])
data.dropna()
data[data.notnull()] # same as above

data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],
    [NA, NA, NA], [NA, 6.5, 3.]])
data
data.dropna() # will drop rows where any column is NA
data.dropna(how='all') # will drop rows where all cols are NA w
data.dropna(how='all', axis=1)
data.dropna(axis=1)

df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
df
df.dropna()
df.dropna(thresh=2) #drop any rows that do not contain at least two observations

df.fillna(0)
df.fillna({1: 0.5, 2: 0}) # use dict to fill col differently
df.fillna(0, inplace=True) # saves call to original
df

data = pd.Series([1., NA, 3.5, NA, 7])
data.fillna(data.mean())

data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                    'k2': [1, 1, 2, 3, 3, 4, 4]})
data.duplicated()
data.drop_duplicates()
data['v1'] = range(7)
data.drop_duplicates(['k1'])
data.drop_duplicates('k1') # also works
data.drop_duplicates(['k1', 'k2'], keep='last')

data = pd.DataFrame({
    'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon',
        'pastrami', 'honey ham', 'nova lox'],
    'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]
    })
data

meat_to_animal = {
        'bacon': 'pig',
        'pulled pork': 'pig',
        'pastrami': 'cow',
        'corned beef': 'cow',
        'honey ham': 'pig',
        'nova lox': 'salmon',
    }
lowercased = data['food'].str.lower()
data['animal'] = lowercased.map(meat_to_animal)
data
data['animal2'] = data['food'].map(lambda x: meat_to_animal[x.lower()])

# replacing values
data = pd.Series([1., -999, 2, -999, -1000, 3])
data.replace(-999, NA) # doesn't save unless inplace=True
data.replace([-999, -1000], [NA, 1e6], inplace=True)
data

data = pd.DataFrame(np.arange(12).reshape((3, 4)),
        index=['Ohio', 'Colorado', 'New York'],
        columns=['one', 'two', 'three', 'four'])
transform = lambda x: x[:4].upper()
def transf(x):
    return x[:4].upper()
data.index.map(transf) # only keeps first characters of index
data.index = data.index.map(transform)

data.rename(index={'OHIO': 'INDIANA'},
        columns={'three': 'peekaboo'})
data.rename(index={'OHIO': 'INDIANA'}, inplace=True)

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
cats
cats.codes
cats.categories
pd.value_counts(cats)
group_names = ['Youth', 'YoungAdult', 'MiddleAge', 'Senior']
pd.cut(ages, bins, labels=group_names)

data = np.random.randn(1000)
cats = pd.qcut(data, 4)
cats
pd.value_counts(cats)
cats = pd.qcut(data, [0, 0.1, 0.5, 0.9, 1])
pd.value_counts(cats)

# Detecting and filtering outliers
data = pd.DataFrame(np.random.randn(1000, 4))
data.describe()
col = data[2]
col[np.abs(col) > 3]
data[(np.abs(data) > 3).any(1)]
data[np.abs(data) > 3] = np.sign(data) * 3
data.describe()

# permutation and random sampling
df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
sampler = np.random.permutation(5)
df.take(sampler) # reorders the rows
df.sample(3) # samples 3 random rows w/o replacement
df.sample(2, replace=True) # resample allowed (for bootstrapping and things)

# computing indicator dummy variables
df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
            'data1': range(6)})
pd.get_dummies(df['key'])
dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy =  df[['data1']].join(dummies)


mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('datasets/movielens/movies.dat', sep='::',
        header=None, names=mnames)
all_genres = []
for x in movies.genres:
    all_genres.extend(x.split('|'))
genres = pd.unique(all_genres)

zero_matrix = np.zeros((len(movies), len(genres)))
dummies = pd.DataFrame(zero_matrix, columns=genres)
gen = movies.genres[0]
gen.split('|')
dummies.columns.get_indexer(gen.split('|'))

for i, gen in enumerate(movies.genres):
    indicies = dummies.columns.get_indexer(gen.split('|'))
    dummies.iloc[i, indicies] = 1

movies_windic = movies.join(dummies.add_prefix('Genre_'))
movies_windic.iloc[2]

np.random.seed(12345)
values = np.random.rand(10)
values
bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
pd.get_dummies(pd.cut(values, bins))

# string manipulation
val = 'a, b, guido'
val.split(',')
pieces = [x.strip() for x in val.split(',')]
pieces
first, second, third = pieces
first + '::' + second + '::' + third
'::'.join(pieces) # better way
val.index('b')
val.find('b')
val.index('z')
val.find('z') # find returns -1 rather than error when not in string
val.count(',')
val.replace(',', ',.,.,')
val

import re
text = "foo      bar\t baz   \tqux"
re.split('\s+', text)
regex = re.compile('\s+')
regex.split(text)
regex.findall(text)

text = """
Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""

pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex = re.compile(pattern, flags=re.IGNORECASE)

regex.findall(text)
m = regex.search(text)
m
text[m.start():m.end()]
print(regex.match(text))
print(regex.sub('REDACTED', text))

# pandas strings
data = {
        'Dave': 'dave@google.com',
        'Steve': 'steve@gmail.com',
        'Rob': 'rob@gmail.com',
        'Wes': np.nan,
        }
data = pd.Series(data)
data.str.contains('gmail')
data.str.findall(pattern, flags=re.IGNORECASE)
matches = data.str.match(pattern, flags=re.IGNORECASE)
matches
data.str[:5]
