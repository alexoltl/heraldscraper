import requests
from bs4 import BeautifulSoup
counter = 0
output_str = []

url = "https://www.nzherald.co.nz/nz/politics/audrey-young-chris-hipkins-three-cabinet-problems/3FHQGMI6TFFUVOA6KOEYFHMX3U/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

for p in soup.find_all("p"):
    if "article__heading-caption hero" not in p["class"]:
        if counter < 4:
            counter += 1
            continue
        output_str.append(p.get_text())

print(output_str)