# Pixel-Art Cyber Bonsai Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a custom animated pixel-art Cyber Bonsai vector asset (`assets/cyber-bonsai.svg`) and integrate it into the About Me table of the GitHub profile README (`yusufjohn-shaik/yusufjohn-shaik`), replacing the external Giphy GIF.

**Architecture:** A standalone vector SVG asset using embedded CSS `@keyframes` and SMIL for infinite loop animations (drifting petals, branch sway, and neon pulse). It relies on SVG pixel art primitives with `shape-rendering="crispEdges"` for sharpness, committed directly to the repository for zero external dependencies and 100% uptime.

**Tech Stack:** SVG, CSS keyframe animations, Markdown, Python (for XML/schema validation tests).

**Spec:** `docs/superpowers/specs/2026-11-06-cyber-bonsai-design.md`

## Global Constraints
- **File location:** Asset saved to `assets/cyber-bonsai.svg`.
- **Palette adherence:** Obsidian `#0b0f17`, midnight `#0f172a`, charcoal wood `#1e2030` / `#2b3044`, foliage and neon `#0284c7`, `#0ea5e9`, `#38bdf8`, `#7dd3fc`.
- **Zero external URLs:** Asset must be self-contained within the SVG file (no external font imports, scripts, or external images).
- **Retina Crispness:** Use `shape-rendering="crispEdges"` on pixel rectangles so it remains sharp without blurry anti-aliasing.

## Review Focus
1. **XML Validity:** Malformed SVG tags or unescaped characters cause GitHub Camo proxy to render broken image placeholders.
2. **Animation Loop Timing:** Petal animation cycles must loop seamlessly without abrupt jumping or visual stutter.
3. **Responsive Bounding Box:** Aspect ratio preservation (`viewBox="0 0 320 280"`) ensuring it scales cleanly inside the 38% width table cell.
4. **Dark Mode Contrast:** Foliage highlights and neon pot trim must maintain high contrast against both dark and dim GitHub backgrounds.
5. **No Layout Shift:** The fixed aspect ratio must not cause table column jitter on load.

---

### Task 1: Create Animated Pixel-Art Cyber Bonsai SVG Asset

**Files:**
- Create: `assets/cyber-bonsai.svg`
- Test: `tests/test_cyber_bonsai.py`

**Interfaces:**
- Produces: `assets/cyber-bonsai.svg` with viewBox `0 0 320 280` and valid CSS keyframe animations (`petal-drift`, `branch-sway`, `neon-glow`).

- [ ] **Step 1: Write test for SVG validity, structure, and required animations**

Create `tests/test_cyber_bonsai.py`:
```python
import xml.etree.ElementTree as ET
import os

def test_svg_validity_and_structure():
    svg_path = "assets/cyber-bonsai.svg"
    assert os.path.exists(svg_path), f"{svg_path} does not exist"
    
    # Check valid XML parse
    tree = ET.parse(svg_path)
    root = tree.getroot()
    
    # Check root attributes
    assert root.tag.endswith('svg')
    assert "0 0 320 280" in root.attrib.get('viewBox', '')
    
    # Check style and keyframes present
    with open(svg_path, 'r', encoding='utf-8') as f:
        content = f.read()
    assert "@keyframes" in content
    assert "petal-drift" in content or "petal" in content
    assert "#38bdf8" in content  # Neon cyan palette
    assert "shape-rendering=\"crispEdges\"" in content
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 tests/test_cyber_bonsai.py`
Expected: FAIL (file `assets/cyber-bonsai.svg` does not exist).

- [ ] **Step 3: Implement `assets/cyber-bonsai.svg`**

Build the pixel-art Cyber Bonsai SVG:
- Geometric obsidian bonsai pot at the base (`y: 210-245`) with neon cyan accent strip (`#38bdf8`) and pot stand legs.
- Stylized pixel trunk with twisted gnarled branches reaching upward and rightward (`#1e2030`, `#2b3044`).
- Multi-layered foliage clusters in pixel blocks with gradient depth (`#0284c7`, `#0ea5e9`, `#38bdf8`, `#bae6fd`).
- 6 individual floating/falling pixel petals with staggered CSS animation delays and drift trajectories.
- Embedded `<style>` block defining `@keyframes petal-drift`, `@keyframes branch-sway`, and `@keyframes neon-glow`.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 tests/test_cyber_bonsai.py`
Expected: PASS with exit code 0.

- [ ] **Step 5: Commit**

```bash
git add assets/cyber-bonsai.svg tests/test_cyber_bonsai.py
git commit -m "feat(assets): create animated pixel-art cyber bonsai svg"
```

---

### Task 2: Integrate Cyber Bonsai into README.md

**Files:**
- Modify: `README.md:46-51`
- Test: `tests/test_readme_integration.py`

**Interfaces:**
- Consumes: `assets/cyber-bonsai.svg` from Task 1.
- Produces: Updated `README.md` referencing `assets/cyber-bonsai.svg` in the About Me table.

- [ ] **Step 1: Write test for README integration**

Create `tests/test_readme_integration.py`:
```python
import os

def test_readme_references_cyber_bonsai():
    readme_path = "README.md"
    assert os.path.exists(readme_path)
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    assert "assets/cyber-bonsai.svg" in content
    assert "media.giphy.com" not in content  # External GIF removed
    assert "alt=\"Pixel-Art Cyber Bonsai\"" in content
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 tests/test_readme_integration.py`
Expected: FAIL (README still references `media.giphy.com`).

- [ ] **Step 3: Update `README.md`**

Replace line 48 in `README.md`:
```html
    <td width="38%" align="center" valign="middle">
      <img src="assets/cyber-bonsai.svg" width="300" alt="Pixel-Art Cyber Bonsai" />
    </td>
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 tests/test_readme_integration.py`
Expected: PASS with exit code 0.

- [ ] **Step 5: Commit**

```bash
git add README.md tests/test_readme_integration.py
git commit -m "feat(profile): integrate animated pixel-art cyber bonsai into about me"
```

---

### Task 3: Full Verification and Cleanup

**Files:**
- Test: Execute all tests (`python3 -m unittest discover tests` or running both test scripts).
- Cleanup: Remove temporary test scripts or retain them in `tests/`.

- [ ] **Step 1: Run comprehensive test suite**

Run:
```bash
python3 tests/test_cyber_bonsai.py
python3 tests/test_readme_integration.py
```
Expected: Both tests exit 0 with clean verification.

- [ ] **Step 2: Verify git status and diff**

Run: `git status && git diff main`
Expected: Only `assets/cyber-bonsai.svg`, `README.md`, and design/plan docs are staged or committed.

- [ ] **Step 3: Final commit & push prep**

Ensure all changes are cleanly committed on a dedicated feature branch `feat/cyber-bonsai`.
