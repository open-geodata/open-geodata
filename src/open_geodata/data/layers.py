#!/usr/bin/env python
# coding: utf-8


import folium


def add_lyr_google_hybrid(min_zoom, max_zoom):
    row = {
        'link': 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        'name': 'Google Hybrid',
        'attribution': 'https://www.google.com/maps',
    }
    lyr = folium.TileLayer(
        tiles=row['link'],
        attr=('<a href="{}" target="blank">{}</a>'.format(row['attribution'], row['name'])),
        name=row['name'],
        min_zoom=min_zoom,
        max_zoom=max_zoom,
        subdomains=['mt0', 'mt1', 'mt2', 'mt3'],
        overlay=False,
        control=True,
        show=True,
    )
    return lyr


def add_lyr_google_satellite(min_zoom, max_zoom):
    row = {
        'link': 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        'name': 'Google Satelite',
        'attribution': 'https://www.google.com/maps',
    }
    lyr = folium.TileLayer(
        tiles=row['link'],
        attr=('<a href="{}" target="blank">{}</a>'.format(row['attribution'], row['name'])),
        name=row['name'],
        min_zoom=min_zoom,
        max_zoom=max_zoom,
        subdomains=['mt0', 'mt1', 'mt2', 'mt3'],
        overlay=False,
        control=True,
        show=False,
    )
    return lyr


def add_lyr_google_terrain(min_zoom, max_zoom):
    row = {
        'link': 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
        'name': 'Google Terrain',
        'attribution': 'https://www.google.com/maps',
    }
    lyr = folium.TileLayer(
        tiles=row['link'],
        attr=('<a href="{}" target="blank">{}</a>'.format(row['attribution'], row['name'])),
        name=row['name'],
        min_zoom=min_zoom,
        max_zoom=max_zoom,
        subdomains=['mt0', 'mt1', 'mt2', 'mt3'],
        overlay=False,
        control=True,
        show=False,
    )
    return lyr


def add_lyr_google_streets(min_zoom, max_zoom):
    row = {
        'link': 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        'name': 'Google Streets',
        'attribution': 'https://www.google.com/maps',
    }
    lyr = folium.TileLayer(
        tiles=row['link'],
        attr=('<a href="{}" target="blank">{}</a>'.format(row['attribution'], row['name'])),
        name=row['name'],
        min_zoom=min_zoom,
        max_zoom=max_zoom,
        subdomains=['mt0', 'mt1', 'mt2', 'mt3'],
        overlay=False,
        control=True,
        show=False,
    )
    return lyr


def add_lyr_cartodbpositron(min_zoom, max_zoom):
    lyr = folium.TileLayer(
        tiles='cartodbpositron',
        attr='Carto',
        name='CartoDB Positron',
        min_zoom=min_zoom,
        max_zoom=max_zoom,
        overlay=False,
        control=True,
        show=False,
    )
    return lyr


if __name__ == '__main__':
    pass
