salut()
async function salut() {
    const response = await (await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")).json();
    document.querySelector("#hello").innerHTML = response["hello"];
  }