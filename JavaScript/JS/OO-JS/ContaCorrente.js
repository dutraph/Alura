import { Cliente } from "./Cliente.js";

export class ContaCorrente{
  static numeroDeConta = 0;
  //#saldo =0; convençao de campo privado "official"
  // - https://github.com/tc39/proposal-class-fields#private-fields  
    set cliente(novoValor){
      if (novoValor instanceof Cliente){
        this._cliente = novoValor;
    }
  }

    get cliente(){
      return this._cliente;
    }

    get saldo(){
      return this._saldo;
    }

    constructor(cliente, agencia){
      this.cliente = cliente;
      this.agencia = agencia;
      this._saldo = 0; // convençao de campo privado "community"

      ContaCorrente.numeroDeConta += 1;
    }

    transferir(valor, conta){
      const valorSacado = this.sacar(valor);
      conta.depositar(valorSacado);
    }
    sacar(valor){
      if (this._saldo >= valor){
        this._saldo -=valor;
        console.log(`Saque realizado pelo titular ${this.cliente.nome} no valor de: R$${valor}.`)
        return valor;
      }
    }
    depositar(valor){ //early return, testa oque nao queremos primeiro. Obs:. o return nesse caso tem a funçao de break
      if (valor <= 0){
        console.log(`Operaçao nao permitida.\n`)
        console.log(`Tentativa de deposito invalido. Valor negativo.`)
        return;
      }
      console.log(`Deposito no valor de R$${valor}.`)
      console.log(`Operaçao aceita! Valor recebebido R$${valor}.`)
      this._saldo +=valor;
    }
    extrato(){
      console.log(`Seu extrato é de R$${this._saldo}.`)
    }
  }