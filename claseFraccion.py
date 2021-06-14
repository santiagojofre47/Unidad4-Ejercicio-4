class Fraccion:
    __numerador = None
    __denominador = None
    __resultado = None

    def __init__(self, numerador = None, denominador = None):
        self.__resultado = 0.0
        self.__numerador = numerador
        self.__denominador = denominador

    def __str__(self):
        return f'{self.__numerador}/{self.__denominador}'    


    def crearResultado(self, unResultado):
        self.__resultado = unResultado

    def convertirAfraccion(self):
        r = self.__numerador/self.__denominador
        return r

    def getDenominador(self):
        return self.__denominador    

    def simplifica(self, m, n):
        while m % n != 0:
            mViejo = m
            nViejo = n

            m = nViejo
            n = mViejo % nViejo
        return n     
        
    def __add__(self, p2):
        n1 = self.convertirAfraccion()
        n2 = p2.convertirAfraccion()
        res = n1+n2
        return res

    def __sub__(self, p2):
        n1 = self.convertirAfraccion()
        n2 = p2.convertirAfraccion()
        res = n1-n2
        return res

    def __mul__(self, p2):
        n1 = self.convertirAfraccion()
        n2 = p2.convertirAfraccion()
        res = n1*n2
        return res

    def __truediv__(self, p2):
        n1 = self.convertirAfraccion()
        n2 = p2.convertirAfraccion()
        res = n1/n2
        return res

if __name__ == '__main__':

    fr1 = Fraccion(1,2)
    fr2 = Fraccion(1,2)
    print(fr1)
    print(fr2)
    res = fr1+fr2
    res2 = fr1-fr2
    res3 = fr1/fr2
    res4 = fr1*fr2
    print(res)
    print(res2)
    print(res3)
    print(res4)


            


