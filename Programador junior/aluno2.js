let alunos = []

function adicionarAluno(nome, nota) {
    if (nome.trim() == "" || typeof(nome) !== "string"){
        console.log("Nome inválido")
    } else if (typeof(nota) !== "number" || nota < 0 || nota > 10){
        console.log("Nota inválida")
    } else {
       alunos.push({
        "nome": nome,
        "nota": nota
       }) 
    }
}
function mostrarAlunos() {
    for(let i = 0; i < alunos.length; i++){
        console.log(`${i + 1}. ${alunos[i].nome}: ${alunos[i].nota}`)
    }
}
function resultadoAluno() {
    for(let i = 0; i < alunos.length; i++){
        if (alunos[i].nota >= 7){
            console.log(`${alunos[i].nome}: Aprovado`)
        } else {
            console.log(`${alunos[i].nome}: Reprovado`)
        }
    }
}
adicionarAluno("Paulo", 8)
adicionarAluno("Maria", 5)
mostrarAlunos()
resultadoAluno()