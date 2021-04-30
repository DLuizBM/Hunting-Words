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
    xhttp.open("GET", "http://localhost:8000/possible_words?caracters=Ola mundo", true);
    //xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    //xhttp.setRequestHeader("X-CSRFToken", getCsrfToken());
    console.log('CARAC ' + getCaracters())
    xhttp.send();
}
