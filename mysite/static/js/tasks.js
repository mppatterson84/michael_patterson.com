const tasksUpdateForm = document.querySelectorAll('.update');
const tasksCompleted = document.querySelectorAll('.completed');

tasksCompleted.forEach(function (e, index) {
    e.addEventListener('change', function () {
        tasksUpdateForm[index].submit();
    });
});
