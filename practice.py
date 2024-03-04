countries={}
a=['Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa']
for i in a:
    print(i)
    country = i.split('/')[1]
    print(country)
    if country not in countries:
                countries[country] = []
    countries[country].append(i)

print(countries)
sorted_countries = sorted(countries.keys())
print(sorted_countries)