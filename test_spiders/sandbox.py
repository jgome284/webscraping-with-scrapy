# Import a scrapy Selector
import scrapy
from scrapy import Selector
from scrapy.html import Response
from scrapy.crawler import CrawlerProcess

# Import requests
import requests

class Spider(scrapy.Spider):
    name = 'ai-black-widow'

    def start_requests(self):
        urls = ['https://www.brookings.edu/articles/how-artificial-intelligence-is-transforming-the-world/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        links = response.xpath('//a/@href').extract()
        filepath = 'links.csv'
        with open(filepath, 'w') as f:
            f.writelines([link + '\n' for link in links])
        for link in links:
            yield reponse.follow(url=link, callback=self.parse2)
    
    def parse2(self, response):
        print('Hello World!')


# Create the Spider class
class DCspider( scrapy.Spider ):
  name = 'dcspider'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = url_short, callback = self.parse )
  # parse method
  def parse( self, response ):
    # Create an extracted list of course author names
    author_names = response.css('p.course-block__author-name::text').extract()
    # Here we will just return the list of Authors
    return author_names

# Import the scrapy library
import scrapy

# Create the Spider class
class DCdescr( scrapy.Spider ):
  name = 'dcdescr'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = url_short, callback = self.parse )
  
  # First parse method
  def parse( self, response ):
    links = response.css( 'div.course-block > a::attr(href)' ).extract()
    # Follow each of the extracted links
    for link in links:
      yield response.follow(url=link, callback=self.parse_descr)
      
  # Second parsing method
  def parse_descr( self, response ):
    # Extract course description
    course_descr = response.css( 'p.course__description::text' ).extract_first()
    # For now, just yield the course description
    yield course_descr

#start crawl!
process = CrawlerProcess()
process.crawl(Spider) 
process.start

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

# Create an XPath string to the desired text.
xpath = '//p[@id="content"]/text()'

# Create a CSS Locator string to the desired text.
css_locator = 'p#content::text'

# Create a CSS Locator string to the desired hyperlink elements
css_locator = 'a.course-block__link'

# Select the hyperlink elements from response and sel
response_as = response.css( css_locator)
sel_as = sel.css( css_locator )

# Examine similarity
nr = len( response_as )
ns = len( sel_as )
for i in range( min(nr, ns, 2) ):
  print( "Element %d from response: %s" % (i+1, response_as[i]) )
  print( "Element %d from sel: %s" % (i+1, sel_as[i]) )
  print( "" )