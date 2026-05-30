let primos = []

function isPrimo(num) {
    let contador = 0;

    for (let i = 1; i <= num; i++){
        if (num % i === 0){
            contador++;
        }
    }

    return contador === 2;
}


for (let num = 1; num <= 100; num++){
    if (isPrimo(num)){
        primos.push(num);
    }
}
console.log(primos)
console.log(`Existem ${primos.length} números primos de 1 até 100`)