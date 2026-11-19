// ---------------- scelta del gioco ----------------
const tabs = document.querySelectorAll('[data-gioco]');
function apri(id) {
  document.querySelectorAll('.gioco').forEach(g => g.classList.toggle('attivo', g.id === id));
  tabs.forEach(t => t.classList.toggle('verde', t.dataset.gioco === id));
  history.replaceState(null, '', '#' + id);
}
tabs.forEach(t => t.addEventListener('click', () => apri(t.dataset.gioco)));
apri((location.hash || '#memory').slice(1));

function mescola(a) { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }

// ---------------- MEMORY ----------------
const IMMAGINI = [
  ['img/timbro-borgo.webp', 1], ['img/timbro-venezia.webp', 1], ['img/timbro-tokyo.webp', 1], ['img/timbro-roma.webp', 1],
  ['img/prato.webp', 0], ['img/muri.webp', 0], ['img/mappa.webp', 0], ['img/valigia.webp', 0],
];
const mem = document.getElementById('memory-griglia');
let girate = [], blocco = false, mosse = 0, coppie = 0;
function nuovoMemory() {
  mem.innerHTML = ''; girate = []; mosse = 0; coppie = 0; aggiornaMem();
  document.getElementById('memory-bravo').textContent = '';
  mescola([...IMMAGINI, ...IMMAGINI]).forEach(([src, timbro]) => {
    const b = document.createElement('button');
    b.className = 'mcarta'; b.dataset.src = src; b.setAttribute('aria-label', 'Carta coperta');
    b.innerHTML = `<span class="in"><span class="f"></span><span class="r${timbro ? ' timbro' : ''}" style="background-image:url(${src})"></span></span>`;
    b.addEventListener('click', () => gira(b));
    mem.appendChild(b);
  });
}
function aggiornaMem() { document.getElementById('memory-mosse').textContent = mosse; document.getElementById('memory-coppie').textContent = coppie; }
function gira(b) {
  if (blocco || b.classList.contains('girata') || b.classList.contains('trovata')) return;
  b.classList.add('girata'); girate.push(b);
  if (girate.length < 2) return;
  mosse++; const [a, c] = girate;
  if (a.dataset.src === c.dataset.src) {
    a.classList.add('trovata'); c.classList.add('trovata'); girate = []; coppie++;
    if (coppie === IMMAGINI.length) document.getElementById('memory-bravo').textContent = `🎉 Bravissimo! Tutte le coppie in ${mosse} mosse!`;
  } else {
    blocco = true;
    setTimeout(() => { a.classList.remove('girata'); c.classList.remove('girata'); girate = []; blocco = false; }, 850);
  }
  aggiornaMem();
}
document.getElementById('memory-nuovo').addEventListener('click', nuovoMemory);
nuovoMemory();

// ---------------- PUZZLE ----------------
const pz = document.getElementById('puzzle-griglia');
let ordine = [], N = 3, scelto = null, mossePz = 0;
function nuovoPuzzle() {
  N = +document.getElementById('puzzle-livello').value;
  const img = document.getElementById('puzzle-immagine').value;
  document.getElementById('puzzle-anteprima').src = img;
  pz.style.gridTemplateColumns = `repeat(${N},1fr)`;
  do { ordine = mescola([...Array(N * N).keys()]); } while (ordine.every((v, i) => v === i));
  scelto = null; mossePz = 0; document.getElementById('puzzle-bravo').textContent = '';
  disegna(img);
}
function disegna(img) {
  img = img || document.getElementById('puzzle-immagine').value;
  pz.innerHTML = '';
  ordine.forEach((p, i) => {
    const b = document.createElement('button');
    b.className = 'pezzo' + (scelto === i ? ' sel' : '');
    const x = p % N, y = Math.floor(p / N);
    b.style.backgroundImage = `url(${img})`;
    b.style.backgroundSize = `${N * 100}% ${N * 100}%`;
    b.style.backgroundPosition = `${x * 100 / (N - 1)}% ${y * 100 / (N - 1)}%`;
    b.setAttribute('aria-label', 'Pezzo ' + (i + 1));
    b.addEventListener('click', () => tocca(i));
    pz.appendChild(b);
  });
  document.getElementById('puzzle-mosse').textContent = mossePz;
}
function tocca(i) {
  if (scelto === null) { scelto = i; disegna(); return; }
  if (scelto !== i) { [ordine[scelto], ordine[i]] = [ordine[i], ordine[scelto]]; mossePz++; }
  scelto = null; disegna();
  if (ordine.every((v, k) => v === k)) document.getElementById('puzzle-bravo').textContent = `🧩 Fatto! Puzzle completato in ${mossePz} mosse!`;
}
['puzzle-livello', 'puzzle-immagine'].forEach(id => document.getElementById(id).addEventListener('change', nuovoPuzzle));
document.getElementById('puzzle-nuovo').addEventListener('click', nuovoPuzzle);
nuovoPuzzle();

// ---------------- QUIZ ----------------
const DOMANDE = [
  ['Che animale è Geko?', ['Un geco', 'Una lucertola gigante', 'Una rana', 'Un camaleonte'], 0],
  ['Di che colore sono i capelli di Zombetta?', ['Verdi', 'Viola', 'Rossi', 'Blu'], 1],
  ['Dove vive Zombetta all\'inizio della storia?', ['A Roma', 'A Tokyo', 'A Borgoquieto', 'A Venezia'], 2],
  ['In quale città c\'è la gondola fantasma?', ['Venezia', 'Tokyo', 'Roma', 'Borgoquieto'], 0],
  ['Nella canzone, dove tiene la mappa Geko?', ['Nella valigia', 'Nello zaino', 'Sotto il cappello', 'Nel cuore'], 3],
  ['Come si chiama il bambino di Tokyo che sa aggiustare tutto?', ['Tommaso', 'Kenta', 'Hiro', 'Mirtillo'], 1],
  ['Sotto quale monte si trova il grande portale rosso?', ['Il Monte Bianco', 'L\'Etna', 'Il monte Fuji', 'Il Vesuvio'], 2],
  ['Qual è l\'ultima tappa del giro del mondo di Zombetta?', ['Roma', 'Parigi', 'Venezia', 'Londra'], 0],
  ['Cosa fa Zombetta quando inciampa?', ['Piange', 'Si arrabbia', 'Torna a casa', 'Si rialza con un salto e una giravolta'], 3],
  ['Quale animale si sveglia di notte nella bottega dei giocattoli di Tokyo?', ['Un drago di carta', 'Un gatto portafortuna', 'Un pesce rosso', 'Un orsetto'], 1],
];
let qOrdine = [], qi = 0, punti = 0;
function nuovoQuiz() { qOrdine = mescola([...DOMANDE.keys()]); qi = 0; punti = 0; mostra(); }
function mostra() {
  const box = document.getElementById('quiz-box');
  if (qi >= qOrdine.length) {
    const msg = punti === DOMANDE.length ? 'Sei un vero esperto di Zombetta e Geko! 🏆' : punti >= 7 ? 'Bravissimo! Conosci benissimo le loro avventure! 🌟' : punti >= 4 ? 'Bene! Leggi un altro libro e riprova! 📚' : 'Guarda qualche cartone e riprova! 🎬';
    box.innerHTML = `<p class="quiz-domanda" style="text-align:center">Hai fatto ${punti} punti su ${DOMANDE.length}!</p><p class="bravo">${msg}</p><p style="text-align:center"><button class="btn" id="quiz-ancora">Rigioca</button></p>`;
    document.getElementById('quiz-ancora').addEventListener('click', nuovoQuiz);
    return;
  }
  const [d, risp, giusta] = DOMANDE[qOrdine[qi]];
  box.innerHTML = `<div class="barra"><span>Domanda ${qi + 1} di ${DOMANDE.length}</span><span>⭐ ${punti}</span></div>
    <p class="quiz-domanda">${d}</p><div class="quiz-risposte"></div><p class="bravo"></p>`;
  const cont = box.querySelector('.quiz-risposte');
  risp.forEach((r, k) => {
    const b = document.createElement('button'); b.textContent = r;
    b.addEventListener('click', () => {
      cont.querySelectorAll('button').forEach(x => x.disabled = true);
      if (k === giusta) { b.classList.add('giusta'); punti++; box.querySelector('.bravo').textContent = 'Giusto! 🎉'; }
      else { b.classList.add('sbagliata'); cont.children[giusta].classList.add('giusta'); box.querySelector('.bravo').textContent = 'Quasi! La risposta giusta è in verde.'; }
      setTimeout(() => { qi++; mostra(); }, 1400);
    });
    cont.appendChild(b);
  });
}
nuovoQuiz();
