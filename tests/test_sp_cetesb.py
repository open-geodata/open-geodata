import unittest


class PolygonTestCase(unittest.TestCase):
    def test_cetesb(self):
        import open_geodata as geo

        # Instancia Classe
        cetesb = geo.sp.cetesb.div_admin.CETESB()

        # Obtem Agência
        ag = cetesb.get_agencia_ambiental(municipio='Piracicaba')

        # Avalia se obteve corretamente
        self.assertEqual(ag['agencia'], 'Agência Ambiental de Piracicaba')
