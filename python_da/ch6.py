import pandas as pd

df = pd.read_csv('examples/ex1.csv')
# df.to_csv(r'examples/ex2.csv', index=False, header=False) # ex2 no longer has header
df2 = pd.read_csv('examples/ex2.csv')
df2
df2 = pd.read_csv('examples/ex2.csv', header=None)
df2
df2 = pd.read_csv('examples/ex2.csv', names=['a','b', 'c', 'd', 'message'])
df2
names=['a','b', 'c', 'd', 'message']
pd.read_csv('examples/ex2.csv', names=names, index_col='message')
!cat examples/csv_mindex.csv # calls to command line
parsed = pd.read_csv('examples/csv_mindex.csv',
        index_col=['key1', 'key2'])
parsed

list(open('examples/ex3.txt'))
result = pd.read_table('examples/ex3.txt', sep='\s+')
result

!cat examples/ex4.csv
pd.read_csv('examples/ex4.csv', skiprows=[0, 2, 3])

# declare what becomes NaN
result = pd.read_csv('examples/ex5.csv', na_values=['NULL']) #NULL included by default though
result
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
pd.read_csv('examples/ex5.csv', na_values=sentinels) # sets NA values for each column

# set pandas displays
# pd.options.display.max_rows = 10 (think 10 is default)
result = pd.read_csv('examples/ex6.csv')
result
pd.read_csv('examples/ex6.csv', nrows=5)

# to read chunk by chunk
chunker = pd.read_csv('examples/ex6.csv', chunksize=1000)
chunker

tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot
tot = tot.sort_values(ascending=False)
tot[:10]

import csv
f = open('examples/ex7.csv')

reader = csv.reader(f)
for line in reader:
    print(line)

# json data
obj = """
{"name": "Wes",
 "places_lived": ["United Stats", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
              {"name": "Katie", "age": 38, "pets": ["Sixes", "Stache", "Cisco"]}]
}
 """

import json
result = json.loads(obj)
result
asjson = json.dumps(result) # sends python back to json

siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])
siblings

!cat examples/example.json
data = pd.read_json('examples/example.json')
data.to_json()

# html data
tables = pd.read_html('examples/fdic_failed_bank_list.html')
df = tables[0] # read html returns list of tables

# look at what year banks failed
close_timestamps = pd.to_datetime(df['Closing Date'])
close_timestamps.dt.year.value_counts()

# xml stuffs
from lxml import objectify

path = 'datasets/mta_perf/Performance_MNR.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()

data = []
skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ',
        'DESIRED_CHANGE', 'DECIMAL_PLACES']

for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)

perf = pd.DataFrame(data)

# excel
pd.read_excel('examples/ex1.xlsx')
xlsx = pd.ExcelFile('examples/ex1.xlsx')
frame = pd.read_excel(xlsx, 'Sheet1')

writer = pd.ExcelWriter('~/ex2.xlsx')
frame.to_excel(writer, 'Sheet1')
writer.save()
frame.to_excel('~/ex222222.xlsx')


# using APIs
import requests

url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
data = resp.json()

issues = pd.DataFrame(data, columns=['number', 'title', 'lables', 'state'])
