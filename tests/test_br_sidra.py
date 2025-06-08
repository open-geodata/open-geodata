import unittest


class PolygonTestCase(unittest.TestCase):
    def test_sidra(self):
        import open_geodata as geo

        # São Carlos
        df = geo.br.ibge.ibge_sidra.get_estimated_population(id_municipio=3548906)

        # Pega Numero de Habitantes para 2019
        n_habitantes = df.loc[df['ano'] == 2019]['n_habitantes'].values[0]

        self.assertEqual(n_habitantes, 251983)
