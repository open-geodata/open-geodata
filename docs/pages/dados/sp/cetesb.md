_Script_ para obter a divisão administrativa da CETESB, em formato tabular.\
Fiz através da iteração da consulta dos municípios por meio do formulário disponível em:

> https://licenciamento.cetesb.sp.gov.br/municipioss.asp?muni=SANTOS

<br>

Os _scripts_ também transformam o dado tabular em arquivos espaciais (_geojson_ e _gpkg_). E cria mapa _folium_.

<br>

## OpenGeodata

É possível também utilizar esse pacote no projeto [OpeGeodata](https://github.com/open-geodata/open-geodata).

```shell
pip3 install sp-cetesb-divadmin
```

<br>

---

## DataGeo

Após algum tempo encontrei também a delimitação das Agências Ambientais no [DataGeo](https://datageo.ambiente.sp.gov.br/). Particularmente eu prefiro consumir a fonte primária de dados, mesmo que seja mais trabalhosa para obtenção, motivo pelo qual deixo os _links_ apenas para registro.

- http://datageo.ambiente.sp.gov.br/serviceTranslator/rest/getXml/Geoserver_Publico/VWM_AGENCIA_CETESB_50_CETESB_20160201_POL/1454333714664/wms
- http://datageo.ambiente.sp.gov.br/geoserver/datageo/VWM_AGENCIA_CETESB_50_CETESB_20160201_POL/wfs?version=1.0.0&request=GetFeature&outputFormat=SHAPE-ZIP&typeName=VWM_AGENCIA_CETESB_50_CETESB_20160201_POL

<br>

---

## DataGeo

![Alt text](https://open-geodata.readthedocs.io/pt/latest/assets/sp_cetesb/2014.11.05%20-%20DD%20325%20-%20Atribui%C3%A7%C3%B5es%20das%20Unidades%20da%20CETESB.pdf){ type=application/pdf style="min-height:50vh;width:100%" }

<br>

---

## Departamentos

As agências, administrativamente, estão vinculadas aos Departamentos da CETESB. Essa informação pode ser relevante para a atuação de determinadas instituições (MPSP).

1. Departamento Gestão Ambiental I
2. Departamento Gestão Ambiental II
3. Departamento Gestão Ambiental III
4. Departamento Gestão Ambiental IV
5. Departamento Gestão Ambiental V

---

## Apenas por curiosidade

Encontrei um documento de 2015,no qual já tentava automaticar a obtenção dos dados da CETESB, usando o programa [Macro Express](https://www.macros.com/).

![Alt text](https://open-geodata.readthedocs.io/pt/latest/assets/sp_cetesb/2025.08.25%20-%20Roteiro%20Atualiza%C3%A7%C3%A3o%20Base%20CETESB.pdf){ type=application/pdf style="min-height:50vh;width:100%" }
