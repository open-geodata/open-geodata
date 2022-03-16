#!/usr/bin/env python
# coding: utf-8

# Funções para carregar dados geoespaciais

import os
import geopandas as gpd
from open_geodata.functions import share_boundary, find_neighbors


def get_dataset_names():
    list_shp = []
    root = os.path.join(os.path.dirname(__file__), 'data', 'geo')
    for path, subdir, files in os.walk(root):
        for file in files:
            list_shp.append(file.split('.', maxsplit=1)[0])
    return list_shp


def load_dataset(name):
    # Checa se existe
    list_shp = get_dataset_names()
    if name not in list_shp:
        raise RuntimeError('"{}" not exists'.format(name))

    # Loop
    root = os.path.join(os.path.dirname(__file__), 'data', 'geo')
    for path, subdir, files in os.walk(root):
        for file in files:
            if file.split('.', maxsplit=1)[0] == name:
                select_file = os.path.join(path, file)

    # Geodataframe
    gdf = gpd.read_file(
        filename=os.path.join(root, select_file),
    )
    gdf.info()
    return gdf


if __name__ == '__main__':
    # dd
    list_shp = get_dataset_names()
    print(list_shp)

    # Lê dados
    gdf = load_dataset('sp_250k_wgs84')
    print(gdf.head())

    # Teste "find_neighbors" attribute table
    #gdf = find_neighbors(gdf, 'municipio_nome')
    #print(gdf.head())

    # Teste "find_neighbors" spatial
    #gdf_interest = gdf.loc[gdf['id_municipio'] == 3548906]
    #gdf = share_boundary(gdf, gdf_interest)
    #print(gdf.head())
