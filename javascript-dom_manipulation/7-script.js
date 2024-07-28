addEventListener("DOMContentLoaded", function () {
    fetch("https://swapi-api.hbtn.io/api/films/?format=json")
        .then((response) => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then((content) => {
            const movies = content.results;
            for (movie of movies) {
                const li = document.createElement("li");
                li.innerText = movie.title;
                document.querySelector("#list_movies").append(li);
            }
        });
});