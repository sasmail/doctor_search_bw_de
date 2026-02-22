import re
from bs4 import BeautifulSoup
import math

# TODO: write unit tests

AMOUNT_DOCS_PER_PAGE = 20

def parse_page(page_response):
    parse_result = BeautifulSoup(page_response, 'html.parser')

    return parse_result

def get_total_number_of_docs(parse_result):
    amount_results = parse_result.find('div', class_='anzahl_treffer').get_text()
    total_amount_docs_list = re.findall(r"von (\d+) Treffern", amount_results)
    total_amount_docs = int(total_amount_docs_list[0])

    return total_amount_docs

def get_number_of_pages(total_amount_docs):
    total_amount_pages = math.ceil(total_amount_docs / AMOUNT_DOCS_PER_PAGE)

    return total_amount_pages