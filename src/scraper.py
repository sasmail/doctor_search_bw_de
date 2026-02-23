import requests
import re

# TODO: write unit tests

def clean_url(url):
    cleaned_url = re.sub(r"[&?]offset=\d+", "", url, count=1)
    return cleaned_url


def fetch_page(cleaned_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    try:
        response = requests.get(cleaned_url, headers=headers)
        if response.status_code != 200:
            print(f"Error: got status code {response.status_code}")
            return None
        page_response = response.text
        return page_response
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def build_url_with_offset(cleaned_url, offset):
    url_with_offset = cleaned_url + f"&offset={offset}"
    return url_with_offset
