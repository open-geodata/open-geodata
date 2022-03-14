#!/usr/bin/env python
# coding: utf-8

import os
import geopandas as gpd

sp_250k = gpd.read_file(
    filename=os.path.join(os.path.dirname(__file__), 'data', 'sp_250k_wgs84.geojson'),
)




if __name__ == '__main__':
    print('sss')

