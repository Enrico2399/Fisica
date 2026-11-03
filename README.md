# Fisica — Esercizi risolti

Pagina statica (un solo file `index.html`) con la teoria per macroargomento (domande d'esame con frase-risposta, schema e applicazioni reali) e gli esercizi di Fisica risolti passo passo, divisi per macroargomento, con formule LaTeX (KaTeX), figure della dispensa e rimandi al formulario d'esame.

## Pubblicazione su GitHub Pages
1. Crea un repo (es. `fisica`) e carica il contenuto di questa cartella.
2. Settings → Pages → *Deploy from a branch* → `main` / root.
3. La pagina sarà su `https://<utente>.github.io/fisica/`.

`index.html` è autosufficiente: CSS di KaTeX con font incorporati, dati e immagini inclusi. Da internet servono solo KaTeX JS (cdnjs) e il font Source Serif 4 (Google Fonts).

## App installabile (offline)
Come la webapp di Metodi Matematici è una PWA: dalla pagina pubblicata su GitHub Pages il pulsante **Installa l'app** (o il menu del browser → *Installa app* / *Aggiungi a Home*) la installa su telefono o PC. Dopo la prima apertura funziona anche senza rete grazie a `service-worker.js`.
Quando aggiorni `index.html`, incrementa `CACHE_APP` in `service-worker.js` (es. `fis-app-v2`) così l'app installata scarica la nuova versione.
L'installazione non funziona aprendo il file in locale (`file://`): serve l'indirizzo https di GitHub Pages.

## Struttura
- `index.html` — la pagina generata
- `manifest.json`, `service-worker.js`, `icon-*.png`, `apple-touch-icon.png`, `favicon-32.png` — installazione come app e uso offline
- `Formulario_esame_Fisica.pdf` — il formulario da scaricare/stampare
- `src/esercizi.tex` — esercizi risolti (sorgente LaTeX)
- `src/formulario_esame.tex` — formulario d'esame (sorgente LaTeX)
- `img/` — figure degli esercizi (PNG, nome = numero esercizio)
- `img_teo/` — schemi della teoria (PNG, `figNN`)
- `build/teoria.py` — teoria per area: introduzione, domande con frase-risposta, concetti, vita reale
- `build/template.html` — HTML/CSS/JS della pagina
- `build/conv.py` — converte i `.tex` e le immagini in `build/data.json`
- `build/build.py` — assembla `index.html`
- `build/katex_inline.css` — CSS di KaTeX 0.16.11 con i font in base64

## Rigenerare dopo una modifica ai .tex o a teoria.py
```
python build/conv.py
python build/build.py
```
Richiede solo Python 3 (nessuna libreria esterna).
