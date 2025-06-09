"""
_summary_

:return: _description_
:rtype: _type_
"""

import urllib.parse
from pathlib import Path

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

import open_geodata as geo

# import os
# import pandas as pd
# from open_geodata import geo
# from paths import input_path, output_path_tab


class CETESB:
    def __init__(self) -> None:
        self.df_agencias_municipios = None

    def get_agencia_ambiental(self, municipio: str):
        """
        Obtem informações de um dado município
        https://licenciamento.cetesb.sp.gov.br/municipioss.asp?muni=SANTOS

        :param mun: Nome do Município (de acordo com a grafia da CETESB)
        :type mun: string
        :return: informações sobre a Agência Ambiental que atua no sminucípio selecionado
        :rtype: dictionary
        """
        # Município
        mun_url = municipio.encode('ISO-8859-1')
        mun_url = urllib.parse.quote(mun_url)
        print(f'{municipio} > {mun_url}')

        # Set URL
        url = f'https://licenciamento.cetesb.sp.gov.br/municipioss.asp?muni={mun_url}'

        # Get Data
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        # time.sleep(1)

        # Get all relevant data
        table = soup.find('table', attrs={'width': '300'})
        rows = table.find_all('tr')

        # Create List Adress
        list_end = [municipio]
        for row in rows:
            text = row.get_text()
            text = ' '.join(text.split())
            text = text.strip()
            list_end.append(text)

        # Rename List
        for i in ['Bairro:', 'Cidade:', 'CEP:', 'Fone:', 'Fax:', 'E-mail:']:
            list_end = np.char.replace(list_end, i, '')
        list_end = [x.strip() for x in list_end]

        # Format Variables
        cep = '{:08d}'.format(int(list_end[5]))
        tel = list_end[6].strip().replace(' ', '').replace('-', ' ')
        fax = list_end[7].strip().replace(' ', '').replace('-', ' ')

        # Create Dictionary
        return {
            'municipio_cetesb': list_end[0],
            'agencia': list_end[1],
            'endereco': list_end[2].split('nº')[0].strip(),
            'numero': list_end[2].split('nº')[1].strip(),
            'bairro': list_end[3],
            'municipio_sede': list_end[4].title(),
            'cep': '{}-{}'.format(cep[:5], cep[5:8]),
            'telefone': f'({tel[:2]}) {tel[3:7]}-{tel[7:]}',
            'fax': f'({fax[:2]}) {fax[3:7]}-{fax[7:]}',
            'email': list_end[8],
            'url': url,
        }

    def get_all_agencias(self):
        #
        package_path = Path(__file__).parents[3].absolute()
        data_path = package_path / 'data'
        # print(data_path)

        # Read Dataframe
        df = pd.read_csv(data_path / 'tab' / 'sp_cetesb' / 'tab_municipios.csv')
        # print(df.head())

        # Create empty list
        list_addresses = []

        # df = df[0:4]  # For tests only
        for index, row in df.iterrows():
            # Create Small Dictionary
            dict_df = {
                'id_municipio': row['id_municipio'],
            }

            # Get Addresses
            list_address = self.get_agencia_ambiental(row['municipio_cetesb'])
            list_address = {**dict_df, **list_address}
            list_addresses.append(list_address)

        # Create Table from dictionarys
        df = pd.DataFrame.from_dict(list_addresses)
        return df

    def get_all_agencias_adjusted(self):
        # Obtem Tabela Padrão com os nomes de municípios
        df_mun = geo.geo.load_dataset('tab.sp.tab_municipio_nome')

        # Obtem Tabela da CETESB
        df_cetesb = self.get_all_agencias()

        # Merge
        df = pd.merge(
            df_mun,
            df_cetesb,
            how='left',
            left_on='id_municipio',
            right_on='id_municipio',
        )

        # Ajustes
        # Split
        df[['endereco', 'complemento']] = df['endereco'].str.split(
            ' - ', expand=True
        )

        # Reorder
        cols = df.columns.tolist()
        cols = cols[0:5] + [cols[-1]] + cols[5:-1]
        df = df[cols]

        #
        # Adjust Table
        df.loc[:, 'endereco'] = (
            df['endereco'].astype(str).apply(lambda x: self._rename_nome(x))
        )
        df.loc[:, 'bairro'] = (
            df['bairro'].astype(str).apply(lambda x: self._rename_nome(x))
        )
        df.loc[:, 'municipio_sede'] = (
            df['municipio_sede']
            .astype(str)
            .apply(lambda x: self._rename_nome(x))
        )
        df.loc[:, 'fax'] = (
            df['fax'].astype(str).apply(lambda x: self._rename_nome(x))
        )
        df.loc[:, 'complemento'] = (
            df['complemento'].astype(str).apply(lambda x: self._rename_nome(x))
        )

        # Deleta colunas
        df = df.drop(['municipio_cetesb'], axis=1, inplace=False)

        # Atribui
        if self.df_agencias_municipios is None:
            self.df_agencias_municipios = df
        return df

    def _rename_nome(self, x):
        x = x.title()
        x = x.strip()
        dict_rename = {
            # Nome
            'Av ': 'Av. ',
            'Av. ': 'Avenida ',
            ' Joao ': ' João ',
            'Ten.': 'Tenente',
            # Basics
            ' Com ': ' com ',
            ' Sobre ': ' sobre ',
            ' Da ': ' da ',
            ' De ': ' de ',
            ' Do ': ' do ',
            ' Das ': ' das ',
            ' Dos ': ' dos ',
            ' A ': ' a ',
            ' As ': ' as ',
            ' Ao ': ' ao ',
            ' Aos ': ' aos ',
            ' E ': ' e ',
            ' O ': ' o ',
            ' Os ': ' os ',
            '(11) -': '',
            '( ) -': '',
            'Jd. ': 'Jardim ',
            'V. ': 'Vila ',
            'Sta.': 'Santa',
            'Pq. ': 'Parque ',
            'Res.': 'Residencial ',
            ' Sao ': ' São ',
            'J.S. Marcos': 'Jardim São Marcos',
            'Jardim-': 'Jardim -',
            'Xxiii': 'XXIII',
            'Ii': 'II',
            # Empty
            'None': '',
            'none': '',
        }
        for k, v in dict_rename.items():
            x = x.replace(k, v)
        x = x.replace('  ', ' ')
        return x.strip()

    def _get_ag_mun(self):
        # Se já rodou
        if isinstance(self.df_agencias_municipios, pd.DataFrame):
            df_ag_mun = self.df_agencias_municipios

        # Senão, roda
        else:
            df_ag_mun = self.get_all_agencias_adjusted()
        return df_ag_mun

    def get_only_agencias(self) -> pd.DataFrame:
        df_ag_mun = self._get_ag_mun()

        # Get column's name
        cols = list(df_ag_mun.columns[2:-1])

        # Group
        df = pd.DataFrame(
            df_ag_mun.groupby(cols, dropna=False)['id_municipio'].count()
        )
        df.reset_index(inplace=True)

        # Delta Última Coluna
        df = df.drop(df.columns[len(df.columns) - 1], axis=1, inplace=False)
        return df

    def get_geodataframe(self):

        # Padrão
        gdf = geo.load_dataset('geo.sp.sp_250k_wgs84')
        gdf = gdf.drop(['municipio_nome'], axis=1, inplace=False)
        gdf['id_municipio'] = gdf['id_municipio'].astype(int)
        gdf['geometry'] = gdf['geometry'].simplify(0.0015)

        # Tabela AgÊncias e Municípios
        df_ag_mun = self._get_ag_mun()

        # Join
        gdf = gdf.merge(df_ag_mun, on='id_municipio', how='left')
        return gdf


if __name__ == '__main__':
    from pathlib import Path

    import pandas as pd

    cetesb = CETESB()
    aa = cetesb.get_agencia_ambiental('Piracicaba')
    print(aa)

    # bb = cetesb.get_all_agencias()
    # print(bb.head())

    cc = cetesb.get_all_agencias_adjusted()
    print(cc.head())
