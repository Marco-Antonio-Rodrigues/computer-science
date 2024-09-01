# .\.venv\Scripts\python.exe -m pip install readchar
from State import State
from AFD import AFD

def teste_y_x(w: str):
    print("{ w in Σ^* | w é um número binario multiplo de 3}")
    q0 = State('q0')
    q1 = State('q1')
    q2 = State('q2')
    q0.setFinal()

    q0.addTransition(q0, '0')
    q0.addTransition(q1, '1')

    q1.addTransition(q0, '1')
    q1.addTransition(q2, '0')

    q2.addTransition(q2, '1')
    q2.addTransition(q1, '0')

    mt = AFD(q0, w)
    mt.run()

if __name__ == "__main__": 
    teste_y_x('00001111')
