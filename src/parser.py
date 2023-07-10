from bs4 import BeautifulSoup
import requests
import json


# Функция для отправки HTTP-запроса к указанному URL и получения HTML-страницы
def fetch_page(url):
    user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 " \
           "Safari/537.36"
    header = {'User-Agent': user}

    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()  # Проверяем статус ответа
        response.encoding = response.apparent_encoding  # Устанавливаем правильную кодировку для текста страницы
        return response.text

    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при получении страницы: {e}")
        return None


# Функция для извлечения ссылок на объявления из страницы выборки olx
def parse_link_from_main_page_olx(url):
    with open("temp/olx.html", 'w', encoding='utf-8') as file:
        file.write(fetch_page(url))

    with open('temp/olx.html', 'r', encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    all_links_ad = soup.find_all(class_="css-rc5s2u")

    all_links_ad_list = []
    for item in all_links_ad:
        link_ad = "https://www.olx.ua" + item.get('href')
        all_links_ad_list.append(link_ad)

    with open("temp/all_links_ad_list.json", "w") as file:
        json.dump(all_links_ad_list, file, indent=4, ensure_ascii=False)


# Функция для извлечения данных объявлений из HTML-кода страницы
def parse_link_from_ad_page_olx(url):
    with open("temp/olx_ad.html", 'w', encoding='utf-8') as file:
        file.write(fetch_page(url))

    with open("temp/olx_ad.html", 'r', encoding='utf-8') as file:
        src = file.read()

    ad_dict = {
        'cost': '',
        'cost_by_square': '',
        'address': '',
        'district': '',
        'microdostrict': '',
        'zk': '',
        'city': '',
        'subway': '',
        'discripion': '',
        'floor': '',
        'number_rooms': '',
        'square_meters': '',
        'publication_date': '',
        'contacts': '',
        'link': '',
    }

    soup = BeautifulSoup(src, 'lxml')
    ad_dict['cost'] = soup.find(class_="css-ddweki er34gjf0").text

    return ad_dict


# Функция для извлечения конкретных деталей из объявления (название, цена, описание и т.д.)
def extract_details(listing):
    pass


if __name__ == '__main__':
    pass
