addEventListener("DOMContentLoaded", function () {
    const redHeaderElement = document.querySelector("#red_header");

    function elementAddClass() {
        document.querySelector("header").classList.add("red");
    }
    redHeaderElement.addEventListener("click", elementAddClass);
});