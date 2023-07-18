from new_building_content_generation import generate_file_for_new_building
from resale_content_generation import generate_file_for_resale

cities_dict = {'Київ': 'Kiev', 'Харків': 'Kharkov', 'Одеса': 'Odessa', 'Дніпро': 'Dnepr', 'Донецьк': 'Donetsk',
               'Запоріжжя': 'Zaporozhye', 'Львів': 'Lviv', 'Кривий Ріг': 'Krivoy Rog', 'Миколаїв': 'Nikolaev',
               'Маріуполь': 'Mariupol', 'Вінниця': 'Vinnitsa', 'Вараш': 'Varash', 'Херсон': 'Kherson',
               'Полтава': 'Poltava',
               'Чернігів': 'Chernigov', 'Черкаси': 'Cherkasy', 'Житомир': 'Zhitomir', 'Суми': 'Sumy',
               'Хмельницький': 'Khmelnitsky', 'Рівне': 'Rovno', 'Чернівці': 'Chernivtsi', 'Тернопіль': 'Ternopil',
               "Кам'янське": 'Kamenskoye', 'Івано-Франківськ': 'Ivano-Frankivsk', 'Кременчук': 'Kremenchug',
               'Луцьк': 'Lutsk', 'Мелітополь': 'Melitopol', 'Нікополь': 'Nikopol', 'Біла Церква': 'Bila Tserkva',
               'Краматорськ': 'Kramatorsk', 'Марганець': 'Marganets', 'Бердянськ': 'Berdyansk', 'Славутич': 'Slavutich',
               'Ужгород': 'Uzhgorod', 'Сєвєродонецьк': 'Severodonetsk', 'Алчевськ': 'Alchevsk',
               'Лисичанськ': 'Lisichansk', 'Павлоград': 'Pavlograd', 'Сімферополь': 'Simferopol',
               'Енергодар': 'Energodar', "Кам'янець-Подільський": 'Kamyanets-Podilskyi', 'Мукачево': 'Mukachevo',
               'Артемівськ': 'Artemovsk', 'Євпаторія': 'Yevpatoria', 'Ізмаїл': 'Izmail', 'Красний Луч': 'Krasny Luch',
               'Новомосковськ': 'Novomoskovsk', 'Дрогобич': 'Drogobych', 'Лозова': 'Lozova', 'Бердичів': 'Berdichev',
               'Стрий': 'Stryi', 'Лубни': 'Lubny', 'Сміла': 'Smela', 'Олександрія': 'Alexandria',
               'Кропивницький': 'Kropivnitsky', 'Шостка': 'Shostka', 'Бровари': 'Brovary',
               'Білгород-Дністровський': 'Belgorod-Dnistrovsky', 'Умань': 'Uman', 'Луганськ': 'Lugansk',
               'Нововолинськ': 'Novovolynsk', 'Макіївка': 'Makeyevka', 'Судак': 'Sudak', 'Світловодськ': 'Svetlovodsk',
               'Ірпінь': 'Irpen', 'Миргород': 'Mirgorod', 'Первомайськ': 'Pervomaysk', 'Токмак': 'Tokmak',
               'Бориспіль': 'Boryspol', "Кам'янка-Дніпровська": 'Kamianka-Dneprovskaya', 'Саки': 'Saki',
               'Вознесенськ': 'Voznesensk', 'Покровськ': 'Pokrovsk', 'Володимир-Волинський': 'Vladimir-Volynsk',
               'Алушта': 'Alushta', 'Новоград-Волинський': 'Novograd-Volynsky', 'Балта': 'Balta',
               'Борислав': 'Borislav', 'Васильків': 'Vasilkov', 'Горішні Плавні': 'Goryshne Plavni',
               'Глухів': 'Glukhov', 'Жовква': 'Zhovkva', "Знам'янка": 'Znamenka', 'Ізюм': 'Izyum', 'Ковель': 'Kovel',
               'Калуш': 'Kalush', 'Коростень': 'Korosten', 'Коломия': 'Kolomyia', 'Конотоп': 'Konotop',
               'Лебедин': 'Lebedin', 'Могилів-Подільський': 'Mogilev-Podolsky', 'Ніжин': 'Nizhyn',
               'Новояворівськ': 'Novoyavorovsk', 'Острог': 'Ostrog', 'Перемишляни': 'Peremyshlyany', 'Пологи': 'Polohy',
               'Ромни': 'Romny', 'Скадовськ': 'Skadovsk', 'Старокостянтинів': 'Starokonstantinov',
               'Трускавець': 'Truskavets', 'Хуст': 'Khust', 'Хорол': 'Khorol', 'Чортків': 'Chertkov',
               'Щастя': 'Schastie', 'Южноукраїнськ': 'Yuzhnoukrainsk', 'Ялта': 'Yalta'}


def user_request(custum_city):
    user_text = custum_city
    if user_text.lower() in [key.lower() for key in cities_dict.keys()]:
        return [user_text, cities_dict[user_text.capitalize()].lower()]
    else:
        print("Некоректне імя міста, імя міста повинно бути Українською")
        return False


def new_generation(build_type, custum_city):

    city = user_request(custum_city)
    if city:
        if build_type == "new":
            generate_file_for_new_building(city)
        elif build_type == "resale":
            generate_file_for_resale(city)
        elif build_type == "all":
            generate_file_for_new_building(city)
            generate_file_for_resale(city)
        else:
            print("incorrect type")


new_generation("resale", 'Одеса')
