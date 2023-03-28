from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def herald_url():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def herald_url_post():
    counter = 0
    output_str = ""

    text = request.form['text']

    response = requests.get(text)
    soup = BeautifulSoup(response.content, "html.parser")

    for p in soup.find_all("p"):
        if "article__heading-caption hero" not in p["class"]:
            if counter < 4:
                counter += 1
                continue
            output_str += p.get_text() + "<br/><br/>"
    
    return output_str

if __name__ == "__main__":
    app.run(debug=True)