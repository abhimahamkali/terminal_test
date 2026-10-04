"""Builds small_dogs_gif_carousel.html — slides 3-15 of the first section of
tendsmall.com/built-for-small-dogs-not-all-dogs, copy verbatim from the live page,
diagrams rebuilt from the site's Framer components (Slide3.tsx, Slide4ani-15ani.tsx):
same geometry, delays, staggers and easing, inside the Cream Poster template."""
import json, pathlib

HERE = pathlib.Path(__file__).parent
N, D0 = 13, 0.75            # D0 = when the diagram starts (the site's INITIAL_DELAY, after our header)

def K(frm, to, t, d, e="spring"):
    return "data-k='" + json.dumps({"from": frm, "to": to, "t": round(t, 3), "d": d, "e": e}) + "'"

def R(frm, to, t, d, p, e="easeOut", mid=None):
    o = {"from": frm, "to": to, "t": round(t, 3), "d": d, "p": p, "e": e}
    if mid: o["mid"] = mid
    return "data-r='" + json.dumps(o) + "' style=\"opacity:0\""

HIDE = {"opacity": 0}
def rise(dy="1.6cqw"): return {"opacity": 0, "transform": f"translateY({dy})"}
SHOW = {"opacity": 1, "transform": "none"}
DRAW0 = {"strokeDashoffset": 1, "opacity": 0}

# ---------------- site slide 3 (Slide3.tsx: lines S2+i*.2, dash S2+.6, closing S2+.8)
D_THREE = ('<div class="three">'
  + "".join(f'<p {K(rise("1.2cqw"), SHOW, D0 + i*.2, .55)}>{l}</p>'
            for i, l in enumerate(["They eat less.", "They burn faster.", "They feel everything sooner"]))
  + f'<p class="dash" {K(HIDE, {"opacity": .45}, D0 + .6, .4, "out")}>—</p></div>')

# ---------------- site slide 4 (Slide4ani: 92/62/34, delay .5 + i*.18, fill 1.0s spring)
def _bar_row(label, color, pct, d, extra=""):
    return (f'<div class="bar-row" {K({"opacity": 0, "transform": "translateX(-0.8cqw)"}, SHOW, d, .4)}>'
            f'<div class="track"><div class="fill" style="background:{color}" '
            f'{K({"transform": "scaleX(0)"}, {"transform": f"scaleX({pct/100})"}, d + .05, 1.0)}></div>{extra}</div>'
            f'<span class="bar-lbl">{label}</span></div>')
D_BARS = ('<div class="bars">' + _bar_row("Eats", "var(--teal)", 92, D0)
          + _bar_row("Absorbs", "var(--teal-lt)", 62, D0 + .18) + _bar_row("Uses", "var(--pink)", 34, D0 + .36) + '</div>')

# ---------------- site slide 5 (Slide5ani: W480 H72, wave 1.4s easeOut, dots +.15+i*.1, rings repeat)
W, H = 480, 72
_wave = (f"M0,{H/2} C{W*.08},{H*.2} {W*.16},{H*.9} {W*.25},{H*.7} S{W*.42},{H*.1} {W*.5},{H*.25} "
         f"S{W*.7},{H*.85} {W*.75},{H*.65} S{W*.92},{H*.1} {W},{H*.55}")
_dots5 = [(W*.10, 28, "WATER"), (W*.36, 56, "FOOD"), (W*.62, 22, "MOVEMENT"), (W*.88, 52, "TEMPERATURE")]
D_WAVE = (f'<svg class="svgd" viewBox="-20 -10 {W+40} {H+52}" style="width:78cqw">'
  f'<path class="draw" d="{_wave}" pathLength="1" fill="none" stroke="#E8366E" stroke-width="2.8" stroke-linecap="round" '
  f'{K(DRAW0, {"strokeDashoffset": 0, "opacity": .8}, D0, 1.4, "easeOut")}/>'
  + "".join(
      "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="none" stroke="#E8366E" stroke-width="1.2" '
              f'{R({"transform": "scale(1)", "opacity": .5}, {"transform": f"scale({s})", "opacity": 0}, D0 + .15 + i*.12 + ri*.35, 1.8, 3.8)}/>'
              for ri, s in enumerate([1.8, 3.0]))
      + f'<circle cx="{x}" cy="{y}" r="7" fill="#E8366E" {K({"transform": "scale(0)", "opacity": 0}, {"transform": "scale(1)", "opacity": 1}, D0 + .15 + i*.1, .4)}/>'
      + f'<text x="{x}" y="{H+28}" text-anchor="middle" font-size="13" font-weight="700" letter-spacing="0.09em" fill="#0A0A0A" '
        f'style="font-family:var(--sans)" {K(HIDE, {"opacity": .55}, D0 + .25 + i*.1, .35, "easeOut")}>{lab}</text>'
      for i, (x, y, lab) in enumerate(_dots5))
  + '</svg>')

# ---------------- site slide 6 (Slide6ani: rows .5 / .65, fills spring, 65% absorbed, "unabsorbed" +.9)
D_CAL = ('<div class="bars">'
  + _bar_row("On the Label", "var(--coral)", 100, D0).replace("translateX(-0.8cqw)", "translateY(1cqw)")
  + _bar_row("In the Dog", "linear-gradient(to right, #E07060, rgba(224,112,96,0.25))", 65, D0 + .15,
             extra=f'<span class="unab" {K(HIDE, {"opacity": .5}, D0 + .15 + .9, .4, "easeOut")}>unabsorbed</span>').replace("translateX(-0.8cqw)", "translateY(1cqw)")
  + '</div>')

# ---------------- site slide 7 (Slide7ani: R120, nodes D0+i*.12, labels +.1, arcs +.45+i*.18, ring pulse every 4s)
import math
_n7 = [(-90, "bowl offered"), (0, "refusal"), (90, "food swap"), (180, "acceptance")]
_p7 = [(150 + 120*math.cos(math.radians(a)), 150 + 120*math.sin(math.radians(a)), l) for a, l in _n7]
def _lbl7(x, y):
    pad = 25
    lx = x + (-pad if x < 145 else pad if x > 155 else 0)
    ly = y + (-pad - 4 if y < 145 else pad + 9 if y > 155 else 5)
    anc = "end" if x < 145 else "start" if x > 155 else "middle"
    return lx, ly, anc
D_LOOP = ('<svg class="svgd" viewBox="-92 -22 484 344" style="width:54cqw"><defs>'
  '<marker id="arr7" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#E8366E"/></marker></defs>'
  + "".join(f'<path class="draw" d="M{a[0]:.1f},{a[1]:.1f} A120,120 0 0,1 {b[0]:.1f},{b[1]:.1f}" pathLength="1" fill="none" stroke="#E8366E" '
            f'stroke-width="1.6" stroke-linecap="round" marker-end="url(#arr7)" '
            f'{K(DRAW0, {"strokeDashoffset": 0, "opacity": .7}, D0 + .45 + i*.18, .6, "easeOut")}/>'
            for i, (a, b) in enumerate(zip(_p7, _p7[1:] + _p7[:1])))
  + "".join(
      f'<circle cx="{x:.1f}" cy="{y:.1f}" r="15" fill="none" stroke="#E8366E" stroke-width="1" '
      f'{R({"transform": "scale(1)", "opacity": .6}, {"transform": "scale(2.2)", "opacity": 0}, D0 + .5 + i*.25, 1.6, 4.0)}/>'
      f'<circle cx="{x:.1f}" cy="{y:.1f}" r="15" fill="#E8366E" {K({"transform": "scale(0)", "opacity": 0}, {"transform": "scale(1)", "opacity": .15}, D0 + i*.12, .35)}/>'
      f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#E8366E" {K({"transform": "scale(0)", "opacity": 0}, {"transform": "scale(1)", "opacity": 1}, D0 + .02 + i*.12, .35)}/>'
      + (lambda lx, ly, anc: f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anc}" font-size="15" font-weight="700" fill="#E8366E" '
         f'style="font-family:var(--sans)" {K(HIDE, {"opacity": 1}, D0 + .1 + i*.12, .3, "easeOut")}>{l}</text>')(*_lbl7(x, y))
      for i, (x, y, l) in enumerate(_p7))
  + '</svg>')

# ---------------- site slide 8 (Slide8ani: spheres fade/scale at .5, labels +.38…+.68, ripples 3.5s every 1.15s)
_rip = lambda t: R({"transform": "scale(0.75)", "opacity": 0}, {"transform": "scale(3)", "opacity": 0}, t, 3.5, 3.5,
                   e="easeOut", mid={"at": .12, "v": {"opacity": .55}})
D_RINGS = (f'<svg class="svgd" viewBox="0 0 300 278" style="width:42cqw" {K({"opacity": 0, "transform": "scale(0.88)"}, SHOW, D0, .7)}><defs>'
  '<radialGradient id="g8c" cx="35%" cy="28%" r="65%"><stop offset="0%" stop-color="rgba(248,200,212,0.22)"/><stop offset="55%" stop-color="rgba(237,130,165,0.14)"/><stop offset="100%" stop-color="rgba(210,60,105,0.20)"/></radialGradient>'
  '<radialGradient id="g8s" cx="38%" cy="32%" r="62%"><stop offset="0%" stop-color="rgba(252,210,225,0.72)"/><stop offset="100%" stop-color="rgba(220,90,135,0.60)"/></radialGradient>'
  '<radialGradient id="g8g" cx="40%" cy="35%" r="60%"><stop offset="0%" stop-color="rgba(248,170,195,0.97)"/><stop offset="100%" stop-color="rgba(195,40,85,0.92)"/></radialGradient></defs>'
  '<circle cx="130" cy="148" r="105" fill="url(#g8c)"/>'
  '<circle cx="130" cy="148" r="76" fill="url(#g8s)" stroke="rgba(232,54,110,0.35)" stroke-width="1.5"/>'
  '<circle cx="130" cy="148" r="45" fill="url(#g8g)" stroke="rgba(232,54,110,0.55)" stroke-width="1.5"/>'
  + "".join(f'<circle cx="130" cy="148" r="45" fill="none" stroke="#E8366E" stroke-width="1.5" {_rip(D0 - .5 + dl)}/>' for dl in (0, 1.15, 2.3))
  + "".join(f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke="#E8366E" stroke-width="1" stroke-dasharray="3 3" stroke-opacity="0.6" {K(HIDE, {"opacity": 1}, D0 + tl, .4, "easeOut")}/>'
            f'<text x="{tx}" y="{ty}" text-anchor="{anc}" font-size="14" font-weight="700" fill="#E8366E" style="font-family:var(--sans)" {K(HIDE, {"opacity": 1}, D0 + tl + .06, .4, "easeOut")}>{lab}</text>'
            for a, b, c, d, tx, ty, anc, lab, tl in [(175, 148, 244, 148, 249, 153, "start", "Gut", .38),
                                                     (184, 94, 218, 65, 223, 63, "start", "Skin", .50),
                                                     (130, 43, 130, 16, 130, 9, "middle", "Coat", .62)])
  + '</svg>')

# ---------------- site slide 9 (Slide9ani: boxes D0+i*.12, lines +.45, focal dot after the 5th line)
_lab9 = ["Digestion", "Hydration", "Energy", "Behaviour", "Coat"]
D_CONV = ('<svg class="svgd" viewBox="-48 -12 576 178" style="width:80cqw">'
  + "".join(f'<line class="draw" x1="{120*i}" y1="38" x2="240" y2="130" pathLength="1" stroke="#fff" stroke-width="1.2" stroke-opacity="0.5" '
            f'{K(DRAW0, {"strokeDashoffset": 0, "opacity": 1}, D0 + .45 + i*.12, .5, "easeOut")}/>' for i in range(5))
  + f'<circle cx="240" cy="130" r="6" fill="#fff" {K({"transform": "scale(0)", "opacity": 0}, {"transform": "scale(1)", "opacity": 1}, D0 + .45 + 5*.12, .4)}/>'
  + "".join(f'<rect x="{120*i-44}" y="0" width="88" height="38" rx="6" fill="#E8366E" {K({"opacity": 0, "transform": "translateY(-8px)"}, SHOW, D0 + i*.12, .4)}/>'
            f'<text x="{120*i}" y="24.3" text-anchor="middle" font-size="14" font-weight="700" fill="#fff" style="font-family:var(--sans)" '
            f'{K(HIDE, {"opacity": 1}, D0 + .1 + i*.12, .3, "easeOut")}>{l}</text>' for i, l in enumerate(_lab9))
  + '</svg>')

# ---------------- site slide 10 (Slide10ani: pill track x -25% → -50% over 18s, fades in at .5)
_base10 = ["• ADD A CHEW", "• ADD A POWDER", "• ADD A TOPPER", "• ADD A SUPPLEMENT", "• ADD A CHEW", "• ADD A POWDER"]
D_MQ = (f'<div class="mq" {K(HIDE, {"opacity": 1}, D0, .5, "easeOut")}><div class="mrow" data-mq=\'{{"p": 18}}\'>'
        + "".join(f'<span class="mp">{p}</span>' for p in _base10 * 4) + '</div></div>')

# ---------------- site slide 11 (Slide11ani: label .4, lines D0+.08+i*.15, outline +.15, table +.4)
def _watch(pre, key, d):
    return (f'<div class="watch" {K({"opacity": 0, "transform": "translateY(0.8cqw)"}, SHOW, d, .45)}>{pre}'
            f'<span class="hl">{key}<svg viewBox="0 0 100 30" preserveAspectRatio="none">'
            f'<rect class="draw" x="1" y="1" width="98" height="28" rx="12" fill="none" stroke="#E8366E" stroke-width="2" '
            f'vector-effect="non-scaling-stroke" pathLength="1" {K(DRAW0, {"strokeDashoffset": 0, "opacity": .65}, d + .15, .45, "easeOut")}/>'
            f'</svg></span>.</div>')
_rows11 = [("4kg","20g",".28","1.2"),("5kg","22g",".31","1.3"),("6kg","25g",".34","1.4"),("7kg","28g",".37","1.5"),
           ("8kg","31g","40","1.6"),("9kg","34g","43","1.7"),("10kg","37g",".46","1.8"),("11kg","40g",".49","1.9")]
D_READ = ('<div class="rd"><div>'
  f'<p class="cap" {K(HIDE, {"opacity": .4}, D0, .3, "easeOut")}>READ THE DOG.</p><div class="lines">'
  + _watch("Watch ", "what she eats", D0 + .08) + _watch("Watch ", "what she leaves", D0 + .23)
  + _watch("Watch how ", "her coat carries", D0 + .38) + _watch("Watch how ", "her energy holds", D0 + .53)
  + f'</div></div><div {K(HIDE, {"opacity": 1}, D0 + .4, .6, "easeOut")}><p class="cap" style="opacity:.4">NOT THE CHART.</p><div class="tbl">'
  + "".join("<div>" + "".join(f"<span>{c}</span>" for c in r) + "</div>" for r in _rows11)
  + '</div></div></div>')

# ---------------- site slide 12 (Slide12ani: nodes D0+i*.08, curved arrows +.45+i*.08)
_n12 = [("Gut", 180, 56), ("Hydration", 294, 138), ("Energy", 252, 276), ("Behaviour", 108, 276), ("Eating", 66, 138)]
_a12 = ["M211,68 Q260,86 281,112", "M292,170 Q288,228 268,256", "M225,294 Q180,308 135,294", "M89,256 Q70,228 68,170", "M82,112 Q102,84 149,68"]
D_PENTA = ('<svg class="svgd" viewBox="0 0 360 340" style="width:40cqw"><defs>'
  '<marker id="arr12" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="rgba(255,255,255,0.55)"/></marker></defs>'
  + "".join(f'<path class="draw" d="{d}" pathLength="1" fill="none" stroke="rgba(255,255,255,0.55)" stroke-width="1.8" stroke-linecap="round" '
            f'marker-end="url(#arr12)" {K(DRAW0, {"strokeDashoffset": 0, "opacity": 1}, D0 + .45 + i*.08, .55)}/>' for i, d in enumerate(_a12))
  + "".join(f'<g {K({"transform": "scale(0.4)", "opacity": 0}, {"transform": "scale(1)", "opacity": 1}, D0 + i*.08, .6)}>'
            f'<circle cx="{x}" cy="{y}" r="48" fill="#E8366E" stroke="#E8366E" stroke-width="1.8"/>'
            f'<text x="{x}" y="{y+5}" text-anchor="middle" font-size="15" font-weight="600" fill="#fff" style="font-family:var(--sans)">{l}</text></g>'
            for i, (l, x, y) in enumerate(_n12))
  + '</svg>')

# ---------------- site slide 13 (Slide13ani: whole row rises at .5)
D_EQ = (f'<div class="eq" {K(rise("1cqw"), SHOW, D0, .55)}><div class="pill l"><span>What your dog eats</span></div>'
        '<span class="times">×</span><div class="pill r">What gets delivered</div></div>')

# ---------------- site slide 14 (Slide14ani: whole block rises at .5; stacked as on the site's mobile layout)
D_ER = (f'<div class="er" {K(rise("1.2cqw"), SHOW, D0, .55)}>'
        '<div class="er-h en"><span class="sym">×</span><span class="w">Enough</span></div>'
        '<div class="er-i en-i"><p>Meets a standard.</p><p>Passes a minimum.</p><p>Fits no dog in particular.</p></div>'
        '<div class="div"></div>'
        '<div class="er-h ri-h"><span class="sym ck">✓</span><span class="w">Right</span></div>'
        '<div class="er-i"><p>Fits the dog in front of you.</p><p>Delivers what it claims.</p><p>Works with the system, not around it.</p></div></div>')

# ---------------- site slide 15 (Slide15ani: lines and bags at D0, D0+.6, D0+1.2)
_BAG = "M20,8 L52,8 L58,20 L58,84 Q58,92 50,92 L22,92 Q14,92 14,84 L14,20 Z"
def _bag(label, color, d):
    return (f'<figure class="bag"><svg viewBox="0 0 72 96"><path d="{_BAG}" fill="rgba(10,10,10,0.08)"/>'
            f'<path d="{_BAG}" fill="{color}" {K(HIDE, {"opacity": 1}, d, .6, "easeOut")}/>'
            f'<path d="M26,8 C28,2 44,2 46,8" fill="none" stroke="{color}" stroke-width="2" {K(HIDE, {"opacity": .8}, d + .1, .4, "easeOut")}/>'
            f'</svg><figcaption>{label}</figcaption></figure>')
D_FITS = ('<div class="fits"><div class="lines">'
  + "".join(f'<p {K({"opacity": 0, "transform": "translateY(1cqw)"}, {"opacity": .8, "transform": "none"}, D0 + i*.6, .5)}>{l}</p>'
            for i, l in enumerate(["Digestion works quietly.", "The coat carries the signal.", "Energy holds a steady line."]))
  + '</div><div class="bags">' + _bag("Eats", "#E07060", D0) + _bag("Absorbs", "#C05040", D0 + .6) + _bag("Uses", "#E8366E", D0 + 1.2)
  + '</div></div>')

# ---------------- slides: copy verbatim from the live page
S = [
 dict(navy=1, h="Small dogs have less room for error.", stage=D_THREE, b="Smaller bodies. Tighter margins. Less buffer.", P=D0 + .8),
 dict(h="Digestion isn't what you see.", sub="Not the empty bowl. Not the clean plate.<br>The invisible part — what the body actually uses.",
      stage=D_BARS, a="What matters isn't what goes in.", b="It's what makes it through.", P=2.3),
 dict(h="Hydration isn't moisture.", sub="It's how the body regulates itself — every hour, all day.<br>Through food, water, movement, temperature.",
      stage=D_WAVE, a="Food plays a part.", b="It doesn't carry the whole thing.", P=2.3),
 dict(navy=1, h="Calories in ≠ Calories used.", sub="What's on the pack isn't what the body extracts.<br>Small dogs burn faster. There's less room for error.",
      stage=D_CAL, a="Unabsorbed calories still count on the label.", b="They don't count for the dog.", P=2.1),
 dict(h="Most picky eating is learned.", sub="Not personality. Not breed.<br>A pattern built between the bowl and the hand that fills it.",
      stage=D_LOOP, a="The food is rarely the problem.", b="The pattern around it is.", P=2.45),
 dict(h="The coat is a signal.", sub="Dullness, dryness, shedding — surface symptoms.<br>What you see outside is what the inside is doing.",
      stage=D_RINGS, a="Treat the coat, treat the surface.", b="Treat the cause, the coat follows.", P=2.0),
 dict(navy=1, setup="Five systems.", h="One mistake.", sub="They all look different. The mistake is the same<br>— treat the symptom, miss the cause.",
      stage=D_CONV, a="Different problems.", b="Same shape.", P=2.3),
 dict(setup="Treat everything the same way,", h="you miss the system.",
      sub="Add something. Expect a result.<br>Add something else. Expect another result.<br>The loop repeats. The cause stays hidden.",
      stage=D_MQ, a="What's missing isn't ingredients.", b="It's a model of how the body actually works.", P=1.8),
 dict(h="Read the dog. Not the chart.", sub="Charts describe dogs in general.<br>Your dog isn't in general.",
      stage=D_READ, a="This is the evidence.", b="Everything else is a proxy.", P=2.0),
 dict(navy=1, h="Your dog isn't separate systems.",
      sub="Gut affects coat. Hydration affects energy. Energy affects behaviour. Behaviour affects eating. Eating affects gut.",
      stage=D_PENTA, a="Treat any one in isolation — incomplete answer.", b="Everything works together. Or nothing quite does.", P=2.2),
 dict(h="What matters most.", sub="Intake is half the equation.<br>Delivery is the other half.<br>The answer is what the body actually receives.",
      stage=D_EQ, b="It's the only number that counts.", P=1.7),
 dict(h="Most food is enough.", stage=D_ER,
      a="The distance between enough and right isn't dramatic.", b="It's just consistent. Every day. For years.", P=1.8),
 dict(h="When food fits the system —", stage=D_FITS, b="Everything downstream settles.", P=2.7, last=1),
]
assert len(S) == N

def frame(i, s):
    n = i + 1
    dots = "".join('<i class="on"></i>' if k == n else "<i></i>" for k in range(1, N + 1))
    setup = f'<div class="setup" {K(rise(), SHOW, .08, .55)}>{s["setup"]}</div>' if s.get("setup") else ""
    sub = f'<p class="sub" {K(rise("1.2cqw"), SHOW, .3, .6)}>{s["sub"]}</p>' if s.get("sub") else ""
    P = s["P"]
    pa = f'<span class="a" {K(rise("1.2cqw"), SHOW, P, .55)}>{s["a"]}</span>' if s.get("a") else ""
    pb = f'<span class="b" {K(rise("1.2cqw"), SHOW, P + (.25 if s.get("a") else 0), .55)}>{s["b"]}</span>'
    swipe = "" if s.get("last") else '<div class="mk br">Swipe →</div>'
    cls = "f" + (" navy" if s.get("navy") else "")
    return f"""
    <div class="framewrap">
      <div class="framelabel">{n:02d} · site slide {n + 2}</div>
      <div class="{cls}" data-name="{n:02d}">
        <div class="mk tl">Built for small dogs. Not all dogs.</div>
        <div class="dots" aria-label="Slide {n} of {N}">{dots}</div>
        <div class="rule t"></div>
        <div class="inner">
          <div class="hd">
            <div class="num" {K(rise("2cqw"), SHOW, 0, .55)}>{n:02d}</div>
            <div class="ht">{setup}<h2 class="h" {K(rise(), SHOW, .12, .55)}>{s["h"]}</h2>{sub}</div>
          </div>
          <div class="stage" {K(HIDE, {"opacity": 1}, .3, .5, "out")}>{s["stage"]}</div>
          <p class="punch">{pa}{pb}</p>
        </div>
        <div class="rule b"></div>
        {swipe}
      </div>
    </div>"""

html = f"""<title>Built For Small Dogs</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Figtree:wght@400;500;600;700;800;900&family=DM+Mono:wght@400;500&display=swap">
<style>
{(HERE / "carousel.css").read_text()}
</style>
<div class="page">
  <header class="masthead">
    <div class="kicker">Animated carousel · {N} frames · 6.5s loop</div>
    <h1>Built for small dogs</h1>
    <p>Slides 3–15 of the first section of tendsmall.com/built-for-small-dogs-not-all-dogs, word for word. Diagrams rebuilt from the site's own animation components, set in the Cream Poster template.</p>
  </header>
  <div class="deck">{"".join(frame(i, s) for i, s in enumerate(S))}
  </div>
</div>
<script>
{(HERE / "animate.js").read_text()}
</script>
"""
(HERE / "small_dogs_gif_carousel.html").write_text(html)
print("wrote", len(html), "bytes")
