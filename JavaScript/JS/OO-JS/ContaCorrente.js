import { Cliente } from "./Cliente.js";

export class ContaCorrente{
    agencia;
    _cliente;
    //#saldo =0; convençao de campo privado "official" - https://github.com/tc39/proposal-class-fields#private-fields
    _saldo = 0; // convençao de campo privado "community"

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
        console.log(`Tentativa de deposito invalido no valor deve ser positivo.`)
        console.log(`Operaçao nao permitida.\n`)
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