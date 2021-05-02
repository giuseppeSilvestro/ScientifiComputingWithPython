import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Create a variable with the url of the website you want to scrap
url = 'http://www.dr-chuck.com/page1.htm'
# create a connection with the website using urllib package
html = urllib.request.urlopen(url).read()
# create an object using BeautifulSoup where to store the html in that page
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags in the html page
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
