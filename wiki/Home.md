O **_OpenGeodata_** tem como objetivo disponibilizar dados espaciais para pequenos projetos. A concepção é que ter os
dados localmente pode ser mais interessante (e barato!) que manter dados em servidores. Alguns dos dados disponíveis no
pacote são:

- **geo.br_ibge.br_ibge**: Limites dos Estados
- **geo.sp.sp_250k_wgs84**: Limites administrativos municipais do Estado de São Paulo.

<br>

Os dados espaciais são compilados no _packages_ do python, disponíveis para serem instalados por meio do _pip install_.
Todos os dados estão em formato _geopackage_ (extensão _.gpkg_) e são comprimidos usando o _7zip_. Existem também alguns
dados em formatos tabulares, em arquivos _.csv_, também comprimidos usando o _7zip_.

Com o pacote **_OpenGeodata_**, os dados espaciais são lidos como _geodataframes_(Geopandas), enquanto os dados
tabulares são lidos como _dataframe_ (Pandas).

O projeto disponibiliza poucos dados, tendo em vista a limitação de 100mb do repositório oficial PyPi, porém é possível
adicionar outros dados dos pacotes listados no [wiki](./wiki/Databases.md)

Para possibilitar testes do pacote, criei
um [Google Colab](https://colab.research.google.com/drive/1s_w9t599OstJ0KS99NusH2EVGYa5twMh?usp=sharing).<br>
Todos os _datasets_ estão com _datum_ WGS84 (EPSG: 4326).


-----

### Instalar

```bash
# Install
pip3 install open-geodata --upgrade
```
