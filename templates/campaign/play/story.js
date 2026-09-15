window.NRStory = {
  start: {
    bg: "",
    text: "<p class='kicker'>{{SLUG}}</p><p>Replace this node. Nested choices go below. Fill docs/LOCK.md before generating art.</p>",
    choices: [
      { label: "Take the long way (example nested branch).", set: { flagA: true }, goto: "branch_a" },
      { label: "Take the short way.", goto: "end" }
    ]
  },
  branch_a: {
    bg: "",
    text: "<p>You took a branch another playthrough can miss.</p>",
    continue: "end"
  },
  end: {
    bg: "",
    text: "<p>Stop beat. Do not continue past the lock.</p>",
    choices: [{ label: "Restart", restart: true }]
  }
};
