



def city_country(city, country, population=''):
    if population:
        citycountry = f'{city}, {country} - population {population}'
    else:
        citycountry = f'{city}, {country}'
    return citycountry.title()


# print(city_country('moscow', 'russia'))
# print(city_country('moscow', 'russia', 5000000))
