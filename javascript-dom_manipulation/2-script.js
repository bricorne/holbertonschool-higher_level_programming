function HColor() {
    var header = document.querySelector('header');
    header.className = 'red';
}

var redHButton = document.getElementById('red_header');
redHButton.addEventListener('click', HColor);