let exercicios = []

// DOM Elements
const exercicioForm = document.getElementById('exercicioForm')
const exerciciosList = document.getElementById('exerciciosList')
const listaVazia = document.getElementById('listaVazia')
const toast = document.getElementById('toast')
const toastMessage = document.getElementById('toastMessage')

// Erros
const nomeError = document.getElementById('nameError')
const serieError = document.getElementById('serieError')
const repeticoesError = document.getElementById('repeticoesError')

// Filtros
const filtrarTodos = document.getElementById('filtrarTodos')
const filtrarPendentes = document.getElementById('filtrarPendentes')
const filtrarConcluidos = document.getElementById('filtrarConcluidos')

// Contadores dos filtros
const contarTodos = document.getElementById('contarTodos')
const contarPendentes = document.getElementById('contarPendentes')
const contarConcluidos = document.getElementById('contarConcluidos')

// Estatísticas
const totalExercicios = document.getElementById('totalExercicios')
const pendentesExercicios = document.getElementById('pendentesExercicios')
const concluidosExercicios = document.getElementById('concluidosExercicios')

let filtroAtual = "todos"

function init() {
    carregarExercicios()
    vincularEventos()
    renderizarExercicios()
    atualizarStatus()
}

function carregarExercicios() {
    try {
        const salvo = localStorage.getItem("exercicios")
        exercicios = salvo ? JSON.parse(salvo) : []
    } catch (error) {
        exercicios = []
    }
}

function salvarExercicios() {
    try {
        localStorage.setItem("exercicios", JSON.stringify(exercicios))
    } catch (error) {
        showToast("Erro ao salvar exercício", "erro")
    }
}

function vincularEventos() {
    exercicioForm.addEventListener("submit", registrarExercicio)
    filtrarTodos.addEventListener("click", () => { filtroAtual = "todos"; renderizarExercicios() })
    filtrarPendentes.addEventListener("click", () => { filtroAtual = "pendentes"; renderizarExercicios() })
    filtrarConcluidos.addEventListener("click", () => { filtroAtual = "concluidos"; renderizarExercicios() })
}

function registrarExercicio(e) {
    e.preventDefault()

    const nome = document.getElementById("exercicioNome").value.trim()
    const series = Number.parseInt(document.getElementById('numeroSerie').value)
    const repeticoes = Number.parseInt(document.getElementById('repeticoesSerie').value)

    let erro = false

    if (!nome) {
        nomeError.classList.remove("hidden")
        erro = true
    } else {
        nomeError.classList.add("hidden")
    }
    if (!series || series < 1 || series > 20) {
        serieError.classList.remove("hidden")
        erro = true
    } else {
        serieError.classList.add("hidden")
    }
    if (!repeticoes || repeticoes < 1 || repeticoes > 15) {
        repeticoesError.classList.remove("hidden")
        erro = true
    } else {
        repeticoesError.classList.add("hidden")
    }

    if (erro) return

    if (exercicios.some((ex) => ex.nome.toLowerCase() === nome.toLowerCase())) {
        showToast("Já existe um exercício com este nome", "erro")
        return
    }

    const exercicio = {
        id: Date.now(),
        nome,
        series,
        repeticoes,
        criadoEm: new Date().toISOString(),
        concluido: false,
        concluidoEm: null,
    }

    exercicios.push(exercicio)
    salvarExercicios()
    exercicioForm.reset()
    renderizarExercicios()
    atualizarStatus()
    showToast("Exercício adicionado com sucesso!")
}

function concluirExercicio(id) {
    const exercicio = exercicios.find((ex) => ex.id === id)
    if (exercicio && !exercicio.concluido) {
        exercicio.concluido = true
        exercicio.concluidoEm = new Date().toISOString()
        salvarExercicios()
        renderizarExercicios()
        atualizarStatus()
        showToast("Exercício concluído! Parabéns!")
    }
}

function removerExercicio(id) {
    console.log('RemoverExercicio chamado, id:', id)
    exercicios = exercicios.filter((ex) => ex.id !== id)
    salvarExercicios()
    renderizarExercicios()
    atualizarStatus()
    showToast("Exercício removido!")
}

function criarCardExercicio(exercicio) {
    const cardClass = exercicio.concluido ? "bg-green-100 border-green-300" : "bg-yellow-100 border-yellow-300"
    const statusText = exercicio.concluido ? "✅ Concluído" : "⏳ Pendente"
    const completedDate = exercicio.concluidoEm ? `<span class="text-green-700 text-sm block mt-1">Concluído em: ${new Date(exercicio.concluidoEm).toLocaleDateString("pt-BR")}</span>` : ""

    return `
      <div class="border rounded-lg p-4 mb-4 ${cardClass}">
        <div class="flex justify-between items-center">
          <div>
            <h3 class="text-lg font-bold">${exercicio.nome}</h3>
            <div class="text-gray-700 text-sm">Séries: ${exercicio.series} | Repetições: ${exercicio.repeticoes}</div>
            <span class="block mt-1">${statusText}</span>
            ${completedDate}
          </div>
          <div class="flex flex-col gap-2">
            ${!exercicio.concluido ? `<button data-id="${exercicio.id}" class="btn btn-success btn-concluir bg-green-600 text-white px-3 py-1 rounded">Concluir</button>` : ""}
            <button data-id="${exercicio.id}" class="btn btn-danger btn-remover bg-red-600 text-white px-3 py-1 rounded">Remover</button>
          </div>
        </div>
      </div>
    `
}

function renderizarExercicios() {
    let lista = exercicios
    if (filtroAtual === "pendentes") {
        lista = exercicios.filter((ex) => !ex.concluido)
    } else if (filtroAtual === "concluidos") {
        lista = exercicios.filter((ex) => ex.concluido)
    }

    // Atualiza contadores dos filtros
    contarTodos.textContent = exercicios.length
    contarPendentes.textContent = exercicios.filter((ex) => !ex.concluido).length
    contarConcluidos.textContent = exercicios.filter((ex) => ex.concluido).length

    if (lista.length === 0) {
        exerciciosList.classList.add("hidden")
        listaVazia.classList.remove("hidden")
        exerciciosList.innerHTML = ""
    } else {
        exerciciosList.classList.remove("hidden")
        listaVazia.classList.add("hidden")
        exerciciosList.innerHTML = lista.map(criarCardExercicio).join("")
    }

    // Atualiza classes dos botões de filtro
    filtrarTodos.className = filtroAtual === "todos" ? "filter-button-active" : "filter-button"
    filtrarPendentes.className = filtroAtual === "pendentes" ? "filter-button-active" : "filter-button"
    filtrarConcluidos.className = filtroAtual === "concluidos" ? "filter-button-active" : "filter-button"
}

function atualizarStatus() {
    const total = exercicios.length
    const concluidos = exercicios.filter((ex) => ex.concluido).length
    const pendentes = total - concluidos

    totalExercicios.textContent = total
    pendentesExercicios.textContent = pendentes
    concluidosExercicios.textContent = concluidos
}

function showToast(message, type = "sucesso") {
    toastMessage.textContent = message
    toast.classList.remove("opacity-0", "translate-y-full")
    toast.classList.add("opacity-100", "translate-y-0")
    if (type === "erro") {
        toast.classList.add("bg-red-600")
        toast.classList.remove("bg-gray-800")
    } else {
        toast.classList.add("bg-gray-800")
        toast.classList.remove("bg-red-600")
    }
    setTimeout(() => {
        toast.classList.add("opacity-0", "translate-y-full")
        toast.classList.remove("opacity-100", "translate-y-0")
    }, 2500)
}

// Disponibiliza funções globais para os botões funcionarem
window.concluirExercicio = concluirExercicio
window.removerExercicio = removerExercicio

// Delegação de eventos para os botões dinâmicos
document.addEventListener("DOMContentLoaded", function() {
    init();
    exerciciosList.addEventListener('click', function(event) {
        if (event.target.classList.contains('btn-remover')) {
            const id = Number(event.target.dataset.id)
            console.log('Remover clicado, id:', id)
            removerExercicio(id)
        }
        if (event.target.classList.contains('btn-concluir')) {
            const id = Number(event.target.dataset.id)
            concluirExercicio(id)
        }
    })
})