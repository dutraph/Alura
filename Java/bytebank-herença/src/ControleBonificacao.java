// CLASSE PARA ATRIBUIR A BONIFICAÇAO AO FUNCIONARIO OU GERENTE

public class ControleBonificacao {

	private double soma;

	public void registra(Gerente gerente) {
		double boni = gerente.getBonificacao();
		
		this.soma += boni;
	}
	
	public void registra(Funcionario funcionario) {
		double boni = funcionario.getBonificacao();
		this.soma = boni;
	}
	public double getSoma() {
		return this.soma;
	}
}
