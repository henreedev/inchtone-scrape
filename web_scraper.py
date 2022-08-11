import requests
import bs4
import pandas as pd
import urllib
from requests_html import HTML
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)


def scrape_google(query):
    
    response = get_source("https://www.google.com/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links

def top_result(query):
    parsed_query = urllib.parse.quote_plus(query)
    results = scrape_google(parsed_query)
    return results[0]

def scrape_search_result(query):
    return scrape_email(top_result(query))

def scrape_email(link):
    response = get_source(link)
    email = response.html.find('a') # finds most stylistic Elements
    return email ## TODO make this return an 'a' tag with "href='mailto:" 

print(scrape_search_result("1218 UK Limited trading as 1218 Global")) # test

# currently getting inconsistent outputs

