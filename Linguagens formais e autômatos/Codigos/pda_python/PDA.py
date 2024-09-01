
class PDA:
    def __init__(self, q):
        self._q = q  # Estado inicial
        self._pilha = ['#']  # Pilha inicial
        self.log = False

    def makeLog(self):
        self.log = True
        
    def run(self, w: str) -> bool:
        return self._run(self._q, w, 0, self._pilha)

    def _run(self, q, w: str, k: int, pilha: list) -> bool:
        transitions = set()

        if k == len(w) and q.isFinal():
            if self.log:
                print(f"{q.getName()}[{k}]: {self._get_pilha(pilha)}")
            self._draw(w, k, transitions)
            return True
        else:
            if k < len(w):
                transitions = self._merge(transitions, q.transitions(w[k], pilha[-1] if pilha else None))
                transitions = self._merge(transitions, q.transitions(w[k], None))
                transitions = self._merge(transitions, q.transitions(None, pilha[-1] if pilha else None))
                transitions = self._merge(transitions, q.transitions(None, None))
                if self.log:
                    print(f"{q.getName()}[{k}]: {self._get_pilha(pilha)}")
                self._draw(w, k, transitions)

            if k == len(w):
                transitions = self._merge(transitions, q.transitions(None, None))
                transitions = self._merge(transitions, q.transitions(None, pilha[-1] if pilha else None))
                if self.log:
                    print(f"{q.getName()}[{k}]: {self._get_pilha(pilha)}")
                self._draw(w, k, transitions)

            if not transitions:
                if self.log:
                    print(f"{q.getName()}[{k}]: {self._get_pilha(pilha)}")
                return self._finish(w, k, transitions)
            else:
                for transition in transitions:
                    edge = transition.getEdge()
                    stack = pilha[:]
                    if edge.getPop() is not None and stack and edge.getPop() == stack[-1]:
                        stack.pop()

                    if edge.getPush() is not None:
                        stack.append(edge.getPush())

                    pos = k
                    if edge.getC() is not None:
                        pos = k + 1

                    result = self._run(transition.getState(), w, pos, stack)
                    if result:
                        return True

                return False

    def _merge(self, transitions1, transitions2):
        return transitions1.union(transitions2)

    def _get_pilha(self, pilha):
        return ''.join(pilha)
    
    def _finish(self, w: str, k: int, transitions: set) -> bool:
        self._draw(w, k, transitions)
        return self._valid(transitions)

    def _valid(self, transitions: set) -> bool:
        if transitions and len(transitions) != 0:
            for i in transitions:
                if i.getState().isFinal():
                    return True
            return False
        else:
            return False

    def _draw(self, w: str, k: int, transitions: set) -> None:
        if self.log:
            print(f"{w[:k]}[", end="")
            c = 0
            for s in transitions:
                c += 1
                print(f"{s.getState().getName()}", end="")
                if c < len(transitions):
                    print(" ", end="")
            print(f"]{w[k:]}")
