function HColor() {
    var header = document.querySelector('header');
    if (header.className == 'red')
        header.className = 'green'
    else
        header.className = 'red'
}

var colorHButton = document.getElementById('toggle_header');
colorHButton.addEventListener('click', HColor);