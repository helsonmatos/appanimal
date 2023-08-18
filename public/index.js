async function carregarAnimais(){
    const reposta = await axios.get('http://127.0.0.1:8000/animais')
    
    const animais = reposta.data

    const lista = document.getElementById('lista-animais')

    animais.forEach(animal => {
        const item = document.createElement('li')
        item.innerHTML = animal.nome
        lista.appendChild(item)
    });
    
}

function manipularFormulario(){
    const form_animal = document.getElementById('form-animal')
    const input_nome = document.getElementById('nome')
    
    form_animal.onsubmit = async (event)=> {
        event.preventDefault()
        const nome_animal = input_nome.value

        await axios.post('http://127.0.0.1:8000/animais', {
            id: 0,
            nome: nome_animal,
            idade: 2,
            sexo: 'macho',
            cor: 'branco'
        })
    }
    
}

function app(){
    console.log("app iniciado")
    carregarAnimais()
    manipularFormulario()
}

app = app()