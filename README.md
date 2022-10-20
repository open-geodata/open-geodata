# Open Geodata

[![Publish Python 🐍 distributions 📦 to PyPI](https://github.com/open-geodata/open-geodata/actions/workflows/publish-to-pypi.yml/badge.svg)](https://github.com/open-geodata/open-geodata/actions/workflows/publish-to-pypi.yml)

- [GitHub](https://github.com/open-geodata/open-geodata)
- [PyPi](https://pypi.org/project/open-geodata/)

<br>

O **_OpenGeodata_** tem como objetivo disponibilizar dados espaciais para pequenos projetos. A concepção é que ter os dados localmente pode ser mais interessante (e barato!) que manter dados em servidores. Alguns dos dados disponíveis no pacote são:

- **geo.br_ibge.br_ibge**: Limites dos Estados
- **geo.sp.sp_250k_wgs84**: Limites administrativos municipais do Estado de São Paulo.

<br>

Os dados espaciais são compilados no _packages_ do python, disponíveis para serem instalados por meio do _pip install_. Todos os dados estão em formato _geopackage_ (extensão _.gpkg_) e são comprimidos usando o _7zip_. Existem também alguns dados em formatos tabulares, em arquivos _.csv_, também comprimidos usando o _7zip_.

Com o pacote **_OpenGeodata_**, os dados espaciais são lidos como _geodataframes_(Geopandas), enquanto os dados tabulares são lidos como _dataframe_ (Pandas).

O projeto disponibiliza poucos dados, tendo em vista a limitação de 100mb do repositório oficial PyPi, porém é possível adicionar outros dados dos pacotes listados abaixo:

- [**sp-ff-apa-corumbatai**](https://pypi.org/project/sp-ff-apa-corumbatai/): dados espaciais da Área de Proteção Ambiental Corumbataí
- [**sp_piracicaba**](https://pypi.org/project/sp-piracicaba/): dados espaciais do Plano Diretor do Município de Piracicaba
- [**sp-bh-pcj-2020-2035**](https://pypi.org/project/sp-bh-pcj-2020-2035/): dados espaciais do Plano das Bacias PCJ 2020-2035.
- [**sp-bh-at**](https://pypi.org/project/sp-bh-at/): dados espaciais do Plano das Bacias do Alto Tietê

<br>

Para possibilitar testes do pacote, criei um [Google Colab](https://colab.research.google.com/drive/1s_w9t599OstJ0KS99NusH2EVGYa5twMh?usp=sharing).<br>
Todos os _datasets_ estão com _datum_ WGS84 (EPSG: 4326).

<br>

---

### Instalar

```bash
# Install
pip3 install open-geodata --upgrade
```

<br>

---

### Como Usar?

O _package_ **open_geodata** disponibiliza poucos _datasets_. A

```python
from open_geodata import geo

# List Datasets (dataframes and geodataframes)
geo.get_dataset()

# Load Dataset
geo.load_dataset('geo.sp.sp_250k_wgs84')
```

<br>

Além desses dados, é possível obter dados de outros packages que são instalados com o _pip install_, a saber:

```python
# List Datasets from package (dataframes and geodataframes)
geo.get_dataset_from_package('sp_piracicaba')

# Load Dataset from package
geo.load_dataset_from_package('sp_piracicaba', 'zips.divisa_municipal')
```

<br>

### Outras Funções

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

### _TODO_

1. <https://github.com/twisted/incremental>
2. Definir os _layers_
3. Participnar dados! https://dev.to/bowmanjd/easily-load-non-python-data-files-from-a-python-package-2e8g
