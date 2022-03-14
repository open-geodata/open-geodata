#!/usr/bin/env python
# coding: utf-8

import os
import geopandas as gpd


def get_dataset_names():
    return os.listdir(os.path.join(os.path.dirname(__file__), 'data'))


def load_dataset(name):
    gdf = gpd.read_file(
        filename=os.path.join(os.path.dirname(__file__), 'data', name),
    )
    return gdf


if __name__ == '__main__':
    print('sss')
