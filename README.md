# Open Geodata

[![Publish Python 🐍 distributions 📦 to PyPI](https://github.com/open-geodata/open-geodata/actions/workflows/publish-to-pypi.yml/badge.svg)](https://github.com/open-geodata/open-geodata/actions/workflows/publish-to-pypi.yml)

<br>

Pacote para disponibilizar dados espaciais!
<br>
Todos os datasets estão com _datum_ WGS84 (EPSG: 4326).

<br>

---

### Instalar

```python
pip3 install open-geodata --upgrade
```

<br>

---

### Como Usar?

```python
from open_geodata import geo

# List geodataframes
geo.get_dataset_names()

# Load geodataframe
geo.load_dataset('sp_250k_wgs84')
```

```python
from open_geodata import lyr

# Add Layers
lyr.base.google_hybrid(min_zoom, max_zoom)
```

```python
from open_geodata import folium_plus

# Create Map
m = folium_plus.adds.create_map_multitiles()
m
```

```python
from open_geodata import converts

converts.df2geojson(df, lat='latitude', long='longitude', remove_coords_properties=True)
```

<br>

---

### _Datasets_

**br_ibge**

<br>

Limites de Municípios e Estados.

**sp_250k**

<br>

Limites administrativos municipais do Estado de São Paulo.

**sp_piracicaba**

<br>

Limites do Plano Diretor do Município de Piracicaba.

<br>

---

### Teste

[Google Colab](https://colab.research.google.com/drive/1s_w9t599OstJ0KS99NusH2EVGYa5twMh?usp=sharing)

<br>

---

### _TODO_

1. <https://github.com/twisted/incremental>
2. Definir os _layers_

Participnar dados!
https://dev.to/bowmanjd/easily-load-non-python-data-files-from-a-python-package-2e8g


import pkg_resources
https://stackoverflow.com/questions/779495/access-data-in-package-subdirectory


Use of pkg_resources is discouraged in favor of importlib.resources, importlib.metadata, and their backports (importlib_resources, importlib_metadata). Please consider using those libraries instead of pkg_resources.

https://setuptools.pypa.io/en/latest/pkg_resources.html