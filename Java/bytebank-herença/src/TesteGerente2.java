
public class TesteGerente2 {

	public static void main(String[] args) {
		
		Gerente2 paulo = new Gerente2();
		
		paulo.setNome("Paulo Dutra");
		paulo.setCpf("1513454543");
		paulo.setSalario(5000);
		
		System.out.println(paulo.getNome());
		System.out.println(paulo.getCpf());
		System.out.println(paulo.getSalario());
		
		System.out.println("Boni " + paulo.getBonificacao());

		
	}

}
