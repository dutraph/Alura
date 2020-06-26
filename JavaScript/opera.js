// Operadores Aritimetios (matematicos)
// Operadores Atribuicao
// Operadores de Comparacao
// Operadores Logicos
// Operadores Bitwise


//#########################################

// Operadores Aritimetios (matematicos)
// +, -, *, /, **
//let salario = 100;
//console.log(salario + salario)

// ++, -- (INCREMENTAR E DECREMENTO )
//let idade = 10;
//console.log(++idade);
//console.log(idade);


// Operadores Atribuicao += / -=
let valorTeclado = 100;
// valorTeclado = valorTeclado + valorTeclado; eh igual ao de baixo
//valorTeclado += valorTeclado; ou valorTeclado -= valorTeclado;
console.log(valorTeclado);


// Operadores de Comparacao
    // Operadores de Igualdade
        // Igualdade estrita (confiavel)

console.log(1 === 1); //True
console.log('1' === 1); //False

        //Igualdade solta (falho)

console.log(1 == 1); //True
console.log('1' == 1); //True

// Operador Ternario
 // se o cliente tiver 100 pts ou mais eh premium, senao, comum

let pts = 100;
// o tipo vai ser definido por: se pts for maior que 100 ele vai ser do tipo premium senao, comum
let tipo = pts >= 100 ? 'Premium' : 'Comum';
console.log(tipo);

// Operadores Logicos
 // and (&&), or, not

 //And (&&)

//console.log(true && false);
let maiorIdade = true;
let possuiCartTrab = true;
let podeAplicar = maiorIdade && possuiCartTrab;

if (podeAplicar === true ? 
    console.log('Prossiga!') : 
    console.log('Nao pode'));

let nome = 'Paulo'
console.log(nome);