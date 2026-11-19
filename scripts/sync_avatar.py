"""Refresh both portraits from the public GitHub avatar and rebuild the README regions."""
import base64
import re
from urllib.request import Request, urlopen

from slice_holo import REGIONS, ROOT, SOURCE, write_region

AVATAR_URL = "https://avatars.githubusercontent.com/u/219871794?s=420&v=4"
ABOUT = ROOT / "assets" / "holo" / "about.svg"
EMBED = re.compile(r'(<image\b[^>]*?\shref=")data:image/[a-z]+;base64,[^"]+(")')


def read_avatar():
    request = Request(AVATAR_URL, headers={"User-Agent": "sumitsaini03-profile-avatar"})
    with urlopen(request, timeout=30) as response:
        body = response.read(2_000_001)
        mime = response.headers.get_content_type()
    valid = {
        "image/jpeg": body.startswith(b"\xff\xd8\xff") and body.endswith(b"\xff\xd9"),
        "image/png": body.startswith(b"\x89PNG\r\n\x1a\n") and body[-8:-4] == b"IEND",
        "image/gif": body.startswith((b"GIF87a", b"GIF89a")) and body.endswith(b";"),
        "image/webp": body.startswith(b"RIFF") and body[8:12] == b"WEBP",
    }
    if len(body) > 2_000_000 or not valid.get(mime):
        raise ValueError("GitHub returned an oversized or unrecognized avatar image")
    return f"data:{mime};base64,{base64.b64encode(body).decode('ascii')}"


def sync_avatar():
    uri = read_avatar()
    updates = {}
    for path in (SOURCE, ABOUT):
        original = path.read_text(encoding="utf-8")
        updated, count = EMBED.subn(lambda m: m[1] + uri + m[2], original)
        if count != 1:
            raise ValueError(f"Expected one embedded portrait in {path.relative_to(ROOT)}")
        if updated != original:
            updates[path] = updated
    for path, updated in updates.items():
        path.write_text(updated, encoding="utf-8")
    for region in REGIONS:
        write_region(*region)


if __name__ == "__main__":
    sync_avatar()
