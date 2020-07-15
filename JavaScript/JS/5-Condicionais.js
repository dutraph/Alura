let listaDeDestinos = new Array(
    ` Salvador`, 
    ` Sao Paulo`, 
    ` Rio de Janeiro`,
    ` Minas Gerais`,
);

function removeDestino(){
    listaDeDestinos.splice(0, 1); // removendo do array, onde 3 é o start e 1 é o num de posiçoes apartir do start a serem deletados.
}
function mostra(valor){
    console.log(valor);
}
const idadeComprador = 18;
const estaAcompanhada = false;
const temPassagem = true;
console.log(`Os destinos possiveis sao ${listaDeDestinos.length}.`);
mostra(listaDeDestinos);

if (idadeComprador >= 18 || estaAcompanhada) {
    console.log('Maior de Idade \n');
    mostra(`Destino ${listaDeDestinos[0]} comprado.\n`);
    removeDestino();
    mostra(`Destinos disponiveis apos a compra.\n\n`)
    mostra(listaDeDestinos);
} else {
    console.log(`Nao pode comprar!`);
    mostra(listaDeDestinos);

}

mostra(`Embarque: \n\n`)
if(idadeComprador >=18 && temPassagem){
    mostra(`Boa viagem!`)
}else{
    mostra(`Nao pode embarcar!`)
}



// function removeDestino(){
//     listaDeDestinos.splice(0, 1); // removendo do array, onde 3 é o start e 1 é o num de posiçoes apartir do start a serem deletados.
// }
// function mostra(valor){
//     console.log(valor);
// }
// const idadeComprador = 19;
// const estaAcompanhada = true;
// console.log(`Os destinos possiveis sao ${listaDeDestinos.length}.`);
// mostra(listaDeDestinos);

// if (idadeComprador >= 18) {
//     console.log('Maior de Idade');
//     mostra(`Destino ${listaDeDestinos[0]} comprado.`);
//     removeDestino();
//     mostra(`Destinos disponiveis apos a compra.`)
//     mostra(listaDeDestinos);
// } else if (estaAcompanhada) {
//     console.log('Esta acompanado, pode comprar');
//     mostra(`Destino ${listaDeDestinos[0]} comprado.`);
//     removeDestino();
//     mostra(`Destinos disponiveis apos a compra.`)
//     mostra(listaDeDestinos);
// } else {
//     console.log(`Nao pode comprar!`);
//     mostra(listaDeDestinos);

// }


