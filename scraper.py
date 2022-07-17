import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Richard_I_of_England"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


def get_citations_needed_count():
    number_citations_needed = 0
    citations = soup.find_all("a")
    for citation in citations:
        if citation.text == "citation needed":
            number_citations_needed += 1
    return number_citations_needed


def get_citations_needed_report():
    pass


if __name__ == '__main__':
    get_citations_needed_count()