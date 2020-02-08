import flask
from bs4 import BeautifulSoup
import requests
from flask import jsonify
from SimpleWebCrawler import Company

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def createDict():
    url = "https://theinternship.io/"
    request = requests.get(url)
    data = request.text
    soup = BeautifulSoup(data, features="html.parser")
    logos = soup.find_all(class_=["center-logos", "list-company"])
    sortedCompany = []
    for i in range(0, len(logos), 2):
        sortedCompany.append(Company(logos[i]['src'], logos[i + 1].contents[0]))
    sortedCompany.sort(reverse=True)
    for companyLogo in sortedCompany:
        print(companyLogo.desc)

    companies = {'companies': []}
    for company in sortedCompany:
        lg = {'logo': company.url}
        companies['companies'].append(lg)

    return companies


@app.route('/', methods=['GET'])
def home():
    companies = createDict()
    return jsonify(companies)

app.run()
