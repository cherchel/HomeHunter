from lxml import html
import requests
import json
from main import city, url_address
import cloudscraper

current_id = 5


# get num of pages
def get_num_new_building():
    if city:
        scraper = cloudscraper.create_scraper()
        response = scraper.get(f"{url_address}/uk/novostroyki/{city}/?isChangeRadius=true")
        tree = html.fromstring(response.content)
        page_buttons = tree.xpath('//*[@id="pagination"]/div/div/div/a')
        if len(page_buttons) >= 1:
            xpath = f'//*[@id="pagination"]/div/div/div/a[{len(page_buttons)}]'  # last page button
            text = tree.xpath(xpath)
            return int(text[0].get('title'))
        else:
            return 1


def get_num_resale():
    if city:
        scraper = cloudscraper.create_scraper()
        geo = requests.get(f'{url_address}/node/api/getGeolocationByStateId?cityId={current_id}')
        geo_dict = json.loads(geo.text)["geolocation"]
        geo_x = geo_dict["geo_X"]
        geo_y = geo_dict["geo_Y"]
        print(geo_x, geo_y)
        link = f"https://dom.ria.com/uk/search/?noSoldOut=1&category=1&realty_type=2&operation=1&state_id=10&city_id=0&in_radius=0&with_newbuilds=0&price_cur=1&wo_dupl=1&complex_inspected=0&sort=inspected_sort&period=0&notFirstFloor=0&notLastFloor=0&with_map=0&photos_count_from=0&secondary=1&firstIteraction=false&fromAmp=0&limit=20&market=2&type=list&city_ids=10&client=searchV2&page=0&ch=242_239,247_252&map_state=30.522927_50.450274_0_14_0"
        response = scraper.get(link)
        response.encoding = 'utf-8'
        content = response.content.decode('utf-8')
        print(content)
        print(link)
        tree = html.fromstring(response.content)
        page_buttons = tree.xpath('//*[@id="domSearchPanel"]/div[4]/span/a')
        print(page_buttons)
        if len(page_buttons) >= 1:
            xpath = f'//*[@id="domSearchPanel"]/div[4]/span/a[{len(page_buttons)}]'  # last page button
            text = tree.xpath(xpath)
            return int(text[0].text_content())
        else:
            return 1


def main():
    print(get_num_resale())
    print("За допомогою функцій в цьому файлі ми отримуємо число сторінок оголошень")


if __name__ == "__main__":
    main()
