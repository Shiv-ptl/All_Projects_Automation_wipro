# import  re
#
# print(re.search("^P", "Python"))
#
# print(re.findall("a.b", "acdb aab adb"))
#
# print(re.findall("[apc]", "apple"))
#
# print(re.findall(r"\d{2}(?=px)", "10px 20em 30px"))

import requests
from bs4 import BeautifulSoup

url = "https://www.myntra.com/men-tshirts"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

tshirts = soup.find_all("div", class_="product-productMetaInfo")

for tshirt in tshirts:
    # Brand
    brand = tshirt.find("h3", class_="product-brand")
    brand = brand.text.strip() if brand else "N/A"

    # Product Name
    info = tshirt.find("h4", class_="product-product")
    info = info.text.strip() if info else "N/A"

    # Price
    price_div = tshirt.find("div", class_="product-price")
    price = price_div.text.strip() if price_div else "N/A"

    print("Brand:", brand)
    print("Info:", info)
    print("Price:", price)
    print("-" * 40)


