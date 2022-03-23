#!/usr/bin/env python
# coding: utf-8


import os
import folium
import webbrowser
import pandas as pd


def create_map_multitiles(location=[-23.9619271, -46.3427499], zoom_start=10):
    """

    :param tile_service:
    :param location:
    :param zoom_start:
    :return:
    """

    # Create Maps
    m = folium.Map(
        location=location,
        zoom_start=zoom_start,
        tiles=None,
    )

    # Read table with all tiles servers
    tiles_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'tab', 'folium'))
    df = pd.read_csv(os.path.join(tiles_path, 'tiles.csv'), index_col=0)

    # Filter some tiles
    # df = df[2:4]
    # df = df.loc[(df['name'] == 'ESRI Satelite') | (df['name'] == 'ESRI Street')]
    # df = df[df['name'].str.startswith(('ESRI'))]
    df = df[df['name'].str.startswith(('Google'))]
    # df = df[df['name'] == 'Google Satellite']

    # Loop
    for index, row in df.iterrows():
        # Create reference to attribution
        ref = '<a href="{}" target="blank">{}</a>'.format(row['attribution'], row['name'])

        # Create multiples tiles layers
        folium.TileLayer(
            tiles=row['link'],
            attr=ref,
            name=row['name'],
        ).add_to(m)

    # Results
    return m


if __name__ == '__main__':
    # Tiles Path
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'tab', 'folium'))
    print(root)

    # Create Paths
    m = create_map_multitiles()
    folium.LayerControl('topright', collapsed=True).add_to(m)

    # Save/Open Map
    down_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    map_file = os.path.join(down_path, 'map_example.html')
    m.save(map_file)
    webbrowser.open(map_file)
