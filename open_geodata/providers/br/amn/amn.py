"""
Agêncio Nacional de Mineração (ANM) - Brazil
This module provides access to the ANM's geospatial data services.
"""

import shutil
import ssl
import urllib.request
from pathlib import Path

import geopandas as gpd
import pandas as pd


class ANM:
    def __init__(self):
        """
        Initialize the ANM data provider.

        :param cache_dir: Directory to cache downloaded data.
        """

        list_tuples = {
            (
                'Áreas de Bloqueio',
                'https://app.anm.gov.br/dadosabertos/SIGMINE/BLOQUEIO.zip',
            ),
            (
                'Áreas de Proteção de Fonte',
                'https://app.anm.gov.br/dadosabertos/SIGMINE/PROTECAO_FONTE.zip',
            ),
            (
                'Áreas de Servidão',
                'https://app.anm.gov.br/dadosabertos/SIGMINE/AREA_SERVIDAO.zip',
            ),
            (
                'Arrendamentos',
                'https://app.anm.gov.br/dadosabertos/SIGMINE/ARRENDAMENTO.zip',
            ),
            (
                'Reservas Garimpeiras',
                'https://app.anm.gov.br/dadosabertos/SIGMINE/RESERVAS_GARIMPEIRAS.zip',
            ),
            (
                'Processos Minerários Ativos - SP',
                'https://app.anm.gov.br/dadosabertos/SIGMINE/PROCESSOS_MINERARIOS/SP.zip',
            ),
        }

        df = pd.DataFrame(list_tuples, columns=['nome', 'url'])
        self.layers = df

    def get_layers(self, layer: str) -> gpd.GeoDataFrame:
        """
        Get the available layers as a GeoDataFrame.

        :return: GeoDataFrame containing the layer names and URLs.
        """
        ssl._create_default_https_context = ssl._create_unverified_context
        url = self.layers.loc[self.layers['nome'] == layer, 'url'].values[0]

        gdf = gpd.read_file(filename=url)
        return gdf

    def download_file(self, layer: str, output_path: str | Path):
        """
        Download a file from the given URL and save it to the cache directory.

        :param url: URL of the file to download.
        :param filename: Name of the file to save in the cache directory.
        :return: Path to the downloaded file.
        """
        # context2 = ssl.SSLContext()
        ssl._create_default_https_context = ssl._create_unverified_context
        for i, row in self.layers.iterrows():
            if layer == row['nome']:
                print(f'Downloading {row["nome"]}...')
                url = row['url']
                url_path = Path(url)
                filepath = Path(output_path) / url_path.name

                # Download
                with (
                    urllib.request.urlopen(url) as r,
                    open(filepath, 'wb') as out_file,
                ):
                    shutil.copyfileobj(r, out_file)


if __name__ == '__main__':
    import tempfile

    import geopandas as gpd

    # Instancia
    amn2 = ANM()

    # Get available layers
    # print(amn2.layers)

    # Download a specific layer
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir = Path(temp_dir)

        amn2.download_file(
            layer='Processos Minerários Ativos - SP', output_path=temp_dir
        )

        # List files in the temporary directory
        list_files = list(temp_dir.glob('*'))

        gdf = gpd.read_file(filename=list_files[0])
        print(gdf.head)

    # Get a specific layer as a GeoDataFrame
    gdf = amn2.get_layers(layer='Processos Minerários Ativos - SP')
    print(gdf.head())
