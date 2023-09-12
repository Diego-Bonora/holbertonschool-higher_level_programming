window.onload=function(){
    document.querySelector("#btn_translate").addEventListener("click", translate);
}

async function translate() {
    const value = document.querySelector("#language_code");
    const data = await (await fetch("https://hellosalut.stefanbohacek.dev/?lang="+value.value)).json();
    document.querySelector("#hello").innerHTML = data["hello"];    
}