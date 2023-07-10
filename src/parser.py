from bs4 import BeautifulSoup
import requests
import fake_useragent
import json


# Функция для отправки HTTP-запроса к указанному URL и получения HTML-страницы
def fetch_page(url):
    user = fake_useragent.UserAgent().random
    header = {'User-Agent': user}
    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()  # Проверяем статус ответа
        response.encoding = response.apparent_encoding  # Устанавливаем правильную кодировку для текста страницы
        return response.text

    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при получении страницы: {e}")
        return None


def parse_link_from_main_page_olx(path):
    with open(path, 'r', encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    all_links_ad = soup.find_all(class_="css-rc5s2u")

    all_links_ad_list = []
    for item in all_links_ad:
        link_ad = "https://www.olx.ua" + item.get('href')
        all_links_ad_list.append(link_ad)

    with open("all_links_ad_list.json", "w") as file:
        json.dump(all_links_ad_list, file, indent=4, ensure_ascii=False)


# Функция для извлечения данных объявлений из HTML-кода страницы
def parse_listing(html):
    pass


# Функция для извлечения конкретных деталей из объявления (название, цена, описание и т.д.)
def extract_details(listing):
    pass


if __name__ == '__main__':
    pass
