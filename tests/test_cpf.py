from cpf import ValidaCpf
import unittest


# python -m unittest


class CpfTest(unittest.TestCase):
    def setUp(self):
        self.x = ValidaCpf()

    def tearDown(self):
        pass

    def test_cpf_pequeno_1(self):
        self.assertFalse(self.x.validador(cpf='123'), False)

    def test_cpf_pequeno_2(self):
        self.assertFalse(self.x.validador(cpf='0123'), False)

    def test_cpf_grande(self):
        self.assertFalse(self.x.validador(cpf='123456789012345'), False)

    def test_cpf_valido_inicial_zero(self):
        self.assertTrue(self.x.validador(cpf='01230123172'), True)

    def test_cpf_valido_final_zero(self):
        self.assertTrue(self.x.validador(cpf='12312300028'), True)

    def test_cpf_valido_com_char_especial_1(self):
        self.assertFalse(self.x.validador(cpf='012/30123172'), False)

    def test_formatar_valido_1(self):
        self.assertEqual(self.x.formatador(cpf='01230123172'), '012.301.231-72')

    def test_formatar_tamanho_invalido_1(self):
        self.assertEqual(self.x.formatador(cpf='1230123172'), False)


if __name__ == '__main__':
    unittest.main()
