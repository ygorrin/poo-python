class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result = self.result + num
        for s in nums:
            self.result += s
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for s in nums:
            self.result -= s
        return self

md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print("Primera Instancia", x)	# debe imprimir 5
sd = MathDojo()
y = sd.add(5).add(9,3,5,7).subtract(5,8,9,6).result
print("Segunda Instancia", y)
hd= MathDojo()
z = hd.add(6).subtract(8,4,2,6).add(5,9,7,4).result
print("Tercera instancia", z)

import unittest

test1 = MathDojo()
test2 = MathDojo()

class IsMathDojoTests(unittest.TestCase):
    # cada método en esta clase es una prueba que se ejecutará 
    def testTwo(self):
        self.assertTrue(test1.add(2).add(2,5,1).subtract(3,2).result, 5)
        return self
        # otra forma de escribir arriba es 
        # self.assertTrue(isEven(2))
    def testThree(self):
        self.assertEqual(test2.add(5).add(9,3,5,7).subtract(5,8,9,6).result==1, True)
        return self
        #  cualquier tarea que desee ejecutar antes de ejecutar cualquier método anterior, colóquelas en el método setUp 
    def setUp(self):
        print("Inicio de Test MathDojo")
        test1.result = 0;
        test2.result = 0;
        # cualquier tarea que quieras ejecutar después de ejecutar las pruebas, ponlas en el método
    def tearDown(self):
        # agrega las tareas tearDown 
        print("Finaliza Test MathDojo")

if __name__ == '__main__':
    unittest.main() # esto ejecuta nuestras pruebas
