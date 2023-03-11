# Open Geodata


[![Publish Python 🐍 distributions 📦 to PyPI](https://github.com/open-geodata/open-geodata/actions/workflows/publish-to-pypi.yml/badge.svg)](https://github.com/open-geodata/open-geodata/actions/workflows/publish-to-pypi.yml)

[GitHub](https://github.com/open-geodata/open-geodata) | [PyPi](https://pypi.org/project/open-geodata/)

<br>

O **_OpenGeodata_** tem como objetivo disponibilizar dados espaciais para pequenos projetos. A concepção é que ter os
dados localmente pode ser mais interessante (e barato!) que manter dados em servidores.\
Alguns dos dados básicos disponíveis no pacote são:

- **geo.br_ibge.br_ibge**: Limites dos Estados
- **geo.sp.sp_050k_wgs84**: Limites administrativos municipais do Estado de São Paulo em escala 1:50.000.
- **geo.sp.sp_250k_wgs84**: Limites administrativos municipais do Estado de São Paulo em escala 1:250.000.

<br>


O projeto disponibiliza poucos dados, tendo em vista a limitação de 100mb do repositório oficial [PyPi](https://pypi.org/). É possível
acessar outros dados instalando pacotes adicionais listados no [wiki/Dados](https://github.com/open-geodata/open-geodata/wiki/Dados)

> Para mais informações, ver [**Wiki**](https://github.com/open-geodata/open-geodata/wiki)

<br>

Para possibilitar testes do pacote, criei
um [Google Colab](https://colab.research.google.com/drive/1s_w9t599OstJ0KS99NusH2EVGYa5twMh?usp=sharing).<br>
Todos os _datasets_ estão com _datum_ WGS84 (EPSG: 4326).

<br>

---

### _TODO_

1. Estudar mais o [incremental](https://github.com/twisted/incremental)
2. Definir os _layers_ para projetos apartados
3. Estudar a possibilidade de participnar dados, conforme mencionado [aqui](https://dev.to/bowmanjd/easily-load-non-python-data-files-from-a-python-package-2e8g)!
