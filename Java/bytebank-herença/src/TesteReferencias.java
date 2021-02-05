

public class TesteReferencias {

	public static void main(String[] args) {
		
//	 	Gerente gerente = new Gerente();
		// OU ainda podemos criar  como no EX:. 1
		// Porem o EX:. 1 eh a mesma coisa que o EX:. 2, o compilador apenas olha referencia a esquerda. 
		// No caso abaixo "Funcionario"
//		Funcionario gerente1 = new Gerente(); // EX:. 1
//		Funcionario gerente2 = new Funcionario(); // EX:. 2
		
		
		
		Gerente g1 = new Gerente();
		g1.setNome("Paulo");
		g1.setSalario(5000.0);
		
		ControleBonificacao controle = new ControleBonificacao();
		
		controle.registra(g1);
		
		System.out.println(controle.getSoma());
		
		
		Funcionario f1 = new Funcionario();
		f1.setNome("Joao");
		f1.setSalario(5000);
		controle.registra(f1);
		
		System.out.println(controle.getSoma());
		
	}

}
