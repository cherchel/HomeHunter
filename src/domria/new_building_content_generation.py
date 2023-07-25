import csv
import requests
from get_all_urls import get_urls_for_new_building
from lxml import html
from field_names.new_building import field_names_for_new_building
from xpaths.new_building import xpaths_for_new_building


def param_list_for_new_building(url=None):
    url_address = "https://dom.ria.com"
    print(url_address + url)
    my_dict = {}
    response = requests.get(url_address + url)
    tree = html.fromstring(response.content)

    # remove blocks #####################################################################
    div_blocks = tree.xpath('//*[@id="content"]/div[2]/main/div')
    leader_blocks = tree.xpath('//*[@id="content"]/div[2]/main/div/div/div[2]')

    if len(div_blocks) > 0:
        print(len(div_blocks))
        for _ in div_blocks:
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
    #########################################################################################

    skip_next = False

    for num, val in enumerate(field_names_for_new_building):
        if num > 18:
            html_text = tree.xpath(xpaths_for_new_building[-1])
        else:
            html_text = tree.xpath(xpaths_for_new_building[num])

        # Use the xpath from the file, the first 18 xpaths are for the selected elements only.
        if num < 18:
            try:
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
            except:
                my_dict[val] = ""
        elif num == 18:
            text = ""
            try:
                for el in html_text[0]:
                    text += f"{el.text_content().replace('·', '').strip()} "
                my_dict[val] = text
            except:
                my_dict[val] = text
        # xpath for all elements after 18 is the same and they are dynamic, the first time i created only keys with empty val
        elif 18 < num < len(field_names_for_new_building) - 1:
            my_dict[val] = ""
        # These fields are dynamic, I use this condition to overwrite values
        elif num == len(field_names_for_new_building) - 1:
            print("my_dict -1", my_dict)
            print(xpaths_for_new_building[-1])
            for el in html_text[0]:
                print(el.text_content())
                place_list = []
                try:
                    # print(el[0][0])
                    for places in el[0][0]:
                        # print(places)
                        place = [x.text_content() for x in places[0]]
                        place_list.append(f'{" ".join(place).strip()}')
                    print(place_list)

                    my_dict[place_list[0].strip()] = f'{" ".join(place_list[1:]).strip()}'
                except:
                    pass
            my_dict[val] = url_address + url

    return my_dict


def generate_file_for_new_building(city):
    urls_list = get_urls_for_new_building(city)
    print(urls_list)
    print(len(urls_list))
    with open(f"../data/domria/{city}_new_building.csv", 'w', newline='', encoding='utf-8') as fh:
        writer = csv.DictWriter(fh, fieldnames=field_names_for_new_building)
        writer.writeheader()
        for url in urls_list:
            writer.writerow(param_list_for_new_building(url))
