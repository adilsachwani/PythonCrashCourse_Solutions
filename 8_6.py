def  city_country(city, country):
    cityCountry = city.title() + ", " +country.title()
    return cityCountry

print(city_country("karachi","pakistan"))
print(city_country("new york","america"))
print(city_country("chennai","india"))