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

#create xpath selector string
mc_selector = '//*[@id="content"]/div/div[@class="byo-block -narrow wysiwyg-block wysiwyg "]/p'

#create a selector list of all paragraph elements within the main content blocks
mc_list = sel.xpath(mc_selector) 

# Print out the number of elements in the xpath selector
print( "There are {0} elements in the xpath selector.").format(len(mc_list))

#extract main content paragraph elements
mc_extracted = mc_list.extract()

#display main content paragraph elements
for content in mc_extracted:
    print(content)

#create a selector string of all paragraph text within the main context section
mt_selector = '//*[@id="content"]//p//text()'

#create a selector list of all main content paragraph text
mt_list = sel.xpath(mt_selector)

#extract main content paragraph text
mt_extracted = mt_list.extract()

#display main content paragraph text
for text in mt_extracted:
    print(text)

#create hyperlinks xpath string
hyperlinks = '//a/@href'

#extract all hyperlinks
links = sel.xpath(hyperlinks)

# Print out the number of hyperlinks
print( "There are {0} hyperlinks in the article in the xpath selector.").format(len(links))

#create css selector string for after content section text
ac_selector = '#afterContent p'

#create css selector list for after content section text
ac_list = sel.css(ac_selector)

# Print out the number of elements in the css selector
print( "There are {0} elements in the xpath selector.").format(len(ac_list))