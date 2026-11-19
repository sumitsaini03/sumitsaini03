# Publishing the Holo Card

The root [README.md](README.md) of [sumitsaini03/sumitsaini03](https://github.com/sumitsaini03/sumitsaini03) supplies the [public profile page](https://github.com/sumitsaini03). Its image paths resolve inside this repository. [ProfileMaxxxing](https://github.com/sumitsaini03/ProfileMaxxxing) is the separate design repository.

## Editing the header

1. Edit [the complete SVG](artwork/holo-id.svg) for artwork or label changes. Update the corresponding HTML link and image alternative in the README when a profile address or handle changes.
2. Run `python scripts/slice_holo.py` from the repository root and commit the regenerated regions in `assets/holo/`.
3. Review the rendered README and open each of the three social tiles. The project cards link to their repositories.

The activity panel and profile metrics are dated snapshots. The original cinematic assets under `assets/` and their generator, `scripts/generate_assets.py`, belong to the earlier design.

## Profile picture

GitHub is the source for both portraits. The **Sync GitHub profile picture** workflow checks hourly, or you can run it manually from Actions. It commits a change only when the artwork differs. To refresh locally, run `python scripts/sync_avatar.py`. The profile uses self-contained images so GitHub can display the photo inside each card.
