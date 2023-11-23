// document.addEventListener('DOMContentLoaded', function () {
//     const darkModeToggle = document.getElementById('darkModeToggle');

//     // Recuperar el estado actual del modo oscuro desde el localStorage
//     const isDarkMode = localStorage.getItem('darkMode') === 'enabled';

//     // Establecer el estado inicial del interruptor
//     darkModeToggle.checked = isDarkMode;

//     // Aplicar el modo oscuro si está habilitado
//     toggleDarkMode(isDarkMode);

//     darkModeToggle.addEventListener('change', function () {
//         const isDarkMode = darkModeToggle.checked;

//         // Guardar el estado actual del modo oscuro en el localStorage
//         localStorage.setItem('darkMode', isDarkMode ? 'enabled' : 'disabled');

//         // Aplicar el modo oscuro
//         toggleDarkMode(isDarkMode);
//     });

//     function toggleDarkMode(isDarkMode) {
//         document.body.classList.toggle('dark-mode', isDarkMode);
//     }
// });

document.addEventListener('DOMContentLoaded', function () {
    const darkModeButton = document.getElementById('dark-theme');
    const lightModeButton = document.getElementById('light-theme');

    // Recuperar el estado actual del modo oscuro desde el localStorage
    let isDarkMode = localStorage.getItem('darkMode') === 'enabled';
    //alert(isDarkMode);

    // Aplicar el modo oscuro si está habilitado
    toggleDarkMode(isDarkMode);

    //al hacer click en el boton de modo oscuro
    darkModeButton.addEventListener('click', function () {
        // Guardar el estado actual del modo oscuro en el localStorage
        localStorage.setItem('darkMode', 'enabled');
        isDarkMode = true
        //alert(isDarkMode);

        // Aplicar el modo oscuro
        toggleDarkMode(isDarkMode);

        function toggleDarkMode(isDarkMode) {
            document.body.classList.toggle('dark-mode', isDarkMode);
        }
    })

    //al hacer click en el boton de modo claro
    lightModeButton.addEventListener('click', function () {
        // Guardar el estado actual del modo oscuro en el localStorage
        localStorage.setItem('darkMode', 'disabled');
        isDarkMode = false
        //alert(isDarkMode);

        // Aplicar el modo oscuro
        toggleDarkMode(isDarkMode);
    })

    function toggleDarkMode(isDarkMode) {
        document.body.classList.toggle('dark-mode', isDarkMode);
        document.body.classList.remove('loading');
    }

})

