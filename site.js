// menu mobile
document.querySelectorAll('.burger').forEach(b => b.addEventListener('click', () => {
  const m = document.querySelector('.menu');
  const open = m.classList.toggle('open');
  b.setAttribute('aria-expanded', open);
}));
// anno nel footer
document.querySelectorAll('.anno').forEach(e => e.textContent = new Date().getFullYear());
// video YouTube: carica il player solo al clic (niente cookie finché non si preme play)
document.querySelectorAll('.video-box[data-yt]').forEach(box => {
  const go = () => {
    box.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + box.dataset.yt +
      '?autoplay=1&rel=0" title="' + (box.dataset.titolo || 'Video') + '" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>';
  };
  box.querySelectorAll('.play, .copertina').forEach(el => el.addEventListener('click', go));
});
