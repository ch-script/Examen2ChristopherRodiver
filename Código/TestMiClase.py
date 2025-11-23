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

    #Tests para VerificaListaCanciones
    def test_cancion_1(self):
        resultado = self.objeto.VerificaListaCanciones(["Canción 1"])
        self.assertEqual(resultado, True)
    def test_cancion_4(self):
        resultado = self.objeto.VerificaListaCanciones(["Canción 4"])
        self.assertEqual(resultado, None)
    def test_vacio(self):
        resultado = self.objeto.VerificaListaCanciones([])
        self.assertEqual(resultado, False)

    #Test para ObtieneMasBailable
    def test_mas_disponible(self):
        resultado = self.objeto.ObtieneMasBailable([0.8,0.7,0.3,0.5])
        self.assertEqual(resultado, 0.8)

    def test_no_lista(self):
        resultado = self.objeto.ObtieneMasBailable("0")
        self.assertEqual(resultado, None)

    def test_un_elemento(self):
        resultado = self.objeto.ObtieneMasBailable([.1])
        self.assertEqual(resultado, 0.1)

    def test_lista_vacia(self):
        resultado = self.objeto.ObtieneMasBailable([])
        self.assertEqual(resultado, None)  

    #Test para Encontrar
    def test_encontrar_5(self):
        resultado = self.objeto.Encuentra([1,2,3,4,"5"], "5")
        self.assertEqual(resultado, False)  
    def test_encontrar_(self):
        resultado = self.objeto.Encuentra([], 0)
        self.assertEqual(resultado, False)

if __name__ == "__main__":
    unittest.main()