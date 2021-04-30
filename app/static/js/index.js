function getCsrfToken(){
    const csrfToken = document.cookie.split('=')[1];
    return csrfToken;
}

function getCaracters(){
    const caracters = document.getElementById("caracters").value
    return caracters;
}

function getAllWords(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            document.getElementById("words").innerHTML = xhttp.responseText;
            console.log(xhttp.responseText)
        }
    }
    //xhttp.open("GET", "http://localhost:8000/possible_words?caracters=Olá mundo", true);
    //xhttp.send();
    //é possível passar informações por um get, como no exemplo acima. possible_words é a rota, caracters é a chave e Olá mundo o valor
    //é possível passar diversar chaves e valores, na view é possível pegar cada uma.
    xhttp.open("POST", "http://localhost:8000", true);
    xhttp.setRequestHeader("X-CSRFToken", getCsrfToken());
    xhttp.setRequestHeader("Content-type", "application/json"); // mandando múltiplos headers
    console.log('CARAC ' + getCaracters())
    const json = {
        'caracteres': getCaracters()
    }
    xhttp.send(JSON.stringify(json));

}
