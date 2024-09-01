import java.util.Stack;

import pda.automata.IPDA;
import pda.automata.IState;

// Esta eh a base de codigo que implementa um PDA, especialmente o metodo RUN
public class PDAImpl implements IPDA{
	protected IState q; // Estado inicial do PDA
	protected final Stack<Character> pilha = new Stack<>(); // Pilha de acesso
	protected boolean log = false; // Se tem ou nao log
	
	public PDAImpl(IState q) {
		this.q = q;
		pilha.add('#');
	}

	@SuppressWarnings("unused")
	@Override
	public boolean run(String w) { // TODO
                char[] texto_fonte = w.toCharArray();
		//TODO: Insira seu codigo com a logica do PDA aqui. Pode-se usar iteracao ou recursao
		return false;
	}
	
	@Override
	public void makeLog() {
		//TODO: insira seu codigo aqui caso deseje fazer log. Sugestao log = true;
	}
}
