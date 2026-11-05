# Publishing and validation

The design is published in two public repositories:

- [ProfileMaxxxing](https://github.com/sumitsaini03/ProfileMaxxxing): the requested design source.
- [sumitsaini03](https://github.com/sumitsaini03/sumitsaini03): the matching-name repository that GitHub displays on [the profile](https://github.com/sumitsaini03).

Both initially contain the same README and six SVG assets. They are independent repositories, not an automated mirror. Future content changes must reach the `main` branch of `sumitsaini03` to update the profile; update ProfileMaxxxing as well to keep the design source aligned.

From this checkout, after committing future changes, publish both:

```sh
git push origin HEAD:main
git push https://github.com/sumitsaini03/sumitsaini03.git HEAD:main
```

## Validation

- All six SVG files parse successfully and all local README image references resolve.
- Browser previews at 1280, 768 and 390 pixels have no horizontal document overflow, missing local images or broken internal anchors.
- The Impeccable mechanical detector returned no findings.
- The design-taste browser inspector was run. Its generic website rules flag the fixed GitHub-style layout, absence of webpage animations and raster-picture count. Those are not a complete pass; the inspector cannot inspect animation or type inside externally rendered SVGs. The actual GitHub document was reviewed visually and the user's requested glass reference takes precedence over a new website style.
- Project facts were checked against public repository READMEs and Telecom's saved evaluation JSON. This profile task did not rerun model training or project benchmarks.

The orbital animation respects reduced motion where supported. GitHub controls page chrome and Markdown styling, and asset changes may be cached briefly.
