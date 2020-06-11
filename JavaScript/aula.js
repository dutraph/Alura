//console.log('Paulo')
//console.log('Bem vindo ao curso')
//let age = 10;
//console.log(age);

//let corSelecionada = null; // Redefinir um valor
//let nome = 'Paulo'; // String literal
//let idade = 25; // Number literal
//let estaAprovado = true; // Boolean
//let sobrenome; // Undefined

// Criando um objeto
let pessoa = {
    nome: 'Paulo',
    idade: 26,
    estaAprovado: true,
    sobrenome: 'Dutra',
    alturaUsuario: 180, 
};

console.log('Nome: '+pessoa.nome);
console.log('idade '+pessoa.idade);

// Arrays

let familia = [29,27];

console.log(familia.length)

//Functions (verbo + Susbstantivo)

let corSite = "azul";
function resetaCor(cor, tonalidade){
    corSite = cor +' '+tonalidade;
};

console.log(corSite);
resetaCor('Verde','escuro');
console.log(corSite);

let nombre = "Pablo";
function mudaNome(novoNome){
    nombre = novoNome;
}

console.log(nombre);
mudaNome('Paulo');
console.log(nombre);

// Tipos de functions
  // Realizar um tarefa e nao devolve nada

function dizerNome(){
    console.log('Thomas')
}
dizerNome();

  // Fazer um calculo ou operacao e retorna algo
function multiplicaPorDois(valor){
    return valor* 2;

}
//console.log(multiplicaPorDois(5)); 

// OU

let result = multiplicaPorDois(5);
console.log(result);



//const alturaUsuario = 180; // const nao permite que a variavel mude
//let pesoUsuario = 99; // let permite que a variavel mude
//let metaUsuario = 85; 
//let nomeUsuario = 'Paulo';

//console.log(   'Nome: ' + nomeUsuario +
//            ' / Peso = ' + pesoUsuario + 
//            ' / Altura = ' + alturaUsuario + 
//            ' / Meta = ' + metaUsuario);

            
//alert ("isso eh um curso de AWS")

