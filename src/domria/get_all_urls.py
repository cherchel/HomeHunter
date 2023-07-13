from lxml import html
import requests
from random import randint
import cloudscraper
from get_pages_val import get_num_new_building
from main import city
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service  # options for run selenium locally
from webdriver_manager.chrome import ChromeDriverManager  # options for run selenium locally
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_urls_for_new_building():
    url_list = []
    print(get_num_new_building())
    scraper = cloudscraper.create_scraper()
    for page in range(1, get_num_new_building() + 1):
        print("Get urls from page:", page)
        if page == 1:
            response = scraper.get(f"https://dom.ria.com/uk/novostroyki/{city[1]}/?isChangeRadius=true")
        else:
            response = scraper.get(f"https://dom.ria.com/uk/novostroyki/{city[1]}/?isChangeRadius=true&page={page}")
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


def get_urls_for_resale():
    """options for run selenium locally """
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.set_window_size(1920, 1080)
    # Going to url
    driver.get("https://dom.ria.com/uk/")
    time.sleep(1)
    # Click the drop-down list for the construction type.
    driver.find_element(By.XPATH, '//div[@id="app"]/div[2]/div/div/div[2]/div').click()
    time.sleep(1)
    # Choose "Вторинний ринок" construction type
    driver.find_element(By.XPATH, '//div[@class="scrollbar"]/div[2]').click()
    time.sleep(1)
    # Press "Шукати" button
    driver.find_element(By.XPATH, '//a[contains(text(),"Шукати")]').click()
    time.sleep(2)
    # Delete default city
    driver.find_element(By.CSS_SELECTOR, "#city path").click()
    time.sleep(1)
    # Click on the input
    driver.find_element(By.ID, "autocomplete").click()
    time.sleep(1)
    # Write our city
    driver.find_element(By.ID, "autocomplete").send_keys(f"{city[0].capitalize()}")
    time.sleep(1)
    # Press Enter
    driver.find_element(By.ID, "autocomplete").send_keys(Keys.ENTER)
    time.sleep(1)
    # Get all page change buttons
    list_pages = driver.find_elements(By.XPATH, '//span[@class="pagerMobileScroll"]/a')
    # If we have buttons, get the maximum value of the page and run a loop to get all the urls.

    all_urls = []
    wait = WebDriverWait(driver, 100)
    if len(list_pages) > 0:
        max_pages = int(list_pages[-1].text)
        print(max_pages)
        for i in range(max_pages):
            # Get all href
            sections_list = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.realty-photo-rotate [href]')))

            [all_urls.append(href.get_attribute('href').replace("https://dom.ria.com", "")) for href in
             sections_list]
            try:
                # We are trying to click the next page button, for this site, simply clicking this button does not work
                element = driver.find_element(By.CLASS_NAME, 'text-r')
                driver.execute_script("arguments[0].click();", element)
                time.sleep(randint(2, 5))
            except:
                # for last page
                pass
    else:
        sections_list = driver.find_elements(By.CSS_SELECTOR, '.realty-photo-rotate [href]')

        try:
            [all_urls.append(href.get_attribute('href').replace("https://dom.ria.com", "")) for href in
         sections_list]
        except:
            #we don't have urls
            pass

    return all_urls


def main():
    resale = get_urls_for_resale()
    print(resale)
    print(len(resale))
    print("За допомогою функцій в цьому файлі ми отримуємо список лінків оголошень")


if __name__ == "__main__":
    main()
