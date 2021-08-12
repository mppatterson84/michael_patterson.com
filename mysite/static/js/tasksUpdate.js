const checkbox = document.querySelector('#id_completed');
const updateForm = document.querySelector('#update-form');

checkbox.addEventListener('change', function () {
    updateForm.submit();
});
