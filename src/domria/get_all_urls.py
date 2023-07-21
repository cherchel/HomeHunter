from lxml import html
import requests
from get_pages_val import get_num_new_building


def get_urls_for_new_building(city):
    url_list = []
    pages_val = get_num_new_building(city)
    print(pages_val)
    for page in range(1, pages_val + 1):
        print("Get urls from page:", page)
        if page == 1:
            response = requests.get(f"https://dom.ria.com/uk/novostroyki/{city[1]}/?isChangeRadius=true")
        else:
            response = requests.get(f"https://dom.ria.com/uk/novostroyki/{city[1]}/?isChangeRadius=true&page={page}")
        tree = html.fromstring(response.content)

        # Sometimes the page displays information as the first element, need delete this element for correct work
        div_blocks = tree.xpath('//*[@id="newbuilds"]/div')
        if len(div_blocks) > 0:
            first_block_class = div_blocks[0].get('class')
            for block in div_blocks[1:]:
                if block.get('class') != first_block_class:
                    parent = block.getparent()
                    parent.remove(block)

        for first_div in range(1, 7):
            try:
                if first_div < 5:
                    # print("first_div", first_div)
                    for second_div in range(1, 4):
                        # print("second_div", second_div)
                        text = tree.xpath(f'//*[@id="newbuilds"]/div[{first_div}]/div[{second_div}]/div[1]/a')
                        url_list.append(text[0].get('href'))

                else:
                    for second_div in range(1, 7):
                        text = tree.xpath(f'//*[@id="newbuilds"]/div[{first_div}]/div[{second_div}]/div[1]/a')
                        url_list.append(text[0].get('href'))
            except IndexError:
                print("page", page, "finish")
                break
    print("Urls:", len(url_list))
    return url_list


def main():
    print("За допомогою функцій в цьому файлі ми отримуємо список лінків оголошень")


if __name__ == "__main__":
    main()
