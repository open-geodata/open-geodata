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

## ArcGIS

- https://mapas.agenciapcj.org.br/arcgis/rest/services
- https://sigel.aneel.gov.br/arcgis/rest/services
- https://geo.anm.gov.br/arcgis/rest/
- https://portal1.snirh.gov.br/server/rest/services