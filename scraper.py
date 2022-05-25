import sys
import time
import re
from categories import category_id
from functions import *
from data import *


def scrape_by_category():

    download_count = 0
    page_number = 1  # change to start from a different page :)

    options = list(category_id.keys())
    selected_category = select_from_list(options)['category']
    gallery_id = str(category_id[selected_category])

    total_pages = int(get_total_pages(gallery_id))

    while page_number <= total_pages:
        print('\n')
        print(f'Page {page_number} out of {total_pages}')

        url = gallery_url(gallery_id, page_number)
        gallery = get_soup(url)
        container = gallery.find('div', {'class': 'flex_centered_container'})
        links = container.find_all('a', attrs={'href': re.compile('/graphics/')})

        for link in links:
            location = link.get('href')
            image_page = get_soup(location)
            title = image_page.find('div', {'class': 'graphic_details_widget'}).find('h1').text
            name = generate_file_name(title)

            try:
                image_src = image_page.find('img', {'class': 'graphic_image'})['src']
                ext = get_ext(image_src)
                suffix = download_count
                download_image(image_src, name=name, ext=ext, suffix=suffix, folder=selected_category)

                download_count += 1

                print_count = str(download_count).rjust(5, '0')
                print(f'{print_count}. Successfully downloaded "{name}{suffix}{ext}"')
                time.sleep(5)
            except TypeError:
                print('Image not found.')
                time.sleep(5)
                continue

        page_number += 1


print('\n' + pad_line(WELCOME_MSG))
command = input(pad_line("To run type '-y' or to quit type '-n'") + '\n')

if command == '-y':
    print('\n')
    scrape_by_category()
if command == '-n':
    sys.exit()
