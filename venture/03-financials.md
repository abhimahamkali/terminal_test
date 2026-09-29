# 03 — Unit Economics, P&L & Capital Plan

> **Constraints update (read `05-first-100k-plan.md` first).** The capital plan and channel
> sequencing below were written for a ₹9–14 lakh launch from a licensed unit. The confirmed
> starting position is **₹1 lakh over 3 months from a home setup in Andhra/Hyderabad**, which
> changes both the budget and the channel order (cafés and gyms first; hotels at month 4+ via a
> co-packer). Treat this file as the destination and `05-first-100k-plan.md` as the route.


All figures INR. Built from your two given inputs: **₹35 per 100 g of blend** and **6 kg/day capacity including packing**.
Assumption flags are marked `[A]` — replace with real quotes as you get them.

---

## 1. Headline finding you need to see first

**Your stated 6 kg/day capacity sits almost exactly at breakeven — and slightly below it if you fund marketing properly.**

- 6 kg/day × 25 days = **50,000 sachets/month** (at 3 g) = your absolute ceiling.
- At a realistic channel mix and a real marketing budget, breakeven lands at roughly **56,000 sachets/month (~6.7 kg/day)**.
- So at full tilt you run a small monthly loss, and you have **no headroom to serve a single large banquet order** without stopping everything else.

This is not a reason to stop. It is a reason to sequence correctly:
1. **Phase 0** — validate the product and the pitch for ~₹1.5 lakh, hand-packed, 10 accounts.
2. **Phase 1** — run at 6 kg/day deliberately *under-marketed*, chasing B2B margin not brand spend. Breakeven ~5.5 kg/day.
3. **Phase 2** — the business only *works* at ~20 kg/day. Plan that capex from day one; don't discover it at month 9.

The single worst outcome available to you is winning a Minerva conference order and being unable to fill it.

---

## 2. Per-sachet cost build (3 g)

| Line | Flat filter bag | Pyramid mesh bag | Stick pack |
|---|---|---|---|
| Blend, 3 g @ ₹0.35/g (your input) | 1.05 | 1.05 | 1.05 |
| Infusion bag + thread + tag `[A]` | 0.45 | 1.20 | — |
| Stick-pack film `[A]` | — | — | 0.75 |
| Metallised printed envelope `[A]` | 0.90 | 0.90 | — |
| Filling + sealing labour (2 staff @ ₹600/day ÷ 2,000) | 0.60 | 0.60 | 0.30 |
| Secondary carton, allocated | 0.35 | 0.35 | 0.35 |
| Wastage + QC @ 5% | 0.17 | 0.21 | 0.12 |
| **COGS / sachet** | **₹3.52** | **₹4.31** | **₹2.57** |
| + Hotel custom digital label `[A]` | +0.65 | +0.65 | +0.65 |
| + Retail carton allocation (box of 10) | +1.70 | +1.70 | +1.70 |

**Planning COGS: ₹3.52** (flat filter, generic envelope). Use pyramid mesh only if the blind taste test in `01-product-packaging.md` §2 demands it — it costs you 22% of your COGS.

**Note on your ₹1–3/gm price reference:** at a ₹3.52 COGS for a 3 g unit, a ₹3–9 retail sachet is structurally impossible. This is the arithmetic proof of the positioning argument in `00-strategy.md`: **sold as rasam, this product cannot make money. Sold as a hot drink at ₹15–25/sachet, it makes 60%+ gross margin.** The pricing is the positioning.

---

## 3. Price list

| Channel | Unit | Price to you | COGS | GM% | Payment terms |
|---|---|---|---|---|---|
| **Hotel — custom branded** | sachet, institutional carton | **8.50** | 4.17 | 51% | 60–90 days |
| **Hotel — generic / banquet** | sachet, bulk | **7.00** | 3.52 | 50% | 60–90 days |
| **Café / gym** | sachet | **9.00** | 3.52 | 61% | 15–30 days |
| **Corporate pantry** | sachet | **8.00** | 3.52 | 56% | 30 days |
| **Retail — box of 10** | via quick commerce | **163 net** *(MRP 249)* | 52.20 | 68% | 15–30 days |

**Quick commerce net realisation, shown fully:**
```
MRP (GST-inclusive)                        249.00
less GST @ 5%  (249 / 1.05)             -> 237.14 ex-GST
less platform margin @ 28%  [A]         ->  66.40
less fulfilment / returns / damages     ->   8.00
= Net realisation to you                   162.74  (~₹16.27 / sachet)
```
**Caution:** platform *advertising* is not in that number. A new brand on Blinkit/Zepto realistically spends 15–25% of GMV on ads to get discovered. Budget it as marketing opex, not as trade margin, and watch it — this line is where quick-commerce brands quietly die.

### The single highest-leverage pricing decision

Do **not** discount hotels to win logos. Moving 23,000 hotel sachets/month from ₹7.00 to ₹8.50 adds **₹34,500/month of gross profit** — which is, almost exactly, the difference between losing money and making money at your capacity.

A low price is permanent and it anchors every future negotiation. Free samples are one-time. **Give away product, never margin.**

---

## 4. Phase 1 P&L — month 6, at 30,000 sachets/month (~3.6 kg/day)

| | Monthly |
|---|---|
| **Revenue** | |
| B2B 24,000 sachets @ ₹8.00 blended | 1,92,000 |
| Retail 6,000 sachets @ ₹16.27 | 97,620 |
| **Total revenue** | **2,89,620** |
| **COGS** 30,000 @ ₹4.00 blended | 1,20,000 |
| **Gross profit** | **1,69,620** *(59%)* |
| **Operating expenses** | |
| Founder (below-market) | 25,000 |
| B2B sales executive (1) + incentive | 40,000 |
| Production staff (1) | 18,000 |
| Rent + utilities (small unit) | 20,000 |
| Logistics / freight | 15,000 |
| Marketing — influencers + content | 40,000 |
| Samples & trade spend | 15,000 |
| CA / compliance / legal | 10,000 |
| Software, phone, misc | 10,000 |
| **Total opex** | **1,93,000** |
| **EBITDA** | **-23,380** |

**Read:** near-breakeven by month 6 on a lean setup. That is a good month-6 outcome for an F&B brand and it is achievable inside your capacity. Breakeven here is ~33,000 sachets/month (**4 kg/day**) — comfortably inside 6 kg/day, *because marketing is deliberately restrained.*

## 5. Phase 2 P&L — month 18, at 100,000 sachets/month (needs ~20 kg/day)

| | Monthly |
|---|---|
| **Revenue** | |
| B2B 60,000 @ ₹8.20 | 4,92,000 |
| Retail 40,000 @ ₹16.27 | 6,50,800 |
| **Total revenue** | **11,42,800** |
| **COGS** | 4,49,000 |
| **Gross profit** | **6,93,800** *(61%)* |
| **Operating expenses** | |
| Founder + 2 sales | 1,20,000 |
| Production staff (3) | 54,000 |
| Rent + utilities | 40,000 |
| Logistics | 60,000 |
| Marketing (incl. quick-commerce ads) | 2,50,000 |
| Samples & trade | 40,000 |
| Compliance / CA / audit | 20,000 |
| Misc + software | 30,000 |
| **Total opex** | **6,14,000** |
| **EBITDA** | **+79,800** *(7% of revenue)* |

Annualised ≈ **₹1.37 crore revenue, ~₹9.6 lakh EBITDA** exiting year 2. Thin but real, and the right shape for a brand still buying distribution. Note you'd still be inside the ₹1.5 crore FSSAI Basic Registration ceiling for most of year 2 — though you'll want the State Licence for sales reasons anyway (`02-compliance-india.md` §2).

---

## 6. Capital requirement

### Phase 0 — Validation (60 days) · **₹1.5 lakh** ← start here

| Item | Cost |
|---|---|
| Formulation trials, 3 flavours, format bake-off | 40,000 |
| 1 SKU nutritional + micro panel (NABL) | 25,000 |
| FSSAI Basic Registration + GST + Udyam | 10,000 |
| Generic envelopes + digital labels, 5,000 units | 15,000 |
| Hotel/café sample kits (100) | 25,000 |
| Light brand + label design | 30,000 |
| Contingency | 5,000 |
| **Total** | **1,50,000** |

**Goal:** 10 paying accounts, a validated format, and a product that beats home-made rasam in a blind test. Nothing else. No trademark filing, no tooling, no inventory.

### Phase 1 — Commercial launch · **₹9–14 lakh**

| Item | Lean (co-pack) | Full (own line) |
|---|---|---|
| Pvt Ltd + GST + FSSAI State + Legal Metrology | 45,000 | 45,000 |
| Trademark clearance search + filing (2 classes) | 29,000 | 29,000 |
| Formulation R&D + pilot batches | 75,000 | 75,000 |
| Lab testing — full panels + shelf life | 80,000 (2 SKU) | 1,20,000 (3 SKU) |
| Brand identity + packaging artwork | 60,000 | 1,00,000 |
| Rotogravure cylinders, 1 generic design | 35,000 | 35,000 |
| First envelope print run (50,000) | 42,500 | 42,500 |
| Semi-auto filling/sealing machine | — *(co-packer's)* | 2,50,000 |
| Weighing, sealing, sundry equipment | 25,000 | 60,000 |
| Opening inventory | 1,00,000 | 1,50,000 |
| B2B website + catalogue *(not a D2C store)* | 40,000 | 50,000 |
| Sampling kits (500) | 60,000 | 60,000 |
| **Working capital buffer** | 3,00,000 | 3,00,000 |
| **Total** | **≈ ₹8,91,500** | **≈ ₹13,76,500** |

**Recommendation: take the lean co-packing route.** You avoid ₹2.5L of tooling before you know which format wins, and a co-packer's existing FSSAI licence and food-safety systems make hotel vendor onboarding dramatically easier than a brand-new unit would.

### Phase 2 — Scale to 20 kg/day · **₹26–31 lakh**

| Item | Cost |
|---|---|
| Automatic inner-outer teabag machine (60–100 bags/min) | 10,00,000 – 15,00,000 |
| Pulveriser + ribbon blender + sieve + metal detector | 3,00,000 |
| Unit fitout to ISO 22000 standard | 4,00,000 |
| ISO 22000 / HACCP certification | 1,25,000 |
| Additional working capital | 8,00,000 |
| **Total** | **₹26,25,000 – 31,25,000** |

Fund this from Phase 1 cash flow plus either an MSME/Mudra term loan (Udyam registration helps here) or a small angel round. Do not raise for Phase 2 before Phase 1 shows repeat orders from at least 15 accounts.

---

## 7. Working capital — the thing that actually kills B2B food brands

| Channel | Terms | Effect |
|---|---|---|
| Hotels | 60–90 days | **Cash sink.** ₹1.3L/month of revenue = ~₹3L locked up |
| Cafés | 15 days, often advance | Cash positive |
| Gyms | 15–30 days | Neutral |
| Corporates | 30 days | Manageable |
| Quick commerce | 15–30 days | Manageable |
| Raw material + packaging | Advance to 30 days | Cash out first |

Three mitigations, in order of usefulness:
1. **Weight your early mix toward cafés, gyms and corporates** — not hotels. Hotels are your brand strategy; cafés are your cash flow. This is the practical version of the point in `00-strategy.md` §5.
2. **Use the MSMED Act.** With Udyam registration, a buyer must pay within 45 days, and interest accrues automatically after that. You rarely have to litigate — citing it in the PO terms changes behaviour.
3. **Ask for advance on the first order from every new hotel.** It is normal for a new vendor, it filters out non-serious accounts, and it sets a precedent.

---

## 8. Sensitivities worth tracking monthly

| Lever | Move | Impact at 50,000 sachets/month |
|---|---|---|
| Hotel price | ₹7.00 → ₹8.50 | **+₹34,500/mo** — your biggest single lever |
| Blend cost | ₹350/kg → ₹250/kg at volume | **+₹15,000/mo** |
| Bag choice | pyramid → flat filter | **+₹39,500/mo** |
| Retail mix | 20% → 40% of volume | **+₹50,000/mo** (but ad spend rises) |
| Q-comm ad spend | 10% → 25% of GMV | **-₹40,000/mo** |
| Labour | manual → automatic filling | **+₹25,000/mo** (needs Phase 2 capex) |

The top two lines are free — they are negotiation, not capex. Do those before you buy a machine.
