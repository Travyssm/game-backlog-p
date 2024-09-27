document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialisation
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // modal initialisation
    let modals = document.querySelectorAll('.modal');
    M.Modal.init(modals, {
        opacity: 0.5
    });
});