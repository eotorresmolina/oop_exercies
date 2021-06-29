'''
[Python]
- OOP
---------------------------
Autor: Torres Molina Emmanuel O.
Version: 1.1
Descripción:
Modificar la clase del archivo "exercise_1.py", de manera 
de verificar que los valores de x;y se encuentren siempre
dentro del rango -1000 a 1000, caso contrario su valor 
debe limitarse a estos valores.

'''

__author__ = "Torres Molina, Emmanuel O."
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"


class Punto():
    def __init__(self, x=0.0, y=0.0):
        if x > 1000:
            self.__mx = 1000
        else:
            self.__mx = x
        if y > 1000:
            self.__my = 1000
        else:
            self.__my = y
        
    def  setPunto(self, x, y):
        if x > 1000:
            self.__mx = 1000
        else:
            self.__mx = x
        if y > 1000:
            self.__my = 1000
        else:
            self.__my = y

    def getPunto(self):
        p = Punto()
        p.__mx = self.__mx
        p.__my = self.__my
        return p

    def setX(self, x):
        if x > 1000:
            self.__mx = 1000
        else:
            self.__mx = x
        
    def setY(self, y):
        if y > 1000:
            self.__my = 1000
        else:
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