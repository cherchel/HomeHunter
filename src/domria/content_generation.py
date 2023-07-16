import csv
import requests
import cloudscraper
from get_all_urls import get_urls_for_new_building
from lxml import html
from main import url_address
from field_names.new_building import field_names_for_new_building
from xpaths.new_building import xpaths_for_new_building


def param_list_for_new_building(url=None):
    # url = "/novostroyka-zhk-kyrylivskyi-gai-4597/"
    # url = '/uk/novostroyka-zhk-kontynental-6850/'
    my_dict = {}
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url_address + url)
    tree = html.fromstring(response.content)

    # remove blocks
    div_blocks = tree.xpath('//*[@id="content"]/div[2]/main/div')
    leader_blocks = tree.xpath('//*[@id="content"]/div[2]/main/div/div/div[2]')

    print(url)
    if len(div_blocks) > 0:
        print(len(div_blocks))
        for i in div_blocks:
            div_blocks = tree.xpath('//*[@id="content"]/div[2]/main/div')
            first_block_class = div_blocks[0].get('class')
            if first_block_class != "twoColumnOnDesktopContainer":
                parent = div_blocks[0].getparent()
                parent.remove(div_blocks[0])
            else:
                break

    if len(leader_blocks) > 0:
        leader_block_class = leader_blocks[0].get('class')
        if leader_block_class != "sc-u8nb37-0 ejozWL":
            parent = leader_blocks[0].getparent()
            parent.remove(leader_blocks[0])
    try:
        print(tree.xpath(xpaths_for_new_building[0])[0].text_content())
    except:
        pass

    skip_next = False
    for num, val in enumerate(field_names_for_new_building):
        try:
            if num > 18:
                html_text = tree.xpath(xpaths_for_new_building[-1])
            else:
                html_text = tree.xpath(xpaths_for_new_building[num])

            if num == len(field_names_for_new_building) - 1:
                for el in html_text[0]:
                    place_list = []
                    for places in el[0][0]:
                        place = [x.text_content() for x in places[0]]
                        place_list.append(f'{" ".join(place).strip()}')
                    my_dict[place_list[0]] = f'{" ".join(place_list[1:]).strip()}'

                my_dict[val] = url_address + url
                break

            if len(html_text):
                if num < 18:
                    text = html_text[0].text_content()
                    if num == 1 and text.lower().startswith("метро"):
                        skip_next = True
                        area = '//*[@class="leftContainer"]/div[3]/div[1]/a[3]'
                        new_text = tree.xpath(area)[0].text_content()
                        my_dict[val] = new_text
                    elif skip_next:
                        street = '//*[@class="leftContainer"]/div[3]/div[1]/a[4]'
                        new_text = tree.xpath(street)[0].text_content()
                        my_dict[val] = new_text
                    else:
                        my_dict[val] = text

                elif num == 18:
                    text = ""
                    for el in html_text[0]:
                        text += f"{el.text_content().replace('·', '').strip()} "
                    my_dict[val] = text

                elif num > 18:
                    my_dict[val] = ""

            else:
                my_dict[val] = "None"
        except:
            pass
    print(my_dict)
    return my_dict


# print(param_list())



def generate_file_for_new_building():
    urls_list = get_urls_for_new_building()
    print(urls_list)
    print(len(urls_list))
    with open("./new_building.csv", 'w', newline='', encoding='utf-8') as fh:
        writer = csv.DictWriter(fh, fieldnames=field_names_for_new_building)
        writer.writeheader()
        for url in urls_list:
            writer.writerow(param_list_for_new_building(url))

