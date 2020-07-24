public class Gerente extends Funcionario{
	

	private int senha; // Declaramos o atributo senha aqui na Classe gerente 
					   // pq ele so pertence a Classe Gerente.
	

	public boolean autentica(int senha) {
		if(this.senha == senha) {
			return true;
			
		}else {
			return false;
		}
	}
	
	 // Nao usamos o this quando o atributo esta na classe mae.
	 // Estamos chamando tambem os medodos getBonificaçao e getSalario da classe mae, 
	 // para nao repetirmos codigo e pq eles sao privados.
	 // Se fossem protected poderiamos usar os atributos com o super diretamente.
	public double getBonificacao() {
		return super.getBonificacao() + super.getSalario();
	}													

}


