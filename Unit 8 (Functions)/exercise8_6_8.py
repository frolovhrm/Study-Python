"""Упражнение 8.6"""

# def city_country(city, country):
#     city_countries = f'"{city}, {country}"'
#     print(city_countries.title())
#
#
# city_country('Moscow', 'RUSSIA')
#
# city_country('Tokio', 'japan')
#
# city_country('paris', 'france')

"""Упражненеие 8.7"""

# def make_album(singer_name, album_name, num = None):
#     album = {singer_name: album_name}
#     if num:
#         album['num'] = num
#     print(album)
#
# make_album('111', 'aaa')
#
# make_album('222', 'bbb', '9')
#
# make_album('333', 'ccc')

"""Упражненеие 8.8"""


def make_album(singer_name, album_name, num=None):
    album = {singer_name: album_name}
    if num:
        album['num'] = num
    return album


while True:
    print('If you inter "q", the programme make quite')
    sn = input('Input singer name: ')
    if sn == 'q': break
    an = input('input album name')
    if an == 'q': break
    print(make_album(sn, an))
