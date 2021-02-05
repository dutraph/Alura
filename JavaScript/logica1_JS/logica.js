let tanque = 40;
let caminhoComGasolina = 480;
let caminhoComAlcool = 600;
let consumoGasolina = caminhoComGasolina/tanque;
let consumoAlcool = caminhoComAlcool/tanque;

function pulaLinha() {
    document.write("<br><br>");
}
function mostra(conteudo) {
    document.write(conteudo) ;
    pulaLinha();
}
pulaLinha();
mostra('O consumo com gasolina é: ' + consumoGasolina + " Km/Litros");
mostra('O consumo com alcool é: ' + consumoAlcool + " Km/Litros");
    if (consumoAlcool < consumoGasolina ? 
        mostra('Melhor usar Gasolina') : 
        mostra('Melhor usar alcool'));

