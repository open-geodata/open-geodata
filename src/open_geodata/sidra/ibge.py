#!/usr/bin/env python
# coding: utf-8

# !pip install sidrapy --upgrade


import sidrapy
import pandas as pd


def get_estimated_population(cod_ibge):
    """
    Retorna a população estimada
    :param cod_ibge:
    :return:
    """
    # Get Table
    df = sidrapy.get_table(
        table_code='6579',
        territorial_level='6',
        ibge_territorial_code=cod_ibge,
        period='all',
        header='n',
    )

    # Dict
    dict_col = {
        'D1C': 'id_municipio',
        'D1N': 'municipio_nome',
        'V': 'n_habitantes',
        'D2N': 'ano'
    }

    # Remane Columns
    df.rename(
        dict_col,
        axis=1,
        inplace=True
    )

    # Select Columns
    df = df[[v for k, v in dict_col.items()]]

    # Adjust Columns
    df.sort_values(by=['ano'], inplace=True)
    df['id_municipio'] = pd.to_numeric(df['id_municipio'], errors='coerce')
    df['n_habitantes'] = pd.to_numeric(df['n_habitantes'], errors='coerce')
    df['ano'] = pd.to_numeric(df['ano'], errors='coerce')

    # Results
    return df


if __name__ == '__main__':
    cod_ibge = '3526902'  # Limeira
    a = get_estimated_population(cod_ibge)
    print(a)
