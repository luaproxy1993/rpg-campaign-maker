(function () {
  const SAVE = "{{SLUG}}:v1";
  const $ = (id) => document.getElementById(id);
  const S = window.NRSheet;
  const NODES = window.NRStory;
  let state = boot();

  function boot() {
    const s = S.base();
    s.node = "start";
    s.flags = [];
    return s;
  }

  function setBg(src) {
    $("bg").style.backgroundImage = src ? "url('" + src + "')" : "none";
  }
  function setSpeaker(spec) {
    const nameEl = $("nameplate");
    const img = $("speaker");
    if (!spec || !spec.name) {
      nameEl.classList.add("hidden");
      img.classList.add("hidden");
      return;
    }
    nameEl.textContent = spec.name;
    nameEl.classList.remove("hidden");
    if (spec.img) { img.src = spec.img; img.classList.remove("hidden"); }
    else img.classList.add("hidden");
  }

  function go(id) {
    state.node = id;
    play();
  }

  function applyChoice(ch) {
    if (ch.restart) { state = boot(); play(); return; }
    S.add(state, ch.apply);
    if (ch.set) Object.keys(ch.set).forEach((k) => { state[k] = ch.set[k]; });
    if (ch.items) ch.items.forEach((it) => S.give(state, it));
    if (ch.check) {
      const r = S.check(state, ch.check.attr, ch.check.skill, ch.check.hard, ch.check.mixed);
      $("dice").classList.remove("hidden");
      $("dice").textContent = r.formula + " = " + r.pool + " → " + r.deg;
    }
    go(ch.goto);
  }

  function play() {
    const node = NODES[state.node];
    if (!node) return;
    $("choices").innerHTML = "";
    $("btn-continue").classList.add("hidden");
    $("dice").classList.add("hidden");
    setBg(node.bg);
    setSpeaker(node.speaker || null);
    $("story").innerHTML = node.text;
    if (node.continue && !node.choices) {
      $("btn-continue").classList.remove("hidden");
      $("btn-continue").onclick = () => go(node.continue);
    }
    (node.choices || []).forEach((ch) => {
      if (ch.visible && !ch.visible(state)) return;
      const b = document.createElement("button");
      b.type = "button";
      b.textContent = ch.label;
      b.addEventListener("click", () => applyChoice(ch));
      $("choices").appendChild(b);
    });
    const sheet = $("sheet");
    if (sheet && !sheet.classList.contains("hidden")) sheet.innerHTML = S.html(state);
  }

  $("btn-reset").addEventListener("click", () => { state = boot(); play(); });
  $("btn-sheet").addEventListener("click", () => {
    $("sheet").classList.toggle("hidden");
    if (!$("sheet").classList.contains("hidden")) $("sheet").innerHTML = S.html(state);
  });

  window.CampaignGame = { getState: () => state, play };
  play();
})();
