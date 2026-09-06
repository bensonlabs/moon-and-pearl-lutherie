'use strict';
document.querySelectorAll('[data-year]').forEach(node => { node.textContent = new Date().getFullYear(); });

const detailControls = document.querySelector('.detail-tabs');
if (detailControls) detailControls.hidden = false;

const details = {
  shaping: { label: '01 / Wood to surface', name: 'A sharp edge. A lighter pass.', description: 'A hand plane and a bench full of shavings. Material comes away a little at a time.', image: 'hand-plane', alt: 'A hand plane beside curled wood shavings on the workbench', caption: 'Shaping / From the Moon & Pearl workshop' },
  inlays: { label: '02 / A small point of color', name: 'Something small. Something your own.', description: 'Custom dot inlays set into wooden fretboards. A repeated detail gives the whole neck its character.', image: 'custom-inlays', alt: 'Turquoise-colored custom dot inlays along wooden fretboards, with the source beads below', caption: 'Inlays / A detail worth looking closer at' },
  assembly: { label: '03 / Bringing the pieces together', name: 'A good fit needs a good hold.', description: 'The fingerboard is glued to the neck and held by an array of clamps. Preparation gives the joint its chance to settle.', image: 'neck-glue-up', alt: 'Red and black clamps holding a fingerboard to a neck in the workshop', caption: 'Assembly / Fingerboard-to-neck glue-up' }
};
document.querySelectorAll('[data-detail]').forEach(button => button.addEventListener('click', () => {
  const detail = details[button.dataset.detail];
  document.querySelectorAll('[data-detail]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  document.getElementById('detail-label').textContent = detail.label;
  document.getElementById('detail-name').textContent = detail.name;
  document.getElementById('detail-description').textContent = detail.description;
  document.getElementById('detail-caption').textContent = detail.caption;
  const photo = document.getElementById('detail-photo');
  photo.src = `assets/${detail.image}.webp`;
  photo.alt = detail.alt;
}));

// Load Instagram only after an explicit click; keep a direct link visible.
const loadReel = document.getElementById('load-reel');
if (loadReel) {
  loadReel.hidden = false;
  loadReel.addEventListener('click', () => {
    const frame = document.createElement('iframe');
    frame.className = 'instagram-frame';
    frame.title = 'Moon & Pearl: turquoise inlays against Granadillo on Instagram';
    frame.src = 'https://www.instagram.com/reel/CqIoQUSIQ2r/embed/';
    frame.allow = 'encrypted-media; fullscreen; picture-in-picture';
    frame.allowFullscreen = true;
    frame.referrerPolicy = 'strict-origin-when-cross-origin';
    document.getElementById('reel-frame').appendChild(frame);
    document.getElementById('reel-cover').hidden = true;
    document.getElementById('reel-status').textContent = 'Instagram may take a moment to open. If the video is unavailable here, use the direct link below.';
    frame.focus();
  }, { once: true });
}
