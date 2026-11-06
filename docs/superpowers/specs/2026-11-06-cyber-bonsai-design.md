# Design Specification: Pixel-Art Cyber Bonsai for GitHub Profile

## 1. Intent & Purpose
Create a unique, bespoke animated pixel-art Cyber Bonsai tree to replace the placeholder external GIF in the "About Me" section of Shaik Yusuf John's GitHub profile (`yusufjohn-shaik/yusufjohn-shaik`). 

The goal is to deliver an artistic, eye-catching visual centerpiece that does not rely on contribution graphs or external third-party services, while matching the repository's obsidian dark (`#0b0f17`) and electric cyan (`#38bdf8`) palette.

---

## 2. Goals & Non-Goals

### Goals
- **Self-Contained Vector Asset:** Produce an animated SVG (`assets/cyber-bonsai.svg`) with pure CSS keyframe and SMIL animations. Zero external API calls, zero rate limits, 100% uptime.
- **Aesthetic Consistency:** Pixel-art bonsai tree with dark wooden trunk, tiered glowing cyan/electric-blue foliage clumps, drifting blossom petals, and a gentle breathing neon aura.
- **Retina Crispness:** Render using SVG pixel primitives (`shape-rendering="crispEdges"`) for sharp pixel perfection on both mobile and 4K displays.
- **Responsive Integration:** Seamlessly integrate into the `About Me` table (38% column width) replacing the 300px Giphy GIF.

### Non-Goals
- No commit graph or GitHub contribution calendar integration.
- No heavy JavaScript execution or external dynamic backend services.

---

## 3. Approaches Considered

1. **Approach 1 (Selected): "About Me" Feature Slot**
   - Place the animated SVG directly inside the About Me table next to the bio text.
   - *Pros:* High visibility immediately upon landing, fixes an existing external dependency, perfectly balances the bio text.
   - *Cons:* Limited to ~300–350px width bounding box.

2. **Approach 2: Full-Width Zen Divider / Footer Centerpiece**
   - Place as a wide divider before the footer quote.
   - *Pros:* Allows a wider panoramic scene.
   - *Cons:* Pushed far down the page where users only see it after scrolling past all projects and stats.

---

## 4. Technical Specification

### 4.1 Asset Specifications (`assets/cyber-bonsai.svg`)
- **Dimensions:** `viewBox="0 0 320 280"`, `width="100%"`, `height="auto"`.
- **Palette:**
  - Pot / Planter: Dark slate & obsidian (`#0f172a`, `#1e293b`, `#334155`) with a cyan neon base rim (`#38bdf8`).
  - Trunk & Branches: Deep charcoal wood tones (`#1e2030`, `#272b3b`, `#3b4259`).
  - Bonsai Foliage: Multi-tiered pixel clumps in deep cyan (`#0284c7`), vibrant electric blue (`#0ea5e9`), and bright highlights (`#38bdf8`, `#7dd3fc`).
  - Falling Petals: 5–7 animated floating pixel petals with varying durations (3s–6s), staggered delays, and horizontal drift.
  - Atmosphere: Soft SVG glow filter (`feDropShadow` / `feGaussianBlur`) on the canopy and lantern/accent lights.
- **Animations:**
  - `drift-falling`: Petals float downward with oscillating lateral sway and opacity fade.
  - `breeze-sway`: Subtle organic rotation/translation on the upper foliage clumps.
  - `neon-pulse`: Soft breathing glow on neon accents.

### 4.2 README Integration (`README.md`)
- Update line 48 in `README.md`:
  ```html
  <td width="38%" align="center" valign="middle">
    <img src="assets/cyber-bonsai.svg" width="300" alt="Animated Pixel-Art Cyber Bonsai" />
  </td>
  ```

---

## 5. Verification Plan
1. Validate SVG XML syntax and render in standard browser.
2. Confirm animations loop smoothly without layout shift or CPU spikes.
3. Verify responsive layout in `README.md` across desktop and mobile widths.
