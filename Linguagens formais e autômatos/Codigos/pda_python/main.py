from Test import *

if __name__ == "__main__": 
    Test.teste_y_x('00001111')
    Test.teste_y_x('11')
    Test.reverso('1001001001')
    Test.calc('a*a+(a+a)')
    
    #  deve passar
    Test.enquanto("eqt(a){eqt(a){}}")
    Test.enquanto("eqt(a){}")

    #  deve falhar
    Test.enquanto("eqt(a){eqt(a){}")
    Test.enquanto("eqt(a){et(a){}}")
    Test.enquanto("eqt(){eqt(a){}}")



