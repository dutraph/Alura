console.log(`Trabalhando com Listas`);
/*
let listaDestinos = [`salvador`, `Sao Paulo`, `Rio de Janeiro`];

console.log(destinos[0]);
*/
// OU

let listaDeDestinos = new Array(
    `Salvador`, 
    `Sao Paulo`, 
    `Rio de Janeiro`,
);

console.log(`Os destinos possiveis sao ${listaDeDestinos.length}: ${listaDeDestinos}`);

console.log(listaDeDestinos);
listaDeDestinos.push(`Minas Gerais`)
console.log(listaDeDestinos);
listaDeDestinos.splice(3,1); // removendo do array, onde 3 é o start e 1 é o num de posiçoes apartir do start a serem deletados.

console.log(listaDeDestinos);
