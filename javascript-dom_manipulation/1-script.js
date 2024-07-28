addEventListener("DOMContentLoaded", function () {
    function changeColor() {
        document.querySelector("header").style.color = "#FF0000";
    }

    const divRedHeader = document.querySelector("#red_header");

    divRedHeader.addEventListener("click", changeColor);
});