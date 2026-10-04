// One shared cycle. Every animation is a Web Animation, so exporting a GIF is just
// "pause everything, set currentTime, screenshot" — deterministic, frame-exact.
(function () {
  var T = 6500, OUT = 6000, GONE = 6400;
  var EASE = {
    spring: "cubic-bezier(0.2, 1.05, 0.35, 1)",   // the site's SPRING
    out:    "cubic-bezier(0.2, 0.7, 0.2, 1)",     // the site's EASE_OUT
    easeOut:"cubic-bezier(0, 0, 0.58, 1)",        // framer-motion "easeOut"
    linear: "linear"
  };
  function once(el, k) {
    var s = k.t * 1000, e = Math.min(s + k.d * 1000, OUT);
    var frames = [
      Object.assign({}, k.from, { offset: 0 }),
      Object.assign({}, k.from, { offset: s / T, easing: EASE[k.e || "spring"] }),
      Object.assign({}, k.to,   { offset: e / T }),
      Object.assign({}, k.to,   { offset: 1 })
    ];
    el.animate(frames, { duration: T, iterations: Infinity, fill: "both" });
  }
  function repeat(el, r) {
    // framer-motion repeat + repeatDelay: one pulse of length d, then rest, then again
    var frames = [Object.assign({}, r.from, { offset: 0, easing: EASE[r.e || "easeOut"] }), Object.assign({}, r.to, { offset: r.d / r.p }), Object.assign({}, r.to, { offset: 1 })];
    if (r.mid) frames.splice(1, 0, Object.assign({}, r.mid.v, { offset: r.mid.at * r.d / r.p, easing: EASE[r.e || "easeOut"] }));
    el.animate(frames, { duration: r.p * 1000, delay: r.t * 1000, iterations: Infinity, fill: "none" });
  }
  function build() {
    document.querySelectorAll("[data-k]").forEach(function (el) { once(el, JSON.parse(el.dataset.k)); });
    document.querySelectorAll("[data-r]").forEach(function (el) { repeat(el, JSON.parse(el.dataset.r)); });
    document.querySelectorAll("[data-mq]").forEach(function (el) {
      var m = JSON.parse(el.dataset.mq);
      el.animate([{ transform: "translateX(-25%)" }, { transform: "translateX(-50%)" }], { duration: m.p * 1000, iterations: Infinity, easing: "linear" });
    });
    // only the diagram leaves and comes back; type, numerals and panels never move
    document.querySelectorAll(".dia").forEach(function (el) {
      el.animate([{ opacity: 1, offset: 0 }, { opacity: 1, offset: OUT / T }, { opacity: 0, offset: GONE / T }, { opacity: 0, offset: 1 }], { duration: T, iterations: Infinity });
    });
    if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      document.getAnimations().forEach(function (a) { a.pause(); a.currentTime = 5000; });
    }
  }
  window.__seek = function (ms) { document.getAnimations().forEach(function (a) { a.pause(); a.currentTime = ms; }); };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", build); else build();
})();
