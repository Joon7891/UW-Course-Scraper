from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Function to attempt to get the 'url' content via HTTP GET request.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if good_response(resp):
                return resp.content
            else:
                return None
    
    except RequestException as e:
        return None

def good_response(response):
    """
    Returns True if the response is HTML.
    """
    resp_type = response.headers['Content-Type'].lower()
    return response.status_code == 200 and \
        resp_type is not None and resp_type.find('html') > -1