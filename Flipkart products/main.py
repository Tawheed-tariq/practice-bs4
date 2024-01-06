import requests
import pandas as pd
from bs4 import BeautifulSoup

product_names = []
product_prices = []
descriptions = []
product_reviews = []


for i in range(2,12):
    url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&param=1112&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlJlYWxtZSBzbWFydHBob25lcyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&wid=34.productCard.PMU_V2_28&page="+str(i)


    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    box = soup.find('div', class_ = '_1YokD2 _3Mn1Gg')

    
    names = box.find_all('div', class_ = "_4rR01T")
    prices = box.find_all('div' , class_ = '_30jeq3 _1_WHN1')
    descs = box.find_all('ul', class_ = '_1xgFaf')
    reviews = box.find_all('div', class_ = '_3LWZlK')


    for name in names:
        product_names.append(name.text)

    for price in prices:
        product_prices.append(price.text)

    for desc in descs:
        descriptions.append(desc.text)

    for review in reviews:
        product_reviews.append(review.text)


df = pd.DataFrame({"Product Name" : product_names, "Price" : product_prices, "Description" : descriptions, "Review" : product_reviews})
df.to_json('mobiles.csv')