document.querySelector("#add_item").addEventListener("click", add_li);
function add_li() {
    document.querySelector(".my_list").innerHTML += `<li>Item</li>`;
  }