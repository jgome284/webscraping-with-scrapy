# Import a scrapy Selector
from scrapy import Selector

# Import requests
import requests

#store url of site for scraping content
url = 'https://www.brookings.edu/articles/how-artificial-intelligence-is-transforming-the-world/'

# Create the string html containing the HTML source
html = requests.get( url ).content

# Create the Selector object sel from html
sel = Selector( text = html )

# Print out the number of elements in the HTML document
print( "There are {0} elements in the HTML document.").format(len(sel.xpath('//*')))

#create a selector list of all paragraph elements
psl = sel.xpath('//p') # select all paragraph elements

#extract paragraph element text
extracted = psl.extract()

#loop through paragraph text
for extract in extracted:
    print(extract)

#extract all hyperlinks
links = sel.xpath('//a/@href')

