var hamburger = document.querySelector('.hamburger')

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('is-active')
    hamburger.classList.toggle('animate__rubberBand')
    hamburger.classList.toggle('animate__jello')
    doubleClickDelay()
})

//disables the hamburger button one millasecond after it is clicked
//and remains disabled for half a second preventing double clicking by the user
function doubleClickDelay() {
    setTimeout(() => {
        hamburger.disabled = true
        setTimeout(() => {
            hamburger.disabled = false
        }, 500)
    }, 1)
}

// // Hide the navbar when scrolling down.
// // Show the navbar when scrolling up.
// var a = window.pageYOffset // 'a' is assigned an initial value
// var nav = document.querySelector('nav.navbar')

// // if the page reloads while scrolled
// if (window.pageYOffset >= 10) {
//     nav.classList.add('animate__slideInDown')
//     nav.classList.remove('amimate__slideOutUp')
// }

// document.addEventListener('scroll', () => {
//     var b = a // 'b' is assigned the value of 'a' to hold
//     a = window.pageYOffset // 'a' is assigned a new value

//     if (pageYOffset >= nav.clientHeight) {
//         if (a <= b) {
//             // show navbar when scrolling up
//             nav.classList.add('animate__slideInDown')
//             nav.classList.remove('animate__slideOutUp')
//         } else if (a > b) {
//             // hide the navbar when scrolling down
//             nav.classList.remove('animate__slideInDown')
//             nav.classList.add('animate__slideOutUp')
//         }
//     } else {
//         // show the navbar when scrolled to the top
//         nav.classList.remove('animate__slideOutUp')
//         nav.classList.remove('animate__slideInDown')
//     }
// })

// ckeditor
// Change the inline style of 'img' and 'figure' tags
// when displayed on a small screen.
if (window.outerWidth < 768) {
    var elements = document.querySelectorAll('img, figure')
    elements.forEach((e) => {
        e.style.float = 'none'
    })
}
