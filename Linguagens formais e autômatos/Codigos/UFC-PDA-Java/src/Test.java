import pda.automata.IPDA;
import pda.automata.IState;
import pda.automata.lib.PDA;

public class Test {// PDA = (Q, Σ, δ, q0, F)
	public static void calc(String w) throws Exception {
		/*
        #  E -> T+E
        #  E -> T
        #  T -> F*E
        #  T -> F
        #  F -> a
        #  F -> (E)
		 */
		
        IState q0 = new State("q0");
        IState q1 = new State("q1");
        IState q2 = new State("q2");
        IState qf = new State("qf");

        IState qa = new State("qa");
        IState qb = new State("qb");
        IState qi = new State("qi");
        IState qj = new State("qj");
        IState qm = new State("qm");
        IState qn = new State("qn");
        
        qf.setFinal();

        q0.addTransition(q1, null, null, '$');
        q1.addTransition(q2, null, null, 'E');
        
        //# E -> T+E
        q2.addTransition(qa, null, 'E', 'E');
        qa.addTransition(qb, null, null, '+');
        qb.addTransition(q2, null, null, 'T');


        //# E -> T
        q2.addTransition(q2, null, 'E', 'T');

        //# T -> F*E
        q2.addTransition(qi, null, 'T', 'E');
        qi.addTransition(qj, null, null, '*');
        qj.addTransition(q2, null, null, 'F');

        //# T -> F
        q2.addTransition(q2, null, 'T', 'F');

        //# F -> a
        q2.addTransition(q2, null, 'F', 'a');

        //# F -> (E)
        q2.addTransition(qm, null, 'F', ')');
        qm.addTransition(qn, null, null, 'E');
        qn.addTransition(q2, null, null, '(');

        q2.addTransition(q2, 'a', 'a', null);
        q2.addTransition(q2, '+', '+', null);
        q2.addTransition(q2, '*', '*', null);
        q2.addTransition(q2, '(', '(', null);
        q2.addTransition(q2, ')', ')', null);


        q2.addTransition(qf, null, '$', null);

        IPDA pda = new PDA(q0);
        pda.makeLog();
        Util.checkout(pda.run(w),w);
	}
	public static void reverso(String w) throws Exception {
		/*
		 * L = { ww^R | w in Î£^*={0,1}}
		*/
		IState q1 = new State("q1");
		IState q2 = new State("q2");
		IState q3 = new State("q3");
		IState q4 = new State("q4");
		q1.setFinal(); 
		q4.setFinal();
		
		q1.addTransition(q2, null, null, '$');
		
		q2.addTransition(q2, '0', null, '0');
		q2.addTransition(q2, '1', null, '1');
		q2.addTransition(q3, null, null, null);
		
		q3.addTransition(q3, '0', '0', null);
		q3.addTransition(q3, '1', '1', null);
		
		q3.addTransition(q4, null, '$', null);
		
		// Aqui estamos usando o PDA da nossa biblioteca pda_automata_lib.jar
		// Tente implementar a sua PDAImpl.java
		// Apos isso, troque para: IPDA pda = new PDAImpl(q1);
		IPDA pda = new PDA(q1);
		pda.makeLog();
		Util.checkout(pda.run(w),w);
		System.out.println("*****************************");
	}
    public static void teste_y_x(String w) throws Exception {
        System.out.println("{ w in Σ^* | w é um número binario multiplo de 3}");
        IState q0 = new State("q0");
        IState q1 = new State("q1");
        IState q2 = new State("q2");
        q0.setFinal();

        q0.addTransition(q0, '0', null, null);
        q0.addTransition(q1, '1', null, null);
        q1.addTransition(q0, '1', null, null);
        q1.addTransition(q2, '0', null, null);
        q2.addTransition(q2, '1', null, null);
        q2.addTransition(q1, '0', null, null);

        IPDA pda = new PDA(q0);
        boolean b = pda.run(w);
        Util.checkout(b, w);
    }
    public static void enquanto(String w) throws Exception {

        IState q0 = new State("q0"); // Estado inicial
        IState q1 = new State("q1"); // Estado após empilhar '$'
        IState q2 = new State("q2"); // Estado após reconhecer 'e'
        IState q3 = new State("q3"); // Estado após reconhecer 'q'
        IState q4 = new State("q4"); // Estado após reconhecer 't'
        IState q5 = new State("q5"); // Estado após reconhecer '(a)'
        IState q6 = new State("q6"); // Estado após reconhecer '{'
        IState q7 = new State("q7"); // Estado final após reconhecer '}'
        IState qf = new State("qf"); // Estado final
    
        // Definir estado final
        qf.setFinal();
    
        // Transições do autômato
        // Empilhar o símbolo inicial $
        q0.addTransition(q1, null, null, '$');  // Empilha '$' ao iniciar
    
        // Reconhecer "eqt"
        q1.addTransition(q2, 'e', null, null);  // Reconhecer 'e'
        q2.addTransition(q3, 'q', null, null);  // Reconhecer 'q'
        q3.addTransition(q4, 't', null, null);  // Reconhecer 't'
    
        // Reconhecer "(a)"
        q4.addTransition(q5, '(', null, null);  // Reconhecer '('
        q5.addTransition(q5, 'a', null, 'a');  // Reconhecer 'a' (condição)
        q5.addTransition(q6, ')', 'a', null);  // Reconhecer ')'
    
        // Abrir um bloco '{' e empilhar
        q6.addTransition(q6, '{', null, '{');   // Empilhar '{'
    
        // Reconhecer conteúdo do bloco: 'a', ou novo 'eqt(...)'
        q6.addTransition(q6, 'a', null, null);  // Reconhecer 'a' dentro do bloco
        q6.addTransition(q2, 'e', null, null);  // Reconhecer 'eqt' dentro do bloco (aninhado)
    
        // Fechar o bloco '}' e desempilhar
        q6.addTransition(q7, '}', '{', null);   // Desempilhar '{'
        q7.addTransition(q7, '}', '{', null);   // Desempilhar '{'
    
        // Finalizar ao encontrar $ na pilha após a última transição
        q7.addTransition(qf, null, '$', null);  // Desempilha '$' e vai para o estado final
    
        // Transição de auto-loop para estados que devem permitir repetição sem consumir
        q5.addTransition(q5, 'a', null, null); // Permitir múltiplos 'a'
    
        // Criação do autômato com pilha
        IPDA pda = new PDA(q0);
        // pda.makeLog();
        // Executar o autômato com a entrada fornecida
        Util.checkout(pda.run(w), w);
    }
}
