# Post Coffee · Dusra Majla — Beverage App

A mobile-first web app for the **Post Coffee Beverage Programme by Pilgrim**
(*Welcome to the Dusra Majla*). Browse the signature drinks by sliding through
a card deck, **select** the one you want, and **reset** to start over.

## Features

- **Slide to explore** — swipe left/right (touch or mouse drag), tap the side
  arrows, use the progress dots, or arrow keys to move between drinks.
- **Select** — tap *Select* on any card to choose it; the order bar at the
  bottom shows your pick and price.
- **Reset** — one tap clears the selection and returns to the first drink.
- **Taste profile** — each drink shows three sliders: *Sweet↔Dry*,
  *Familiar↔Curious*, *Light↔Bold*.
- **Installable** — includes a web manifest so it can be added to a phone
  home screen and run full-screen (PWA).

## The menu

| # | Drink | Ingredients | Price |
|---|-------|-------------|-------|
| 1 | After Rain | Elderflower · Lavender · Tonic | INR 350+ |
| 2 | Ruby Darling | Blackberry · Lemon · Soda | INR 400+ |
| 3 | High Tide | Ginger Ale · Coconut Water · Lime | INR 350+ |
| 4 | Peach Drift | Peach · Tonic · Tabasco | INR 400+ |
| 5 | Wild Fire | Pineapple · Jalapeño · Soda | INR 400+ |
| 6 | Gin Signature | SOBER Gin · Pineapple · Coconut | INR 400+ |
| 7 | Rum Signature | SOBER Rum · Blueberry · Soda | INR 400+ |
| 8 | Whiskey Signature | SOBER Whiskey · Orange · Smoke | INR 400+ |

> Taste-profile values are an interpretation of each drink's description, since
> the source menu shows the scales but not exact marker positions.

## Run it

No build step — it's a single self-contained page.

```bash
# open directly
open index.html            # macOS
xdg-open index.html        # Linux

# or serve locally (recommended for phone testing / PWA install)
python3 -m http.server 8000
# then visit http://<your-ip>:8000 on your phone
```

## Files

- `index.html` — the entire app (HTML + CSS + JS inline)
- `manifest.webmanifest` — PWA metadata for home-screen install
