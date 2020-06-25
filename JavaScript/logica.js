var tanque = 40;
var caminhoComGasolina = 480;
var caminhoComAlcool = 600;
var consumoGasolina = caminhoComGasolina/tanque;
var consumoAlcool = caminhoComAlcool/tanque;

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

