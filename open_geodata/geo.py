"""


"""


import os
import py7zr
import pprint
import pandas as pd
import geopandas as gpd
import seaborn as sns
import importlib.resources
from pathlib import Path


def get_dataset_names():
    """

    """
    package_path = Path(__file__).absolute().parent
    data_path = package_path / 'data'
    #print(':>>>> ', package_path)
    file_data = data_path.rglob('*.*')
    list_shp = [x for x in file_data]
    list_shp = [x.relative_to(data_path) for x in list_shp]
    list_shp = [str(x.as_posix()) for x in list_shp]  # Convert to text
    #list_shp = [str(x) for x in list_shp]
    list_shp = [x.split('.', maxsplit=1)[0]
                for x in list_shp]  # Splita no . e pega primeira parte
    # list_shp = [x.replace('\\', '.') for x in list_shp] # Convert Paths Windows
    list_shp = [x.replace('/', '.') for x in list_shp]  # Convert Paths Linux

    #list_shp = []
    # root = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))
    # for path, subdir, files in os.walk(root):
    #     for file in files:
    #         list_shp.append(file.split('.', maxsplit=1)[0])

    list_shp.sort()
    return list_shp


def load_dataset(name):
    """
    Funções para carregar dados geoespaciais

    :param name:
    :return:
    """
    filename = name.replace('.', '/')
    filename = Path(filename)
    package_path = Path(__file__).absolute().parent
    data_path = package_path / 'data'
    file_path = data_path / filename

    # Checa se existe
    list_shp = get_dataset_names()
    if name not in list_shp:
        raise RuntimeError(f'"{filename}" not exists')

    # Checa se existe mais de um
    if list_shp.count(name) > 1:
        raise RuntimeError(
            f'Exists "{list_shp.count(name)}" datasets named "{name}"')

    # Teste ambos tipos de arquivos
    file_path_7z = file_path.with_suffix('.7z')
    file_path_csv = file_path.with_suffix('.csv')

    # Load por tipo de arquivo
    if file_path_7z.is_file():
        # Geodataframe
        with py7zr.SevenZipFile(file_path_7z, 'r') as archive:
            allfiles = archive.getnames()

            # Quero apenas um arquivo por gpkg
            if len(allfiles) == 1:
                for filename, bio in archive.read(allfiles).items():
                    pass
            else:
                raise RuntimeError('.7z tem mais de um gpkg')
        return gpd.read_file(bio)

    # Se o arquivo é um
    if file_path_csv.is_file():
        return pd.read_csv(file_path_csv)


def get_dataset_names_others(pkg_name):
    """
    Pega dados dos pacotes
    Os dados preciso estar disponibilizados em .7z ou .csv

    """
    # sss
    package_path = importlib.resources.files(pkg_name)
    return [p.name for p in package_path.rglob('*') if p.suffix in ('.7z', '.csv')]


def load_dataset_others(package_name, dataset_name):
    """

    """
    package_path = importlib.resources.files(package_name)
    for p in package_path.rglob('*'):
        # print(p)
        if p.name == dataset_name:
            with py7zr.SevenZipFile(p, 'r') as archive:
                allfiles = archive.getnames()

                # Quero apenas um arquivo por gpkg
                if len(allfiles) == 1:
                    for filename, bio in archive.read(allfiles).items():
                        pass
                else:
                    raise RuntimeError('.zip tem mais de um gpkg')
            return gpd.read_file(bio)


def create_colors(input_geojson, col_categories):
    """
    Funçao que cria dictionary com colors para layers
    :param input_geojson:
    :param col_categories:
    :return:
    """
    gdf = gpd.read_file(input_geojson)

    list_cols = list(set(gdf.columns))
    if col_categories not in list_cols:
        print('"col_categories" must  be in:')
        print(list_cols)

    # Set palette
    palette_polygon = 'Paired'

    # Get list of unique values
    categories = list(set(gdf[col_categories]))
    categories.sort()

    # See the palette chosed
    pal = sns.color_palette(palette_polygon, n_colors=len(categories))

    # Set dictionary
    color_polygon = dict(zip(categories, pal.as_hex()))
    return color_polygon


if __name__ == '__main__':
    from open_geodata import geo
    from open_geodata.functions import share_boundary, find_neighbors

    # List Geodata
    list_shp = get_dataset_names()
    pprint.pprint(list_shp)

    # Read Geaodata
    gdf = load_dataset('geo.sp.sp_250k_wgs84')
    print(gdf.head())

    # List Geodata
    #list_shp = get_dataset_names_others('sp_piracicaba')
    # pprint.pprint(list_shp)
    # for i in list_shp:
    #     #print(i.parents[2])
    #     a = i.relative_to(i.parents[2])
    #     print(a)

    #gdf = load_dataset_others('sp_piracicaba', 'divisa_municipal.7z')
    # gdf = load_dataset('divisa_municipal') # Localmente funciona
    # gdf = geo.load_dataset('divisa_abairramento')  # Pacote não funciona

    # Teste "find_neighbors" attribute table
    # gdf = find_neighbors(gdf, 'municipio_nome')

    # Teste "find_neighbors" spatial
    # gdf_interest = gdf.loc[gdf['id_municipio'] == 3548906]
    # gdf = share_boundary(gdf, gdf_interest)

    # Results
    # print(gdf.head())

    # df = load_dataset('tab_municipio_ugrhi')
    # print(df.head())

    # create_colors(
    #     os.path.join('outorgas.gpkg'),
    #     col_categories = 'uso'
    # )
