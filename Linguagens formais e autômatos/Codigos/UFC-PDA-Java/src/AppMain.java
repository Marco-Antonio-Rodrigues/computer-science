public class AppMain { // PDA = (Q, Σ, δ, {qi}, F)

	public static void main(String[] args) throws Exception {
	    //Test.teste_y_x("00001111");
	    //Test.reverso("1001001001");
	    // Test.calc("a*a+(a+a)");

		// deve passar
		Test.enquanto("eqt(a){eqt(a){}}");
		Test.enquanto("eqt(a){}");

		// deve falhar
		Test.enquanto("eqt(a){eqt(a){}");
		Test.enquanto("eqt(a){et(a){}}");
		Test.enquanto("eqt(){eqt(a){}}");
	}
}
