from lxml import html
import requests


# get num of pages
def get_num_new_building(city):
    url_address = "https://dom.ria.com"
    if city:
        response = requests.get(f"{url_address}/uk/novostroyki/{city[1]}/?isChangeRadius=true")
        tree = html.fromstring(response.content)
        page_buttons = tree.xpath('//*[@id="pagination"]/div/div/div/a')
        if len(page_buttons) >= 1:
            xpath = f'//*[@id="pagination"]/div/div/div/a[{len(page_buttons)}]'  # last page button
            text = tree.xpath(xpath)
            return int(text[0].get('title'))
        else:
            return 1


def main():
    print("За допомогою функцій в цьому файлі ми отримуємо число сторінок оголошень")


if __name__ == "__main__":
    main()
