import json

print("Extracting countries from admin0.geojson...")

fd = open('admin0.geojson')
json_data = json.load(fd, encoding="utf-8")
fd.close()

for feature in json_data["features"]:
  country_name = feature["properties"]["admin"]
  #print(country_name)

  country = { 'type': 'FeatureCollection', 'features': [feature]}

  fd = open('countries/' + country_name + '.geojson', 'w')
  json.dump(country, fd, encoding="utf-8", sort_keys=True)
  fd.close()
