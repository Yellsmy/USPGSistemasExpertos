// if ('serviceWorker' in navigator) {
//     window.addEventListener('load', function(){
//         navigator.serviceWorker.register('./service_worker.js')
//             .then(function() {
//                 console.log('Archivo registrado exitosamente');
//             })
//     })
// };

if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('./service_worker.js')
            .then(function(registration) {
                console.log('Service Worker registrado exitosamente con el alcance:', registration.scope);
            }).catch(function(error) {
                console.error('Error al registrar el Service Worker:', error);
            });
    });
}
