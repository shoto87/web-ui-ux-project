
function toggleFormMode() {
    const formContainers = document.querySelectorAll('.form-container');
    formContainers.forEach(container => container.classList.toggle('signup-mode'));
    formContainers.forEach(container => container.classList.toggle('hiding-mode'));
}