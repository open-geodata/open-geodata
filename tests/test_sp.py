import unittest


class PolygonTestCase(unittest.TestCase):
    def test_sp_1(self):
        # Imports
        import open_geodata as geo

        # Instancia Classe
        db = geo.data.DB(db='sp')

        # Obtem Agência
        # print(db.json)

        # Avalia se obteve corretamente
        self.assertIsInstance(db.json, dict)

    def test_sp_2(self):
        # Imports
        import open_geodata as geo

        # Instancia Classe
        db = geo.data.DB(db='sp')

        # Avalia se obteve corretamente
        self.assertIsInstance(db.list_data, list)

    def test_sp_3(self):
        # Imports
        import open_geodata as geo

        # Instancia Classe
        df_mun = geo.data.load_dataset(db='sp', name='tab.municipio_nome')
        id_municipio = df_mun[df_mun['municipio_nome'] == 'Piracicaba'][
            'id_municipio'
        ].values[0]
        # print(id_municipio)

        # Avalia se obteve corretamente
        self.assertEqual(id_municipio, 3538709)
