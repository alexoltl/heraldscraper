import requests
from bs4 import BeautifulSoup

counter = 0
output_str = ""

url = input("Link to article: ")

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

for p in soup.find_all("p"):
    if "article__heading-caption hero" not in p["class"]:
        if counter < 4:
            counter += 1
            continue
        output_str += p.get_text() + "\n\n"

print(output_str)