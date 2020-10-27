dict_of_country = {
    'Ukraine': 'Kiev',
    'Belarus': 'Minsk',
    'GB': 'London',
    'USA': 'Washington'
}

list_of_country = ['Poland', 'Ukraine', 'China', 'Turkey', 'GB', 'Kiev']

for country in list_of_country:
    if country in dict_of_country.keys():
        print(country + " - " + dict_of_country[country])