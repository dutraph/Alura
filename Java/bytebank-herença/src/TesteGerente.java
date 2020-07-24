
public class TesteGerente {
	
	public static void main(String[] args) {
		
		Gerente g1 = new Gerente();
		g1.setNome("Alexandre");
		g1.setSalario(10000); // A bonificação do gerente é o dobro do salario 
		
		g1.setSenha(-265344);
		
		g1.autentica(123123); // Aqui posso fazer isso pois usei a referencia Gerente a esquerda.
		
		Funcionario g2 = new Gerente();
		
		g2.setNome("Jonas");
		//g2.autentica(123123);  // Aqui não consigo fazer isso pois usando a referencia Funcionario,
								 // ele nao enxerga o método autentica que usa o atributo senha
		g2.setSalario(2000);
		System.out.println(g2.getSalario());
		g2.getBonificacao();
		
		
		Funcionario f1 = new Funcionario();
		f1.setNome("Paulo");
		f1.setSalario(4000.0); // R$200,00(5% de bonif.) 
		

		
		EditorDeVideo ev = new EditorDeVideo();
		ev.setNome("Gaveta");
		ev.setSalario(5000.0); //  R$250,00(5% de bonif.) + R$100,00 = R$350,00 
		
		Funcionario d = new Designer();
		d.setSalario(2000);
		
		
		ControleBonificacao controle = new ControleBonificacao();

		
		controle.registra(g1);
		controle.registra(f1);
		controle.registra(ev);
		controle.registra(d);
	
		System.out.println("A soma de todas as bonificações é: R$"+controle.getSoma());
		
	}

}
