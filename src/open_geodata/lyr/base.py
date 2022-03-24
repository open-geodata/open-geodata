#!/usr/bin/env python
# coding: utf-8


import folium


def google_hybrid(min_zoom, max_zoom):
    row = {
        'link': 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        'name': 'Google Hybrid',
        'attribution': 'https://www.google.com/maps',
    }
    return folium.TileLayer(
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


def google_satellite(min_zoom, max_zoom):
    row = {
        'link': 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        'name': 'Google Satelite',
        'attribution': 'https://www.google.com/maps',
    }
    return folium.TileLayer(
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


def google_terrain(min_zoom, max_zoom):
    row = {
        'link': 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
        'name': 'Google Terrain',
        'attribution': 'https://www.google.com/maps',
    }
    return folium.TileLayer(
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


def google_streets(min_zoom, max_zoom):
    row = {
        'link': 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        'name': 'Google Streets',
        'attribution': 'https://www.google.com/maps',
    }
    return folium.TileLayer(
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


def cartodb_positron(min_zoom, max_zoom):
    return folium.TileLayer(
        tiles='cartodbpositron',
        attr='Carto',
        name='CartoDB Positron',
        min_zoom=min_zoom,
        max_zoom=max_zoom,
        overlay=False,
        control=True,
        show=False,
    )


if __name__ == '__main__':
    pass
