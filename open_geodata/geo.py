"""
sssss
"""

import importlib.resources
import json
import pkgutil
import pprint
import tempfile
from pathlib import Path
from urllib.parse import quote, unquote, urlparse, urlunparse

import geopandas as gpd
import pandas as pd
import pooch
import py7zr
from more_itertools import one, only


class DB:
    def __init__(self, db='general', project='open_geodata') -> None:
        self.project = project
        self.cache = None

        json_data = pkgutil.get_data(
            package=self.project, resource=f'db/{db}.json'
        )
        if isinstance(json_data, bytes):
            self.json_raw = json.loads(json_data)
        else:
            raise Exception('Erro!')
        self.json = self._flatten()
        # self._check_keys()

    def _flatten(self):
        flat = {}
        for outer_key, inner_dict in self.json_raw.items():
            for inner_key, value in inner_dict.items():
                new_key = f"{outer_key}.{inner_key}"
                flat[new_key] = value
        return flat

    def _check_keys(self):
        for dict_data in self.json.values():
            if all(key in dict_data for key in ['url', 'hash']):
                pass
            else:
                raise Exception('Falta chaves')

    @property
    def list_data(self):
        return list(self.json.keys())

    def get_base_url(self, name):
        if name not in self.list_data:
            raise Exception('Nome Inválido')

        #
        url = self.json[name]['url']
        scheme = urlparse(url=url).scheme
        netloc = urlparse(url=url).netloc
        path = Path(urlparse(url=url).path).parent.as_posix()
        params = urlparse(url=url).params
        query = urlparse(url=url).query
        fragment = urlparse(url=url).fragment

        url = urlunparse((scheme, netloc, path, params, query, fragment))
        url = quote(url, safe=':/')
        return url

    def _get_hash(self, name):
        if name not in self.list_data:
            raise Exception('Nome Inválido')

        return self.json[name]['hash']

    def _get_filename(self, name):
        if name not in self.list_data:
            raise Exception('Nome Inválido')

        #
        url = self.json[name]['url']
        path = Path(urlparse(url=url).path)
        return unquote(path.name)

    def get_registry(self, name):
        return {self._get_filename(name=name): self._get_hash(name=name)}

    def _create_cache_for_data(self, name):
        self.cache = pooch.create(
            path=pooch.os_cache(project=self.project),
            base_url=self.get_base_url(name=name),
            # version='v1.8.2',
            # version_dev='main',
            registry=self.get_registry(name=name),
        )
        return self.cache

    def get_data(self, name):
        self.cache = self._create_cache_for_data(name=name)
        return self.cache.fetch(fname=self._get_filename(name=name))

    def get_filehash_sha256(self, name):
        filename = self.get_data(name=name)
        return pooch.file_hash(filename, alg="sha256")

    def read_7z(self, name, *args, **kwargs) -> gpd.GeoDataFrame:
        file_path_7z = self.get_data(name=name)

        layer = kwargs.get('layer', None)
        with py7zr.SevenZipFile(file_path_7z, 'r') as archive:
            allfiles = archive.getnames()

            # Quero apenas um arquivo por gpkg
            if len(allfiles) == 1:
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_dir = Path(temp_dir)
                    archive.extract(path=temp_dir, targets=allfiles)

                    #
                    filename = list(temp_dir.glob('*'))[0]
                    ext = filename.suffix.lower()
                    if ext in ['.gpkg']:
                        return gpd.read_file(filename=filename, layer=layer)
                    else:
                        raise Exception(
                            f'Não tem configuração para extesão {ext}'
                        )

            else:
                raise RuntimeError('.zip tem mais de um gpkg')


# def _ajust_list_files(list_files):
#     """

#     :param list_files:
#     :return:
#     """
#     # Convert to text
#     list_files = [str(x.as_posix()) for x in list_files]

#     # Splita no . e pega primeira parte
#     list_files = [x.split('.', maxsplit=1)[0] for x in list_files]

#     # Convert Paths Linux
#     list_files = [x.replace('/', '.') for x in list_files]
#     list_files = list(set(list_files))
#     list_files.sort()
#     return list_files


# def _read_7z_file(file_path_7z):
#     if file_path_7z.is_file():


def load_dataset(db, name) -> pd.DataFrame | gpd.GeoDataFrame:
    """
    Funções para carregar dados geoespaciais

    :param dataset_name:
    :return:
    """

    db_obj = DB(db=db)
    filepath = db_obj.get_data(name=name)
    # filename = dataset_name.replace('.', '/')
    # filename = Path(filename)
    # package_path = Path(__file__).absolute().parent
    # data_path = package_path / 'data'
    # file_path = data_path / filename

    # Checa se existe
    # list_shp = get_dataset_names()
    # if dataset_name not in list_shp:
    #     raise RuntimeError(f'"{filename}" not exists')

    # # Checa se existe mais de um
    # if list_shp.count(dataset_name) > 1:
    #     raise RuntimeError(
    #         f'Exists "{list_shp.count(dataset_name)}" datasets named "{dataset_name}"'
    #     )

    # Teste ambos tipos de arquivos
    ext = Path(filepath).suffix.lower()

    # Load por tipo de arquivo
    if ext in ['.7z']:
        return db_obj.read_7z(name=name)

    # Se o arquivo é um
    elif ext in ['.csv', '.xls', '.xlsx']:
        return pd.read_csv(filepath)

    else:
        raise Exception('Deu ruim')


# def get_dataset_names():
#     """
#     fdfddfd

#     """
#     package_path = Path(__file__).absolute().parent
#     data_path = package_path / 'data'
#     list_files = data_path.rglob('*.*')
#     list_files = [x for x in list_files]
#     list_files = [x.relative_to(data_path) for x in list_files]
#     return _ajust_list_files(list_files)


# def load_dataset(dataset_name) -> pd.DataFrame | gpd.GeoDataFrame:
#     """
#     Funções para carregar dados geoespaciais

#     :param dataset_name:
#     :return:
#     """

#     filename = dataset_name.replace('.', '/')
#     filename = Path(filename)
#     package_path = Path(__file__).absolute().parent
#     data_path = package_path / 'data'
#     file_path = data_path / filename

#     # Checa se existe
#     list_shp = get_dataset_names()
#     if dataset_name not in list_shp:
#         raise RuntimeError(f'"{filename}" not exists')

#     # Checa se existe mais de um
#     if list_shp.count(dataset_name) > 1:
#         raise RuntimeError(
#             f'Exists "{list_shp.count(dataset_name)}" datasets named "{dataset_name}"'
#         )

#     # Teste ambos tipos de arquivos
#     file_path_7z = file_path.with_suffix('.7z')
#     file_path_csv = file_path.with_suffix('.csv')

#     # Load por tipo de arquivo
#     if file_path_7z.is_file():
#         return _read_7z_file(file_path_7z)

#     # Se o arquivo é um
#     elif file_path_csv.is_file():
#         return pd.read_csv(file_path_csv)

#     else:
#         print('Não encontrado')


# def get_dataset_from_package(package_name):
#     """
#     Pega dados dos pacotes
#     Os dados preciso estar disponibilizados em .7z ou .csv

#     """
#     # sss
#     package_path = importlib.resources.files(package_name)
#     list_files = [
#         x for x in package_path.rglob('*') if x.suffix in ('.7z', '.csv')
#     ]
#     list_files = [x.relative_to(package_path) for x in list_files]
#     list_files = [x.relative_to('data') for x in list_files]
#     for path in ['input', 'output']:
#         try:
#             list_files = [x.relative_to(path) for x in list_files]
#         except:
#             pass
#     return _ajust_list_files(list_files)


# def load_dataset_from_package(package_name, dataset_name):
#     """ """
#     # Importa o Package
#     package_path = importlib.resources.files(package_name)
#     print(package_path)

#     #
#     filename = dataset_name.replace('.', '/')
#     filename = Path(filename)
#     print(f'O nome do arquivo é {filename}')

#     # Lista de Arquivo
#     list_7zips = list(package_path.rglob(f'{filename}*.7z'))
#     list_csv = list(package_path.rglob(f'{filename}*.csv'))

#     # Pega Valor Único
#     file_path_7z = only(list_7zips)
#     file_path_csv = only(list_csv)

#     # Prints
#     # print(f'A lista de 7zip é: {file_path_7z}')
#     # print(f'A lista de csv é: {file_path_csv}')

#     if file_path_7z is not None and file_path_7z.is_file():
#         return _read_7z_file(file_path_7z)

#     elif file_path_csv is not None and file_path_csv.is_file():
#         return pd.read_csv(file_path_csv)

#     else:
#         print('Não encontrado')


# if __name__ == '__main__':
#     from open_geodata import geo
#     from open_geodata.functions import find_neighbors, share_boundary

#     # # List Geodata
#     list_shp = get_dataset_names()
#     pprint.pprint(list_shp)

#     # # Read Geaodata
#     gdf = load_dataset('geo.sp.sp_250k_wgs84')
#     print(gdf.head())

#     # # List Geodata
#     list_shp = get_dataset_from_package('sp_piracicaba')
#     pprint.pprint(list_shp)

#     gdf = load_dataset_from_package('sp_piracicaba', 'geo.divisa_municipal')
#     print(gdf.head())

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
