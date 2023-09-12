function addli() {
    var newLi = document.createElement("li");
    newLi.textContent = "Item";
    list.appendChild(newLi);
}

var addItem = document.getElementById("add_item");
var list = document.querySelector(".my_list");
addItem.addEventListener("click", addli);