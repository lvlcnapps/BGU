import json

with open('cities.txt', 'r') as f, open('filtered_cities.txt', 'w') as f2:
    cities = json.loads(f.read())
    print(cities)
    min_pop = int(input('Enter minimum population: '))
    print('Cities with population greater than', min_pop)
    sorted_cities = {}
    for city, population in cities.items():
        if population >= min_pop:
            sorted_cities[city] = population
    print(sorted_cities)
    json.dump(sorted_cities, f2)
