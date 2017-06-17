from cnpj import Cnpj
import unittest


class CnpjTest(unittest.TestCase):
    def setUp(self):
        self.x = Cnpj()

    def tearDown(self):
        pass

    def test_cnpj_valido_1(self):
        self.assertTrue(self.x.validador(cnpj='64623626000137'), True)

    def test_cnpj_valido_2(self):
        self.assertTrue(self.x.validador(cnpj='64.623.626/0001-37'), True)

    def test_cnpj_valido_3(self):
        self.assertTrue(self.x.validador(cnpj='76673674000119'), True)

    def test_cnpj_valido_4(self):
        self.assertTrue(self.x.validador(cnpj='76.673.674/0001-19'), True)

    def test_cnpj_valido_5(self):
        self.assertTrue(self.x.validador(cnpj='37446564000162'), True)

    def test_cnpj_valido_6(self):
        self.assertTrue(self.x.validador(cnpj='37.446.564/0001-62'), True)

    def test_cnpj_fornatador_1(self):
        self.assertTrue(self.x.formator(cnpj='64623626000137'), True)

    def test_cnpj_fornatador_2(self):
        self.assertTrue(self.x.formator(cnpj='64.623.626/0001-37'), True)

    def test_cnpj_fornatador_3(self):
        self.assertTrue(self.x.formator(cnpj='64 623 626 0001 37'), True)

    def test_cnpj_fornatador_4(self):
        self.assertTrue(self.x.formator(cnpj='76673674000119'), True)

    def test_cnpj_fornatador_5(self):
        self.assertTrue(self.x.formator(cnpj='76.673.674/0001-19'), True)

    def test_cnpj_fornatador_6(self):
        self.assertTrue(self.x.formator(cnpj='76 673 674 0001 19'), True)

    def test_cnpj_fornatador_7(self):
        self.assertTrue(self.x.formator(cnpj='37446564000162'), True)

    def test_cnpj_fornatador_8(self):
        self.assertTrue(self.x.formator(cnpj='37.446.564/0001-62'), True)

    def test_cnpj_fornatador_9(self):
        self.assertTrue(self.x.formator(cnpj='37 446 564 0001 62'), True)
