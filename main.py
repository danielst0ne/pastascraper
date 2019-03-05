from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

url = "https://reddit.com/r/copypasta"
content = urlopen(url).read()
soup = BeautifulSoup(content,'html.parser')
print (soup)
