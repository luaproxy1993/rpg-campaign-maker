window.NRSheet = {
  base: function () {
    return {
      strength: 1, dexterity: 1, stamina: 1,
      charisma: 1, manipulation: 1, composure: 1,
      intelligence: 1, wits: 1, resolve: 1,
      athletics: 0, combat: 0, drive: 1, persuasion: 0,
      subterfuge: 0, awareness: 0, investigation: 0, survival: 0, technology: 0,
      health: 5, healthMax: 5, items: []
    };
  },
  add: function (s, delta) {
    if (!delta) return;
    Object.keys(delta).forEach(function (k) {
      s[k] = (s[k] || 0) + delta[k];
    });
  },
  give: function (s, it) {
    s.items = s.items || [];
    s.items.push(it);
  },
  check: function (s, attr, skill, hard, mixed) {
    hard = hard || 4;
    mixed = mixed == null ? 2 : mixed;
    var pool = (s[attr] || 0) + (s[skill] || 0);
    var deg = pool >= hard ? "success" : pool >= mixed ? "mixed" : "fail";
    return { pool: pool, hard: hard, deg: deg, formula: attr + "+" + skill };
  },
  html: function (s) {
    var items = (s.items || []).map(function (it) { return it.name || it.id; }).join(", ") || "—";
    return "<h2>Sheet</h2><p>Health " + s.health + "/" + s.healthMax + "</p><p>Items: " + items + "</p>";
  },
  recalc: function () {}
};
