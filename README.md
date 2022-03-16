# Open Geodata

[![Publish Python 🐍 distributions 📦 to PyPI](https://github.com/open-geodata/open-geodata/actions/workflows/publish-to-pypi.yml/badge.svg)](https://github.com/open-geodata/open-geodata/actions/workflows/publish-to-pypi.yml)

<br>

Pacote para disponibilizar dados espaciais!
<br>
Todos os datasets estão com *datum* WGS84 (EPSG: 4326).

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
geo.load_dataset('sp_250k_wgs84.geojson')
```

<br>

---

### *Datasets*

**sp_250k**
<br>
Limites administrativos municipais do Estado de São Paulo. 

<br>

---

### *TODO*

1. https://github.com/twisted/incremental
