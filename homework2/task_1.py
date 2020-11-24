import requests
from bs4 import BeautifulSoup


SITE_URL = 'https://sinoptik.ua/'


def get_request(site_url, city, date=False):
    city = 'погода-' + city

    this_day = None
    if date:
        this_day = date.split('-')[-1]

    site_url = site_url + '/' + city
    if date:
        site_url = site_url + '/' + date

    page = requests.get(site_url)
    soup = BeautifulSoup(page.text, 'html.parser')

    if soup.find('div', class_='r404') is not None:
        print('wrong request')
    else:
        if not date:
            temp = soup.find('div', class_='temperature')

            temp_min = temp.find('div', class_='min')
            temp_max = temp.find('div', class_='max')

            return temp_min.text.split(' ')[-1], temp_max.text.split(' ')[-1]
        else:
            all_tabs = soup.find_all('div', 'main')

            for tab in all_tabs:
                if int(tab.find('p', class_='date').text) == int(this_day):
                    temp = tab.find('div', class_='temperature')

                    temp_min = temp.find('div', class_='min')
                    temp_max = temp.find('div', class_='max')

                    return temp_min.text.split(' ')[-1], temp_max.text.split(' ')[-1]


def get_default_request(site_url):
    page = requests.get(site_url)
    soup = BeautifulSoup(page.text, 'html.parser')

    if soup.find('div', class_='r404') is not None:
        print('wrong request')
    else:
        city = soup.find('div', class_='cityName')
        temp = soup.find('div', class_='temperature')

        temp_min = temp.find('div', class_='min')
        temp_max = temp.find('div', class_='max')

        print(city.text.strip() + ': ' + temp_min.text.split(' ')[-1] + ' ' + temp_max.text.split(' ')[-1])


get_default_request(SITE_URL)

while True:
    text = input('Enter city> ')

    if text == 'exit':
        break
    elif text != '':
        date = input('Enter date YYYY-MM-DD or press Enter> ')
        if date != '':
            res = get_request(SITE_URL, text, date)
            print(f'show city:{text} for date: {date}: {str(res[0])} {str(res[1])}')
        else:
            res = get_request(SITE_URL, text)
            print(f'show city:{text} for today: {str(res[0])} {str(res[1])}')
