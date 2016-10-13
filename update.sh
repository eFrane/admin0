#!/usr/bin/env sh
ne_countries="http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_countries.zip"

wget $ne_countries

unzip ne_10m_admin_0_countries.zip
ogr2ogr -f GeoJSON -t_srs crs:84 admin0.geojson ne*.shp
rm ne*

python countrysplit.py

rm admin0.geojson
