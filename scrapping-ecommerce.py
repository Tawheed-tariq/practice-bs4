import urllib.request , urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
data = urllib.request.urlopen(url , context=ctx).read() # stores the data in unicode string
soup = BeautifulSoup(data, 'html.parser') # stores all the html data of the url

#get all the boxes containing product information
boxes = soup.find_all('div', class_ = 'card product-wrapper thumbnail')


# get prices of all the products
prices = soup.find_all('h4', class_ = 'float-end price card-title pull-right')
for price in prices:
    print(price.string)

# get names of all products 
names = soup.find_all('a', class_ = 'title')
for name in names:
    print(name.text)

# get description of each product
descriptions = soup.find_all('p', class_ = 'description card-text')
for description in descriptions:
    print(description.string)

