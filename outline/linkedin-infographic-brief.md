# LinkedIn Promotional Infographic

**Illustrator Brief — Comprehensive & Self-Sufficient**

---

## Purpose and Context

This is a **promotional infographic** for sharing on LinkedIn to drive readership of the published paper:

**"Beyond SMILES: Evaluating Agentic Systems for Drug Discovery"**
arXiv:2602.10163 — Edward Wijaya

The infographic must work as a **standalone visual** that communicates the paper's core thesis in a single image. A viewer scrolling LinkedIn should:
1. Stop scrolling (visual hook within 1 second)
2. Understand the paper's thesis (within 5 seconds)
3. Want to read the full paper (within 15 seconds)

This is NOT a paper figure. It is a marketing asset. It should be visually striking, shareable, and optimized for social media feeds.

---

## Target Audience

- Drug discovery practitioners (computational and experimental)
- Biotech founders and executives
- AI/ML researchers working in life sciences
- Pharma R&D leaders evaluating agentic AI tools
- Academic researchers in computational biology, cheminformatics

**Assumption:** The viewer has heard of "AI agents" in drug discovery but has not read this paper. They may or may not be technical.

---

## Dimensions and Format

| Spec | Value |
|------|-------|
| **Orientation** | Landscape |
| **Dimensions** | 1200 x 675 px (LinkedIn recommended) |
| **Alternative** | 1920 x 1080 px (16:9, scales down cleanly) |
| **Resolution** | 150 DPI minimum (screen-optimized, not print) |
| **File formats** | PNG (primary for upload), SVG (editable source), layered source file |
| **File name** | `linkedin-infographic-beyond-smiles` |

**Critical:** Must remain legible on mobile (375 px wide viewport). Test by scaling the image to 50% and checking if the 5 gap titles and paper title are still readable.

---

## Color Scheme

**Dark navy/teal base with orange/amber accents on white text.**

This scheme conveys scientific authority and credibility while the amber signals "attention needed," matching the paper's gap-analysis framing.

| Role | Hex | Usage |
|------|-----|-------|
| Dark Navy | #0B1D33 | Primary background |
| Deep Teal | #0D4F4F | Secondary background, section fills |
| Teal Accent | #1A8A7D | Borders, dividers, secondary highlights |
| Amber/Orange | #E8912D | Gap numbers, callouts, key highlights, warning accents |
| Gold | #F5C842 | Sparingly for emphasis on critical text |
| White | #FFFFFF | Primary text, headings |
| Light Gray | #B0BEC5 | Secondary text, descriptions |
| Off-White | #E8E8E8 | Tertiary text, fine details |

**Rationale:**
- Dark background stops the scroll (most LinkedIn feeds are white/light gray)
- Amber/orange = "warning, gaps ahead" (fits the paper's corrective tone)
- Teal = scientific credibility without being cold
- Avoid red (too aggressive) and green (too optimistic)

---

## Typography

| Element | Style | Size (at 1200px width) | Color |
|---------|-------|------------------------|-------|
| Paper title | Bold sans-serif (Inter, Helvetica Neue, or similar) | 28-32 px | White (#FFFFFF) |
| Subtitle / tagline | SemiBold sans-serif | 16-18 px | Amber (#E8912D) |
| Gap numbers (1-5) | Bold, large | 36-42 px | Amber (#E8912D) |
| Gap titles | Bold sans-serif | 16-18 px | White (#FFFFFF) |
| Gap descriptions | Regular sans-serif | 11-13 px | Light Gray (#B0BEC5) |
| arXiv citation | Regular sans-serif | 11 px | Light Gray (#B0BEC5) |
| Author name | Regular sans-serif | 12 px | White (#FFFFFF) |

**Rule:** All text must be readable when image is displayed at 600 px wide on a phone. If it is not readable at that size, the text is too small or too dense. Err on the side of fewer words at larger sizes.

---

## Layout

The infographic has three horizontal zones:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│                    HEADER ZONE (15%)                         │
│          Paper title + tagline + author/arXiv                │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│                    MAIN ZONE (70%)                           │
│                                                              │
│  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐          │
│  │Gap 1 │  │Gap 2 │  │Gap 3 │  │Gap 4 │  │Gap 5 │          │
│  │      │  │      │  │      │  │      │  │      │          │
│  └──────┘  └──────┘  └──────┘  └──────┘  └──────┘          │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│                    FOOTER ZONE (15%)                         │
│         Takeaway line + arXiv URL + QR code (optional)       │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## Zone 1: Header (Top 15%)

**Background:** Darkest navy (#0B1D33) or subtle gradient from #0B1D33 to #0D4F4F

### Content (top to bottom):

1. **Paper title (large, bold, white):**
   "Beyond SMILES: Evaluating Agentic Systems for Drug Discovery"

2. **Tagline (amber, slightly smaller, positioned below title):**
   "5 Critical Blind Spots in Current AI Agent Systems"

3. **Author line (small, light gray, right-aligned or below tagline):**
   "Edward Wijaya | arXiv:2602.10163"

### Optional visual element:
A thin amber horizontal rule (1-2 px) separating the header from the main zone.

---

## Zone 2: Main Content (Middle 70%)

**Background:** Deep teal (#0D4F4F) or a slightly lighter shade than the header to create depth.

### Layout: Five gap cards in a row

Five equally-spaced vertical cards, each representing one gap. Cards should be arranged left to right, numbered 1 through 5.

**Card dimensions (approximate):** 200 x 350 px each at 1200 px width, with 16-20 px gutters between cards.

### Card Design (each card):

```
┌─────────────────────┐
│                     │
│     [ICON]          │  ← Simple icon (60x60 px)
│                     │
│        1            │  ← Large amber number
│                     │
│  THE SMALL          │  ← Bold white title (2-3 words)
│  MOLECULE BIAS      │
│                     │
│  Peptide discovery  │  ← Light gray description
│  needs protein      │     (2-3 short lines max)
│  language models,   │
│  not SMILES strings │
│                     │
└─────────────────────┘
```

**Card styling:**
- Background: Slightly lighter teal (#15605A) or semi-transparent white overlay (rgba 255,255,255, 0.05)
- Border: 1 px solid teal accent (#1A8A7D), or left border only (3 px amber for visual rhythm)
- Corner radius: 8 px
- No drop shadows

### The Five Gap Cards

**Card 1: The Small Molecule Bias**
- Icon: A peptide chain (linked amino acid circles) with a "not equal" sign next to a SMILES text string
- Number: 1
- Title: "Small Molecule Bias"
- Description: "Peptides and biologics need protein language models, not molecular fingerprints. No agent supports PLM fine-tuning."

**Card 2: The In Vivo-In Silico Bridge**
- Icon: A mouse silhouette with a data trend line overlaid, and a gap/break in the line
- Number: 2
- Title: "In Vivo-In Silico Gap"
- Description: "Animal studies, behavioral phenotyping, and longitudinal imaging data have zero agent support."

**Card 3: Multi-Paradigm, Not Multi-Agent**
- Icon: Multiple interlocking gears or nodes of different shapes (circle, hexagon, square, triangle) connected, representing RL, PLM, CV, ML
- Number: 3
- Title: "Multi-Paradigm Gap"
- Description: "Real projects need RL, protein language models, computer vision, and classical ML orchestrated together."

**Card 4: The Small Biotech Reality**
- Icon: A single person silhouette next to a small building, contrasted with (or instead of) a large corporate building
- Number: 4
- Title: "Small Biotech Reality"
- Description: "Tiny datasets, limited compute, one-person AI teams. Current agents assume AstraZeneca-scale resources."

**Card 5: Multi-Objective Trade-offs**
- Icon: A balance scale (tilted) or a simplified Pareto curve with two axes
- Number: 5
- Title: "Multi-Objective Blind Spot"
- Description: "Safety vs efficacy vs stability requires Pareto reasoning. Agents optimize a single metric."

### Visual flow between cards

A subtle connecting element between cards to suggest these gaps are related:
- Option A: Thin dashed amber line connecting the top of each card
- Option B: Faint dotted arrows between cards
- Option C: No connection (cleaner, may be better for readability)

Use judgment; if the connections add clutter, omit them.

---

## Zone 3: Footer (Bottom 15%)

**Background:** Darkest navy (#0B1D33), matching header

### Content (left to right):

**Left side (60% width):**
- Takeaway line (white, bold, 14-16 px):
  "Current agentic AI is built for large pharma, small-molecule workflows. It fails everywhere else."

**Right side (40% width, right-aligned):**
- arXiv URL: "arxiv.org/abs/2602.10163" (light gray, 12 px)
- Optional: Small QR code linking to the paper (white on dark navy, ~60x60 px)

---

## Icon Style

- **Flat, outlined style** with 2 px stroke weight
- White outlines on dark backgrounds
- Amber (#E8912D) fill or accent on key elements within the icon
- No gradients, no 3D, no photorealistic elements
- Consistent visual language across all 5 icons (same stroke weight, same level of detail)
- Scientific but approachable (think Nature Reviews, not corporate clip art)
- Each icon should be recognizable at 40x40 px (when viewed on mobile)

---

## Visual Hierarchy (Priority Order)

What the viewer should notice, in order:

1. **Paper title** ("Beyond SMILES") — largest, highest contrast
2. **Tagline** ("5 Critical Blind Spots") — amber, immediately below title
3. **The five gap titles** — bold white text in each card
4. **The amber numbers** (1-5) — anchoring each card
5. **Icons** — giving visual identity to each gap
6. **Descriptions** — for those who look closer
7. **Footer / arXiv link** — for those who want to read the paper

If the viewer only reads #1, #2, and #3, they should understand the paper's thesis.

---

## What This Infographic Must Communicate

In a single glance:
- There is a paper that critically evaluates AI agents for drug discovery
- It identifies 5 specific blind spots (not vague criticism, concrete gaps)
- The author has practitioner authority (this is from someone who does the work, not a theorist)

The tone is **constructive-critical**, not hostile. The message is "here is what is missing" not "everything is broken." This is a field correction that practitioners will recognize as true.

---

## What NOT to Do

- **Do not make it look like a corporate slide deck** — no gradient backgrounds, no stock photos, no bullet points in boxes
- **Do not use more than 100 words total** in the descriptions — this is social media, not a poster. If text is dense, cut ruthlessly
- **Do not include any proprietary information** — no company names, drug names, or internal project details
- **Do not use clip art or stock icons** — all visual elements should be custom-drawn in a consistent style
- **Do not use emdashes** — use commas, periods, or semicolons instead (author preference)
- **Do not use red-green as the only distinction** between any elements (colorblind safety)
- **Do not add decorative molecular structures in the background** unless they are subtle and do not interfere with text readability
- **Do not clutter** — white space (or dark space, in this case) is your friend. When in doubt, remove elements rather than add them

---

## Background Visual Elements (Optional, Subtle)

If the design feels too plain with solid colors, consider ONE of these (not all):

- **Option A:** Very faint (5-10% opacity) molecular network pattern in the background of the main zone, using teal lines slightly lighter than the background
- **Option B:** Subtle geometric mesh or hexagonal pattern (suggesting molecular structure) at very low opacity
- **Option C:** Abstract data visualization elements (faint scatter plot dots, curve fragments) ghosted behind the cards

These must be barely visible and must NOT compete with the text or icons. If they reduce readability even slightly, remove them.

---

## Mobile Readability Test

Before finalizing, scale the image to these sizes and verify readability:

| Platform | Display Width | Must Be Readable |
|----------|---------------|-------------------|
| LinkedIn feed (desktop) | ~552 px | Paper title, tagline, all 5 gap titles, descriptions |
| LinkedIn feed (mobile) | ~375 px | Paper title, tagline, all 5 gap titles |
| LinkedIn post detail (desktop) | ~745 px | Everything |
| Twitter/X (if cross-posted) | ~506 px | Paper title, tagline, all 5 gap titles |

If the 5 gap titles are not readable at 375 px width, increase their font size or reduce description text.

---

## Delivery Checklist

- [ ] PNG (1200 x 675 px) — primary upload file
- [ ] PNG (1920 x 1080 px) — high-res version
- [ ] SVG — editable vector source
- [ ] Layered source file (Figma / Illustrator / Affinity Designer)
- [ ] Mobile readability verification (screenshots at 375 px width)
- [ ] Colorblind simulation check (protanopia, deuteranopia)

---

## Reference: The NotebookLM Version

A NotebookLM-generated infographic exists as a reference (see attached screenshot). It correctly uses a dark teal + amber color scheme and captures the 5 gaps. However, it has several issues the illustrator version should fix:

- Text is too small and dense for social media
- Too many visual elements competing for attention
- The paper title "Beyond SMILES" is not prominent enough
- Gap 4 (Small Biotech Reality) is underweighted
- Overall, too much information — a promotional infographic should be sparser and bolder than a paper summary

The illustrator version should be **cleaner, bolder, and more readable** than the NotebookLM version while conveying the same core message.

---

## Reference: Paper Abstract

For the illustrator's understanding of the paper's content:

> Agentic systems for drug discovery have demonstrated autonomous synthesis planning, literature mining, and molecular design. We ask how well they generalize. Evaluating six frameworks against 15 task classes drawn from peptide therapeutics, in vivo pharmacology, and resource-constrained settings, we find five capability gaps: no support for protein language models or peptide-specific prediction, no bridges between in vivo and in silico data, reliance on LLM inference with no pathway to ML training or reinforcement learning, assumptions tied to large-pharma resources, and single-objective optimization that ignores safety-efficacy-stability trade-offs. A paired knowledge-probing experiment suggests the bottleneck is architectural rather than epistemic: four frontier LLMs reason about peptides at levels comparable to small molecules, yet no framework exposes this capability. We propose design requirements and a capability matrix for next-generation frameworks that function as computational partners under realistic constraints.

---

*Brief version: 1.0 — 2026-02-12*
