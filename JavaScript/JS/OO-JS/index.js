class Cliente{
  nome;
  cpf;
  rg;
}

class ContaCorrente{
  agencia;
  saldo;
  deposito;
  saque;
  extrato;
  transferencia;
}

const cliente1 = new Cliente();

cliente1.nome = "Ricardo";
cliente1.rg = 12345567;
cliente1.cpf = 11122233309;
// cliente1.agencia = 1001;
// cliente1.saldo = 0;


const cliente2 = new Cliente();
cliente2.nome = "Alice";
cliente2.cpf = 88822233309;
cliente2.rg = 123455432;
// cliente2.agencia = 1001;
// cliente2.saldo = 0;

const contaCorrenteRicardo = new ContaCorrente();
contaCorrenteRicardo.saldo = 0;
contaCorrenteRicardo.agencia = 1001;
contaCorrenteRicardo.deposito 

console.log(cliente1);
console.log(cliente2);