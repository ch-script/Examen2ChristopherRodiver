import unittest
from Examen2 import MiClase

class TestMiClase(unittest.TestCase):
    
    def setUp(self):
        self.objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2"], [0.8, 0.9])
    
    # Tests para ObtieneValencia
    def test_obtiene_valencia_con_digitos_impares(self):
        resultado = self.objeto.ObtieneValencia(1234567)
        self.assertEqual(resultado, 4)
    
    def test_obtiene_valencia_todos_pares(self):
        resultado = self.objeto.ObtieneValencia(2468)
        self.assertEqual(resultado, 0)
    
    
    # Tests para DivisibleTempo
    def test_divisible_tempo_numero_normal(self):
        resultado = self.objeto.DivisibleTempo(10)
        self.assertEqual(resultado, [1, 2, 5, 10])
    
    def test_divisible_tempo_numero_primo(self):
        resultado = self.objeto.DivisibleTempo(7)
        self.assertEqual(resultado, [1, 7])
    
    def test_divisible_tempo_numero_compuesto(self):
        resultado = self.objeto.DivisibleTempo(12)
        self.assertEqual(resultado, [1, 2, 3, 4, 6, 12])
    
    def test_divisible_tempo_numero_uno(self):
        resultado = self.objeto.DivisibleTempo(1)
        self.assertEqual(resultado, [1])


if __name__ == "__main__":
    unittest.main()