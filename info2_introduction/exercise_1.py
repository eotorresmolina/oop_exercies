'''
[Python]
- OOP
---------------------------
Autor: Torres Molina Emmanuel O.
Version: 1.1
Descripción:
Definir e implementar una clase Punto:

- Variables miembro:
mx y my - del tipo double, que representan las coordenadas (x; y) del punto.

- Métodos miembro públicos:
setPunto: recibe los valores de x e y en dos variables double.
getPunto: devuelve el valor del punto (en formato class Punto). 
setX y setY; que dan valor a x e y. 
getX y getY; que devuelven los valores de x e y. 

La creación del objeto debe permitir o no, las siguientes expresiones:
Punto pa; # mx y my se inicializan en cero.
Punto pb (23.3,56.8); # mx se inicializa con 23.3 y my con 56.8.

La inicialización del objeto con un solo parámetro debe dar error de sintaxis, por ejemplo la línea:
Punto pc (34.4); # error de sintaxis.

'''

__author__ = "Torres Molina, Emmanuel O."
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"


class Punto():
    def __init__(self, x=0.0, y=0.0):
        self.__mx = x
        self.__my = y
        
    def  setPunto(self, x, y):
        self.__mx = x
        self.__my = y

    def getPunto(self):
        p = Punto()
        p.__mx = self.__mx
        p.__my = self.__my
        return p

    def setX(self, x):
        self.__mx = x
        
    def setY(self, y):
        self.__my = y

    def getX(self):
        return self.__mx

    def getY(self):
        return self.__my


if __name__ == '__main__':
    pa = Punto()
    pb = Punto(23.3, 56.8)
    pc = Punto(2456.77, 8655.6564)
    pd = Punto()
    pd.setPunto(28.9, 94)
    pe = Punto(23.45, 24.9)
    pe.setX(99)
    pe.setY(101)
    pf = pb.getPunto()
    
    print('Puntos del Objeto pa: {};{}'.format(pa.getX(), pa.getY()))
    print('Puntos del Objeto pb: {};{}'.format(pb.getX(), pb.getY()))
    print('Puntos del Objeto pc: {};{}'.format(pc.getX(), pc.getY()))
    print('Puntos del Objeto pd: {};{}'.format(pd.getX(), pd.getY()))
    print('Puntos del Objeto pe: {};{}'.format(pe.getX(), pe.getY()))
    print('Puntos del Objeto pf: {};{}'.format(pf.getX(), pf.getY()))