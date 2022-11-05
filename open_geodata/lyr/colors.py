
"""


"""


import geopandas as gpd
import seaborn as sns


def create_colors(input_geojson, col_categories):
    """
    Funçao que cria dictionary com colors para layers
    :param input_geojson:
    :param col_categories:
    :return:
    """
    gdf = gpd.read_file(input_geojson)

    list_cols = list(set(gdf.columns))
    if col_categories not in list_cols:
        print('"col_categories" must  be in:')
        print(list_cols)

    # Set palette
    palette_polygon = 'Paired'

    # Get list of unique values
    categories = list(set(gdf[col_categories]))
    categories.sort()

    # See the palette chosed
    pal = sns.color_palette(palette_polygon, n_colors=len(categories))

    # Set dictionary
    color_polygon = dict(zip(categories, pal.as_hex()))
    return color_polygon


if __name__ == '__main__':
    pass
