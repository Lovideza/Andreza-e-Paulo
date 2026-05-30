let tarefas = []
function adicionarTarefa(texto) {
    if (texto.trim()==="" || typeof(texto)!=="string"){
        console.log("Tarefa inválida")
    } else {
        tarefas.push({
            texto: texto,
            concluida: false
        })
    }
}
function mostrarTarefas() {
    for (let i = 0; i <= tarefas.length; i++){
        console.log(`${i + 1}. ${tarefas[i].texto} || Concluida: ${tarefas[i].concluida}`)
    }
}
function concluirTarefa(indice) {
    let posicao = indice - 1
    if (posicao >= 0 && posicao < tarefas.length){
        tarefas[i].concluida = true
    }
}

function removerTarefa(params) {
    
}
adicionarTarefa("Estudar JavaScript")
adicionarTarefa("Estudar pra prova")
mostrarTarefas()