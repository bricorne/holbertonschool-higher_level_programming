function HColor() {
    var header = document.querySelector('header');
    header.style.color = '#FF0000';
}

var redHButton = document.getElementById('red_header');
redHButton.addEventListener('click', HColor);