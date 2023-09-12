function fetchCharacterName() {
    fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
        .then(response => {
            if (!response.ok) {
                throw new Error('error');
            }
            return response.json();
        })

        .then(data => {
            const Name = data.name;
            document.getElementById('character').textContent = Name;
        })
}

fetchCharacterName();