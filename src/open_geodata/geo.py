#!/usr/bin/env python
# coding: utf-8

# Funções para carregar dados geoespaciais

import os
import geopandas as gpd
from open_geodata.functions import share_boundary


def get_dataset_names():
    return os.listdir(os.path.join(os.path.dirname(__file__), 'data'))


def load_dataset(name):
    gdf = gpd.read_file(
        filename=os.path.join(os.path.dirname(__file__), 'data', name),
    )
    gdf.info()
    return gdf


if __name__ == '__main__':
    # Lê dados
    gdf = load_dataset('sp_250k_wgs84.geojson')
    print(gdf.head())

    # Teste "find_neighbors" attribute table
    # gdf = find_neighbors(gdf, 'municipio_nome')
    print(gdf.head())

    # Teste "find_neighbors" spatial
    gdf_interest = gdf.loc[gdf['id_municipio'] == 3548906]
    gdf = share_boundary(gdf, gdf_interest)
    print(gdf.head())
