"""
Móodulo para acessar as malhas municipais do IBGE

"""

from pathlib import Path

import geopandas as gpd
import requests


class IBGE:
    def __init__(self):
        pass

    def get_malhas_municipais(self, estado: str = 'SP') -> gpd.GeoDataFrame:
        """
        _summary_


        >>> import open_geodata as geo


        :param url: _description_
        :type url: _type_
        :return: _description_
        :rtype: _type_
        """
        # Obtem dados do IBGE
        gdf = gpd.read_file(
            filename=f'http://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2018/UFs/{estado}/{estado.lower()}_municipios.zip'
        )

        # Renomeia Colunas
        gdf = gdf.rename(
            columns={
                'NM_MUNICIP': 'nome_municipio',
                'CD_GEOCMU': 'id_municipio',
            }
        )
        # Converte o tipo de dado da coluna id_municipio para int
        gdf['id_municipio'] = gdf['id_municipio'].astype(int)

        # Reordena colunas
        gdf = gdf[['id_municipio', 'nome_municipio', 'geometry']]

        return gdf

    def download_malhas_municipais(
        self, estado: str = 'SP', output_path: str | Path = './'
    ) -> None:
        """
        Download das malhas municipais do IBGE para o estado especificado.

        :param estado: Sigla do estado (ex: 'SP' para São Paulo)
        :param output_path: Caminho onde os arquivos serão salvos
        """
        url = f'http://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2018/UFs/{estado}/{estado.lower()}_municipios.zip'
        filename = Path(url).name
        # Download
        r = requests.get(url, allow_redirects=True)
        open(Path(output_path) / filename, 'wb').write(r.content)


if __name__ == "__main__":
    ibge = IBGE()
    gdf = ibge.get_malhas_municipais()
    gdf = gdf.loc[gdf['id_municipio'] == 3504206]
    print(gdf.head())
    print(gdf['id_municipio'] == 3504206)
