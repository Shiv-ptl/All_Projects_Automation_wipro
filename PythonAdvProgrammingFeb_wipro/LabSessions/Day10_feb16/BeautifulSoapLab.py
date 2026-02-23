#1) Parse HTML – Extract title and h1

from bs4 import BeautifulSoup

html = '''
<html>
<head><title>My Page</title></head>
<body>
<h1>Welcome</h1>
<p>This is a paragraph.</p>
</body>
</html>
'''


soup = BeautifulSoup(html, "html.parser")

title = soup.title.text
h1 = soup.find("h1").text

print("Title:", title)
print("H1:", h1)


# 2) Extract All Paragraphs
paragraphs = soup.find_all("p")

for p in paragraphs:
    print(p.text)

import requests



url= "http://books.toscrape.com/"
headers = {
    "User-Agent": "Chrome/120.0.0.0"
}

response = requests.get(url, headers= headers)
print(response.status_code)


soup = BeautifulSoup(response.text , features="html.parser")
# 3) Extract All Links and Count

links = soup.find_all("a")
print("\nTotal links:", len(links))

for link in links[:10]:
    print(link.get("href"))

# 4) Extract Attributes
first_link = soup.find("a")
print("\nAttributes of first link:", first_link.attrs)

# 5) Extract First h2
first_h2 = soup.find("h2")
if first_h2:
    print("\nFirst h2:", first_h2.text.strip())
# 6) Extract Bold Text
bolds = soup.find_all("b")
print("\nBold texts:")
for b in bolds:
    print(b.text)
# 7) Extract All href Values
hrefs = [a.get("href") for a in soup.find_all("a")]
print("\nFirst 10 href values:", hrefs[:10])
# 8) Get All Text Without Tags
print("\nPage text sample:")
print(soup.get_text()[:500])

# 9) Extract Title from Website
print("\nTitle:", soup.title.text)

# 10) Extract All Headings
print("\nAll Headings:")
for i in range(1, 7):
    for heading in soup.find_all(f"h{i}"):
        print(f"h{i}:", heading.text.strip())


# 11) Extract Table Data
tables = soup.find_all("table")

for table in tables:
    rows = table.find_all("tr")
    for row in rows:
        cols = row.find_all(["td", "th"])
        data = [col.text.strip() for col in cols]
        print(data)

# 12) Extract Images
images = soup.find_all("img")

print("\nImages:")
for img in images:
    print(img.get("src"))