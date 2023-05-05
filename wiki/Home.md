O **_OpenGeodata_** tem como objetivo disponibilizar dados espaciais para pequenos projetos. A concepção é que ter os
dados localmente pode ser mais interessante (e barato!) que manter dados em servidores.\
Alguns dos dados básicos disponíveis no pacote são:

- **geo.br_ibge.br_ibge**: Limites dos Estados
- **geo.sp.sp_050k_wgs84**: Limites administrativos municipais do Estado de São Paulo em escala 1:50.000.
- **geo.sp.sp_250k_wgs84**: Limites administrativos municipais do Estado de São Paulo em escala 1:250.000.

<br>

Os dados espaciais são compilados no _packages_ do python, disponíveis para serem instalados por meio do _pip install_.
Todos os dados estão em formato _geopackage_ (extensão _.gpkg_) e são comprimidos usando o _7zip_. Existem também alguns
dados em formatos tabulares, em arquivos _.csv_, também comprimidos usando o _7zip_.

Com o pacote **_OpenGeodata_**, os dados espaciais são lidos como _geodataframes_(Geopandas), enquanto os dados
tabulares são lidos como _dataframe_ (Pandas).

O projeto disponibiliza poucos dados, tendo em vista a limitação de 100mb do repositório oficial [PyPi](https://pypi.org/). É possível
acessar outros dados instalando pacotes adicionais listados no [wiki](./wiki/Databases.md)

Para possibilitar testes do pacote, criei
um [Google Colab](https://colab.research.google.com/drive/1s_w9t599OstJ0KS99NusH2EVGYa5twMh?usp=sharing).<br>
Todos os _datasets_ estão com _datum_ WGS84 (EPSG: 4326).

- [earthnow](https://earthnow.usgs.gov/observer/?sessionId=8e5a1e6dd8f15ef0eb3cb4c8bbf725928507)
- [earth :: an animated map of global wind, weather, and ocean conditions](http://earth.nullschool.net/#current%2Fwind%2Fsurface%2Flevel%2Forthographic%3D46.17%2C5.18%2C248)
- [EOS-EarthData](https://eos-earthdata.sr.unh.edu/)
- [Earth View](http://earthview.withgoogle.com/)
- [flightradar24](http://www.flightradar24.com/)
- [glovis](http://glovis.usgs.gov/)
- [Intact Forest Landscapes](http://www.intactforests.org/)
- [European Soil Data Centre (ESDAC)](https://esdac.jrc.ec.europa.eu/)
- [RedList](https://www.iucnredlist.org/)
- [Landsat Science](https://landsat.gsfc.nasa.gov/)
- [SRTM](http://srtm.csi.cgiar.org/SELECTION/inputCoord.asp)
- [arquivoestado](http://www.arquivoestado.sp.gov.br/web/digitalizado/cartografico/documentos_cartograficos)
- [GIS Lounge](https://www.gislounge.com/)
- [GIS Café](http://www.giscafe.com/)
- [Story Maps](https://storymaps.arcgis.com/)
- [ArcGIS Resource Center](https://resources.arcgis.com/en/help/)
- [ArcGIS Online](http://www.arcgis.com/home/)
- [ArcScripts](http://arcscripts.esri.com/)
- [Landsat Imagery](http://www.esri.com/software/landsat-imagery)
- [ESRI](http://www.esri.com/)
- [EuroStat](https://ec.europa.eu/eurostat/web/main/home)
- [ssss](http://datageo.casamilitar.sp.gov.br/geonetworkgrd/srv/por/catalog.search#/home)
- [Instituto Geográfico e Cartográfico](http://www.igc.sp.gov.br/)
- [Blog do Fernando Quadro](https://www.fernandoquadro.com.br/)
