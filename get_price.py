import re
import requests
from bs4 import BeautifulSoup

# We want to find the first price in the price ranges shown inside the text of the span we are extracting using the regex below
pattern = re.compile("^[$][\d]{1,}.\d{2}")
total=0

# List where we will store price ranges and extract regex later
product_prices = []

# viewall=True not showing all items so have to use each page which is annoying
url1 = "https://www.metallica.com/store/digital-downloads/"
url2 = "https://www.metallica.com/store/digital-downloads/?start=24&sz=24"

request1 = requests.get(url1)
request2 = requests.get(url2)

soup1 = BeautifulSoup(request1.content, "html.parser")
soup2 = BeautifulSoup(request2.content, "html.parser")

prices1 = soup1.find_all('div', class_="product-pricing")
prices2 = soup2.find_all('div', class_="product-pricing")


# find the text inside each span
for span in soup1.find_all("span", class_="product-sales-price"):
    text = span.find(text=True,recursive=False)
    product_prices.append(text)

for span in soup2.find_all("span", class_="product-sales-price"):
    text = span.find(text=True,recursive=False)
    product_prices.append(text)


# match with the regex and calcualte total
for price in product_prices:
    mp3_price = pattern.search(price).group()
    total+=float(mp3_price[1:])

# todo: convert it to the greatest currency in the world before printing (£)
total = round(total,2)
print(f"${total}")


