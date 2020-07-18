export class Conta{
  constructor(saldoInicial,cliente,agencia){
    this._saldo = saldoInicial;
    this._cliente = cliente;
    this._agencia = agencia;
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
    console.log(`O extrato da poupança é: R$${this._saldo}.`)
  }
}