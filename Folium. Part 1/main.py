import folium
from countries import population, coordinates

map = folium.Map(location=[46, 15], zoom_start=5)

def transform(a: str):
    first_letter = a[0]
    body = a[1:]
    body = body.lower()
    return "{0}{1}".format(first_letter, body)

population = {a: b for a, b in population}
coordinates = {transform(a): [b[0], c[0]] for a, b, c in coordinates}

keys = set(population.keys()) & set(coordinates.keys())

population = {a: b for a, b in population.items() if a in keys}
coordinates = {transform(a): b for a, b in coordinates.items() if a in keys}

for country in keys:
    marker = folium.Marker(location=coordinates[country], 
                                            popup="{0} {1:.3f}m".format(country, population[country] / 10**6), 
                                            icon=folium.Icon(color='red'))
                                            
    marker.add_to(map)                                        

map.save('C:\\map.html')
