import json

path = 'datasets/bitly_usagov/example.txt'

open(path).readline()

records = [json.loads(line) for line in open(path)]

time_zones = [rec['tz'] for rec in records] # doens't work since some no tz field

time_zones = [rec['tz'] for rec in records if 'tz' in rec] # doens't work since some no tz field

# "wrong way" and other non-pandas way
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

from collections import defaultdict

def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts

counts = get_counts(time_zones)

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

top_counts(counts)

from collections import Counter
counts = Counter(time_zones)
counts.most_common(10)

# using pandas
import pandas as pd

frame = pd.DataFrame(records)

frame.info()

frame['tz'][:10]

tz_counts = frame.tz.value_counts()
tz_counts[:10]

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_]
