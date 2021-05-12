function getCsrfToken(){
    const csrfToken = document.cookie.split('=')[1];
    return csrfToken;
}

function getCaracters(){
    const caracters = document.getElementById("caracters").value
    return caracters;
}

function convertToJson(){
    const json = {
        "caracters": getCaracters()
    }
    return JSON.stringify(json)
}

function treatResponse(response){
    let words = document.getElementById("words")
    if(response.words.length > 0) {
        words.innerHTML = response.words
    }else{
         words.innerHTML = "Desculpe, nenhuma palavra encontrada."
    }
}

function getAllWords(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            let response = JSON.parse(xhttp.responseText) // When receiving data from a web server, the data is always a string.
            treatResponse(response)                       // JSON.parse() transforma a string em JavaScript object
        }
    }
    xhttp.open("POST", "http://localhost:8000", true);
    xhttp.setRequestHeader("X-CSRFToken", getCsrfToken());
    xhttp.setRequestHeader("Content-type", "application/json"); // mandando múltiplos headers
    xhttp.setRequestHeader("Accept", "application/json")
    xhttp.send(convertToJson());
    //xhttp.open("GET", "http://localhost:8000/possible_words?caracters=Olá mundo", true);
    //xhttp.send();
    //é possível passar informações por um get, como no exemplo acima. possible_words é a rota, caracters é a chave e Olá mundo o valor
    //é possível passar diversar chaves e valores, na view é possível pegar cada uma.
}
