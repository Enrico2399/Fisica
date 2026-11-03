/*
 * Service worker per l'uso offline (stesso schema della webapp di Metodi Matematici).
 * - CACHE_APP: i file del sito; cambia il numero di versione quando aggiorni index.html.
 * - CACHE_RUNTIME: KaTeX e il font da CDN. Le URL contengono la versione, quindi restano valide.
 */
const CACHE_APP = "fis-app-v1";
const CACHE_RUNTIME = "fis-runtime-v1";

const APP_ASSETS = [
  "./",
  "index.html",
  "manifest.json",
  "Formulario_esame_Fisica.pdf",
  "icon-192.png",
  "icon-512.png",
  "apple-touch-icon.png",
  "favicon-32.png",
];
const RUNTIME_ASSETS = [
  "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.js",
  "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/contrib/auto-render.min.js",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_APP).then((c) => Promise.all(APP_ASSETS.map((u) => precacheOne(c, u))))
      .then(() => caches.open(CACHE_RUNTIME))
      .then((c) => Promise.allSettled(RUNTIME_ASSETS.map((u) => precacheOne(c, u))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE_APP && k !== CACHE_RUNTIME).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  const own = new URL(req.url).origin === self.location.origin;
  const cacheName = own ? CACHE_APP : CACHE_RUNTIME;
  event.respondWith(
    caches.open(cacheName).then((cache) =>
      cache.match(req).then((cached) => {
        // Pagina del sito: prima la rete (cosi' gli aggiornamenti arrivano subito), poi la cache se offline.
        if (own && req.mode === "navigate") {
          return fetch(req).then((resp) => { if (resp.ok) cache.put(req, resp.clone()); return resp; })
            .catch(() => cached || cache.match("index.html"));
        }
        if (cached) return cached;
        return fetch(req).then((resp) => {
          if (resp && (resp.ok || resp.type === "opaque")) cache.put(req, resp.clone());
          return resp;
        }).catch(() => { if (req.mode === "navigate") return cache.match("index.html"); throw new Error("offline: " + req.url); });
      })
    )
  );
});

async function precacheOne(cache, url) {
  try {
    if (await cache.match(url)) return;
    let resp;
    try { resp = await fetch(url, { mode: "cors" }); } catch (e) { resp = await fetch(url, { mode: "no-cors" }); }
    if (resp && (resp.ok || resp.type === "opaque")) await cache.put(url, resp);
  } catch (e) { /* verra' messo in cache al primo utilizzo */ }
}
