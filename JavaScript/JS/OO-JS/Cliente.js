export class Cliente{    
    get rg(){
      this._rg;
      return this._rg;
    }
    get cpf(){
      this._cpf;
      return this._cpf;
    }

    constructor(nome, cpf, rg){ //esses parametros sao para entrar no new Cliente(nome, cpf, rg)
      this.nome = nome;
      this._cpf = cpf;
      this._rg = rg;
    }


  }