import requests
from lxml import html

url = "https://news.ycombinator.com"
resp = requests.get(url)

data = html.fromstring(resp.content)

title = data.find(".//title").text
print(title)

#links
links = data.xpath("//a/@href")
print(links)

#links+ url

links = data.xpath("//a")

for link in links:
        print(link.text)
        print(link.get("href"))

print("using class--->")


#extract the data using class name
titlelines = data.find(".//span[@class = 'titleline']")

#print(titlelines)

for title in titlelines:
    print(title.text)