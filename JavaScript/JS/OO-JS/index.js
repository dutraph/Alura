import {Cliente} from "./Cliente.js"
import {ContaCorrente} from "./ContaCorrente.js"

const conta1 = new ContaCorrente();
const cliente1 = new Cliente();
cliente1.nome = "Ricardo";
cliente1.cpf = 11122233309;
cliente1.rg = 12345567;
conta1.agencia = 1001;
//conta1.depositar(2000);
conta1.cliente = cliente1;
//console.log(conta1);

const cliente2 = new Cliente();
cliente2.nome = "Alice";
cliente2.cpf = 88822233309;
cliente2.rg = 123455432;

const conta2 = new ContaCorrente();
conta2.cliente =cliente2;
conta2.agencia = 1001;


//conta2.depositar(1999.00);
//console.log(`Nome:`,conta2.cliente.nome,`/ cpf:`,conta2.cliente.cpf);
console.log(conta2.saldo);
//conta1.transferir(50, conta2);