xpaths_for_new_building = [
    '//*[@class="leftContainer"]/div[3]/div[1]/a[1]',  # City
    '//*[@class="leftContainer"]/div[3]/div[1]/a[2]',  # Район
    '//*[@class="leftContainer"]/div[3]/div[1]/a[3]',  # Вулиця
    '//*[@class="leftContainer"]/div[3]/h1',  # Назва ЖК
    '//*[@temp_data-tm="buildClassName"]',  # Клас ЖК
    # Однокімнатні квартири
    '//*[contains(@class, "plansRow")][1]/td[2]/div/div',
    # Площа від
    '//*[contains(@class, "plansRow")][1]/td[3]/div',
    # Ціна за м2 в грн
    '//*[contains(@class, "plansRow")][1]/td[4]/div',
    # 'Ціна за м2 в дол'
    '//*[contains(@class, "plansRow")][1]/td[5]/div/div/div',
    # Двохкімнатні квартири
    '//*[contains(@class, "plansRow")][2]/td[2]/div/div',
    # Площа від
    '//*[contains(@class, "plansRow")][2]/td[3]/div',
    # 'Ціна за м2 в грн',
    '//*[contains(@class, "plansRow")][2]/td[4]/div',
    # Ціна за м2 в дол
    '//*[contains(@class, "plansRow")][2]/td[5]/div/div/div',
    # Трьохкімнатні квартири
    '//*[contains(@class, "plansRow")][3]/td[2]/div/div',
    # Площа від
    '//*[contains(@class, "plansRow")][3]/td[3]/div',
    # Ціна за м2 в грн
    '//*[contains(@class, "plansRow")][3]/td[4]/div',
    # Ціна за м2 в дол
    '//*[contains(@class, "plansRow")][3]/td[5]/div/div/div',
    # Рік побудування
    '//*[@temp_data-tm="commissioning_date_all_object"]',
    # Час до метро
    '//*[@temp_data-tm="map_block"]/div[1]/div[1]/table//tr',
    # Все
    '//*[@id="content"]/div[2]/main/div[3]/div'
]
