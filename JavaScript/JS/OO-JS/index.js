import {Cliente} from "./Cliente.js";
import {ContaCorrente} from "./ContaCorrente.js";
import {ContaPoupanca} from "./ContaPoupanca.js";
//import {Conta} from "./Conta.js";

const cliente1 = new Cliente(`Ricardo`, 11122233309, 12345567);
const cliente2 = new Cliente(`Alice`, 88822233309, 123455432);
const cliente3 = new Cliente(`Paulo`, 14577110792, 238871772);
const conta1 = new ContaCorrente(cliente1,1001);
const conta2 = new ContaPoupanca(200,cliente2,1001);
//const conta3 = new Conta(`cliente3`,1001);
//conta1.cliente = cliente1;

// conta2.cliente = cliente2;

// conta3.cliente = cliente3;

const conta1Poup = new ContaPoupanca(50,cliente1,1001);

conta1.depositar(1000);
console.log(conta1);
//console.log(conta1Poup);
conta1.sacar(100);
conta1.extrato();
//conta1.teste();

conta1Poup.depositar(150);
conta1Poup.extrato();
conta1Poup.sacar(20);
conta1Poup.extrato();

console.log(conta1Poup);
console.log(conta1);
conta1.transferir(400, conta1Poup);
conta1Poup.extrato();
console.log(conta1Poup);

console.log(conta1);
