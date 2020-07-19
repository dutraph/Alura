import { Conta } from "./Conta.js";

export class ContaCorrente extends Conta{
  static numeroDeConta = 0;
  constructor(cliente,agencia){
    super (0,cliente,agencia);
    ContaCorrente.numeroDeConta += 1;
  }
  teste(){
    super.teste();
    console.log('teste na classe conta corrente!');
  }

  //Sobreescreve o comportamento de sacar da class mãe Conta
  sacar(valor){
    let taxa = 1.1
    return this._sacar(valor,taxa);
   
  }
}