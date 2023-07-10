import parser
import json


# Функция для вызова парсера и обработки страницы с объявлениями недвижимости по указанному URL
def parse_estate_page(url):
    parser.parse_link_from_main_page_olx(url)

    with open("temp/all_links_ad_list.json", 'r') as file:
        all_links = json.load(file)

    ad_dict = parser.parse_link_from_ad_page_olx(all_links[0])

    print(ad_dict)


# Функция для сохранения полученных данных в CSV файл
def save_to_csv(data):
    pass


# Основной файл, который будет запускать парсер и управлять им.
# В нем реализована логику для передачи ссылок на страницы сайтов,
# обработка результатов парсинга и сохранение данных в CSV файл.
if __name__ == '__main__':
    us_url = "https://www.olx.ua/uk/nedvizhimost/kvartiry/prodazha-kvartir/?currency=UAH&search%5Bfilter_enum_property_type_appartments_sale%5D%5B0%5D=12&search%5Bfilter_enum_number_of_rooms_string%5D%5B0%5D=odnokomnatnye&search%5Bfilter_enum_apartments_object_type%5D%5B0%5D=primary_market&search%5Bfilter_enum_apartments_dev_type%5D%5B0%5D=elite"
    parse_estate_page(us_url)
