import re

phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_regex.search('My number is 666-234-3456')
print('Phone number found: ' + mo.group())
