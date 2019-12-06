import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.johnlewis.com/asus-chromebook-flip-c433ta-intel-core-m3-4gb-ram-64gb-emmc-14-inch-full-hd-silver/p4811855'
TAG_NAME = 'p'
QUERY = {'class': 'price price--large'}

response = requests.get(URL)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
element = soup.find(TAG_NAME, QUERY)
string_price = element.text.strip()

pattern = re.compile(r"(\d+,?\d*\.\d\d)")
match = pattern.search(string_price).group(1).replace(",","")
price = float(match)
print(price)
