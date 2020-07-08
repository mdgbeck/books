import bs4, requests

example_file = open('12_example.html')
example_soup = bs4.BeautifulSoup(example_file, 'html.parser')

elems = example_soup.select('#author')

type(elems)
len(elems)

str(elems[0])

elems[0].getText()

elems[0].attrs

# alternate read in 
soup = bs4.BeautifulSoup(open('12_example.html'), 'html.parser')
span_elem = soup.select('span')[0]
str(span_elem)

span_elem.get('id')

span_elem.get('nonexistent_addr') == None

span_elem.attrs
