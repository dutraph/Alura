
public class TesteFuncionario {

	public static void main(String[] args) {
		
		Funcionario paulo = new Funcionario();
		
		paulo.setNome("Paulo Dutra");
		paulo.setCpf("1513454543");
		paulo.setSalario(5000);
		
		System.out.println(paulo.getNome());
		System.out.println(paulo.getCpf());
		System.out.println(paulo.getSalario());
		
		System.out.println("Boni " + paulo.getBonificacao());

		
	}

}
