#!/usr/bin/env python
# coding: utf-8

import geopandas as gpd
from shapely.geometry import Point


def dms2dd(coord):
    """
    Convert geographic coordinates in
    format degrees, minutes and seconds (23°06’12,48”S)
    in decimal degrees (e.g. -23.10346666666667)

    Estilo Informações Técnicas CETESB

    :param coord: string 23°06’12,48”S
    :return: float -23.10346666666667
    """
    # Splitar coordenada
    graus = float(coord.split('°')[0])
    minutos = float((coord.split('°')[1]).split('’')[0])
    segundos = float((((coord.split('°')[1]).split('’')[1]).split('”')[0]).replace(',', '.'))
    direction = (((coord.split('°')[1]).split('’')[1]).split('”')[1])

    # Calcular
    coord_dm = graus + (minutos / 60) + (segundos / 3600)

    # Converter parâmetro textual
    if direction in ('S', 's', 'O', 'o'):
        return coord_dm * -1
    else:
        return coord_dm


def dms2dd_infoaguas(coord_dms):
    """

    Para usar em uma coluna
    df.loc[:, 'latitude_dd'] = df['latitude_dms'].astype(str).apply(lambda x: dms2dd(x))

    :param coord_dms:
    :return:
    """
    coord_dms = coord_dms.strip()
    try:
        coord_deg = float(coord_dms.split(' ', maxsplit=2)[0])
        coord_min = float(coord_dms.split(' ', maxsplit=2)[1])
        coord_sec = float(coord_dms.split(' ', maxsplit=2)[2])
        coord_dd = coord_deg + (coord_min / 60) + (coord_sec / 3600)
        coord_dd = coord_dd * -1
    except:
        coord_dd = 0
    return coord_dd


def df2geojson(df, lat='latitude', long='longitude', remove_coords_properties=True):
    """
    Convert um dataframe, com colunas de latitude e longitude, em um objeto geojson de pontos
    https://notebook.community/gnestor/jupyter-renderers/notebooks/nteract/pandas-to-geojson

    # Usage
    feature_collection = dataframe2geojson(df, lat='latitude_dd', long='longitude_dd', remove_coords_properties=False)

    with open('file.geojson', 'w', encoding='utf-8') as f:
        json.dump(feature_collection, f, ensure_ascii=False)


    :param df:
    :param lat: Nome da coluna no dataframe que tem os dados de latitude
    :param long: Nome da coluna no dataframe que tem os dados de longitude
    :param remove_coords_properties:
    :return:
    """

    # Create a new python dict to contain our geojson data, using geojson format
    geojson = {'type': 'FeatureCollection', 'features': []}

    # Loop through each row in the dataframe and convert each row to geojson format
    for _, row in df.iterrows():
        # Create a feature template to fill in
        feature = {
            'type': 'Feature',
            'properties': {},
            'geometry': {
                'type': 'Point',
                'coordinates': [],
            }
        }

        # Fill in the coordinates
        feature['geometry']['coordinates'] = [row[long], row[lat]]

        # for each column, get the value and add it as a new feature property
        properties = list(df.columns)
        if remove_coords_properties:
            properties.remove(lat)
            properties.remove(long)

        for prop in properties:
            feature['properties'][prop] = row[prop]

        # Add this feature (aka, converted dataframe row) to the list of features inside our dict
        geojson['features'].append(feature)

    return geojson


def df2geojson2(df, lat='latitude', long='longitude', epsg=4326):
    """

    :param epsg:
    :param df:
    :param lat:
    :param long:
    :param remove_coords_properties:
    :return:
    """
    # Create Geometry
    geometry = [Point(xy) for xy in zip(df[long], df[lat])]

    # Create Geodataframe
    gdf = gpd.GeoDataFrame(
        df,
        crs='EPSG:{}'.format(epsg),
        geometry=geometry
    )
    gdf.drop([lat, long], axis=1, inplace=True, errors='ignore')
    return gdf


if __name__ == '__main__':
    print(dms2dd('23°06’12,48”S'))
    print(dms2dd_infoaguas('22 13 52'))
