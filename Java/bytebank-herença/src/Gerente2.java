public class Gerente2 extends Funcionario{
	

	private int senha; // Declaramos o atributo senha aqui na Classe gerente 
					   // pq ele so pertence a Classe Gerente.
	
	
	public boolean setSenha(int senha) {
		if(senha <= 0) {
			System.out.println("Senha invalida!");
			return false;
		}else {
		this.senha = senha;
		return true;
		}
	}
	public boolean autentica(int senha) {
		if(this.senha == senha) {
			System.out.println("Acesso liberado!");
			return true;
			
		}else {
			System.out.println("Senha incorreta");
			return false;
		}
	}
	
	 // Nao usamos o this quando o atributo esta na classe mae.
	 // Estamos chamando tambem os medodos getBonificaçao e getSalario da classe mae, 
	 // para nao repetirmos codigo e pq eles sao privados.
	 // Se fossem protected poderiamos usar os atributos com o super diretamente.
	public double getBonificacao() {
		System.out.println("Metodo do gerente2 OK!");
		return super.getBonificacao() + super.getSalario();
	}													

}


