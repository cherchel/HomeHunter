from domria.main import domria_new_generation

custom_cities = []

def get_result():
    pass

def make_new_file_for_one_city(build_type, custum_city):
    domria_new_generation(build_type, custum_city)


def regenerate_content(custom_cities):
    for custum_city in custom_cities:
        make_new_file_for_one_city("all", custum_city)


make_new_file_for_one_city('resale', 'Одеса')