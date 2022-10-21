"""


"""


import py7zr
import pprint
import pandas as pd
import geopandas as gpd
import importlib.resources
from pathlib import Path

from more_itertools import one, only


def _ajust_list_files(list_files):
    list_files = [str(x.as_posix()) for x in list_files]  # Convert to text
    list_files = [x.split('.', maxsplit=1)[0]
                  for x in list_files]  # Splita no . e pega primeira parte
    list_files = [x.replace('/', '.')
                  for x in list_files]  # Convert Paths Linux
    list_files = list(set(list_files))
    list_files.sort()
    return list_files


def _read_7z_file(file_path_7z):
    if file_path_7z.is_file():
        with py7zr.SevenZipFile(file_path_7z, 'r') as archive:
            allfiles = archive.getnames()

            # Quero apenas um arquivo por gpkg
            if len(allfiles) == 1:
                for filename, bio in archive.read(allfiles).items():
                    pass
            else:
                raise RuntimeError('.zip tem mais de um gpkg')
        return gpd.read_file(bio)


def get_dataset_names():
    """

    """
    package_path = Path(__file__).absolute().parent
    data_path = package_path / 'data'
    list_files = data_path.rglob('*.*')
    list_files = [x for x in list_files]
    list_files = [x.relative_to(data_path) for x in list_files]
    return _ajust_list_files(list_files)


def load_dataset(dataset_name):
    """
    Funções para carregar dados geoespaciais

    :param dataset_name:
    :return:
    """

    filename = dataset_name.replace('.', '/')
    filename = Path(filename)
    package_path = Path(__file__).absolute().parent
    data_path = package_path / 'data'
    file_path = data_path / filename

    # Checa se existe
    list_shp = get_dataset_names()
    if dataset_name not in list_shp:
        raise RuntimeError(f'"{filename}" not exists')

    # Checa se existe mais de um
    if list_shp.count(dataset_name) > 1:
        raise RuntimeError(
            f'Exists "{list_shp.count(dataset_name)}" datasets named "{dataset_name}"')

    # Teste ambos tipos de arquivos
    file_path_7z = file_path.with_suffix('.7z')
    file_path_csv = file_path.with_suffix('.csv')

    # Load por tipo de arquivo
    if file_path_7z.is_file():
        return _read_7z_file(file_path_7z)

    # Se o arquivo é um
    elif file_path_csv.is_file():
        return pd.read_csv(file_path_csv)

    else:
        print('Não encontrado')


def get_dataset_from_package(package_name):
    """
    Pega dados dos pacotes
    Os dados preciso estar disponibilizados em .7z ou .csv

    """
    # sss
    package_path = importlib.resources.files(package_name)
    list_files = [x for x in package_path.rglob(
        '*') if x.suffix in ('.7z', '.csv')]
    list_files = [x.relative_to(package_path) for x in list_files]
    list_files = [x.relative_to('data') for x in list_files]
    for path in ['input', 'output']:
        try:
            list_files = [x.relative_to(path) for x in list_files]
        except:
            pass
    return _ajust_list_files(list_files)


def load_dataset_from_package(package_name, dataset_name):
    """

    """
    package_path = importlib.resources.files(package_name)
    print(package_path)
    filename = dataset_name.replace('.', '/')
    filename = Path(filename)    

    # Lista de Arquivo
    list_7zips = list(package_path.rglob(f'{filename}*.7z'))
    list_csv = list(package_path.rglob(f'{filename}*.csv'))

    # Pega Valor Único
    file_path_7z = only(list_7zips)
    file_path_csv = only(list_csv)

    if file_path_7z.is_file():
        return _read_7z_file(file_path_7z)

    elif file_path_csv.is_file():
        return pd.read_csv(file_path_csv)

    else:
        print('Não encontrado')


if __name__ == '__main__':
    from open_geodata import geo
    from open_geodata.functions import share_boundary, find_neighbors

    # # List Geodata
    list_shp = get_dataset_names()
    pprint.pprint(list_shp)

    # # Read Geaodata
    gdf = load_dataset('geo.sp.sp_250k_wgs84')
    print(gdf.head())

    # # List Geodata
    list_shp = get_dataset_from_package('sp_piracicaba')
    pprint.pprint(list_shp)

    gdf = load_dataset_from_package('sp_piracicaba', 'geo.divisa_municipal')
    print(gdf.head())

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
    # for i in list_shp:
    #     #print(i.parents[2])
    #     a = i.relative_to(i.parents[2])
    #     print(a)
