    document.addEventListener('DOMContentLoaded', function() {
        // Update form count
        function updateFormCount() {
            const forms = document.querySelectorAll('.image-form');
            const totalForms = document.querySelector('[name="images-TOTAL_FORMS"]');
            if (totalForms) {
                totalForms.value = forms.length;
            }
        }

        // Auto-update form count on page load and after any changes
        updateFormCount();

        // Add form functionality (optional enhancement)
        const formset = document.querySelector('[name="images-TOTAL_FORMS"]');
        if (formset) {
            const parentDiv = formset.parentElement;
            parentDiv.innerHTML = formset.parentElement.innerHTML.replace(/id_images-/g, 'id_');
        }
    });