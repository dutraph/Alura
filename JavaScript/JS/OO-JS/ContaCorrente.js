import { Cliente } from "./Cliente.js";
import { Conta } from "./Conta.js";

export class ContaCorrente extends Conta{
  static numeroDeConta = 0;
  constructor(cliente,agencia){
    super (cliente,agencia);
    ContaCorrente.numeroDeConta += 1;
  }
}