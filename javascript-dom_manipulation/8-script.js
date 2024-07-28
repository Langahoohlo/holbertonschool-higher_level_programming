document.addEventListener("DOMContentLoaded", function () {
    fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
        .then((response) => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then((data) => {
            const helloValue = data.hello;
            document.getElementById("hello").textContent = helloValue;
        })
        .catch((error) => {
            console.error("Error fetching translation:", error);
        });
});