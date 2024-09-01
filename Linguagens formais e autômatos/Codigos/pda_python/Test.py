from State import State
from Util import Util
from PDA import PDA
class Test:
    @staticmethod
    def calc(w):
        #  E -> T+E
        #  E -> T
        #  T -> F*E
        #  T -> F
        #  F -> a
        #  F -> (E)
        q0 = State('q0')
        q1 = State('q1')
        q2 = State('q2')
        qf = State('qf')

        qa = State('qa')
        qb = State('qb')
        qi = State('qi')
        qj = State('qj')
        qm = State('qm')
        qn = State('qn')
        
        qf.setFinal()

        q0.addTransition(q1, None, None, '$')
        q1.addTransition(q2, None, None, 'E')
        
        # E -> T+E
        q2.addTransition(qa, None, 'E', 'E')
        qa.addTransition(qb, None, None, '+')
        qb.addTransition(q2, None, None, 'T')


        # E -> T
        q2.addTransition(q2, None, 'E', 'T')

        # T -> F*E
        q2.addTransition(qi, None, 'T', 'E')
        qi.addTransition(qj, None, None, '*')
        qj.addTransition(q2, None, None, 'F')

        # T -> F
        q2.addTransition(q2, None, 'T', 'F')

        # F -> a
        q2.addTransition(q2, None, 'F', 'a')

        # F -> (E)
        q2.addTransition(qm, None, 'F', ')')
        qm.addTransition(qn, None, None, 'E')
        qn.addTransition(q2, None, None, '(')

        q2.addTransition(q2, 'a', 'a', None)
        q2.addTransition(q2, '+', '+', None)
        q2.addTransition(q2, '*', '*', None)
        q2.addTransition(q2, '(', '(', None)
        q2.addTransition(q2, ')', ')', None)


        q2.addTransition(qf, None, '$', None)

        pda = PDA(q0)
        # pda.makeLog()
        Util.checkout(pda.run(w),w)

    @staticmethod
    def teste_y_x(w):
        print("{ w in Σ^* | w é um número binario multiplo de 3}")
        q0 = State('q0')
        q1 = State('q1')
        q2 = State('q2')
        q0.setFinal()

        q0.addTransition(q0, '0', None, None)
        q0.addTransition(q1, '1', None, None)
        q1.addTransition(q0, '1', None, None)
        q1.addTransition(q2, '0', None, None)
        q2.addTransition(q2, '1', None, None)
        q2.addTransition(q1, '0', None, None)

        pda = PDA(q0)
        # pda.makeLog()
        b = pda.run(w)
        Util.checkout(b, w)

    @staticmethod
    def reverso(w): #L = { ww^R | w in Σ^*={0,1}}
        q1 = State('q1')
        q2 = State('q2')
        q3 = State('q3')
        q4 = State('q4')
        q4.setFinal()
        
        q1.addTransition(q2, None, None, '$')	
        q2.addTransition(q2, '0', None, '0')
        q2.addTransition(q2, '1', None, '1')
        q2.addTransition(q3, None, None, None)
        q3.addTransition(q3, '0', '0', None)
        q3.addTransition(q3, '1', '1', None)
        q3.addTransition(q4, None, '$', None)

        pda = PDA(q1)
        b = pda.run(w)
        Util.checkout(b,w)
    @staticmethod    
    def enquanto(w: str) -> None:
        q0 = State("q0")  # Estado inicial
        q1 = State("q1")  # Estado após empilhar '$'
        q2 = State("q2")  # Estado após reconhecer 'e'
        q3 = State("q3")  # Estado após reconhecer 'q'
        q4 = State("q4")  # Estado após reconhecer 't'
        q5 = State("q5")  # Estado após reconhecer '(a)'
        q6 = State("q6")  # Estado após reconhecer '{'
        q7 = State("q7")  # Estado final após reconhecer '}'
        qf = State("qf")  # Estado final

        # Definir estado final
        qf.setFinal()

        # Transições do autômato
        q0.addTransition(q1, None, None, '$')  # Empilha '$' ao iniciar
        
        # Reconhecer "eqt"
        q1.addTransition(q2, 'e', None, None)  # Reconhecer 'e'
        q2.addTransition(q3, 'q', None, None)  # Reconhecer 'q'
        q3.addTransition(q4, 't', None, None)  # Reconhecer 't'

        # Reconhecer "(a)"
        q4.addTransition(q5, '(', None, None)  # Reconhecer '('
        q5.addTransition(q5, 'a', None, 'a')  # Reconhecer 'a' (condição)
        q5.addTransition(q6, ')', 'a', None)  # Reconhecer ')'

        # Abrir um bloco '{' e empilhar
        q6.addTransition(q6, '{', None, '{')   # Empilhar '{'
        
        # Reconhecer conteúdo do bloco: 'a', ou novo 'eqt(...)'
        q6.addTransition(q6, 'a', None, None)  # Reconhecer 'a' dentro do bloco
        q6.addTransition(q2, 'e', None, None)  # Reconhecer 'eqt' dentro do bloco (aninhado)

        # Fechar o bloco '}' e desempilhar
        q6.addTransition(q7, '}', '{', None)   # Desempilhar '{'
        q7.addTransition(q7, '}', '{', None)   # Desempilhar '{'

        # Finalizar ao encontrar $ na pilha após a última transição
        q7.addTransition(qf, None, '$', None)  # Desempilha '$' e vai para o estado final

        # Transição de auto-loop para estados que devem permitir repetição sem consumir
        q5.addTransition(q5, 'a', None, None)  # Permitir múltiplos 'a'

        pda = PDA(q0)
        # pda.makeLog()
        Util.checkout(pda.run(w),w)