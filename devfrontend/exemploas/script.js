// Obtém referências para os elementos HTML do DOM
const form = document.getElementById('formTarefa'); // Formulário para adicionar tarefas
const tarefaInput = document.getElementById('tarefaInput'); // Campo de entrada de texto
const listaTarefas = document.getElementById('listatarefas') // Lista onde as tarefas são exibidas

// Array que armazena todas as tarefas
let tarefas = []

// Adiciona um evento de escuta ao formulário quando é enviado
form.addEventListener("submit", function(e) {
    e.preventDefault() // Impede o comportamento padrão do formulário (recarregar a página)
    const textoValue = tarefaInput.value.trim(); // Obtém o valor do input e remove espaços em branco

    // Validação: verifica se o campo não está vazio
    if (textoValue === "") {
        alert("Por favor, insira uma tarefa válida");
        return; // Para a execução da função se estiver vazio
    }

    tarefas.push(textoValue); // Adiciona a nova tarefa ao array
    tarefaInput.value = ""; // Limpa o campo de entrada
    atualizarLista(); // Chama a função para atualizar a lista na tela
});

// Função que atualiza a exibição da lista de tarefas na tela
function atualizarLista() {
    listaTarefas.innerHTML = ""; // Limpa todo o conteúdo da lista
    tarefas.forEach((tarefa, index) => { // Percorre cada tarefa no array
        const li = document.createElement("li"); // Cria um novo elemento <li>
        li.textContent = tarefa; // Define o texto da tarefa
        li.innerHTML += `<button onclick="removerTarefa(${index})">Remover</button>`; // Adiciona botão de remover com o índice da tarefa
        listaTarefas.appendChild(li); // Adiciona o <li> à lista na tela
    }); 
}

// Função que remove uma tarefa específica do array
function removerTarefa(index) {
    tarefas.splice(index, 1); // Remove 1 elemento do array na posição do índice
    atualizarLista(); // Atualiza a lista na tela após remover
}