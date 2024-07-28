addEventListener("DOMContentLoaded", function () {
    addItem = () => {
        const newItem = document.createElement("li");
        newItem.innerText = "Item";
        document.querySelector(".my_list").append(newItem);
    };

    const addItemElement = document.querySelector("#add_item");
    addItemElement.addEventListener("click", addItem);
});