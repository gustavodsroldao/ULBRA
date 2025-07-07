let exercicios = []
let filtro = []

// Manipulando DOM
const exercicioForm = document.getElementById('exercicioForm')
const exerciciosList = document.getElementById('exerciciosList')
const listaVazia = document.getElementById('listaVazia')
const toast = document.getElementById('toat')
const toastMessage = document.getElementById('toastMessage')

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
    exercicioForm.addEventListener("submit", registrarExercicio)

    // Filtros
    document.getElementById("filtrarTodos").addEventListener("click", () => setFilter("all"))   
    document.getElementById("filtrarPendetes").addEventListener("click", () => setFilter("pendentes"))   
    document.getElementById("filtrarConcluidos").addEventListener("click", () => setFilter("concluidos"))   

}

function registrarExercicio(e) {
    e.preventDefault()

    // Campos do form
    const exercicioNome = document.getElementById("exercicioNome").value.trim()
    const numeroSerie = Number.parseInt(document.getElementById('numeroSerie').value)
    const repeticoesSerie = Number.parseInt(document.getElementById('repeticoesSerie').value)

    // verificar duplicatas
    if (exercicios.some((ex) => ex.nome.toLowerCase() === name.toLowerCase())) {
        showToast("Já existe um exercício com este nome", "error")
        return
    }

    const exercicio = {
        id: Date.now(),
        nome,
        series,
        repeticoesSerie,
        criadoEm: new Date.now().toISOString(),
        concluidoEm: null,
    }

    exercicios.push(exercicio)
    salvarExercicios()
    limparFormulario()
    showToast("Exercicio adicionado com sucesso!")
}

// limpar form
function limparFormulario() {
    document.getElementById("exercicioNome").reset()
}

function concluirExercicio() {
    const exercicio = exercicios.find((ex) => ex.id === id)
    if (exercicio && !exercicio.completado) {
        exercicio.completado = true,
        exercicio.completadoEm = new Date.toISOString()
        salvarExercicios()
        carregarExercicios()
        atualizarStatus()
        showToast("Exercício concluído! Parabéns!")
    }
}





