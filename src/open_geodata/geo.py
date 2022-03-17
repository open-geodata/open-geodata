#!/usr/bin/env python
# coding: utf-8

# Funções para carregar dados geoespaciais

import os
import py7zr
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

    # Checa se existe mais de um
    if list_shp.count(name) > 1:
        raise RuntimeError('Exists "{}" datasets "{}"'.format(list_shp.count(name), name))

    # Find file
    root = os.path.join(os.path.dirname(__file__), 'data', 'geo')
    for path, subdir, files in os.walk(root):
        for file in files:
            if file.split('.', maxsplit=1)[0] == name:
                select_file = os.path.join(path, file)

    # ff
    filename = os.path.basename(select_file)
    extension = os.path.splitext(filename)[1][1:]

    # Load por tipo de arquivo
    if extension == '7z':
        # Geodataframe
        with py7zr.SevenZipFile(select_file, 'r') as archive:
            allfiles = archive.getnames()

            # Quero apenas um arquivo por gpkg
            if len(allfiles) == 1:
                for filename, bio in archive.read(allfiles).items():
                    pass
            else:
                raise RuntimeError('.zip tem mais de um gpkg')
        gdf = gpd.read_file(bio)

    if extension == 'geojson':
        gdf = gpd.read_file(os.path.join(select_file))

    gdf.info()
    return gdf


if __name__ == '__main__':
    # dd
    #list_shp = get_dataset_names()
    #print(list_shp)

    # Lê dados
    #gdf = load_dataset('sp_250k_wgs84')
    gdf = load_dataset('divisa_municipal')
    print(gdf.head())

    # Teste "find_neighbors" attribute table
    #gdf = find_neighbors(gdf, 'municipio_nome')
    #print(gdf.head())

    # Teste "find_neighbors" spatial
    #gdf_interest = gdf.loc[gdf['id_municipio'] == 3548906]
    #gdf = share_boundary(gdf, gdf_interest)
    #print(gdf.head())
