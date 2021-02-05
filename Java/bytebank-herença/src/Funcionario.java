public class Funcionario{
	
	private String nome;
	private String cpf;
	private double salario; //Deixamos private e usamos o getter na classe filho.
	//protected double salario; //Protected esta visivel para a classe filho, porem nao eh usual.
	private static int totalDeContas;
	
	public Funcionario(/*String nome, String cpf, double salario */) {
//		Funcionario.totalDeContas++;
//		setNome(nome);
//		setCpf(cpf);
//		setSalario(salario);
	}
	
	public double getBonificacao() {
		System.out.println("Metodo Funcionario padrao OK!");
		return getSalario() * 0.05;
	}
	
	public String getNome() {
		return this.nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getCpf() {
		return this.cpf;
	}
	public void setCpf(String cpf) {
		this.cpf = cpf;
	}
	public double getSalario() {
		return this.salario;
	}
	public void setSalario(double salario) {
		this.salario = salario;
	}

	public static int getTotalDeContas() {
		return Funcionario.totalDeContas;
	}
}


