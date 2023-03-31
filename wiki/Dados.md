## APA Corumbatai


Dados espaciais da Área de Proteção Ambiental Corumbataí, disponibilizados no
pacote [PyPi](https://pypi.org/project/sp-ff-apa-corumbatai/) e
repositório [GitHub](https://github.com/open-geodata/sp_ff_apa-corumbatai).

```shell
# Instalar
pip3 install sp-ff-apa-corumbatai --upgrade
```

<br>

Após instalar é possível consumir os dados.

```python
# Imports
from open_geodata import geo

# List Datasets from package (dataframes and geodataframes)
geo.get_dataset_from_package('sp_ff_apa_corumbatai')

# Load Dataset from package
geo.load_dataset_from_package('sp_ff_apa_corumbatai', 'geo.apa_corumbatai_geologia')
```

<br>


-----


## Plano Diretor de Piracicaba


Dados espaciais do Plano Diretor do Município de Piracicaba, disponibilizados no
pacote [PyPi](https://pypi.org/project/sp-piracicaba/) e
repositório [GitHub](https://github.com/open-geodata/sp_piracicaba).

```shell
# Instalar
pip3 install sp-piracicaba --upgrade
```

```python
# Imports
from open_geodata import geo

# List Datasets from package (dataframes and geodataframes)
geo.get_dataset_from_package('sp_piracicaba')

# Load Dataset from package
geo.load_dataset_from_package('sp_piracicaba', 'geo.divisa_abairramento')
```

<br>


-----


## Plano das Bacias PCJ 2020-2035


Dados espaciais do Plano das Bacias PCJ 2020-2035, disponibilizados no
pacote [PyPi](https://pypi.org/project/sp-bh-pcj-2020-2035/) e
repositório [GitHub](https://github.com/open-geodata/sp_bh_pcj-2020-2035).

```shell
# Instalar
pip3 install sp-bh-pcj-2020-2035 --upgrade
```

```python
# Imports
from open_geodata import geo

# List Datasets from package (dataframes and geodataframes)
geo.get_dataset_from_package('sp_bh_pcj_2020_2035')

# Load Dataset from package
geo.load_dataset_from_package('sp_bh_pcj_2020_2035', 'geo.limite da bacia pcj - poligonos')
```

<br>


-----


# Plano de Bacias do Alto Tietê


Dados espaciais do Plano de Bacias do Alto Tietê, disponibilizados no
pacote [PyPi](https://pypi.org/project/sp-bh-at/) e
repositório [GitHub](https://github.com/open-geodata/sp_bh_at).

```shell
# Instalar
pip3 install sp-bh-at --upgrade
```

```python
# Imports
from open_geodata import geo

# List Datasets from package (dataframes and geodataframes)
geo.get_dataset_from_package('sp_bh_at')

# Load Dataset from package
geo.load_dataset_from_package('sp_bh_at', 'geo.06_bacia_alto_tiete')
```

<br>


-----


# Divisão Administrativa CETESB


Dados espaciais da Divisão Administrativa da CETESB, disponibilizados no
pacote [PyPi](https://pypi.org/project/sp-cetesb-divadmin/) e
repositório [GitHub](https://github.com/open-geodata/sp_cetesb_divadmin).

```shell
# Instalar
pip3 install sp-cetesb-divadmin --upgrade
```

```python
# Imports
from open_geodata import geo

# List Datasets from package (dataframes and geodataframes)
geo.get_dataset_from_package('sp_cetesb_divadmin')

# Load Dataset from package
geo.load_dataset_from_package('sp_cetesb_divadmin', 'geo.sp_cetesb')
```

<br>


-----


# Divisão Administrativa TJSP


Dados espaciais da Divisão Administrativa do TJSP, disponibilizados no
pacote [PyPi](https://pypi.org/project/sp-tjsp-divadmin/) e
repositório [GitHub](https://github.com/open-geodata/sp_tjsp_divadmin).

```shell
# Instalar
pip3 install sp-tjsp-divadmin --upgrade
```

```python
# Imports
from open_geodata import geo

# List Datasets from package (dataframes and geodataframes)
geo.get_dataset_from_package('sp_tjsp_divadmin')

# Load Dataset from package
geo.load_dataset_from_package('sp_tjsp_divadmin', 'geo.sp_tjsp_divadmin')
```

<br>

------


# Divisão Administrativa MPSP


Dados espaciais da Divisão Administrativa do MPSP, disponibilizados no
pacote [PyPi](https://pypi.org/project/sp-mpsp-divadmin/) e
repositório [GitHub](https://github.com/open-geodata/sp_mpsp_divadmin/).

```shell
# Instalar
pip3 install sp-mpsp-divadmin --upgrade
```

```python
# Imports
from open_geodata import geo

# List Datasets from package (dataframes and geodataframes)
geo.get_dataset_from_package('sp_mpsp_divadmin')

# Load Dataset from package
geo.load_dataset_from_package('sp_mpsp_divadmin', 'geo.sp_cetesb')
```

<br>

------


## Outras Bases de Dados


Abaixo são listadas outras bases de dados para avaliar se são relevantes para estudos e projetos.

Até o momento não foram desenvolvidos pacotes para obtenção e possibilidade de uso com o OpenGeodata.

- [EuroStat](https://ec.europa.eu/eurostat/web/main/home)