function fetchHello() {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => {
            if (!response.ok) {
                throw new Error('error');
            }
            return response.json();
        })

        .then(data => {
            const text = document.getElementById("hello");
            const hellotrad = data.hello;
            text.textContent = hellotrad;
        });
}

fetchHello();