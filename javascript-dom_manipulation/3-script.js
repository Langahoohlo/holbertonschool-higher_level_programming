addEventListener("DOMContentLoaded", function () {
    const toggleHeader = document.querySelector("#toggle_header");
    const headerElement = document.querySelector("header");

    function elementchangeClass() {
        if (headerElement.classList.contains("red")) {
            headerElement.classList.remove("red");
            headerElement.classList.add("green");
        } else {
            headerElement.classList.remove("green");
            headerElement.classList.add("red");
        }
    }

    toggleHeader.addEventListener("click", elementchangeClass);
});