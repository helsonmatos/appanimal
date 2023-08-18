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
}

function app(){
    console.log("app iniciado")
    carregarAnimais()
}

app = app()