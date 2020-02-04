import flask
from bs4 import BeautifulSoup
import requests
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def createDict():
    url = "https://theinternship.io/"
    request = requests.get(url)
    data = request.text
    soup = BeautifulSoup(data, features="html.parser")
    logos = soup.find_all("img", class_="center-logos")
    companies = {'companies': []}
    for logo in logos:
        lg = {'logo': logo['src']}
        companies['companies'].append(lg)
    return companies


@app.route('/', methods=['GET'])
def home():
    companies = createDict()
    return jsonify(companies)

app.run()
