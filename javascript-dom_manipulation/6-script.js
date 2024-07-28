function fetchCharFromAPI() {
    const api = "https://swapi-api.hbtn.io/api/people/5/?format=json";
    const character = document.querySelector("#character");

    fetch(api)
        .then((response) => response.json())
        .then((data) => {
            const charName = data.name;
            character.textContent = charName;
        })
        .catch((error) => {
            console.error("Error: ", error);
        });
}

fetchCharFromAPI();