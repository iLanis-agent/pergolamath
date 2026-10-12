(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function round1(x) { return Math.round(x * 10) / 10; }

  function rafterPlan(spanCm, pitchCm) {
    if (!(spanCm > 0) || !(pitchCm > 0)) return { error: "the span and the labeled pitch must be positive" };
    if (spanCm < pitchCm) return { error: "the span is shorter than one labeled pitch" };
    var rafters = Math.floor(spanCm / pitchCm) + 1;
    var spare = round1(spanCm - (rafters - 1) * pitchCm);
    var verdict;
    if (rafters <= 4) verdict = "a sparse roof";
    else if (rafters <= 8) verdict = "a typical roof";
    else verdict = "a dense roof";
    return { rafters: rafters, spare: spare, verdict: verdict };
  }

  function postPlan(runCm, bayCm) {
    if (!(runCm > 0) || !(bayCm > 0)) return { error: "the run and the labeled bay must be positive" };
    var bays = Math.ceil(runCm / bayCm);
    var posts = bays + 1;
    var verdict;
    if (bays === 1) verdict = "a single bay";
    else if (bays <= 3) verdict = "a modest run";
    else verdict = "a long run";
    return { bays: bays, posts: posts, verdict: verdict };
  }

  function shadePlan(widthCm, depthCm, coverPct) {
    if (!(widthCm > 0) || !(depthCm > 0)) return { error: "the width and depth must be positive" };
    if (!(coverPct > 0) || !(coverPct <= 100)) return { error: "the labeled coverage must sit above 0 and at or under 100" };
    var shade = round1(widthCm * depthCm / 10000 * coverPct / 100);
    var verdict;
    if (shade < 3) verdict = "a dappled corner";
    else if (shade < 8) verdict = "a sitting spot";
    else verdict = "a full terrace";
    return { shade: shade, verdict: verdict };
  }

  function renderRafter(r, spanCm, pitchCm) {
    return "A span " + spanCm + " cm at a labeled " + pitchCm + " cm pitch takes " + plural(r.rafters, "rafter") + ", both ends included, with " + r.spare + " cm of extra spacing - " + r.verdict + ".";
  }

  function renderPost(r, runCm, bayCm) {
    return "A run " + runCm + " cm long at a labeled " + bayCm + " cm bay becomes " + plural(r.bays, "bay") + " and " + plural(r.posts, "post") + " - " + r.verdict + ".";
  }

  function renderShade(r, widthCm, depthCm, coverPct) {
    return "A footprint " + widthCm + " cm x " + depthCm + " cm at a labeled " + coverPct + "% coverage throws " + r.shade + " sq m of shade - " + r.verdict + ".";
  }

  var api = { rafterPlan: rafterPlan, postPlan: postPlan, shadePlan: shadePlan, renderRafter: renderRafter, renderPost: renderPost, renderShade: renderShade };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.PergolaMath = api;
})(this);
