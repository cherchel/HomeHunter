import time

import requests
# content = requests.get("https://dom.ria.com/uk/search/?noSoldOut=1&category=1&realty_type=2&operation=1&state_id=10&city_id=0&in_radius=0&with_newbuilds=0&price_cur=1&wo_dupl=1&complex_inspected=0&sort=inspected_sort&period=0&notFirstFloor=0&notLastFloor=0&with_map=0&photos_count_from=0&secondary=1&firstIteraction=false&fromAmp=0&limit=20&market=2&type=list&city_ids=10&client=searchV2&page=0&ch=242_239,247_252&map_state=30.522927_50.450274_0_14_0")
#
# print(content.text)


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service  # options for run selenium locally
from webdriver_manager.chrome import ChromeDriverManager  # options for run selenium locally
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

city = 'Вишгород'


def driver() -> webdriver:
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
    driver.find_element(By.ID, "autocomplete").send_keys(f"{city}")
    time.sleep(1)
    # Press Enter
    driver.find_element(By.ID, "autocomplete").send_keys(Keys.ENTER)
    time.sleep(1)
    # Get all page change buttons
    list_pages = driver.find_elements(By.XPATH, '//span[@class="pagerMobileScroll"]/a')
    # If we have buttons, get the maximum value of the page and run a loop to get all the urls.

    all_urls = []
    if len(list_pages) > 0:
        max_pages = int(list_pages[-1].text)

        for i in range(max_pages):
            # Get all href
            sections_list = driver.find_elements(By.CSS_SELECTOR, '.realty-photo-rotate [href]')
            [all_urls.append(href.get_attribute('href').replace("https://dom.ria.com", "")) for href in
             sections_list]
            print(all_urls)
            print(len(all_urls))
            try:
                # We are trying to click the next page button, for this site, simply clicking this button does not work
                element = driver.find_element(By.CLASS_NAME, 'text-r')
                driver.execute_script("arguments[0].click();", element)
                time.sleep(2)
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
    print(len(set(all_urls)))
    time.sleep(30)

    return all_urls




driver()
