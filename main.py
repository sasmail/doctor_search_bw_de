from src import parser as par
from src import scraper as scr
from src import results as res
from src import exporter as exp

import time

# TODO: restructure properly
# MAIN PART
# 1. get URL

def prepare_data_for_export():

    # 1. get URL from user
    url = input("Enter the url to scrape: ")

    # 2. get path from user of where to store files
    user_path = input("Enter the path to save to: ")

    # 3. clean URL
    cleaned_url = scr.clean_url(url)

    # 4. save response
    page_response = scr.fetch_page(cleaned_url)

    # 5. parse results
    parse_result = par.parse_page(page_response)

    # 6. get total amount of docs
    total_amount_docs = par.get_total_number_of_docs(parse_result)

    # 7. check how many sub_pages
    number_of_sub_pages = par.get_number_of_pages(total_amount_docs)

    # 8. save row of each doctor
    rows_from_result = res.get_rows(parse_result)

    # 8. doc dict
    all_doctors = res.build_doc_dict(rows_from_result)

    for page in range(1, number_of_sub_pages):
        # 1. giving script some time to breathe
        time.sleep(2)

        # 2. calculate offset
        offset = page * 20
        print(f"Processing page: {page}")

        # 3. generate cleaned_url with offset
        url_with_offset = scr.build_url_with_offset(cleaned_url, offset)

        # 4. save response
        page_response = scr.fetch_page(url_with_offset)

        # 5. parse results
        parse_result = par.parse_page(page_response)

        # 6. prepare rows for building doc_dict
        rows_from_result = res.get_rows(parse_result)

        # 7. get docs of current page
        new_doctors = res.build_doc_dict(rows_from_result)

        # 8. add new_doctors to all_doctors
        all_doctors.extend(new_doctors)
        print(f"Processed page: {page}")


    exp.export_data(all_doctors, user_path)




if __name__ == '__main__':
    all_doctors = prepare_data_for_export()