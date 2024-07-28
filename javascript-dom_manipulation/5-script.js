addEventListener('DOMContentLoaded', function () {
    updateText = () => (document.querySelector('header').innerText = 'New Header!!!');
    document.querySelector('#update_header').addEventListener('click', updateText);
});