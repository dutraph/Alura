let listaDeDestinos = new Array(
    `Salvador`, 
    `Sao Paulo`, 
    `Rio de Janeiro`,
    `Minas Gerais`,
);

function removeDestino(n){
    listaDeDestinos.splice(n, 1); 
}
function mostra(valor){
    console.log(valor);
}
const idadeComprador = 17;
const estaAcompanhada = false;
let temPassagem = false;
const destino = 'Salvador';
let msg = " "
let destinoExiste = false;
console.log(`\n Os destinos possiveis sao ${listaDeDestinos.length}.`);
mostra(listaDeDestinos);

const podeComprar = (idadeComprador >= 18 || estaAcompanhada); 
let contador = 0;
while (contador < listaDeDestinos.length){
    if (listaDeDestinos[contador] == destino){
        destinoExiste = true; 
        break;        
    }else { 
        destinoExiste = false;        
    }
    contador++;  
}

if (podeComprar && destinoExiste){
    console.log('Boa Viagem!')
}else {
    console.log('Tivemos um erro!! Volte ao posto de compra!')
}

// for (var contador = 0; contador < listaDeDestinos.length; contador++){
//     if (listaDeDestinos[contador] == destino){
//         console.log('Destino Encontrado.')
//         break;
//     }
// }
/*{
    console.log('Liberado.');
    mostra(`Destino ${listaDeDestinos[0]} comprado.\n`);
    removeDestino(0);
    temPassagem = true;
    mostra(`Destinos disponiveis apos a compra.`)
    mostra(listaDeDestinos);
} else {
    console.log(`\n Nao pode comprar!`);
    temPassagem = false;
    mostra(listaDeDestinos);
}

mostra(`\n Embarque: \n`)
if((idadeComprador >=18 && temPassagem) || estaAcompanhada) {
    mostra(`Boa viagem!`)
}else{
    mostra(`Nao pode embarcar!`)
}*/