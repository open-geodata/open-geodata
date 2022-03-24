#!/usr/bin/env python
# coding: utf-8


import os
import folium
import webbrowser
import pandas as pd
import branca as bc


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


def modify_header_legend(m):
    """
    """

    # Header to Add
    head = """
    {% macro header(this, kwargs) %}
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
    <script>$( function() {
        $( ".maplegend" ).draggable({
            start: function (event, ui) {
                $(this).css({
                    right: "auto",
                    top: "auto",
                    bottom: "auto"
                });
            }
        });
    });
    </script>
    {% endmacro %}
    """

    # Add Header
    macro = bc.element.MacroElement()
    macro._template = bc.element.Template(head)
    m.get_root().add_child(macro)

    # CSS to Add (on Header)
    css = """
    {% macro header(this, kwargs) %}
    <style type='text/css'>
      .maplegend {
        position: absolute;
        z-index:9999;
        background-color: rgba(255, 255, 255, 1);
        border-radius: 5px;
        border: 2px solid #bbb;
        padding: 10px;
        font-size:14px;
        right: 10px;
        bottom: 20px;
      }
      .maplegend .legend-title {
        text-align: left;
        margin-bottom: 5px;
        font-weight: bold;
        font-size: 90%;
        }
      .maplegend .legend-scale ul {
        margin: 0;
        margin-bottom: 0px;
        padding: 0;
        float: left;
        list-style: none;
        }
      .maplegend .legend-scale ul li {
        font-size: 80%;
        list-style: none;
        margin-left: 0;
        line-height: 18px;
        margin-bottom: 2px;
        }
      .maplegend ul.legend-labels li span {
        display: block;
        float: left;
        height: 16px;
        width: 30px;
        margin-right: 5px;
        margin-left: 0;
        border: 0px solid #ccc;
        }
      .maplegend .legend-source {
        font-size: 80%;
        color: #777;
        clear: both;
        }
      .maplegend a {
        color: #777;
        }
    </style>
    {% endmacro %}
    """

    # Add CSS (on Header)
    macro = bc.element.MacroElement()
    macro._template = bc.element.Template(css)
    m.get_root().add_child(macro)
    return m


def add_categorical_legend(m, title, color_by_label):
    """
    """

    # Modify Header
    m = modify_header_legend(m)

    # ddd
    body = f"""
    <div id='maplegend {title}' class='maplegend'>
        <div class='legend-title'>{title}</div>
        <div class='legend-scale'>
            <ul class='legend-labels'>"""

    # Loop Categories
    for label, color in color_by_label.items():
        body += f"""
                <li><span style='background:{color}'></span>{label}</li>"""
    body += """
            </ul>
        </div>
    </div>
    """
    # Add Body
    body = bc.element.Element(body)
    m.get_root().html.add_child(body)
    return m


if __name__ == '__main__':
    from src.open_geodata.lyr.pd_piracicaba import macrozona

    # Create Map
    m = create_map_multitiles()

    # Add Layers
    m.add_child(macrozona())

    # Add Layer Control
    folium.LayerControl('topright', collapsed=False).add_to(m)

    # Add Lagend
    colors = {
        'MADE': '#0173b2',
        'MANU': '#de8f05',
        'MAPH': '#029e73',
        'MCU': '#d55e00',
        'MRU': '#cc78bc',
        'MUC': '#ca9161'
    }
    # m = modify_header_legend(m)
    m = add_categorical_legend(m, title='Legenda', color_by_label=colors)

    # Save/Open Map
    down_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    map_file = os.path.join(down_path, 'map_example.html')
    m.save(map_file)
    webbrowser.open(map_file)
