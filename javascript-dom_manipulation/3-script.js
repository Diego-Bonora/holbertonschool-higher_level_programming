document.querySelector("#toggle_header").addEventListener("click", toggle_color);
function toggle_color() {
    if ( document.querySelector("header").className == "green" ) {
        document.querySelector("header").className = "red";
    }else{
        document.querySelector("header").className = "green";
    }
  }