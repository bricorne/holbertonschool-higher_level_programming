function newHeader() {
    var header = document.querySelector('header')
    header.textContent = "New Header!!!";
}

var headerButton = document.getElementById('update_header');
headerButton.addEventListener('click', newHeader);