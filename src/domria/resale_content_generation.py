import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service  # options for run selenium locally
from webdriver_manager.chrome import ChromeDriverManager  # options for run selenium locally
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
import csv

from field_names.resale import field_names_for_resale

general_xpath = '//*[@id="domSearchPanel"]/div[1]/section'


def generate_file_for_resale(city):
    with open(f"../data/domria/{city}_resale.csv", 'w', newline='', encoding='utf-8') as fh:
        writer = csv.DictWriter(fh, fieldnames=field_names_for_resale)
        writer.writeheader()

        """options for run selenium locally """
        try:
            driver_service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=driver_service)
        except:
            driver = webdriver.Chrome()

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
        driver.find_element(By.CSS_SELECTOR, '#city > svg').click()
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

        wait = WebDriverWait(driver, 100)
        if len(list_pages) > 0:
            max_pages = int(list_pages[-1].text)
            print(max_pages)
            for i in range(max_pages):
                print('page:', i + 1)
                # Get all announcement on the page and add in list
                action(writer, driver, wait)

                try:
                    # We are trying to click the next page button, for this site, simply clicking this button does not work
                    element = driver.find_element(By.CLASS_NAME, 'text-r')
                    driver.execute_script("arguments[0].click();", element)
                    time.sleep(randint(6, 16))
                except:
                    # for last page
                    pass

        else:
            action(writer, driver, wait)


def action(writer, driver, wait):
    sections_list = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.realty-photo-rotate [href]')))
    for announcement in range(1, len(sections_list) + 1):
        announcement_dict = {}
        xpath = f'{general_xpath}[{announcement}]'
        # print(driver.find_element(By.XPATH, f"{xpath}/div[2]/h3/a").get_attribute(
        #     'href'))
        location = driver.find_elements(By.XPATH, f"{xpath}/div[2]/span")
        if len(location) == 1:
            try:
                announcement_dict['Місто'] = location[0].text.split(", ")[1]
                if location[0].text.split(",")[0] != location[0].text.split(", ")[1]:
                    announcement_dict['Район'] = location[0].text.split(",")[0]
                else:
                    announcement_dict['Район'] = "-"
            except:
                announcement_dict['Місто'] = location[0].text
                announcement_dict['Район'] = "-"

        elif len(location) == 2:
            try:
                announcement_dict['Місто'] = location[1].text.split(", ")[1]
                announcement_dict['ЖК'] = location[0].text
                if location[1].text.split(",")[0] != location[1].text.split(", ")[1]:
                    announcement_dict['Район'] = location[1].text.split(",")[0]
                else:
                    announcement_dict['Район'] = "-"
            except:
                announcement_dict['Місто'] = location[1].text
                announcement_dict['Район'] = "-"
                announcement_dict['ЖК'] = location[0].text

        try:
            announcement_dict['Вулиця'] = driver.find_element(By.XPATH, f"{xpath}/div[2]/h3/a").text
        except:
            announcement_dict['Вулиця'] = ""
        try:
            announcement_dict['Кількість кімнат'] = driver.find_element(By.XPATH,
                                                                        f"{xpath}/div[2]/div[2]/span[1]").text
        except:
            announcement_dict['Кількість кімнат'] = ""
        try:
            announcement_dict['Загальна площа'] = driver.find_element(By.XPATH,
                                                                      f"{xpath}/div[2]/div[2]/span[2]").text
        except:
            announcement_dict['Загальна площа'] = ""
        try:
            announcement_dict['Поверх'] = driver.find_element(By.XPATH, f"{xpath}/div[2]/div[2]/span[3]").text
        except:
            announcement_dict['Поверх'] = ""
        try:
            announcement_dict['Ціна за об\'єкт в дол'] = driver.find_element(By.XPATH,
                                                                             f"{xpath}/div[2]/div[1]/div/b").text
        except:
            announcement_dict['Ціна за об\'єкт в дол'] = ""
        try:
            announcement_dict['Ціна за м2 в дол'] = driver.find_element(By.XPATH,
                                                                        f"{xpath}/div[2]/div[1]/div/span").text
        except:
            announcement_dict['Ціна за м2 в дол'] = ""
        try:
            announcement_dict['URL'] = driver.find_element(By.XPATH, f"{xpath}/div[2]/h3/a").get_attribute(
                'href')
        except:
            announcement_dict['URL'] = ""

        writer.writerow(announcement_dict)
