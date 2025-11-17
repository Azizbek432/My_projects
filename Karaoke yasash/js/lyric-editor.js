/* js/lyric-editor.js
   Izoh: Bu skript sizga .lrc yaratishda yordam beradi.
   Ishlash tartibi:
   - Foydalanuvchi audio yuklaydi (yoki serverdan tanlaydi)
   - Raw lyrics oynasiga satrlarni joylaydi (har bir satr yangi qatorda)
   - "Start capture" bosilganda, audio o'ynatilganda har safar Space bosilganda hozirgi satr vaqti olinadi
   - Oxirida "Export .lrc" bosilganda .lrc matnini tayyorlab beradi
*/

const audioInput = document.getElementById('audio-file');
const loadBtn = document.getElementById('load-file');
const editorAudio = document.getElementById('editor-audio');
const rawLyrics = document.getElementById('raw-lyrics');
const startBtn = document.getElementById('start-capture');
const stopBtn = document.getElementById('stop-capture');
const exportBtn = document.getElementById('export-lrc');
const capturedDiv = document.getElementById('captured');
const clearBtn = document.getElementById('clear');

let capturing = false;
let lines = []; // {time, text}
let index = 0;  // qaysi satrga timestamp qo'yilmoqda

// Local audio yuklash
loadBtn.addEventListener('click', () => {
  const file = audioInput.files[0];
  if (!file) { alert('Avvalo audio fayl tanlang'); return; }
  const url = URL.createObjectURL(file);
  editorAudio.src = url;
  editorAudio.load();
});

// Start/stop capture
startBtn.addEventListener('click', () => {
  // Satrlarni massivga ajratamiz
  index = 0;
  const raw = rawLyrics.value.split(/\r?\n/).filter(l => l.trim() !== '');
  if (raw.length === 0) { alert('Avvalo lyricsni pastga yozing (har satr yangi qatorda).'); return; }
  lines = raw.map(text => ({ text, time: null }));
  capturedDiv.innerHTML = '';
  capturing = true;
  editorAudio.focus();
  alert('Capture boshlandi. Audio o\'ynatib, har satrni boshlashda Space tugmasini bosing.');
});

// Stop capture
stopBtn.addEventListener('click', () => {
  capturing = false;
  alert('Capture to‘xtadi.');
});

// Space bosilganda vaqtni saqlash
document.addEventListener('keydown', (e) => {
  if (!capturing) return;
  if (e.code === 'Space') {
    e.preventDefault();
    if (!editorAudio.src) { alert('Audio yuklanmagan'); return; }
    if (index >= lines.length) { alert('Barcha satrlar uchun timestamp berilgan'); return; }
    const t = editorAudio.currentTime;
    lines[index].time = t;
    // DOM ga chiqaramiz (mm:ss.xx format)
    const mm = Math.floor(t / 60).toString().padStart(2,'0');
    const ss = Math.floor(t % 60).toString().padStart(2,'0');
    const cs = Math.floor((t - Math.floor(t)) * 100).toString().padStart(2,'0');
    const timestr = `[${mm}:${ss}.${cs}]`;
    const div = document.createElement('div');
    div.textContent = `${timestr} ${lines[index].text}`;
    capturedDiv.appendChild(div);
    index++;
  }
});

// Export .lrc fayl sifatida matnni tayyorlash va nusxalash
exportBtn.addEventListener('click', () => {
  // Tekshirish: hamma satrga vaqt berilganmi?
  const missing = lines.findIndex(l => l.time === null);
  if (missing !== -1) {
    if (!confirm('Ba\'zi satrlarga timestamp berilmagan. Hali davom etasizmi yoki eksport qilishni istaysizmi?')) {
      return;
    }
  }

  const parts = [];
  for (const l of lines) {
    if (l.time === null) {
      
      parts.push(`[00:00.00] ${l.text}`);
    } else {
      const t = l.time;
      const mm = Math.floor(t / 60).toString().padStart(2,'0');
      const ss = Math.floor(t % 60).toString().padStart(2,'0');
      const cs = Math.floor((t - Math.floor(t)) * 100).toString().padStart(2,'0');
      parts.push(`[${mm}:${ss}.${cs}] ${l.text}`);
    }
  }
  const lrc = parts.join('\n');
 
  navigator.clipboard.writeText(lrc).then(() => {
    alert('.lrc matni clipboardga nusxalandi. Endi uni lyrics papkasiga fayl sifatida saqlang (masalan: another-love.lrc).');
  }).catch(err => {

    const w = window.open('', '_blank', 'width=600,height=600');
    w.document.write('<pre>' + escapeHtml(lrc) + '</pre>');
    w.document.title = 'export.lrc';
    alert('Clipboardga yozib bo‘lmadi — yangi oynada .lrc ko‘rinadi. Uni nusxalab olib .lrc faylga saqlang.');
  });
});

clearBtn.addEventListener('click', () => {
  rawLyrics.value = '';
  capturedDiv.innerHTML = '';
  lines = [];
  index = 0;
});

function escapeHtml(s){ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
