// Criar um sistema que:

//Permite adicionar números em um array
//Mostra todos os números
//Mostra:
//Quantos números existem
//A soma total
//O maior número

let numeros = [];

// adiciona um número no array
function adicionarNumero(num) {
    numeros.push(num);
}

// mostra todos os números
function mostrarNumeros() {
    console.log("Números:", numeros);
}

// mostra estatísticas
function mostrarEstatisticas() {
    console.log(`Quantidade: ${numeros.length}`);

    let soma = 0;
    let maior = numeros[0];

    for (let i = 0; i < numeros.length; i++){
        soma += numeros[i];

        if (numeros[i] > maior){
            maior = numeros[i];
        }
    }

    console.log(`Soma: ${soma}`);
    console.log(`Maior: ${maior}`);
}

// testes
adicionarNumero(7);
adicionarNumero(18);
adicionarNumero(1);

mostrarNumeros();
mostrarEstatisticas();