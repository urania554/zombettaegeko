#!/usr/bin/env python3
"""Genera le pagine del sito di Zombetta e Geko (header e footer condivisi)."""
import os
import os
OUT = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://zombettaegeko.it'
# Negozio: False = solo prenotazioni via email/Instagram; True = Stripe + modulo + condizioni di vendita
NEGOZIO_ATTIVO = False
EMAIL = 'zombettaegeko@gmail.com'
COND_LINK = '· <a href="condizioni.html">Condizioni di vendita</a> ' if NEGOZIO_ATTIVO else ''

YT = 'https://www.youtube.com/@ZombettaGeko'
IG = 'https://www.instagram.com/zombettaegeko/'
TT = 'https://www.tiktok.com/@zombettaegeko'
FB = 'https://www.facebook.com/zombettaegeko/'
AMZ = ['https://www.amazon.it/dp/B0HQX4SNHK', 'https://www.amazon.it/dp/B0HQX1T3Z9',
       'https://www.amazon.it/dp/B0HRY223DW', 'https://www.amazon.it/dp/B0HRYVKGC1']

MENU = [('index.html', 'Home'), ('libri.html', 'Libri'), ('video.html', 'Cartoni'),
        ('canzone.html', 'Canzone'), ('giochi.html', 'Giochi'), ('negozio.html', 'Shop')]

def page(fname, title, desc, body, extra_js=''):
    nav = '\n'.join(f'<li><a href="{h}"{" aria-current=page" if h == fname else ""}>{t}</a></li>' for h, t in MENU)
    html = f'''<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/img/og.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="img/favicon.png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="preload" href="fonts/fredoka-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="top">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Zombetta e Geko, home"><img class="tondo" src="img/logo-tondo.webp" alt="" width="58" height="58"><img src="img/logo.webp" alt="Zombetta e Geko" width="160" height="58"></a>
    <button class="burger" aria-label="Apri il menu" aria-expanded="false">☰</button>
    <nav><ul class="menu">
{nav}
    </ul></nav>
  </div>
</header>
<main>
{body}
</main>
<footer>
  <div class="wrap">
    <div>
      <img src="img/logo.webp" alt="" width="200" style="margin-bottom:12px">
      <p>Una bambina zombie, un geco e una valigia piena di misteri. Storie da leggere e guardare insieme, per piccoli e grandi.</p>
    </div>
    <div>
      <h3>Segui le avventure</h3>
      <ul>
        <li><a href="{YT}" rel="noopener">YouTube</a></li>
        <li><a href="{IG}" rel="noopener">Instagram</a></li>
        <li><a href="{FB}" rel="noopener">Facebook</a></li>
        <li><a href="{TT}" rel="noopener">TikTok</a></li>
      </ul>
    </div>
    <div>
      <h3>L'autrice</h3>
      <p>Le storie di Zombetta e Geko sono di Cinzia Molisano.<br><a href="https://cinziamolisano.it" rel="noopener">cinziamolisano.it</a></p>
    </div>
    <p class="piccolo">© <span class="anno">2026</span> Cinzia Molisano · Zombetta e Geko · Questo sito non usa cookie. {COND_LINK}· <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="privacy.html">Privacy</a></p>
  </div>
</footer>
<script src="site.js"></script>
{extra_js}
</body>
</html>
'''
    open(os.path.join(OUT, fname), 'w').write(html)

ONDA = '<svg class="onda" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0,30 C240,60 480,0 720,30 C960,60 1200,0 1440,30 L1440,60 L0,60 Z" fill="{c}"/></svg>'

LIBRI = [
    (1, 'Un amico per partire', 'Borgoquieto', 'Zombetta vive in una casetta in collina e i pezzetti le scappano via. Un giorno, nello zaino, trova un piccolo geco… e il viaggio comincia.'),
    (2, 'Il segreto della gondola fantasma', 'Venezia', 'Tra canali, campanili e gondole, Zombetta e Geko inseguono un mistero che galleggia sull\'acqua.'),
    (3, 'Il segreto del portale rosso', 'Tokyo', 'Un gatto portafortuna che si sveglia, una volpe che cammina sull\'acqua e un segreto sotto il grande portale rosso.'),
    (4, 'Il cuore di Gramigna', 'Roma', 'L\'ultima tappa del viaggio: a Roma tutti i misteri arrivano al loro cuore.'),
]

EP = [
    (1, 'La casetta di Zombetta', 'd0_W8UJYSJU', '2026-11-01', None),
    (2, 'Briciole in soffitta', '3ud5t2PDVxk', '2026-11-04', None),
    (3, 'Si parte!', 'vgoni33N3Uc', '2026-11-13T18:00', None),
    (4, "C'è qualcuno nello zaino", 'RBKYDuNxQSA', '2026-11-20T18:30', 'img/ep4.webp'),
    (5, 'Il treno sbagliato', 'IeZ6eT7AnyQ', '2026-11-27T18:30', 'img/ep5.webp'),
    (6, 'La carrozza degli oggetti smarriti', 'qYlCKg7E54E', '2026-12-04T18:30', 'img/ep6.webp'),
    (7, "Venezia all'alba", 'tKEzNgtxRBY', '2026-12-11T18:30', 'img/ep7.webp'),
]
MESI = ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre']
def data_it(d):
    y, m, g = d[:10].split('-'); return f'{int(g)} {MESI[int(m)-1]}'

def card_ep(n, t, vid, uscita, img):
    src = img or f'https://i.ytimg.com/vi/{vid}/hqdefault.jpg'
    return f'''<article class="card ep" data-uscita="{uscita}" data-link="https://youtu.be/{vid}">
  <img src="{src}" alt="Episodio {n}: {t}" loading="lazy" width="640" height="360">
  <div class="corpo">
    <span class="etichetta">Episodio {n}</span>
    <h3>{t}</h3>
    <p class="data" hidden>Esce il {data_it(uscita)} su YouTube</p>
    <a class="btn piccolo" href="https://youtu.be/{vid}" rel="noopener">▶ Guarda</a>
  </div>
</article>'''

EP_JS = '''<script>
// mostra "Guarda" solo per gli episodi già usciti, altrimenti la data di uscita
const ora = new Date();
document.querySelectorAll('[data-uscita]').forEach(c => {
  if (new Date(c.dataset.uscita) > ora) {
    c.querySelector('.data').hidden = false;
    const b = c.querySelector('.btn'); if (b) b.remove();
    c.querySelector('.etichetta').classList.add('presto');
  }
});
</script>'''

def card_libro(n, t, citta, testo):
    return f'''<article class="card libro storta">
  <img src="img/libro{n}.webp" alt="Copertina del Volume {n}: {t}" loading="lazy" width="560" height="840">
  <div class="corpo">
    <span class="num">Volume {n}</span>
    <h3>{t}</h3>
    <span class="etichetta citta">📍 {citta}</span>
    <p>{testo}</p>
    <a class="btn piccolo" href="{AMZ[n-1]}" rel="noopener">Su Amazon →</a>
  </div>
</article>'''

# ------------------------------------------------------------------ HOME
home = f'''
<section class="hero">
  <div class="wrap">
    <div>
      <img class="logo-grande" src="img/logo.webp" alt="Zombetta e Geko" width="520" height="300">
      <h1 style="font-size:clamp(1.6rem,3.4vw,2.4rem)">Una bambina zombie, un geco<br>e una valigia piena di misteri</h1>
      <p class="sotto">Libri illustrati, cartoni animati, una canzone da cantare e giochi.</p>
      <div class="bottoni">
        <a class="btn" href="libri.html">📚 I libri</a>
        <a class="btn verde" href="video.html">▶ I cartoni</a>
        <a class="btn rosa" href="canzone.html">🎵 La canzone</a>
      </div>
    </div>
    <div style="position:relative">
      <div class="quadro"><img src="img/viaggio.webp" alt="Zombetta cammina con la valigia verso la città, Geko spunta dallo zaino" width="800" height="1192"></div>
      <span class="adesivo" style="left:-14px;bottom:30px">In viaggio si va!</span>
    </div>
  </div>
</section>
{ONDA.format(c="#efe4ff")}
<section class="sez lilla" style="padding-top:30px">
  <div class="wrap">
    <div class="titolo-sez"><span class="occhiello">I protagonisti</span><h2>Chi sono Zombetta e Geko?</h2></div>
    <div class="griglia g2">
      <div class="personaggio z"><img src="img/prato.webp" alt="Zombetta salta felice nel prato" loading="lazy">
        <div><h3>Zombetta</h3><p>Ha i capelli viola tutti spettinati, la pelle verdina e un passo un po' storto. A volte un pezzetto le scappa via… ma lei ride più forte di tutti, si rialza e riparte.</p></div></div>
      <div class="personaggio g"><img src="img/muri.webp" alt="Geko si arrampica sul muro con la lente d'ingrandimento" loading="lazy">
        <div><h3>Geko</h3><p>È piccolino e cammina sui muri. Scova gli indizi negli angoli più bui e, quando Zombetta si distrae, la mappa la tiene lui… nel cuore.</p></div></div>
    </div>
  </div>
</section>
{ONDA.format(c="#fffdf7").replace('<svg', '<svg style="background:#efe4ff"')}
<section class="sez carta" style="padding-top:30px">
  <div class="wrap">
    <div class="titolo-sez"><span class="occhiello">4 viaggi, 4 città</span><h2>Il giro del mondo di Zombetta</h2>
      <p>Borgoquieto, Venezia, Tokyo e Roma: ogni libro è una tappa, e ogni tappa nasconde un pezzo del mistero.</p></div>
    <div class="griglia g4">
      {''.join(f'<a class="card storta" href="libri.html" style="text-decoration:none"><img src="img/libro{n}.webp" alt="Volume {n}: {t}" loading="lazy" width="560" height="840"><div class="corpo"><span class="etichetta citta">📍 {c}</span><h3>{t}</h3></div></a>' for n, t, c, _ in LIBRI)}
    </div>
    <p style="text-align:center;margin-top:34px"><a class="btn" href="libri.html">Scopri i libri</a></p>
  </div>
</section>
{ONDA.format(c="#e3f6d8").replace('<svg', '<svg style="background:#fffdf7"')}
<section class="sez verde" style="padding-top:30px">
  <div class="wrap">
    <div class="griglia g3">
      <div class="card"><img src="img/canzone.webp" alt="" loading="lazy"><div class="corpo"><h3>🎵 La canzone</h3><p>Canta con Zombetta e Geko: il testo si colora mentre cantano.</p><a class="btn piccolo rosa" href="canzone.html">Ascolta</a></div></div>
      <div class="card"><img src="img/ep4.webp" alt="" loading="lazy"><div class="corpo"><h3>▶ I cartoni</h3><p>Ogni venerdì un nuovo episodio sul canale YouTube.</p><a class="btn piccolo verde" href="video.html">Guarda</a></div></div>
      <div class="card"><img src="img/valigia.webp" alt="" loading="lazy" style="aspect-ratio:16/9;object-fit:cover"><div class="corpo"><h3>🧩 Giochi</h3><p>Memory, puzzle e il quiz per veri esperti di Zombetta.</p><a class="btn piccolo" href="giochi.html">Gioca</a></div></div>
    </div>
  </div>
</section>
<section class="sez carta">
  <div class="wrap">
    <div class="avviso">
      <h2>Per maestre e biblioteche</h2>
      <p>Le avventure di Zombetta e Geko nascono per essere lette insieme: in classe, in biblioteca, prima della nanna. Cinzia incontra i bambini con un'indagine vera sulla valigia di Zombetta: indizi da esaminare, teorie da confrontare e un reperto da lasciare nella valigia.</p>
      <a class="btn" href="{IG}" rel="noopener">Scrivici per un incontro</a>
    </div>
  </div>
</section>
'''
page('index.html', 'Zombetta e Geko – Libri, cartoni e giochi per bambini',
     'Le avventure di Zombetta, una bambina zombie, e del suo amico geco Geko: libri illustrati, cartoni animati, la canzone e i giochi.', home)

# ------------------------------------------------------------------ LIBRI
libri = f'''
<section class="pagina-testa"><div class="wrap">
  <h1>I libri</h1>
  <p>Quattro libri illustrati, quattro città e un unico grande mistero. Da leggere insieme o da soli.</p>
</div></section>
<section class="sez" style="padding-top:30px"><div class="wrap">
  <div class="griglia g4">
    {''.join(card_libro(*l) for l in LIBRI)}
  </div>
</div></section>
<section class="sez lilla"><div class="wrap" style="display:grid;grid-template-columns:minmax(0,320px) 1fr;gap:40px;align-items:center">
  <img src="img/libro5.webp" alt="Copertina de L'avventura completa, volumi 1-4" loading="lazy" style="border:var(--bordo);border-radius:18px;box-shadow:var(--ombra);transform:rotate(-2deg)">
  <div>
    <span class="etichetta">Novità · Tutti e 4 i volumi</span>
    <h2>L'avventura completa</h2>
    <p>Tutti e quattro i volumi in un unico libro: perfetto da leggere in classe, da tenere sul comodino o da regalare a Natale e ai compleanni.</p>
    <p><b>Ora disponibile su Amazon.</b></p>
    <a class="btn" href="https://www.amazon.it/dp/B0HSN2BTC6" rel="noopener">Su Amazon →</a>
  </div>
</div></section>
<style>@media (max-width:700px){{.lilla .wrap{{grid-template-columns:1fr!important}}}}</style>
'''
page('libri.html', 'I libri di Zombetta e Geko', 'I libri illustrati de Le avventure di Zombetta e Geko: Borgoquieto, Venezia, Tokyo e Roma. Su Amazon.', libri)

# ------------------------------------------------------------------ VIDEO
video = f'''
<section class="pagina-testa"><div class="wrap">
  <h1>I cartoni animati</h1>
  <p>Le avventure di Zombetta e Geko diventano cartoni: un nuovo episodio ogni venerdì sul canale YouTube.</p>
  <p style="margin-top:18px"><a class="btn rosa" href="{YT}?sub_confirmation=1" rel="noopener">🔔 Iscriviti al canale</a></p>
</div></section>
<section class="sez" style="padding-top:30px"><div class="wrap">
  <div class="titolo-sez"><span class="occhiello">Volume 1</span><h2>Un amico per partire</h2></div>
  <div class="griglia g3">
    {''.join(card_ep(*e) for e in EP)}
  </div>
</div></section>
'''
page('video.html', 'I cartoni di Zombetta e Geko', 'Gli episodi animati de Le avventure di Zombetta e Geko su YouTube: un nuovo episodio ogni venerdì.', video, EP_JS)

# ------------------------------------------------------------------ CANZONE
strofe = [
    ('i', 'Ritornello – insieme', "Zombetta e Geko, in viaggio si va,<br>con una valigia e tanta curiosità!<br>Un passo che dondola, una coda che va:<br>dove c'è un amico, la casa sarà!"),
    ('z', 'Zombetta', "Ho il passo un po' storto e la pelle verdina,<br>ma rido più forte di ogni bambina.<br>Se inciampo per strada mi rialzo così:<br>un salto, una giravolta… e via di qui!"),
    ('g', 'Geko', "Io sono piccino, cammino sui muri,<br>scovo gli indizi negli angoli più scuri.<br>Se lei si distrae, ci penso io:<br>la mappa la tengo nel cuore mio!"),
    ('i', 'Ritornello – insieme', "Zombetta e Geko, in viaggio si va…"),
    ('i', 'Insieme', "Un abbraccio, un sorriso, un amico in più,<br>ogni cuore che incontri ci porta più su…<br>Chissà cosa c'è nella valigia, chissà:<br>la prossima avventura ce lo dirà!"),
    ('i', 'Ritornello finale – insieme', "Zombetta e Geko, in viaggio si va,<br>con una valigia e tanta curiosità!<br>Un passo che dondola, una coda che va:<br>dove c'è un amico, la casa sarà!"),
]
canzone = f'''
<section class="pagina-testa"><div class="wrap">
  <h1>La canzone di Zombetta e Geko</h1>
  <p>Canta con loro! Nel video il testo si colora: <b class="chi-z">rosa</b> per Zombetta, <b class="chi-g">verde</b> per Geko e <b class="chi-i">giallo</b> quando cantano insieme.</p>
</div></section>
<section class="sez" style="padding-top:30px"><div class="wrap" style="max-width:900px">
  <div data-uscita="2026-11-22T11:30">
    <div class="video-box" data-yt="JZ6NbpbDOK4" data-titolo="La canzone di Zombetta e Geko">
      <img class="copertina" src="img/canzone.webp" alt="La canzone di Zombetta e Geko">
      <button class="play" aria-label="Guarda il video della canzone">▶</button>
    </div>
    <p class="data nota-privacy" hidden style="font-size:1.1rem;opacity:1;font-weight:800">🎉 Il video esce lunedì 23 novembre alle 17:00!</p>
  </div>
  <p class="nota-privacy">Il video si apre da YouTube solo quando premi play.</p>
</div></section>
<section class="sez lilla"><div class="wrap" style="max-width:900px">
  <div class="titolo-sez"><span class="occhiello">Da cantare insieme</span><h2>Il testo</h2></div>
  <div class="testo-canzone">
    {''.join(f'<div><b class="chi-{c}">{t}</b>{s}</div>' for c, t, s in strofe)}
  </div>
  <p style="text-align:center;margin-top:28px"><button class="btn bianco" onclick="window.print()">🖨 Stampa il testo</button></p>
</div></section>
<style>@media print{{header,footer,.pagina-testa,.sez:first-of-type,.btn,.titolo-sez .occhiello{{display:none!important}}.sez{{padding:0}}.testo-canzone{{box-shadow:none}}}}</style>
'''
CANZ_JS = '''<script>
const box = document.querySelector('[data-uscita]');
if (new Date(box.dataset.uscita) > new Date()) {
  box.querySelector('.data').hidden = false;
  box.querySelector('.play').remove();
  box.querySelector('.copertina').style.cursor = 'default';
  box.querySelector('.video-box').removeAttribute('data-yt');
}
</script>'''
# lo script della data va prima di site.js: lo inseriamo nel body
page('canzone.html', 'La canzone di Zombetta e Geko – con testo', 'La canzone ufficiale di Zombetta e Geko, con il testo da cantare e stampare.', canzone.replace('</section>\n<section class="sez lilla">', '</section>' + CANZ_JS + '\n<section class="sez lilla">', 1))

# ------------------------------------------------------------------ NEGOZIO
# Dati del negozio: completare prima della pubblicazione
NEG = dict(prezzo='6,00', prezzo_sacca='4,00', spedizione='4,99', spedizione_casa='7,10', stripe='https://buy.stripe.com/9B68wP8tjdfOc9KcligIo00',   # link Payment Link di Stripe
           venditore='Cinzia Molisano', email='zombettaegeko@gmail.com', indirizzo='')
taglie = ['2 anni', '4 anni', '6 anni', '8 anni', '10 anni']
colori = [('bianco', '#ffffff'), ('celeste', '#a9d4f5'), ('rosa', '#f6a6cf'), ('giallo', '#ffe45c')]
def opts(lst): return ''.join(f'<option>{x}</option>' for x in lst)
stripe_btn = (f'<a class="btn verde" href="{NEG["stripe"]}" rel="noopener">💳 Compra subito con carta</a>'
              if NEG['stripe'] else '')
negozio = f'''
<section class="pagina-testa"><div class="wrap">
  <h1>La maglietta del Club</h1>
  <p>Per entrare nel Club degli amici di Zombetta e partire per il giro del mondo… vestiti per l'occasione!</p>
</div></section>
<section class="sez" style="padding-top:30px"><div class="wrap">
  <div class="prodotto-big">
    <div class="galleria">
      <img id="foto-grande" src="img/club.webp" alt="Il bollino del Club degli amici di Zombetta" width="700" height="700">
      <div class="miniature">
        <button type="button" data-img="img/club.webp" aria-label="Davanti: bollino del Club"><img src="img/club.webp" alt=""></button>
        <button type="button" data-img="img/giro-retro.webp" aria-label="Retro: il giro del mondo"><img src="img/giro-retro.webp" alt=""></button>
        <button type="button" data-img="img/giro-fronte.webp" aria-label="Retro: Zombetta e Geko"><img src="img/giro-fronte.webp" alt=""></button>
      </div>
    </div>
    <div>
      <span class="etichetta presto">Prima edizione · pezzi limitati</span>
      <h2>Maglietta del Club di Zombetta e Geko</h2>
      <p class="prezzo">{NEG["prezzo"]} €</p>
      <p><b>Davanti</b> il bollino del <b>Club degli amici di Zombetta</b>, sul lato del cuore. <b>Dietro</b> scegli tu: le tappe del <b>giro del mondo</b> (Borgoquieto, Venezia, Tokyo, Roma) oppure <b>Zombetta e Geko</b>.</p>
      <ul class="dettagli">
        <li>100% cotone, per bambini dai 2 ai 10 anni</li>
        <li>4 colori: bianco, celeste, rosa e giallo</li>
        <li>Stampa DTF morbida, lavabile in lavatrice a 30° al rovescio</li>
        <li>Spedizione in Italia con InPost {NEG["spedizione"]} € (a un Locker o Point vicino a te): <b>una sola spedizione fino a 3 magliette</b> · ritiro a mano gratis</li>
      </ul>
      <div class="colori-pallini">{''.join(f'<span title="{n}" style="background:{c}"></span>' for n, c in colori)}</div>
      <div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:20px">
        {stripe_btn}
        <a class="btn" href="#ordina">📝 Ordina con bonifico o ritiro a mano</a>
      </div>
    </div>
  </div>
</div></section>

<section class="sez lilla" id="ordina"><div class="wrap" style="max-width:760px">
  <div class="titolo-sez"><span class="occhiello">Senza carta di credito</span><h2>Ordina con bonifico o ritiro a mano</h2>
    <p>Compila il modulo: ti rispondiamo via email con il totale e l'IBAN. La maglietta parte appena arriva il bonifico.</p></div>
  <form class="modulo" name="ordine" method="POST" action="grazie.html" data-netlify="true" netlify-honeypot="campo-esca">
    <input type="hidden" name="form-name" value="ordine">
    <p hidden><label>Non compilare: <input name="campo-esca"></label></p>
    <div id="righe">
      <div class="riga">
        <label>Retro<select name="retro_1"><option>Il giro del mondo</option><option>Zombetta e Geko</option></select></label>
        <label>Colore<select name="colore_1">{opts([c for c, _ in colori])}</select></label>
        <label>Taglia<select name="taglia_1">{opts(taglie)}</select></label>
        <label>Quantità<input type="number" name="quantita_1" min="1" max="10" value="1"></label>
      </div>
    </div>
    <button type="button" class="btn piccolo bianco" id="aggiungi">+ Aggiungi un'altra maglietta</button>
    <label>Consegna
      <select name="consegna" id="consegna"><option>Spedizione InPost ({NEG["spedizione"]} € ogni 3 magliette)</option><option>Ritiro a mano (gratis)</option></select></label>
    <div class="due">
      <label>Nome e cognome<input name="nome" required autocomplete="name"></label>
      <label>Email<input type="email" name="email" required autocomplete="email"></label>
    </div>
    <div id="lab-indirizzo" class="due"><label>Locker o Point InPost preferito<input name="locker" placeholder="Es. ITROM19027 o indirizzo del Locker"><a class="btn piccolo bianco" style="justify-self:start;margin-top:6px" href="https://inpost.it/en/find-location" target="_blank" rel="noopener">📍 Trova il Locker più vicino</a></label><label>Cellulare (per il codice di ritiro)<input type="tel" name="telefono" autocomplete="tel"></label><label style="grid-column:1/-1">Il tuo indirizzo (CAP e città bastano se scegli il Locker)<textarea name="indirizzo" rows="2" autocomplete="street-address"></textarea></label></div>
    <label>Note (facoltativo)<textarea name="note" rows="2"></textarea></label>
    <p class="totale">Totale: <b id="totale">–</b></p>
    <label class="check"><input type="checkbox" required> Ho letto le <a href="condizioni.html">condizioni di vendita</a> e l'<a href="privacy.html">informativa privacy</a>.</label>
    <button class="btn rosa" type="submit">Invia l'ordine</button>
    <p class="nota-privacy" style="text-align:left">Inviare il modulo non comporta nessun pagamento: l'ordine diventa definitivo quando ricevi la nostra email e fai il bonifico.</p>
  </form>
</div></section>
'''
NEG_JS = '''<script>
const PREZZO = %s, SPED = %s;
document.querySelectorAll('.miniature button').forEach(b => b.addEventListener('click', () => document.getElementById('foto-grande').src = b.dataset.img));
let n = 1;
document.getElementById('aggiungi').addEventListener('click', () => {
  if (n >= 6) return; n++;
  const r = document.querySelector('.riga').cloneNode(true);
  r.querySelectorAll('select,input').forEach(e => { e.name = e.name.replace(/_\\d+$/, '_' + n); if (e.type === 'number') e.value = 1; });
  document.getElementById('righe').appendChild(r); calcola();
});
function calcola() {
  let q = 0; document.querySelectorAll('.riga input[type=number]').forEach(i => q += Math.max(0, +i.value || 0));
  const sped = document.getElementById('consegna').selectedIndex === 0;
  document.getElementById('lab-indirizzo').hidden = !sped;
  document.querySelector('[name=indirizzo]').required = sped; document.querySelector('[name=telefono]').required = sped;
  const nsped = sped && q ? Math.ceil(q / 3) : 0;
  const tot = q * PREZZO + nsped * SPED;
  document.getElementById('totale').textContent = tot.toFixed(2).replace('.', ',') + ' €' + (q ? ' (' + q + ' magliett' + (q > 1 ? 'e' : 'a') + (nsped ? ' + ' + (nsped > 1 ? nsped + ' spedizioni' : 'spedizione') : '') + ')' : '');
}
document.querySelector('.modulo').addEventListener('input', calcola); calcola();
</script>''' % (NEG["prezzo"].replace(",", "."), NEG["spedizione"].replace(",", "."))
if NEGOZIO_ATTIVO: page('negozio.html', 'La maglietta del Club di Zombetta e Geko', 'Le magliette per bambini del Club degli amici di Zombetta: bollino sul cuore e il giro del mondo sul retro.', negozio, NEG_JS)

grazie = f'''
<section class="sez"><div class="wrap"><div class="avviso">
  <h1>Grazie! 🎉</h1>
  <p>Abbiamo ricevuto il tuo ordine. Entro un giorno ti scriviamo all'email che hai indicato con il totale e l'IBAN per il bonifico (controlla anche lo spam).</p>
  <p>Zombetta e Geko stanno già preparando la valigia!</p>
  <a class="btn" href="index.html">Torna alla home</a>
</div></div></section>
'''
if NEGOZIO_ATTIVO: page('grazie.html', 'Ordine ricevuto – Zombetta e Geko', 'Grazie per il tuo ordine.', grazie)
else: page('grazie.html', 'Prenotazione ricevuta – Zombetta e Geko', 'Grazie per la prenotazione.', '''
<section class="sez"><div class="wrap"><div class="avviso">
  <h1>Grazie! 🎉</h1>
  <p>Abbiamo ricevuto la tua prenotazione. Ti scriviamo presto all'email che hai indicato con il totale, come pagare e i tempi di consegna (controlla anche lo spam).</p>
  <p>Zombetta e Geko stanno già preparando la valigia!</p>
  <a class="btn" href="index.html">Torna alla home</a>
</div></div></section>
''')

V = NEG['venditore']; E = NEG['email'] or EMAIL; IND = NEG['indirizzo'] or '[INDIRIZZO]'
condizioni = f'''
<section class="sez legale"><div class="wrap" style="max-width:820px">
<h1>Condizioni di vendita</h1>
<p><i>Ultimo aggiornamento: novembre 2026</i></p>
<h2>1. Chi vende</h2>
<p>Le magliette di Zombetta e Geko sono vendute da {V}, {IND}, email {E} (di seguito "la venditrice").</p>
<h2>2. Prodotti e prezzi</h2>
<p>I prodotti sono descritti nella pagina <a href="negozio.html">Magliette</a>. I prezzi sono in euro e comprendono ogni imposta dovuta. Il costo di spedizione ({NEG["spedizione"]} € per ogni pacco fino a 3 magliette, in Italia con InPost, consegna a un Locker o Point) è indicato prima della conferma; il ritiro a mano è gratuito. I colori a schermo possono differire leggermente dal prodotto reale.</p>
<h2>3. Come si ordina e si paga</h2>
<p><b>Con carta:</b> il pagamento avviene sulla pagina sicura di Stripe; la venditrice non vede né conserva i dati della carta. Il contratto si conclude quando ricevi l'email di conferma del pagamento.</p>
<p><b>Con bonifico:</b> inviando il modulo d'ordine fai una richiesta. La venditrice risponde via email con totale e IBAN; il contratto si conclude con questa conferma e l'ordine viene evaso all'arrivo del bonifico. Se il bonifico non arriva entro 7 giorni l'ordine si considera annullato.</p>
<h2>4. Spedizione</h2>
<p>Le magliette vengono spedite in Italia entro 7 giorni lavorativi dal pagamento. I tempi del corriere possono variare.</p>
<h2>5. Diritto di recesso</h2>
<p>Hai 14 giorni dalla consegna per recedere dall'acquisto senza dare spiegazioni, scrivendo a {E}. La maglietta va restituita entro i 14 giorni successivi, non indossata né lavata; le spese di restituzione sono a tuo carico. Il rimborso del prezzo e della spedizione standard avviene entro 14 giorni con lo stesso metodo di pagamento usato.</p>
<h2>6. Garanzia</h2>
<p>Se il prodotto arriva difettoso o diverso da quello ordinato, scrivi a {E} con una foto: verrà sostituito o rimborsato. Resta valida la garanzia legale di conformità prevista dal Codice del Consumo.</p>
<h2>7. Cura del prodotto</h2>
<p>Lavare a 30° al rovescio, non usare candeggina, non stirare direttamente sulla stampa, non asciugare in asciugatrice.</p>
<h2>8. Reclami e legge applicabile</h2>
<p>Per qualsiasi problema scrivi a {E}. Al contratto si applica la legge italiana; per i consumatori è competente il foro del luogo di residenza o domicilio.</p>
</div></section>
'''
if NEGOZIO_ATTIVO: page('condizioni.html', 'Condizioni di vendita – Zombetta e Geko', 'Condizioni di vendita delle magliette di Zombetta e Geko.', condizioni)

PRIV_ORD = ("""<p><b>Ordini:</b> nome, email, indirizzo e dettagli dell'ordine servono solo a gestire l'acquisto e la spedizione (base giuridica: esecuzione del contratto) e a rispettare gli obblighi fiscali (obbligo di legge). I pagamenti con carta sono gestiti da Stripe, che tratta i dati di pagamento come titolare autonomo.</p>""" if NEGOZIO_ATTIVO else '<p><b>Ordini e prenotazioni:</b> se compili il modulo d\'ordine o ci scrivi via email o su Instagram, usiamo nome e cognome, email, cellulare, indirizzo, il Locker o Point InPost scelto e i dettagli dell\'ordine solo per risponderti, gestire l\'ordine e spedire (base giuridica: esecuzione del contratto e misure precontrattuali richieste da te). Li cancelliamo quando non servono più, o prima se ce lo chiedi.</p>')
PRIV_DEST = ('<h2>A chi vengono comunicati</h2>\n<p>Netlify (ricezione dei moduli e hosting), Stripe (pagamenti con carta), InPost (spedizione: nome, cellulare ed email per la consegna al Locker). I dati non vengono venduti né usati per pubblicità.</p>\n<h2>Quanto vengono conservati</h2>\n<p>Per il tempo necessario a gestire l\'ordine e, per i dati richiesti dalla legge fiscale, per 10 anni.</p>' if NEGOZIO_ATTIVO else '<h2>A chi vengono comunicati</h2>\n<p>Il sito è ospitato da Netlify, che tratta i dati tecnici di navigazione e riceve per nostro conto i moduli di prenotazione. Per le spedizioni comunichiamo al corriere (InPost o Poste Italiane) nome, cellulare, email, indirizzo e il Locker o Point di consegna. I dati non vengono venduti né usati per pubblicità.</p>')
privacy = f'''
<section class="sez legale"><div class="wrap" style="max-width:820px">
<h1>Informativa privacy</h1>
<p><i>Ultimo aggiornamento: novembre 2026</i></p>
<h2>Titolare</h2>
<p>{V}{(', ' + IND) if NEGOZIO_ATTIVO else ''}, email {E}.</p>
<h2>Quali dati e perché</h2>
<p><b>Navigazione:</b> il sito non usa cookie né strumenti di statistica o pubblicità. Il fornitore di hosting (Netlify) registra dati tecnici come l'indirizzo IP per sicurezza e funzionamento.</p>
<p><b>Video:</b> i video di YouTube si caricano dalla versione "privacy avanzata" (youtube-nocookie.com) solo quando premi play; da quel momento si applica l'informativa di Google.</p>
{PRIV_ORD}
{PRIV_DEST}
<h2>I tuoi diritti</h2>
<p>Puoi chiedere in ogni momento di accedere ai tuoi dati, correggerli, cancellarli o limitarne l'uso, scrivendo a {E}. Puoi anche presentare reclamo al Garante per la protezione dei dati personali (garanteprivacy.it).</p>
<h2>Bambini</h2>
<p>Il sito è pensato per essere usato dai bambini insieme a un adulto. Gli ordini devono essere fatti da un adulto.</p>
</div></section>
'''
page('privacy.html', 'Privacy – Zombetta e Geko', 'Informativa privacy del sito Zombetta e Geko.', privacy)



if not NEGOZIO_ATTIVO:
    foto_m = [
        ('maglia-celeste-retro-zombetta.webp', 'Retro "Zombetta e Geko"', 'Il logo e Zombetta con Geko sulla spalla, con la scritta "Il giro del mondo · Tour 2026".'),
        ('maglia-celeste-retro-giro.webp', 'Retro "Il giro del mondo"', 'Come una vera maglietta da tour: Borgoquieto, Venezia, Tokyo e Roma, unite dalle stelline.'),
        ('maglia-celeste-fronte.webp', 'Davanti', 'Il bollino del Club degli amici di Zombetta, sul lato del cuore.'),
        ('maglia-rosa-retro-giro.webp', 'Anche in rosa', 'Ogni maglietta si sceglie in bianco, celeste, rosa o giallo.'),
    ]
    oggetto = 'Ordine Zombetta e Geko'
    corpo = 'Ciao! Vorrei ordinare:%0A- magliette (retro, colore, taglia, quantità):%0A- sacche, quantità:%0ANome e cognome:%0ACellulare:%0AIndirizzo, città e CAP:%0ALocker InPost (se lo sai):%0A'
    fcard = lambda i, t, d: f'<article class="card prodotto"><div class="foto"><img src="img/{i}" alt="Maglietta del Club: {t}" loading="lazy"></div><div class="corpo"><h3>{t}</h3><p>{d}</p></div></article>'
    riga_m = lambda n: f'''<div class="riga" data-riga="{n}">
        <label>Retro<select name="retro_{n}"><option>Zombetta e Geko</option><option>Il giro del mondo</option></select></label>
        <label>Colore<select name="colore_{n}">{opts([c for c, _ in colori])}</select></label>
        <label>Taglia<select name="taglia_{n}">{opts(taglie)}</select></label>
        <label>Quantità<input type="number" name="quantita_{n}" min="0" max="10" value="1"></label>
      </div>'''
    pren_html = f'''
<section class="pagina-testa"><div class="wrap">
  <h1>Shop</h1>
  <p>Le magliette e la sacca del <b>Club degli amici di Zombetta</b>, stampate a mano una per una.</p>
</div></section>
<section class="sez" style="padding-top:30px"><div class="wrap">
  <div class="titolo-sez"><span class="etichetta">Disponibile</span><h2>Le magliette del Club</h2>
    <p>Davanti il bollino del <b>Club degli amici di Zombetta</b>; dietro a scelta <b>Zombetta e Geko</b> oppure <b>Il giro del mondo</b>. 100% cotone, taglie da 2 a 10 anni, in bianco, celeste, rosa e giallo.</p>
    <p class="prezzo">{NEG["prezzo"]} € a maglietta</p></div>
  <img src="img/maglie-rosa-celeste.webp" alt="Le magliette del Club in rosa e celeste: retro Il giro del mondo, retro Zombetta e Geko e il bollino del Club sul davanti" style="max-width:640px;width:100%;margin:0 auto;display:block;border-radius:18px">
  <div class="griglia g2" style="max-width:860px;margin:22px auto 0;gap:22px">
    <img src="img/maglie-giallo.webp" alt="Le magliette del Club in giallo" loading="lazy" style="width:100%;border-radius:18px">
    <img src="img/maglie-bianco.webp" alt="Le magliette del Club in bianco" loading="lazy" style="width:100%;border-radius:18px">
  </div>
  <p style="text-align:center;margin-top:24px"><a class="btn rosa" href="#ordina">Ordina</a></p>
</div></section>
<section class="sez" style="padding-top:10px"><div class="wrap">
  <div class="griglia g2" style="align-items:center;gap:36px">
    <img src="img/sacca-nera.webp" alt="La sacca nera del Club con la scritta Il giro del mondo di Zombetta e Geko e il bollino del Club" style="border-radius:18px;width:100%">
    <div>
      <span class="etichetta">Disponibile</span>
      <h2 style="margin:10px 0">La sacca del Club</h2>
      <p>La sacca zainetto in <b>cotone riciclato nero</b>, con i cordini, per la scuola, la palestra o il viaggio. Davanti la scritta <b>"Il giro del mondo di Zombetta e Geko"</b> e il bollino del <b>Club degli amici di Zombetta</b>.</p>
      <p class="prezzo" style="margin:12px 0">{NEG["prezzo_sacca"]} €</p>
      <a class="btn rosa" href="#ordina">Ordina</a>
    </div>
  </div>
</div></section>
<section class="sez lilla" id="ordina"><div class="wrap" style="max-width:820px">
  <div class="titolo-sez"><h2>Ordina</h2>
    <p>Compila il modulo: ti scriviamo noi via email con il totale e come pagare. Il pacco parte appena arriva il pagamento.</p>
    <p>Spedizione in Italia: <b>InPost</b> a un Locker o Point {NEG["spedizione"]} € oppure <b>a casa</b> con Poste Italiane {NEG["spedizione_casa"]} €. <b>Una sola spedizione fino a 3 articoli</b>. Ritiro a mano gratis.</p></div>
  <form class="modulo" name="prenotazione" method="POST" action="/grazie.html" data-netlify="true" netlify-honeypot="campo-esca" id="form-pren">
    <input type="hidden" name="form-name" value="prenotazione">
    <p hidden><label>Non compilare: <input name="campo-esca"></label></p>
    <textarea name="riepilogo" hidden></textarea>
    <p style="margin:0;font-weight:700">Magliette ({NEG["prezzo"]} €)</p>
    <div id="righe">
      {riga_m(1)}
    </div>
    <button type="button" class="btn piccolo bianco" id="aggiungi">+ Aggiungi un'altra maglietta</button>
    <div class="due">
      <label>Sacche ({NEG["prezzo_sacca"]} €)<input type="number" name="sacche" min="0" max="10" value="0"></label>
      <label>Consegna<select name="consegna"><option>InPost a un Locker o Point ({NEG["spedizione"]} €)</option><option>A casa con Poste Italiane ({NEG["spedizione_casa"]} €)</option><option>Ritiro a mano (gratis)</option></select></label>
    </div>
    <div class="due">
      <label>Nome e cognome<input name="nome" required autocomplete="name"></label>
      <label>Email<input type="email" name="email" required autocomplete="email"></label>
    </div>
    <label>Cellulare<input type="tel" name="cellulare" required autocomplete="tel" inputmode="tel" placeholder="Per gli avvisi del corriere"></label>
    <fieldset id="dati-inpost" style="border:0;padding:0;margin:0;display:grid;gap:16px">
      <label>Indirizzo (via e numero civico)<input name="indirizzo" autocomplete="street-address" data-inpost></label>
      <div class="due">
        <label>Città<input name="citta" autocomplete="address-level2" data-inpost></label>
        <label>CAP e provincia<input name="cap" autocomplete="postal-code" placeholder="es. 24121 BG" data-inpost></label>
      </div>
      <div id="dati-locker" style="display:grid;gap:16px">
      <label>Locker o Point InPost preferito (facoltativo)<input name="locker" placeholder="Codice o indirizzo, es. MIL123M o Via Roma 1"></label>
      <p style="margin:-8px 0 0;font-size:.9em">Trovalo sulla <a href="https://inpost.it/en/find-location" target="_blank" rel="noopener">mappa InPost</a>. Se non lo sai, lo scegliamo noi vicino al tuo indirizzo.</p>
      </div>
    </fieldset>
    <label>Note (facoltativo)<textarea name="note" rows="2"></textarea></label>
    <p class="totale">Totale: <b id="totale">–</b></p>
    <p id="avviso-vuoto" style="margin:-6px 0 0;color:#c0392b;display:none">Scegli almeno una maglietta o una sacca.</p>
    <label class="check"><input type="checkbox" required> <span>Ho letto l'<a href="privacy.html">informativa privacy</a>.</span></label>
    <button class="btn rosa" type="submit">Invia l'ordine</button>
  </form>
  <p style="text-align:center;margin-top:22px">Preferisci scriverci? <a href="mailto:{EMAIL}?subject={oggetto.replace(' ', '%20')}&body={corpo.replace(' ', '%20')}">{EMAIL}</a> · <a href="{IG}" rel="noopener">Instagram</a></p>
</div></section>
'''

    PREN_JS = """<script>
{
const PM = %s, PS = %s, SP = %s, SPC = %s;
const form = document.getElementById('form-pren'), righe = document.getElementById('righe');
let n = 1;
document.getElementById('aggiungi').addEventListener('click', () => {
  n++; const r = righe.querySelector('.riga').cloneNode(true); r.dataset.riga = n;
  r.querySelectorAll('[name]').forEach(el => { el.name = el.name.replace(/_\\d+$/, '_' + n); if (el.type === 'number') el.value = 1; });
  righe.appendChild(r); calcola();
});
function calcola() {
  let qm = 0; const voci = [];
  righe.querySelectorAll('.riga').forEach(r => { const q = Math.max(0, parseInt(r.querySelector('[name^=quantita]').value) || 0); if (q) { qm += q; voci.push('Maglietta · retro ' + r.querySelector('[name^=retro]').value + ' · colore ' + r.querySelector('[name^=colore]').value + ' · taglia ' + r.querySelector('[name^=taglia]').value + ' · quantità ' + q); } });
  const qs = Math.max(0, parseInt(form.sacche.value) || 0); if (qs) voci.push('Sacca · quantità ' + qs);
  const pezzi = qm + qs, tipo = form.consegna.selectedIndex, nsp = tipo < 2 && pezzi ? Math.ceil(pezzi / 3) : 0;
  const tot = qm * PM + qs * PS + nsp * (tipo === 0 ? SP : SPC);
  const sped = tipo < 2, box = document.getElementById('dati-inpost'), lk = document.getElementById('dati-locker');
  box.hidden = !sped; box.style.display = sped ? 'grid' : 'none';
  lk.style.display = tipo === 0 ? 'grid' : 'none';
  box.querySelectorAll('[data-inpost]').forEach(el => el.required = sped);
  const totTxt = tot.toFixed(2).replace('.', ',') + ' €';
  form.riepilogo.value = voci.join('\\n') + '\\nConsegna: ' + form.consegna.value + '\\nTotale: ' + totTxt;
  document.getElementById('totale').textContent = pezzi ? totTxt + (nsp ? ' (con ' + (nsp > 1 ? nsp + ' spedizioni' : 'la spedizione') + ')' : '') : '–';
  return pezzi;
}
form.addEventListener('input', calcola); form.addEventListener('change', calcola);
form.addEventListener('submit', e => { const ok = calcola() > 0; document.getElementById('avviso-vuoto').style.display = ok ? 'none' : 'block'; if (!ok) e.preventDefault(); });
calcola();
}
</script>""" % (NEG["prezzo"].replace(",", "."), NEG["prezzo_sacca"].replace(",", "."), NEG["spedizione"].replace(",", "."), NEG["spedizione_casa"].replace(",", "."))
    page('negozio.html', 'Shop – Zombetta e Geko', 'Le magliette e la sacca del Club degli amici di Zombetta: ordina online, spedizione InPost o a casa.', pren_html, PREN_JS)


# ------------------------------------------------------------------ GIOCHI
giochi = '''
<section class="pagina-testa"><div class="wrap">
  <h1>Giochi</h1>
  <p>Allena la memoria, ricomponi le avventure e scopri quanto conosci Zombetta e Geko!</p>
</div></section>
<section class="sez" style="padding-top:20px"><div class="wrap">
  <div class="giochi-menu">
    <button class="btn" data-gioco="memory">🃏 Memory</button>
    <button class="btn" data-gioco="puzzle">🧩 Puzzle</button>
    <button class="btn" data-gioco="quiz">❓ Quiz</button>
  </div>

  <div class="gioco" id="memory">
    <h2 style="text-align:center">Memory del viaggio</h2>
    <div class="barra"><span>Mosse: <span id="memory-mosse">0</span> · Coppie: <span id="memory-coppie">0</span>/8</span><button class="btn piccolo" id="memory-nuovo">Nuova partita</button></div>
    <div class="memory" id="memory-griglia"></div>
    <p class="bravo" id="memory-bravo"></p>
  </div>

  <div class="gioco" id="puzzle">
    <h2 style="text-align:center">Il puzzle di Zombetta</h2>
    <p style="text-align:center">Tocca due pezzi per scambiarli e ricomponi l'immagine.</p>
    <div class="barra">
      <label>Immagine
        <select id="puzzle-immagine">
          <option value="img/prato.webp">Nel prato</option>
          <option value="img/viaggio.webp">In viaggio</option>
          <option value="img/valigia.webp">La valigia magica</option>
          <option value="img/mappa.webp">Geko e la mappa</option>
          <option value="img/muri.webp">Geko investigatore</option>
        </select></label>
      <label>Pezzi
        <select id="puzzle-livello"><option value="3">9 (facile)</option><option value="4">16 (medio)</option><option value="5">25 (difficile)</option></select></label>
      <span>Mosse: <span id="puzzle-mosse">0</span></span>
      <button class="btn piccolo" id="puzzle-nuovo">Mescola</button>
    </div>
    <div style="display:grid;grid-template-columns:1fr 140px;gap:20px;align-items:start" class="puzzle-area">
      <div class="puzzle" id="puzzle-griglia"></div>
      <div><p style="font-weight:800;margin-bottom:6px">Modello</p><img id="puzzle-anteprima" alt="Immagine da ricomporre" style="border:3px solid var(--viola-scuro);border-radius:12px"></div>
    </div>
    <p class="bravo" id="puzzle-bravo"></p>
  </div>

  <div class="gioco" id="quiz">
    <h2 style="text-align:center">Quanto conosci Zombetta e Geko?</h2>
    <div id="quiz-box"></div>
  </div>
</div></section>
<style>@media (max-width:600px){.puzzle-area{grid-template-columns:1fr!important}.puzzle-area img{max-width:140px}.memory{gap:8px}}</style>
'''
page('giochi.html', 'Giochi di Zombetta e Geko – memory, puzzle e quiz', 'Giochi gratuiti per bambini con Zombetta e Geko: memory, puzzle e quiz.', giochi, '<script src="giochi.js"></script>')
print('giochi ok')

# ------------------------------------------------------------------ 404, robots, sitemap
page('404.html', 'Pagina non trovata – Zombetta e Geko', 'Questa pagina non esiste.', '''
<section class="sez"><div class="wrap"><div class="avviso">
  <h1>Ops! Pagina persa 🦎</h1>
  <p>Geko l'ha cercata dappertutto, perfino nello zaino, ma questa pagina non c'è.</p>
  <a class="btn" href="/index.html">Torna alla home</a>
</div></div></section>
''')
PAGINE = ['', 'libri.html', 'video.html', 'canzone.html', 'giochi.html', 'negozio.html', 'privacy.html']
open('sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + ''.join(f'  <url><loc>{SITE}/{p}</loc></url>\n' for p in PAGINE) + '</urlset>\n')
open('robots.txt', 'w').write(f'User-agent: *\nDisallow: /grazie.html\nSitemap: {SITE}/sitemap.xml\n')
_h = open('404.html').read().replace('<head>', '<head>\n<base href="/">', 1); open('404.html', 'w').write(_h)
