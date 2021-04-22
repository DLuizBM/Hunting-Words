function getAllWords(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            document.getElementById("words").innerHTML = xhttp.responseText;
        }
    }
    xhttp.open("GET", "http://localhost:8000/words", true);
    xhttp.send();
}
