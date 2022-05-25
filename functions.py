from bs4 import BeautifulSoup
import os
import re
import time
import requests
import inquirer
from theme.glitter import Glitter
from data import DOMAIN, HEADERS, GALLERY_LOCATION


def get_location(url):
    return url.replace(DOMAIN, '')


# request to selected domain, in this case glitter-graphics
def request(url):
    url = get_location(url)
    return requests.get(DOMAIN + url, headers=HEADERS)


# request to any domain, accepts full url
def request_other(url):
    return requests.get(url, headers=HEADERS, allow_redirects=True)


def get_soup(url):
    page = request(url)

    if page.status_code == 200:  # run scraper if page is online
        return BeautifulSoup(page.content, 'html.parser')


def download_image(url, name, ext, suffix, folder):
    while True:
        try:
            # Create folder if it doesn't exist already
            if not os.path.isdir(folder):
                os.mkdir(folder)
            res = request_other(url)

            open(os.path.join(folder, name + str(suffix) + ext), 'wb').write(res.content)
            break
        except ConnectionError:
            print('Connection error, please wait...')
            time.sleep(5)


# Select an option in the console and return it
def select_from_list(options):
    question = [
        inquirer.List(
            'category',
            message='Select category',
            choices=options,
            carousel=True
        ),
    ]

    return inquirer.prompt(question, theme=Glitter())


# Get url for the current gallery page
def gallery_url(gallery_id, number):
    return GALLERY_LOCATION + gallery_id + f'&page={number}'


# Get total number of pages. Don't change yet as we haven't started scraping.
def get_total_pages(gallery_id):
    page = get_soup(gallery_url(gallery_id, 1))
    pager = page.find('div', {'class': 'pager_widget'})
    time.sleep(5)
    last_page_number = pager.find_all('a', {'class': 'pager_button'})[-2].text

    return last_page_number


def last_slice(string, symbol):
    return string.split(symbol, -1)[-1]


def generate_file_name(string):
    return re.sub(r'[^a-zA-Z0-9]+', ' ', last_slice(string, '» ')).strip()


def get_ext(url):
    return '.' + url.split('.', -1)[-1]


def pad_line(string):
    return '{:#^50}'.format(' ' + string + ' ')
