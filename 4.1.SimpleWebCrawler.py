from bs4 import BeautifulSoup
import requests

class Company:
    def __init__(self,url: str ,desc : str):
        self.url = url
        self.desc = desc

    def __lt__(self, other):
        return len(self.desc) < len(other.desc)
    def __gt__(self, other):
        return len(self.desc) > len(other.desc)
    def __le__(self, other):
        return len(self.desc) <= len(other.desc)
    def __ge__(self, other):
        return len(self.desc) >= len(other.desc)
    def __eq__(self, other):
        return len(self.desc) == len(other.desc)
    def __ne__(self, other):
        return len(self.desc) != len(other.des)

if __name__ == "__main__":
    url = "https://theinternship.io/"
    request = requests.get(url)
    data = request.text
    soup = BeautifulSoup(data, features="html.parser")
    logos = soup.find_all(class_=["center-logos", "list-company"])
    sortedCompany = []
    for i in range(0, len(logos), 2):
        sortedCompany.append(Company(logos[i]['src'],logos[i+1].contents[0]))
    sortedCompany.sort(reverse=True)
    for companyLogo in sortedCompany:
        print(companyLogo.url)
