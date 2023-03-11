### Como Usar?


Inicialmente o pacote deve ser instalado

```bash
# Install
pip3 install open-geodata --upgrade
```

<br>

O _package_ **open_geodata** disponibiliza poucos _datasets_ nativamente.

```python
from open_geodata import geo

# List Datasets (dataframes and geodataframes)
geo.get_dataset_names()

# Load Dataset
geo.load_dataset('geo.sp.sp_250k_wgs84')
```

<br>

Além desses dados, é possível obter dados de outros *packages* que são instalados com o _pip install_, a saber:

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
geo.load_dataset_from_package('sp_piracicaba', 'geo.divisa_municipal')
```
