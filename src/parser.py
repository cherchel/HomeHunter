from bs4 import BeautifulSoup
import requests
import fake_useragent


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


# Функция для извлечения данных объявлений из HTML-кода страницы
def parse_listing(html):
    pass


# Функция для извлечения конкретных деталей из объявления (название, цена, описание и т.д.)
def extract_details(listing):
    pass


if __name__ == '__main__':
    page_url = "https://www.olx.ua/uk/nedvizhimost/kvartiry/prodazha-kvartir/?currency=UAH&search%5Bfilter_enum_repair%5D%5B0%5D=1&search%5Bfilter_enum_furnish%5D%5B0%5D=yes&search%5Bfilter_enum_number_of_rooms_string%5D%5B0%5D=odnokomnatnye&search%5Bfilter_enum_apartments_object_type%5D%5B0%5D=primary_market&search%5Bfilter_enum_apartments_dev_type%5D%5B0%5D=elite"
    page_html = fetch_page(page_url)
    parse_listing(page_html)
