import os
import folium
import geopandas as gpd
import seaborn as sns


def macrozona():
    # Input
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'geo', 'sp_piracicaba'))
    gdf = gpd.read_file(os.path.join(root, 'macrozonas.geojson'))
    gdf = gdf.to_crs(epsg=4326)

    # Column with category
    col_categories = 'Macrozona'

    # Set palette
    palette_polygon = 'Paired'
    palette_polygon = 'colorblind'

    # Get list of unique values
    categories = set(gdf[col_categories])
    categories = list(categories)
    categories.sort()

    # See the palette chosed
    pal = sns.color_palette(palette_polygon, n_colors=len(categories))

    # Set dictionary
    color_polygon = dict(zip(categories, pal.as_hex()))

    # Popup
    gdf['PopUp'] = gdf.apply(popup_macrozona, axis=1)

    # Shapefile
    lyr = folium.features.GeoJson(
        gdf,
        name='Macrozoneamento',
        style_function=lambda x: {
            'fillColor': color_polygon[x['properties']['Macrozona']],
            'color': color_polygon[x['properties']['Macrozona']],
            'weight': 0,
            'fillOpacity': 0.3
        },
        popup=folium.GeoJsonPopup(
            fields=['PopUp'],
            aliases=['Macrozona'],
            labels=False,
            sticky=True,
            localize=True,
            style=f"""
            background-color: #F0EFEF;
            """,
            parse_html=True,
            max_width=400,
        ),
        tooltip=folium.features.GeoJsonTooltip(
            fields=['Macrozona', ],
            aliases=['Macrozona', ],
            labels=True,
            sticky=True,
            opacity=0.9,
            direction='auto',
        ),
        highlight_function=lambda x: {
            'weight': 3
        },
        embed=False,
        zoom_on_click=False,
        control=True,
        show=False,
    )
    return lyr


# PopUp
def popup_macrozona(row):
    descriptions = {
        'MADE': 'Macrozona de Desenvolvimento Rural',
        'MANU': 'Macrozona de Núcleos Urbanos Isolados',
        'MAPH': 'Macrozona de Proteção Hídrica e Ambiental',
        'MCU': 'Macrozona de Contenção Urbana',
        'MRU': 'Macrozona de Restrição Urbana',
        'MUC': 'Macrozona de Urbanização Consolidada',
    }
    macrozona = row['Macrozona']
    description = descriptions[macrozona]
    popup = """
    <div>
    <h4>Plano Diretor de Piracicaba</h4>
    <h5>Lei Complementar nº 405/2019</h5>
    <b>{}</b>
    </div>    
    """.format(description)
    return popup


def perimetro_urbano():
    # Input
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'geo', 'sp_piracicaba'))
    gdf = gpd.read_file(os.path.join(root, 'divisa_perimetro.geojson'))
    gdf = gdf.to_crs(epsg=4326)

    # Shapefile
    lyr = folium.features.GeoJson(
        gdf,
        name='Perimetro Urbano',
        style_function=lambda x: {
            'fillColor': '#E1E1E1',
            'color': '#E1E1E1',
            'weight': 2,
            'fillOpacity': 0.5,
        },
        tooltip=folium.features.GeoJsonTooltip(
            fields=['Nome', ],
            aliases=['Nome', ],
            labels=True,
            sticky=True,
            opacity=0.9,
            direction='auto',
        ),
        embed=False,
        zoom_on_click=False,
        control=True,
        show=False,
    )
    return lyr


def divisa_municipal():
    # Input
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'geo', 'sp_piracicaba'))
    gdf = gpd.read_file(os.path.join(root, 'divisa_municipal.geojson'))
    gdf = gdf.to_crs(epsg=4326)

    # Shapefile
    lyr = folium.features.GeoJson(
        gdf,
        name='Divisão Municipal',
        style_function=lambda x: {
            'fillColor': '#FAE878',
            'color': '#FAE878',
            'weight': 2,
            'fillOpacity': 0.0,
        },
        embed=False,
        zoom_on_click=False,
        control=True,
        show=True,
    )
    return lyr


def divisa_urbano_rural():
    # Input
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'geo', 'sp_piracicaba'))
    gdf = gpd.read_file(os.path.join(root, 'divisa_urbanorural.geojson'))
    gdf = gdf.to_crs(epsg=4326)

    # Set dictionary
    color_polygon = {
        'Área Rural': '#F1A51F',
        'Área Urbana': '##E1E1E1',
    }

    # Shapefile
    lyr = folium.features.GeoJson(
        # gjson,
        gdf,
        name='Divisão Urbano Rural',
        style_function=lambda x: {
            'fillColor': color_polygon[x['properties']['Area']],
            'color': color_polygon[x['properties']['Area']],
            'weight': 1,
            'fillOpacity': 0.3
        },
        embed=False,
        zoom_on_click=False,
        control=True,
        show=False,
    )
    return lyr


def divisa_abairramento():
    # Input
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'geo', 'sp_piracicaba'))
    gdf = gpd.read_file(os.path.join(root, 'divisa_abairramento.geojson'))
    gdf = gdf.to_crs(epsg=4326)

    # Shapefile
    lyr = folium.features.GeoJson(
        gdf,
        name='Divisão Abairramento',
        style_function=lambda x: {
            'fillColor': '#CFCFCF',
            'color': '#CFCFCF',
            'weight': 1,
            'fillOpacity': 0.3
        },
        tooltip=folium.features.GeoJsonTooltip(
            fields=['NomeBairro'],
            aliases=['Bairro'],
            labels=True,
            sticky=True,
            opacity=0.9,
            direction='auto',
        ),

        highlight_function=lambda x: {
            'weight': 3
        },
        embed=False,
        zoom_on_click=False,
        control=True,
        show=False,
    )
    return lyr


if __name__ == '__main__':
    pass
