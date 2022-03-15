#!/usr/bin/env python
# coding: utf-8


# Funções para trabalhar com dados geoespaciais


def find_neighbors(gdf, column_name):
    """
    Encontre os vizinhos e insere coluna "neighbors" no geodataframe com seus nomes

    :param column_name: Título da Coluna que contém o nome do vizinho
    :param gdf: geodataframe de input
    :return: geodataframe com uma coluna "neighbors", com o nome dos vizinhos
    """
    gdf['neighbors'] = ''

    for index, row in gdf.iterrows():
        neighbors = gdf[gdf['geometry'].touches(row['geometry'])][column_name].tolist()
        gdf.at[index, 'neighbors'] = ', '.join(neighbors)
    return gdf


def share_boundary(gdf, gdf_interest):
    """
    Adaptação de https://stackoverflow.com/questions/66153429/selecting-polygons-which-shares-a-boundary-with-target-polygon-in-python-prefera
    :param gdf:
    :param gdf_interest:
    :return:
    """
    if len(gdf_interest['geometry']) == 1:
        gdf_interest = gdf_interest['geometry'].values[0]
    else:
        print('"gdf_interest" tem mais de um polígono')

    return gdf[gdf.geometry.apply(lambda x: x.touches(gdf_interest))]


if __name__ == '__main__':
    pass
