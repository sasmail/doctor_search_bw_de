from src import parser as par
from src import scraper as scr
from src import results as res
from src.results import build_doc_dict

# TODO: restructure properly
# MAIN PART
# 1. get URL
url = input("Enter the url to scrape: ")

# 2. clean URL
cleaned_url = scr.clean_url(url)

# 3. save response
page_response = scr.fetch_page(cleaned_url)

# 4. parse results
parse_result = par.parse_page(page_response)

# 5. get total amount of docs
total_amount_docs = par.get_total_number_of_docs(parse_result)

# 6. check how many sub_pages
number_of_sub_pages = par.get_number_of_pages(total_amount_docs)

# 7.
rows_from_result = res.get_rows(parse_result)

# 8. doc dict
doctors_info = build_doc_dict(rows_from_result)