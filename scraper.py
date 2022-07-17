import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(URL):
    """
    Arguments:
        URL: web address to scrape

    Returns:
        value: a count of all the citations needed on a web page.
    """
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    number_citations_needed = 0
    citations = soup.find_all("a")
    for citation in citations:
        if citation.text == "citation needed":
            number_citations_needed += 1
    return number_citations_needed


def get_citations_needed_report(URL):
    """
    Arguments:
        URL: web address to scrape.

    Returns:
        text: the text that requires a citation.
    """
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    citations = soup.find_all("p")
    for citation in citations:
        if "citation needed" in citation.text:
            text_of_citation = citation.text.split("citation needed")
            citation_text = text_of_citation[0] + "citation needed]"
            return citation_text
