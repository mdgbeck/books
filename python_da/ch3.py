import bisect

c = [1, 2, 2, 2, 3, 4, 5, 7]

bisect.bisect(c, 6) # finds where
bisect.insort(c, 6) # insets in


seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
seq[-2: ]
seq[1:-4:2]
seq[::-1]
seq[5:2]  # return empty but not an error

# enumerate tracks iteration
i = 0
for value in collection:
    # do something
    i += 1
# is the same as
for i, value in enumerate(collection):
    # do something


some_list = ['list', 'bar', 'baz']
mapping = {}

for i, v in enumerate(some_list):
    mapping[v] = i

mapping

x = [7, 3, 1, 6, 3, 5]
sorted(x) # returns sorted list but keeps original in place
x.sort() # sorts original list
x

# zip combines lists
seq1 = ['a', 'b', 'c']
seq2 = ['one', 'two', 'three']
seq3 = [True, False]

x = zip(seq1, seq2)
list(x)

list(zip(seq1, seq2, seq3))

for i, (a, b) in enumerate(zip(seq1, seq2)):
    print('{0}: {1}, {2}'.format(i, a, b))
    

pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')] 

first_names, last_names = zip(*pitchers)
first_names
last_names

d = {
        'a': 'some value',
        'b': [1, 2, 3, 4],
        'c': 'nonsense',
    }

d[7] = 'an integer'
d
d['b']
d[5] = 'other value'
d['dummy'] = 'another dumb value'
d
del d[5]
d
dum = d.pop('dummy')
dum
list(d.keys())
list(d.values())

d.update({'b' : 'foo', 'c' : 12})
d

# two ways to make dicts from seq
value_list = ['one', 'two', 'three']
key_list = ['a', 'b', 'c']
mapping = {}
for key, value in zip(key_list, value_list):
    mapping[key] = value
mapping

# option b for better
mapping = dict(zip(key_list, value_list))
mapping

# better way to do following
if key in some_dict:
    value = some_dict[key]
else:
    value = default_value

value = some_dict.get(key, default_value)


words = ['apple', 'bat', 'bar', 'atom', 'book']

by_letter = {}

for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
by_letter
# becomes
by_letter = {}
for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)
by_letter
# and becomes
by_letter = []
from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
    by_letter[word[o]].append(word)
by_letter

# sets
a = set([1, 2, 3, 4, 5])
b = {4, 5, 6, 7, 8}

a.union(b)
a | b

a.intersection(b)
a & b

# list comprehensions
res = []
for val in collections:
    if condition:
        res.append(expr)
[expr for val in collection if condition]

strings = ['a', 'as', 'bat', 'cat', 'dove', 'python']
[x.upper() for x in strings if len(x) > 3]

# dict comprehension
dict_comp = {key_expr : value_expr for value in collection if conditions}
unique_lengths = {len(x) for x in strings}
unique_lengths
set(map(len, strings)) # also can use map

loc_map = {val : index for index, val in enumerate(strings)}
loc_map

# nest comps
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steve'],
        ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]


names_of_interest = []
for names in all_data:
    enough_es = [name for name in names if name.count('e') >= 2]
    names_of_interest.extend(enough_es)
names_of_interest


res = [name for names in all_data for name in names
        if name.count('e') >= 2]
res

some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for tup in some_tuples for x in tup]
flattened

import re

states = ['   Alabama', 'Georgia!', 'Georgia', 'georgia', 'FlorIDa', 'south   CarolIna##', 'West virginia?']
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result

clean_strings(states)

# probably better to do
def remove_punct(value):
    return re.sub('[[!#?]', '', value)

clean_ops = [str.strip, remove_punct, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result

clean_strings(states, clean_ops)

for x in map(remove_punct, states):
    print(x)

for i in states:
    x = remove_punct(i)
    print(x)

# lambda functions
def short_func(x):
    return x*2

equiv_func = lambda x: x*2

short_func(3)
equiv_func(3)

def apply_to_list(some_list, f):
    return [f(x) for x in some_list]

ints = [4, 0, 1, 5, 6, ]
apply_to_list(ints, lambda x:x * 2)

strings = ['foo', 'card', 'bar', 'aaa', 'abab', 'michael', 'aaaaaaaaaaaaaaa', 'abcdefghijklmnopqrstuvwxyz']
strings.sort(key=lambda x: len(set(list(x))))
strings

def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2 # nothing happens until requested

gen = squares()

gen = (x ** 2 for x in range(100))
gen
dict((i, i**2) for i in range(6))

import itertools
first_letter = lambda x: x[0]

names = ['Alan', 'Adam', 'Wes', 'Will', 'Alber', 'Steven']
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names)) # names is a generator

x
