from  bs4 import BeautifulSoup
import requests


# Install and import BeautifulSoup from the bs4 module.
# Write a simple program to parse a small HTML string.
# Given this HTML:
html_doc = """<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
  </body></html>"""
# Extract the title text.
# Extract the <h1> text.
# Extract the paragraph text.

soup = BeautifulSoup(html_doc, features="html.parser")
print(soup)

# Extract the title text.
title = soup.find("title")
print(f"Title is : {title.text}")

# Extract the <h1> text.
h = soup.find("h1")
print(f"h1 is : {h.text}")

# Extract the paragraph text.
para = soup.find("p")
print(f"Paragraph  is : {para.text}")


# Write a program to:
# Find the first <a> tag.
# Print its href attribute.
# Use .prettify() to format parsed HTML.
url = "http://books.toscrape.com"
headers = {
    # user - agent - who is making the request and from where
    "User-Agent": "Mozilla/5.0"
}


response = requests.get(url, headers=headers)
print(response.status_code)
# parse the html
soup = BeautifulSoup(response.text, features="html.parser")


# html code is printed
print(soup.prettify())   # Use .prettify() to format parsed HTML.

first_anchorTag = soup.find("a")   # Find the first <a> tag.
print(first_anchorTag)

href_firstAnchortag = soup.find("a")["href"]
print(href_firstAnchortag)

# What is the difference between:
# find()   --returns the first matching HTML element as a Tag object    || Stops at the first match.
# find_all()  ---searches the entire document and returns a ResultSet   || Scans the entire document.




# 2.Scrape product details from an e-commerce sample page:
# Product name
# Price
# Rating
# Availability
# Extract all image URLs from a webpage.

url = "http://books.toscrape.com"
headers = {
    # user - agent - who is making the request and from where
    "User-Agent": "Mozilla/5.0"
}


response = requests.get(url, headers=headers)
print(response.status_code)
# parse the html
soup = BeautifulSoup(response.text, features="html.parser")


# html code is printed
print(soup.prettify())

books = soup.find_all("article", class_="product_pod")

# extract title and price in the books
for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text
    #rating =book.find("p")["class_"]     ---- XXXXXX   wrong
    # Rating (stored inside class name)
    rating = book.find("p", class_="star-rating")["class"][1]
    #avalability =
    #img_url = book.find("a")["href"]
    # Extract clickable book page URL
    relative_url = book.find("div", class_="image_container").find("a")["href"]
    full_url = url + relative_url.replace("../", "")
    print("Title:", title)
    print("Price", price)
    print("Rating : ",rating)
    print("Image url :",full_url)

# url = "https://www.myntra.com/men-tshirts"
# headers = {
#     # user - agent - who is making the request and from where
#     "User-Agent": "Mozilla/5.0"
# }
#
#
# response = requests.get(url, headers=headers)
# print(response.status_code)
# # parse the html
# soup = BeautifulSoup(response.text, features="html.parser")
#
#
# # html code is printed
# print(soup.prettify())
#
# tshirts = soup.find_all("div", class_="product-productMetaInfo")
#
# for tshhirt in tshirts:
#     brand = tshhirt.find("h3",class_ = "product-brand").text
#     info = tshhirt.find("h4", class_ = "product-product")
#     price = tshhirt.find("div", class_="product-price")("span")("span",class_ = "product-strike").text
#     print("Brand:", brand)
#     print("Info L ",info)
#     print("Price", price)
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.myntra.com/men-tshirts"
#
# headers = {
#     "User-Agent": "Mozilla/5.0"
# }
#
# response = requests.get(url, headers=headers)
# print("Status Code:", response.status_code)
#
# soup = BeautifulSoup(response.text, "html.parser")
#
# tshirts = soup.find_all("div", class_="product-productMetaInfo")
#
# for tshirt in tshirts:
#     # Brand
#     brand = tshirt.find("h3", class_="product-brand")
#     brand = brand.text.strip() if brand else "N/A"
#
#     # Product Name
#     info = tshirt.find("h4", class_="product-product")
#     info = info.text.strip() if info else "N/A"
#
#     # Price
#     price_div = tshirt.find("div", class_="product-price")
#     price = price_div.text.strip() if price_div else "N/A"
#
#     print("Brand:", brand)
#     print("Info:", info)
#     print("Price:", price)
#     print("-" * 40)

