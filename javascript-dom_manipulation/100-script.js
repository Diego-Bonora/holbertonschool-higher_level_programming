window.onload=function(){
    document.querySelector("#add_item").addEventListener("click", add_li);
    document.querySelector("#remove_item").addEventListener("click", delete_li);
    document.querySelector("#clear_list").addEventListener("click", clear);
}

function add_li() {
    document.querySelector(".my_list").innerHTML += "<li>Item</li>";
}
function delete_li() {
    document.querySelector(".my_list").removeChild(document.querySelector(".my_list").lastElementChild);
}
function clear() {
    document.querySelector(".my_list").innerHTML = "";
}