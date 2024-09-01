from State import State
class AFD: #AFD = (Q, Σ, δ, q0, F)
    def __init__(self, q: State, w: str):
        self.q = q
        self.w = w

    def run(self):
        if(self.q==None or self.w==None): return False

        for c in list(self.w):
            transition = self.q.transition(c)
            if transition != None:
                qNext = transition.getState()
                print(f'{self.q.getName()} ({c}) -> {qNext.getName()}')
                self.q = qNext
            else:
                print(f'{c} nao pertence ao alfabeto ou nao possui transicao!!')
                return False
            
        return self.print_result()
    
    def print_result(self):
        """ Print and Return True (ok) or False (no ok)"""
        if(self.q.isFinal):
            print(f'Reconheceu: {self.w}')
        else:
            print(f'Não reconheceu: {self.w}')
        return self.q.isFinal

