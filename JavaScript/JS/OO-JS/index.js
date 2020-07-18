import {Cliente} from "./Cliente.js";
import {ContaCorrente} from "./ContaCorrente.js";
import {ContaPoupanca} from "./ContaPoupanca.js";
import {Conta} from "./Conta.js";
const conta1 = new Conta( 0,`cliente1`, 1001);
const conta2 = new Conta(`cliente2`, 1001);
const conta3 = new Conta(`cliente3`,1001);
const cliente1 = new Cliente(`Ricardo`, 11122233309, 12345567);
const cliente2 = new Cliente(`Alice`, 88822233309, 123455432);
const cliente3 = new Cliente(`Paulo`, 14577110792, 238871772);
conta1.cliente = cliente1;

conta2.cliente = cliente2;

conta3.cliente = cliente3;

const contaPoupanca = new Conta(50, cliente1, 1001);

conta1.depositar(10000);

conta1.extrato();

contaPoupanca.extrato();
console.log(contaPoupanca);
console.log(conta1);