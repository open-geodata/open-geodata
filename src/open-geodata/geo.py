#!/usr/bin/env python
# coding: utf-8

import os
import geopandas as gpd


try:
    print('Local!')
    gdf_sp = gpd.read_file(
        filename=os.path.join(os.path.dirname(__file__), 'data', 'sp_250k_wgs84.geojson'),
    )

except Exception as e:
    print('Exception')
    gdf_sp = gpd.read_file(
        filename='https://raw.githubusercontent.com/open-geodata/open-geodata/main/src/open-geodata/data/sp_250k_wgs84.geojson',
    )

print(gdf_sp)
