O **_OpenGeodata_** tem como objetivo disponibilizar dados espaciais para pequenos projetos. A concepção é que ter os
dados localmente pode ser mais interessante (e barato!) que manter dados em servidores.\
Alguns dos dados básicos disponíveis no pacote são:

- **geo.br_ibge.br_ibge**: Limites dos Estados
- **geo.sp.sp_050k_wgs84**: Limites administrativos municipais do Estado de São Paulo em escala 1:50.000.
- **geo.sp.sp_250k_wgs84**: Limites administrativos municipais do Estado de São Paulo em escala 1:250.000.

<br>

Os dados espaciais são compilados no _packages_ do python, disponíveis para serem instalados por meio do _pip install_. Todos os dados estão em formato _geopackage_ (extensão _.gpkg_) e são comprimidos usando o _7zip_. Existem também alguns dados em formatos tabulares, em arquivos _.csv_, também comprimidos usando o _7zip_.

Com o pacote **_OpenGeodata_**, os dados espaciais são lidos como _geodataframes_(Geopandas), enquanto os dados tabulares são lidos como _dataframe_ (Pandas).

O projeto disponibiliza poucos dados, tendo em vista a limitação de 100mb do repositório oficial [PyPi](https://pypi.org/). É possível acessar outros dados instalando pacotes adicionais listados...

Para possibilitar testes do pacote, criei
um [Google Colab](https://colab.research.google.com/drive/1s_w9t599OstJ0KS99NusH2EVGYa5twMh?usp=sharing).<br>
Todos os _datasets_ estão com _datum_ WGS84 (EPSG: 4326).

<br>

Alguma dúvida, sugestão e/ou contribuição, favor reportar um [problema/_issue_](https://github.com/michelmetran/open-geodata/issues).

!!! note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.



!!! note "Phasellus posuere in sem ut cursus"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.