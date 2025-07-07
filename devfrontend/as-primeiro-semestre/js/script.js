let exercicios = []
let filtro = []

// Manipulando DOM
const exercicioForm = document.getElementById('exercicioForm')
const exerciciosList = document.getElementById('exerciciosList')
const listaVazia = document.getElementById('listaVazia')
const toast = document.getElementById('toat')
const toastMessage = document.getElementById('toastMessage')

// Campos do form
const exercicioNome = document.getElementById('exercicioNome')
const numeroSerie = document.getElementById('numeroSerie')
const repeticoesSerie = document.getElementById('repeticoesSerie')

// Erros
const nomeError = document.getElementById('nomeError')
const serieError = document.getElementById('serieError')
const repeticoesError = document.getElementById('repeticoesError')

// Filtros
const filtrarTodos = document.getElementById('filtrarTodos')
const filtrarPendentes = document.getElementById('filtrarPendentes')
const filtrarConcluidos = document.getElementById('filtrarConcluidos')

// Exibição das estastísticas

const totalExercicios = document.getElementById('totalExercicios')
const pendentesExercicios = document.getElementById('pendentesExercicios')
const concluidosExercicios = document.getElementById('concluidosExercicios')

function init() {
    carregarExercicios()
    salvarExercicios()
    demo()
}

function carregarExercicios() {
    try {
        const salvo = localStorage.get("exercicios")
        exercicios = saved ? JSON.parse(saved) : []
    } catch (error) {
        alert("Erro ao carregar exercícios", error)
        exercicios = []
    }
}

function salvarExercicios() {
    try {
        const salvar = localStorage.setItem("exercicios", JSON.stringify("exercicios"))
    } catch (error) {
        alert("Erro ao salvar exercício", error)
    }
}

function demo() {
    if (exercicios === 0) {
        const demo = [
            { nome: "Flexão de braço", series: 3, repeticoes: 12},
            { nome: "Agachamento", series: 3, repeticoes: 15},
            { nome: "Prancha", series: 3, repeticoes: 4}
        ]

        demo.forEach((ex) => {
            exercicios.push({
                id: Math.random(),
                nome: ex.nome,
                series: ex.series,
                repeticoes: ex.repeticoes,
                concluido: false,
                criadoEm: new Date().toISOString(),
                concluidoEm: null
            })
        })

        salvarExercicios()
    }
}

function vincularEventos() {
    // Vinculando form
    exercicioForm.addEventListener("submit", handleSubmit)

    // Validando em real time
    exercicioNome.addEventListener("input", () => validateForm("nome"))
    numeroSerie.addEventListener("input", () => validateForm("serie"))
    repeticoesSerie.addEventListener("input", () => validateForm("repeticoes"))

    // Filtros
    document.getElementById("filtrarTodos").addEventListener("click", () => setFilter("all"))   
    document.getElementById("filtrarPendetes").addEventListener("click", () => setFilter("pendentes"))   
    document.getElementById("filtrarConcluidos").addEventListener("click", () => setFilter("concluidos"))   
    
}





