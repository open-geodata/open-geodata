Além das funções principais (para listar e carregar dados), o pacote entrega outras funções para uso com dados
geoespaciais.


## Maps Folium


Cria mapa folium com diversos *titles* diferentes.

```python
from open_geodata import folium_plus

# Create Map
m = folium_plus.adds.create_map_multitiles()
m
```

## Layers


Cria objetos de *layers* para serem inlcuidos no map folium.

```python
from open_geodata import lyr

# Add Layers
lyr.base.google_hybrid(min_zoom, max_zoom)
```

## Convert


Será removido!
Usei em um projeto quando não sabia fazer de outra forma.

```python
from open_geodata import converts

converts.df2geojson(df, lat='latitude', long='longitude', remove_coords_properties=True)
```
