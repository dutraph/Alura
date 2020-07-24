
public class TesteGerente {
	
	public static void main(String[] args) {
		
		Gerente g1 = new Gerente();
		
		g1.setNome("Alexandre Pardal");
		g1.setCpf("4324234234");
		g1.setSalario(10000);
		
		ControleBonificacao controle = new ControleBonificacao();
		
		controle.registra(g1);
		
		System.out.println(g1.getNome());
		
		System.out.println("Seu salario com bonificaçao eh R$"+ (g1.getSalario()+g1.getBonificacao()));
		
		
		Funcionario f1 = new Funcionario();
		
		f1.setNome("Paulo");
		f1.setSalario(4000.0);
		
		controle.registra(f1);
		
		System.out.println(f1.getNome());

		System.out.println("Seu salario com bonificaçao eh R$"+ (f1.getSalario()+f1.getBonificacao()));
	}

}
