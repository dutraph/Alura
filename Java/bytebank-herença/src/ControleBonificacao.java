// CLASSE PARA ATRIBUIR A BONIFICAÇAO À MAIS DE UM GRUPO DE FUNCIONARIO.

public class ControleBonificacao {

	private double soma;

//	public void registra(Gerente gerente) {
//		double boni = gerente.getBonificacao();
//		
//		this.soma += boni;
//	}
//	
//	
//	public void registra (EditorDeVideo editor) {
//		double boni = editor.getBonificacao();
//		this.soma += boni;
//		
//	}
//	
	
	// APENAS PRECISAMOS DE UM METODO REFERENCIANDO A CLASSE MÃE.
	public void registra(Funcionario f) { // ISSO FUNCIONA POR CAUSA DA REFERENCIA Funcionario 
		double boni = f.getBonificacao(); // QUANDO USAR O OBJETO Gerente() por exemplo, VAI RETORNAR O getBonicicacao da class Gerente.
		this.soma += boni;
	}
	public double getSoma() {
		return this.soma;
	}
}
