document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialisation
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // modal initialisation
    let modals = document.querySelectorAll('.modal');
    M.Modal.init(modals, {
        opacity: 0.5
    });

    // datepicker initialisation
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: {done: "Select"}
    });

    // select initialisation
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);
});