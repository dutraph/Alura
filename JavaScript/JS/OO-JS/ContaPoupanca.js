import { Conta } from "./Conta.js";

export class ContaPoupanca extends Conta{
    constructor(saldoInicial,cliente,agencia){ 
      super (saldoInicial,cliente,agencia);  
    }
    extrato(){
      console.log(`O extrato da conta poupança é: R$${this._saldo}.`)
    }
}