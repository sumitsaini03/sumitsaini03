# Holo Card design

The identity card uses Sumit’s current GitHub avatar in the supplied GitSkins frame, with language icons and animated sheen. The README follows the reference’s sequence of biography, four repository cards, language powers, and contribution history. The artwork uses the dark collector-card palette in both GitHub themes.

| Element | Colour |
| --- | --- |
| Card background | `#07070d` |
| Social tiles | `#11111d` with a `#2a2a44` outline |
| Foil edge | `#7c3aed` → `#22d3ee` → `#4ade80` → `#f472b6` |
| LinkedIn, LeetCode, X | `#94cbff`, `#ffd18a`, `#c4c1ff` |
| Contribution count | `#74ead5` |

GitHub displays each SVG as an image. The three profile links are HTML anchors around individual regions of the identity card. The six regions share a single coordinate system, and the portrait honors reduced-motion preferences.

Edit the complete header in [artwork/holo-id.svg](artwork/holo-id.svg). Rebuild its image regions with `python scripts/slice_holo.py`. The other panels are editable SVGs under [assets/holo](assets/holo). All visible assets are served from this repository.
