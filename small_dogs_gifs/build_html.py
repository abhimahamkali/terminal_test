"""Builds small_dogs_gif_carousel.html: an intro frame plus slides 3-15 of the first section of
tendsmall.com/built-for-small-dogs-not-all-dogs. Copy is verbatim from the live page (split into
a serif setup and a black payoff); diagrams are rebuilt from the site's Framer components
(Slide3.tsx, Slide4ani-15ani.tsx). Type and frame are static; only the diagram animates."""
import json, math, pathlib

HERE = pathlib.Path(__file__).parent
D0 = 0.5                      # the site's INITIAL_DELAY

def K(frm, to, t, d, e="spring"):
    return "data-k='" + json.dumps({"from": frm, "to": to, "t": round(t, 3), "d": d, "e": e}) + "'"
def R(frm, to, t, d, p, e="easeOut", mid=None):
    o = {"from": frm, "to": to, "t": round(t, 3), "d": d, "p": p, "e": e}
    if mid: o["mid"] = mid
    return "data-r='" + json.dumps(o) + "' style=\"opacity:0\""
HIDE = {"opacity": 0}
SHOW = {"opacity": 1, "transform": "none"}
def rise(dy): return {"opacity": 0, "transform": f"translateY({dy})"}
DRAW0 = {"strokeDashoffset": 1, "opacity": 0}
POP0 = {"transform": "scale(0)", "opacity": 0}
SANS = 'style="font-family:var(--sans)"'

# --- site slide 3 (Slide3.tsx: lines i*.2; the live page shows no dash before the closing line)
D_THREE = ('<div class="three">'
  + "".join(f'<p {K(rise("1.2cqw"), SHOW, D0 + i*.2, .55)}>{l}</p>'
            for i, l in enumerate(["They eat less.", "They burn faster.", "They feel everything sooner"]))
  + '</div>')

# --- site slides 4 and 6 (Slide4ani / Slide6ani)
def _bar_row(label, color, pct, d, enter, extra=""):
    return (f'<div class="bar-row" {K(enter, SHOW, d, .4 if "X" in enter["transform"] else .45, "spring" if "X" in enter["transform"] else "out")}>'
            f'<div class="track"><div class="fill" style="background:{color}" '
            f'{K({"transform": "scaleX(0)"}, {"transform": f"scaleX({pct/100})"}, d + .05, 1.0)}></div>{extra}</div>'
            f'<span class="bar-lbl">{label}</span></div>')
_inX = {"opacity": 0, "transform": "translateX(-0.8cqw)"}
_inY = {"opacity": 0, "transform": "translateY(1cqw)"}
D_BARS = ('<div class="bars">' + _bar_row("Eats", "var(--teal)", 92, D0, _inX)
          + _bar_row("Absorbs", "var(--teal-lt)", 62, D0 + .18, _inX) + _bar_row("Uses", "var(--dacc)", 34, D0 + .36, _inX) + '</div>')
D_CAL = ('<div class="bars">' + _bar_row("On the Label", "var(--coral)", 100, D0, _inY)
         + _bar_row("In the Dog", "linear-gradient(to right, #E07060, rgba(224,112,96,0.25))", 65, D0 + .15, _inY,
                    extra=f'<span class="unab" {K(HIDE, {"opacity": .5}, D0 + .15 + .9, .4, "easeOut")}>unabsorbed</span>')
         + '</div>')

# --- site slide 5 (Slide5ani)
W, H = 480, 72
_wave = (f"M0,{H/2} C{W*.08},{H*.2} {W*.16},{H*.9} {W*.25},{H*.7} S{W*.42},{H*.1} {W*.5},{H*.25} "
         f"S{W*.7},{H*.85} {W*.75},{H*.65} S{W*.92},{H*.1} {W},{H*.55}")
_d5 = [(W*.10, 28, "WATER"), (W*.36, 56, "FOOD"), (W*.62, 22, "MOVEMENT"), (W*.88, 52, "TEMPERATURE")]
D_WAVE = (f'<svg class="svgd" viewBox="-20 -10 {W+40} {H+52}" style="width:84cqw">'
  f'<path class="draw as" d="{_wave}" pathLength="1" fill="none" stroke-width="2.8" stroke-linecap="round" {K(DRAW0, {"strokeDashoffset": 0, "opacity": .8}, D0, 1.4, "easeOut")}/>'
  + "".join(
      "".join(f'<circle class="as" cx="{x}" cy="{y}" r="7" fill="none" stroke-width="1.2" '
              f'{R({"transform": "scale(1)", "opacity": .5}, {"transform": f"scale({s})", "opacity": 0}, D0 + .15 + i*.12 + ri*.35, 1.8, 3.8)}/>' for ri, s in enumerate([1.8, 3.0]))
      + f'<circle class="af" cx="{x}" cy="{y}" r="7" {K(POP0, {"transform": "scale(1)", "opacity": 1}, D0 + .15 + i*.1, .4)}/>'
      + f'<text x="{x}" y="{H+28}" text-anchor="middle" font-size="13" font-weight="700" letter-spacing="0.09em" fill="#0A0A0A" {SANS} '
        f'{K(HIDE, {"opacity": .55}, D0 + .25 + i*.1, .35, "easeOut")}>{lab}</text>'
      for i, (x, y, lab) in enumerate(_d5))
  + '</svg>')

# --- site slide 7 (Slide7ani)
_p7 = [(150 + 120*math.cos(math.radians(a)), 150 + 120*math.sin(math.radians(a)), l)
       for a, l in [(-90, "bowl offered"), (0, "refusal"), (90, "food swap"), (180, "acceptance")]]
def _lbl7(x, y):
    lx = x + (-25 if x < 145 else 25 if x > 155 else 0)
    ly = y + (-30 if y < 145 else 40 if y > 155 else 6)
    return lx, ly, ("end" if x < 145 else "start" if x > 155 else "middle")
D_LOOP = ('<svg class="svgd" viewBox="-100 -26 500 356" style="width:60cqw"><defs>'
  '<marker id="arr7" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path class="af" d="M0,0 L6,3 L0,6 Z"/></marker></defs>'
  + "".join(f'<path class="draw as" d="M{a[0]:.1f},{a[1]:.1f} A120,120 0 0,1 {b[0]:.1f},{b[1]:.1f}" pathLength="1" fill="none" stroke-width="1.7" '
            f'stroke-linecap="round" marker-end="url(#arr7)" {K(DRAW0, {"strokeDashoffset": 0, "opacity": .7}, D0 + .45 + i*.18, .6, "easeOut")}/>'
            for i, (a, b) in enumerate(zip(_p7, _p7[1:] + _p7[:1])))
  + "".join(
      f'<circle class="as" cx="{x:.1f}" cy="{y:.1f}" r="15" fill="none" stroke-width="1" '
      f'{R({"transform": "scale(1)", "opacity": .6}, {"transform": "scale(2.2)", "opacity": 0}, D0 + .5 + i*.25, 1.6, 4.0)}/>'
      f'<circle class="af" cx="{x:.1f}" cy="{y:.1f}" r="15" {K(POP0, {"transform": "scale(1)", "opacity": .15}, D0 + i*.12, .35)}/>'
      f'<circle class="af" cx="{x:.1f}" cy="{y:.1f}" r="4.5" {K(POP0, {"transform": "scale(1)", "opacity": 1}, D0 + .02 + i*.12, .35)}/>'
      + (lambda lx, ly, anc: f'<text class="af" x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anc}" font-size="21" font-weight="700" {SANS} '
                             f'{K(HIDE, {"opacity": 1}, D0 + .1 + i*.12, .3, "easeOut")}>{l}</text>')(*_lbl7(x, y))
      for i, (x, y, l) in enumerate(_p7))
  + '</svg>')

# --- site slide 8 (Slide8ani)
_rip = lambda t: R({"transform": "scale(0.75)", "opacity": 0}, {"transform": "scale(3)", "opacity": 0}, t, 3.5, 3.5, mid={"at": .12, "v": {"opacity": .55}})
D_RINGS = (f'<svg class="svgd" viewBox="0 0 300 278" style="width:46cqw" {K({"opacity": 0, "transform": "scale(0.88)"}, SHOW, D0, .7)}><defs>'
  '<radialGradient id="g8c" cx="35%" cy="28%" r="65%"><stop offset="0%" stop-color="rgba(248,200,212,0.22)"/><stop offset="55%" stop-color="rgba(237,130,165,0.14)"/><stop offset="100%" stop-color="rgba(205,58,84,0.20)"/></radialGradient>'
  '<radialGradient id="g8s" cx="38%" cy="32%" r="62%"><stop offset="0%" stop-color="rgba(250,212,222,0.72)"/><stop offset="100%" stop-color="rgba(205,80,110,0.60)"/></radialGradient>'
  '<radialGradient id="g8g" cx="40%" cy="35%" r="60%"><stop offset="0%" stop-color="rgba(240,160,180,0.97)"/><stop offset="100%" stop-color="rgba(180,40,72,0.92)"/></radialGradient></defs>'
  '<circle cx="130" cy="148" r="105" fill="url(#g8c)"/>'
  '<circle class="as" cx="130" cy="148" r="76" fill="url(#g8s)" stroke-opacity="0.35" stroke-width="1.5"/>'
  '<circle class="as" cx="130" cy="148" r="45" fill="url(#g8g)" stroke-opacity="0.55" stroke-width="1.5"/>'
  + "".join(f'<circle class="as" cx="130" cy="148" r="45" fill="none" stroke-width="1.5" {_rip(dl)}/>' for dl in (0, 1.15, 2.3))
  + "".join(f'<line class="as" x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke-width="1" stroke-dasharray="3 3" stroke-opacity="0.6" {K(HIDE, {"opacity": 1}, D0 + tl, .4, "easeOut")}/>'
            f'<text class="af" x="{tx}" y="{ty}" text-anchor="{anc}" font-size="16" font-weight="700" {SANS} {K(HIDE, {"opacity": 1}, D0 + tl + .06, .4, "easeOut")}>{lab}</text>'
            for a, b, c, d, tx, ty, anc, lab, tl in [(175, 148, 244, 148, 249, 154, "start", "Gut", .38),
                                                     (184, 94, 218, 65, 223, 63, "start", "Skin", .50),
                                                     (130, 43, 130, 16, 130, 9, "middle", "Coat", .62)])
  + '</svg>')

# --- site slide 9 (Slide9ani)
D_CONV = ('<svg class="svgd" viewBox="-48 -12 576 178" style="width:84cqw">'
  + "".join(f'<line class="draw" x1="{120*i}" y1="38" x2="240" y2="130" pathLength="1" stroke="#fff" stroke-width="1.2" stroke-opacity="0.5" '
            f'{K(DRAW0, {"strokeDashoffset": 0, "opacity": 1}, D0 + .45 + i*.12, .5, "easeOut")}/>' for i in range(5))
  + f'<circle cx="240" cy="130" r="6" fill="#fff" {K(POP0, {"transform": "scale(1)", "opacity": 1}, D0 + .45 + 5*.12, .4)}/>'
  + "".join(f'<rect class="af" x="{120*i-44}" y="0" width="88" height="38" rx="6" {K({"opacity": 0, "transform": "translateY(-8px)"}, SHOW, D0 + i*.12, .4)}/>'
            f'<text x="{120*i}" y="24.3" text-anchor="middle" font-size="14" font-weight="700" fill="#fff" {SANS} {K(HIDE, {"opacity": 1}, D0 + .1 + i*.12, .3, "easeOut")}>{l}</text>'
            for i, l in enumerate(["Digestion", "Hydration", "Energy", "Behaviour", "Coat"]))
  + '</svg>')

# --- site slide 10 (Slide10ani)
_b10 = ["• ADD A CHEW", "• ADD A POWDER", "• ADD A TOPPER", "• ADD A SUPPLEMENT", "• ADD A CHEW", "• ADD A POWDER"]
D_MQ = (f'<div class="mq" {K(HIDE, {"opacity": 1}, D0, .5, "easeOut")}><div class="mrow" data-mq=\'{{"p": 18}}\'>'
        + "".join(f'<span class="mp">{p}</span>' for p in _b10 * 4) + '</div></div>')

# --- site slide 11 (Slide11ani)
def _watch(pre, key, d):
    return (f'<div class="watch" {K({"opacity": 0, "transform": "translateY(0.8cqw)"}, SHOW, d, .45)}>{pre}'
            f'<span class="hl">{key}<svg viewBox="0 0 100 30" preserveAspectRatio="none">'
            f'<rect class="draw as" x="1" y="1" width="98" height="28" rx="12" fill="none" stroke-width="2" vector-effect="non-scaling-stroke" pathLength="1" '
            f'{K(DRAW0, {"strokeDashoffset": 0, "opacity": .7}, d + .15, .45, "easeOut")}/></svg></span>.</div>')
_r11 = [("4kg","20g",".28","1.2"),("5kg","22g",".31","1.3"),("6kg","25g",".34","1.4"),("7kg","28g",".37","1.5"),
        ("8kg","31g","40","1.6"),("9kg","34g","43","1.7"),("10kg","37g",".46","1.8"),("11kg","40g",".49","1.9")]
D_READ = ('<div class="rd"><div>'
  f'<p class="cap" {K(HIDE, {"opacity": .4}, D0, .3, "easeOut")}>READ THE DOG.</p><div class="lines">'
  + _watch("Watch ", "what she eats", D0 + .08) + _watch("Watch ", "what she leaves", D0 + .23)
  + _watch("Watch how ", "her coat carries", D0 + .38) + _watch("Watch how ", "her energy holds", D0 + .53)
  + f'</div></div><div {K(HIDE, {"opacity": 1}, D0 + .4, .6, "easeOut")}><p class="cap" style="opacity:.4">NOT THE CHART.</p><div class="tbl">'
  + "".join("<div>" + "".join(f"<span>{c}</span>" for c in r) + "</div>" for r in _r11) + '</div></div></div>')

# --- site slide 12 (Slide12ani)
_n12 = [("Gut", 180, 56), ("Hydration", 294, 138), ("Energy", 252, 276), ("Behaviour", 108, 276), ("Eating", 66, 138)]
_a12 = ["M211,68 Q260,86 281,112", "M292,170 Q288,228 268,256", "M225,294 Q180,308 135,294", "M89,256 Q70,228 68,170", "M82,112 Q102,84 149,68"]
D_PENTA = ('<svg class="svgd" viewBox="8 0 344 340" style="width:47cqw"><defs>'
  '<marker id="arr12" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="rgba(255,255,255,0.55)"/></marker></defs>'
  + "".join(f'<path class="draw" d="{d}" pathLength="1" fill="none" stroke="rgba(255,255,255,0.55)" stroke-width="1.8" stroke-linecap="round" '
            f'marker-end="url(#arr12)" {K(DRAW0, {"strokeDashoffset": 0, "opacity": 1}, D0 + .45 + i*.08, .55)}/>' for i, d in enumerate(_a12))
  + "".join(f'<g {K({"transform": "scale(0.4)", "opacity": 0}, {"transform": "scale(1)", "opacity": 1}, D0 + i*.08, .6)}>'
            f'<circle class="af" cx="{x}" cy="{y}" r="48"/>'
            f'<text x="{x}" y="{y+5.5}" text-anchor="middle" font-size="16" font-weight="600" fill="#fff" {SANS}>{l}</text></g>'
            for i, (l, x, y) in enumerate(_n12))
  + '</svg>')

# --- site slide 13 (Slide13ani; stacked, as on the site's mobile layout)
D_EQ = (f'<div class="eq" {K(rise("1cqw"), SHOW, D0, .55)}><div class="pill l"><span>What your dog eats</span></div>'
        '<span class="times">×</span><div class="pill r">What gets delivered</div></div>')

# --- site slide 14 (Slide14ani; two columns as on the site's desktop layout)
D_ER = (f'<div class="er" {K(rise("1.2cqw"), SHOW, D0, .55)}>'
        '<div class="er-col en"><div class="er-h"><span class="sym">×</span><span class="w">Enough</span></div>'
        '<p>Meets a standard.</p><p>Passes a minimum.</p><p>Fits no dog in particular.</p></div>'
        '<div class="er-div"></div>'
        '<div class="er-col ri"><div class="er-h"><span class="sym ck">✓</span><span class="w">Right</span></div>'
        '<p>Fits the dog in front of you.</p><p>Delivers what it claims.</p><p>Works with the system, not around it.</p></div></div>')

# --- site slide 15 (Slide15ani)
_BAG = "M20,8 L52,8 L58,20 L58,84 Q58,92 50,92 L22,92 Q14,92 14,84 L14,20 Z"
def _bag(label, color, d):
    return (f'<figure class="bag"><svg viewBox="0 0 72 96"><path d="{_BAG}" fill="rgba(10,10,10,0.08)"/>'
            f'<path d="{_BAG}" style="fill:{color}" {K(HIDE, {"opacity": 1}, d, .6, "easeOut")}/>'
            f'<path d="M26,8 C28,2 44,2 46,8" fill="none" style="stroke:{color}" stroke-width="2" {K(HIDE, {"opacity": .8}, d + .1, .4, "easeOut")}/>'
            f'</svg><figcaption>{label}</figcaption></figure>')
D_FITS = ('<div class="fits"><div class="lines">'
  + "".join(f'<p {K({"opacity": 0, "transform": "translateY(1cqw)"}, {"opacity": .8, "transform": "none"}, D0 + i*.6, .5)}>{l}</p>'
            for i, l in enumerate(["Digestion works quietly.", "The coat carries the signal.", "Energy holds a steady line."]))
  + '</div><div class="bags">' + _bag("Eats", "#E07060", D0) + _bag("Absorbs", "#C05040", D0 + .6) + _bag("Uses", "var(--dacc)", D0 + 1.2)
  + '</div></div>')

# ---------------- slides: copy verbatim from the live page
# kind: "wide" (panel sized to the diagram) or "arch" (arch window; side "l"/"r")
S = [
 dict(kind="wide", lab="Less room", setup="Small dogs have", pay="less room for error.", dia=D_THREE,
      b="Smaller bodies. Tighter margins. Less buffer."),
 dict(kind="wide", lab="Digestion", setup="Digestion", pay="isn't what you see.", dia=D_BARS,
      sub="Not the empty bowl. Not the clean plate.<br>The invisible part — what the body actually uses.",
      a="What matters isn't what goes in.", b="It's what makes it through."),
 dict(kind="wide", lab="Hydration", setup="Hydration", pay="isn't moisture.", dia=D_WAVE,
      sub="It's how the body regulates itself — every hour, all day.<br>Through food, water, movement, temperature.",
      a="Food plays a part.", b="It doesn't carry the whole thing."),
 dict(kind="wide", navy=1, lab="Calories", setup="Calories in", pay="≠ Calories used.", dia=D_CAL,
      sub="What's on the pack isn't what the body extracts.<br>Small dogs burn faster. There's less room for error.",
      a="Unabsorbed calories still count on the label.", b="They don't count for the dog."),
 dict(kind="arch", side="l", lab="Picky eating", setup="Most picky eating", pay="is learned.", dia=D_LOOP,
      sub="Not personality. Not breed.<br>A pattern built between the bowl and the hand that fills it.",
      a="The food is rarely the problem.", b="The pattern around it is."),
 dict(kind="arch", side="r", lab="Coat", setup="The coat", pay="is a signal.", dia=D_RINGS,
      sub="Dullness, dryness, shedding — surface symptoms.<br>What you see outside is what the inside is doing.",
      a="Treat the coat, treat the surface.", b="Treat the cause, the coat follows."),
 dict(kind="wide", navy=1, lab="Five systems", setup="Five systems.", pay="One mistake.", dia=D_CONV,
      sub="They all look different. The mistake is the same<br>— treat the symptom, miss the cause.",
      a="Different problems.", b="Same shape."),
 dict(kind="wide", lab="The loop", setup="Treat everything the same way,", pay="you miss the system.", dia=D_MQ, mq=1,
      sub="Add something. Expect a result.<br>Add something else. Expect another result.<br>The loop repeats. The cause stays hidden.",
      a="What's missing isn't ingredients.", b="It's a model of how the body actually works."),
 dict(kind="wide", lab="Read the dog", setup="Read the dog.", pay="Not the chart.", dia=D_READ,
      sub="Charts describe dogs in general.<br>Your dog isn't in general.",
      a="This is the evidence.", b="Everything else is a proxy."),
 dict(kind="arch", side="l", navy=1, lab="Systems", setup="Your dog isn't", pay="separate systems.", dia=D_PENTA,
      sub="Gut affects coat. Hydration affects energy. Energy affects behaviour. Behaviour affects eating. Eating affects gut.",
      a="Treat any one in isolation — incomplete answer.", b="Everything works together. Or nothing quite does."),
 dict(kind="arch", side="r", lab="What matters", setup="What matters", pay="most.", dia=D_EQ,
      sub="Intake is half the equation.<br>Delivery is the other half.<br>The answer is what the body actually receives.",
      b="It's the only number that counts."),
 dict(kind="wide", lab="Enough", setup="Most food", pay="is enough.", dia=D_ER,
      a="The distance between enough and right isn't dramatic.", b="It's just consistent. Every day. For years."),
 dict(kind="arch", side="l", lab="The system", setup="When food fits", pay="the system —", dia=D_FITS,
      b="Everything downstream settles.", last=1),
]
TOTAL = len(S) + 1

def chrome(n):
    dots = "".join('<i class="on"></i>' if k == n else "<i></i>" for k in range(1, TOTAL + 1))
    return (f'<div class="mk tl">Small dogs, actually</div><div class="dots" aria-label="Slide {n} of {TOTAL}">{dots}</div>'
            f'<div class="rule t"></div>')

def low(s):
    pa = f'<span class="a">{s["a"]}</span>' if s.get("a") else ""
    return (f'<div class="low"><div class="setup">{s["setup"]}</div><h2 class="pay">{s["pay"]}</h2>'
            f'<p class="punch">{pa}<span class="b">{s["b"]}</span></p></div>')

def frame(i, s):
    n, num = i + 2, f"{i + 1:02d}"
    # captions wrap naturally: no forced breaks, and the two closing lines flow as one paragraph
    sub = f'<p class="body">{s["sub"].replace("<br>", " ")}</p>' if s.get("sub") else ""
    pa = f'<span class="a">{s["a"]}</span> ' if s.get("a") else ""
    swipe = "" if s.get("last") else '<div class="mk br">Swipe →</div>'
    return f"""
    <div class="framewrap">
      <div class="framelabel">{num} · site slide {i + 3}</div>
      <div class="f{" navy" if s.get("navy") else ""}" data-name="{num}">
        {chrome(n)}
        <div class="num">{num}</div>
        <div class="inner">
          <div class="top"><div class="setup">{s["setup"]}</div><h2 class="pay">{s["pay"]}</h2></div>
          <div class="mid"><div class="dia">{s["dia"]}</div></div>
          <div class="caps">{sub}<p class="punch">{pa}<span class="b">{s["b"]}</span></p></div>
        </div>
        <div class="rule b"></div>{swipe}
      </div>
    </div>"""

INTRO = f"""
    <div class="framewrap">
      <div class="framelabel">00 · Intro</div>
      <div class="f intro" data-name="00">
        {chrome(1)}
        <div class="inner">
          <div class="dome"><img src="img/intro.jpg" alt="A small Cavapoo sitting alone in a wide, empty cream room." style="object-position:50% 62%"></div>
          <div class="low"><h2 class="pay">Small dogs.<br>Small system.</h2>
            <p class="body">Every bite, sip, and treat has to do more.</p></div>
        </div>
        <div class="rule b"></div><div class="mk br">Swipe →</div>
      </div>
    </div>"""

html = f"""<title>Built For Small Dogs</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Figtree:wght@400;500;600;700;800;900&family=DM+Mono:wght@400;500&display=swap">
<style>
{(HERE / "carousel.css").read_text()}
</style>
<div class="page">
  <header class="masthead">
    <div class="kicker">Animated carousel · {TOTAL} frames · 6.5s loop</div>
    <h1>Small dogs, actually</h1>
    <p>An intro, then slides 3–15 of the first section of tendsmall.com/built-for-small-dogs-not-all-dogs, word for word. Type and frame are still; only each diagram moves, rebuilt from the site's own animation components.</p>
  </header>
  <div class="deck">{INTRO}{"".join(frame(i, s) for i, s in enumerate(S))}
  </div>
</div>
<script>
{(HERE / "animate.js").read_text()}
</script>
"""
(HERE / "small_dogs_gif_carousel.html").write_text(html)
print("wrote", len(html), "bytes,", TOTAL, "frames")
