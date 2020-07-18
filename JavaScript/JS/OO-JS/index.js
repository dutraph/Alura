import {Cliente} from "./Cliente.js"
import {ContaCorrente} from "./ContaCorrente.js"

const conta1 = new ContaCorrente( `cliente1`, 1001);
const conta2 = new ContaCorrente(`cliente2`, 1001);
const conta3 = new ContaCorrente(`cliente3`,1001);
const cliente1 = new Cliente(`Ricardo`, 11122233309, 12345567);
const cliente2 = new Cliente(`Alice`, 88822233309, 123455432);
const cliente3 = new Cliente(`Paulo`, 14577110792, 238871772);
conta1.cliente = cliente1;

conta2.cliente = cliente2;

conta3.cliente = cliente3;


// console.log(conta1);
// console.log(conta2);

// conta1.depositar(3000);
// conta1.transferir(1000, conta2);

// console.log(conta1);
// console.log(conta2);
// console.log(`Nosso banco tem `,ContaCorrente.length, `contas ativas...`);

console.log(ContaCorrente.numeroDeConta);