#!/usr/bin/env python
# coding: utf-8


import os
import py7zr
import pandas as pd
import geopandas as gpd


def get_dataset_names():
    """

    """
    list_shp = []
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))
    for path, subdir, files in os.walk(root):
        for file in files:
            list_shp.append(file.split('.', maxsplit=1)[0])

    list_shp.sort()
    return list_shp


def load_dataset(name):
    """
    Funções para carregar dados geoespaciais

    :param name:
    :return:
    """
    # Checa se existe
    list_shp = get_dataset_names()
    if name not in list_shp:
        raise RuntimeError('"{}" not exists'.format(name))

    # Checa se existe mais de um
    if list_shp.count(name) > 1:
        raise RuntimeError('Exists "{}" datasets named "{}"'.format(list_shp.count(name), name))

    # Find file
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))
    for path, subdir, files in os.walk(root):
        for file in files:
            if file.split('.', maxsplit=1)[0] == name:
                select_file = os.path.join(path, file)

    # File
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
        return gpd.read_file(bio)

    # Se o arquivo é um
    if extension == 'geojson':
        return gpd.read_file(select_file)

    # Se o arquivo é um
    if extension == 'csv':
        return pd.read_csv(select_file)


if __name__ == '__main__':
    from open_geodata import geo
    from open_geodata.functions import share_boundary, find_neighbors

    # List Geodata
    list_shp = get_dataset_names()
    print(list_shp)

    # Read Geaodata
    gdf = load_dataset('sp_250k_wgs84')
    # gdf = load_dataset('divisa_municipal') # Localmente funciona
    # gdf = geo.load_dataset('divisa_abairramento')  # Pacote não funciona

    # Teste "find_neighbors" attribute table
    # gdf = find_neighbors(gdf, 'municipio_nome')

    # Teste "find_neighbors" spatial
    # gdf_interest = gdf.loc[gdf['id_municipio'] == 3548906]
    # gdf = share_boundary(gdf, gdf_interest)

    # Results
    # print(gdf.head())

    df = load_dataset('tab_municipio_ugrhi')
    print(df.head())
