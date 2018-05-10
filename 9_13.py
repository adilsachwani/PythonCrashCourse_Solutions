from collections import OrderedDict

cities = OrderedDict()

cities['pakistan'] = 'karachi'
cities['america'] = 'new york'
cities['india'] = 'mumbai'
cities['uae'] = 'dubai'

cities = {'pakistan':'karachi',
          'america':'new york',
          'india':'mumbai',
          'uae':'dubai'}

for country,city in cities.items():
    print(country.title() + "'s famous city is " + city.title() + "\n")