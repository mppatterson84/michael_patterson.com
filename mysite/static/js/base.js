var hamburger = document.querySelector('.hamburger');

hamburger.addEventListener('click', () => {
    if (!hamburger.classList.contains('collapsed')) {
        hamburger.classList.add('is-active');
        hamburger.classList.remove('animate__rubberBand');
        hamburger.classList.add('animate__jello');
    } else {
        hamburger.classList.remove('is-active');
        hamburger.classList.add('animate__rubberBand');
        hamburger.classList.remove('animate__jello');
    }
});
