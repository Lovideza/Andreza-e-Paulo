let notas = []
function adicionarNota(nota) {
    if (nota >= 0 && nota <= 10){
    notas.push(nota)
    } else {
        console.log("Nota inválida")
    }
}
function mostrarNotas() {
    console.log(notas)
}
function estatisticas() {
    let soma = 0;
    let maior = notas[0];
    let menor = notas[0];

    for (let i = 0; i < notas.length; i++){
        soma += notas[i];

        if (notas[i] > maior){
            maior = notas[i];
        }

        if (notas[i] < menor){
            menor = notas[i];
        }
    }

    let media = soma / notas.length;

    console.log(`Média: ${media}`);
    console.log(`Maior: ${maior}`);
    console.log(`Menor: ${menor}`);

    if (media >= 7){
        console.log("Condição: Aprovado");
    } else if (media >= 5){
        console.log("Condição: Recuperação");
    } else {
        console.log("Condição: Reprovado");
    }
}

adicionarNotas(8)
adicionarNotas(7)
adicionarNotas(6)
mostrarNotas()
estatisticas()