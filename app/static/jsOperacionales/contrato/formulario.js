document.addEventListener('DOMContentLoaded', () => {
    var quill = new Quill('#quill-container', {
        modules: {
            toolbar: [
                [{ header: [1, 2, false] }],
                ['bold', 'italic', 'underline'],
                ['image', 'code-block']
            ]
        },
        scrollingContainer: '#scrolling-container',
        placeholder: 'Compose an epic...',
        theme: 'snow'  // or 'bubble'
    });
});