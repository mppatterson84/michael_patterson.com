// Listen for a keydown event on the document.
document.addEventListener('keydown', (event) => {
    // If ctrl or command and s are pressed on the keyboard.
    if (event.code == 'KeyS' && (event.ctrlKey || event.metaKey)) {
        // Prevent the browser save window from opening.
        event.preventDefault();
        // If the keys are pressed once (not held down).
        if (!event.repeat) {
            // Click the selected button.
            document.getElementsByName('_continue')[0].click();
        }
    }
});
