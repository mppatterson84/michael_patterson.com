if (window.outerWidth < '992') {
    console.log('small screen')
    document
        .querySelector('head')
        .insertAdjacentHTML(
            'afterbegin',
            '<link rel="preload" as="image" href="https://images.unsplash.com/photo-1612694537513-b772cb21f725?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=768&q=80&orient=90&sat=25&bri=10">'
        )
} else {
    console.log('large screen')
    document
        .querySelector('head')
        .insertAdjacentHTML(
            'afterbegin',
            '<link rel="preload" as="image" href="https://images.unsplash.com/photo-1612694537513-b772cb21f725?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1920&q=80&orient=0&sat=25&bri=10">'
        )
}
