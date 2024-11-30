var cacheName = 'cacheFacturacion';
var filesToCache = [
    './',
    './styles/Facturacion.css',
    './styles/Login.css',
    './styles/Precios.css',
    './style.css',
    './index.html',
    './manifest.json',
    './logo.jpg',
    '../src/main.js',
    '../src/auth/authService.js',
    '../src/components/PDFGenerador.js',
    '../src/routes/index.js',
    '../src/services/FacturacionService.js',
    '../src/services/PreciosService.js',
    '../src/views/Facturacion/CreateInvoiceModal.js',
    '../src/views/Facturacion/FacturacionView.js',
    '../src/views/Login/LoginView.js',
    '../src/views/Precios/PreciosView.js',
    '../src/views/PDF/PDFView.js',
    '../src/views/HomeView.js'
];

// self.addEventListener("fetch", function(event) {
//     event.respondWith(
//         caches.match(event.request).then(function(response) {
//             return response || fetch(event.request);
//         })
//     );
// });


self.addEventListener('install', function(event) {
    console.log('[ServiceWorker] Install');
    event.waitUntil(
        caches.open(cacheName).then(function(cache) {
            return cache.addAll(filesToCache).catch(function(error) {
                console.error('Failed to cache', error);
                throw error;
            });
        })
    );
    self.skipWaiting();
});


self.addEventListener('activate', function(event) {
    console.log('[ServiceWorker] Activate');
    event.waitUntil(
        caches.keys().then(function(keyList) {
            return Promise.all(keyList.map(function(key) {
                if (key !== cacheName) {
                    console.log('[ServiceWorker] Removing old cache', key);
                    return caches.delete(key);
                }
            }));
        })
    );
    return self.clients.claim();
});


self.addEventListener('fetch', function(event) {
    console.log('[ServiceWorker] Fetch', event.request.url);
    event.respondWith(
        caches.match(event.request).then(function(response) {
            return response || fetch(event.request).then(function(response) {
                return caches.open(cacheName).then(function(cache) {
                    cache.put(event.request.url, response.clone());
                    return response;
                });
            });
        }).catch(function(error) {
            console.error('Fetching failed:', error);
            throw error;
        })
    );
});