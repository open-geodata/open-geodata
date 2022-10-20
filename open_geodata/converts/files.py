"""

"""

import py7zr
from pathlib import Path


import geopandas as gpd
from shapely.geometry import Point






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
    print('Estudar:\nhttps://geopandas.org/en/stable/docs/reference/api/geopandas.points_from_xy.html')
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


def df2gdf(df, lat='latitude', long='longitude', epsg=4326):
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
        crs=f'EPSG:{epsg}',
        geometry=geometry
    )
    gdf.drop([lat, long], axis=1, inplace=True, errors='ignore')
    return gdf


def convert_to_7zip(input_path, output_path, extension='gpkg'):
    """

    :return:
    """
    list_files = list(input_path.rglob(f'*.{extension}'))    
    if len(list_files) == 0:        
        raise RuntimeError(f'Não existem arquivos "{extension}" na pasta {input_path}')

    for file in list_files:
        # Paths
        zip7_filepath = output_path / f'{file.stem}.7z'

        # Write 7zip
        with py7zr.SevenZipFile(zip7_filepath, 'w') as archive:
            archive.write(file, file.name)

        # Print
        print(f'Arquivo "{file.name}" convertido para "{file.stem}.7z"')
    
    print(f'Foram convertidos {len(list_files)} arquivos com sucesso!')
    return 0



if __name__ == '__main__':
    
    # Convert
    data_path = Path(__file__).parents[1].joinpath('data')
    ibge_path = data_path / 'geo' / 'br_ibge'
    convert_to_7zip(ibge_path, ibge_path)

    pass