function fetchListTitle() {
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
        .then(response => {
            if (!response.ok) {
                throw new Error('error');
            }
            return response.json();
        })

        .then(data => {
            const movies = data.results;

            movies.forEach((movie) => {
                const movtitle = movie.title;
                const newli = document.createElement("li");

                newli.textContent = movtitle;
                movieList.appendChild(newli);
            });
        });
}

const movieList = document.getElementById("list_movies");
fetchListTitle();