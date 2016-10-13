import json
from os import path, mkdir

print("Extracting countries from admin0.geojson...")

fd = open('admin0.geojson')
json_data = json.load(fd, encoding="utf-8")
fd.close()

countrymap = []

for feature in json_data["features"]:
    formal_en = feature["properties"]["FORMAL_EN"]
    iso_alpha = feature["properties"]["ISO_A2"] # ISO 3166-1 ALPHA 2 Country Code
    continent = feature["properties"]["CONTINENT"]

    info = { "name": formal_en }

    # fallback to administrative name if formal english is unavailable
    if formal_en == None:
        formal_en = feature["properties"]["ADMIN"]

    # fallback to full name (asciified)
    if iso_alpha == "-99":
        iso_alpha = feature["properties"]["ADMIN"].decode('utf-8').encode('ascii', 'ignore').lower().replace(' ', '-')
        info["disputed"] = True

    print("Processing " + formal_en + "...")

    feature["crs"] = { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" }}

    continent = continent.lower().replace(' ', '-').replace('(', '').replace(')', '')
    if not path.exists(continent):
        mkdir(continent)

    filename = continent + "/" + iso_alpha + ".geojson"
    info["filename"] = filename

    with open(filename, "w") as f:
        f.write("{}\n".format(json.dumps(feature, encoding="utf-8")))

    countrymap.append(info)

with open("countrymap.json", "w") as f:
    f.write("{}\n".format(json.dumps(countrymap, encoding="utf-8", indent=4)))
