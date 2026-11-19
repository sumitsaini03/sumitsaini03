"""Build the six GitHub README image regions from the editable Holo Card."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "artwork" / "holo-id.svg"
OUTPUT = ROOT / "assets" / "holo"
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)

# Each row's widths add up to 880. Keep the matching percentages in README.md.
REGIONS = [
    ("header", (0, 0, 880, 190), ("collector", "identity"), "Sumit Saini · @sumitsaini03 · Delhi Technological University"),
    ("portrait-center", (0, 190, 440, 96), ("collector",), "Portrait detail"),
    ("linkedin", (440, 190, 198, 96), ("linkedin",), "Sumit Saini on LinkedIn"),
    ("leetcode", (638, 190, 242, 96), ("leetcode",), "sumitsainidsa on LeetCode"),
    ("card-base", (0, 286, 638, 174), ("collector", "contributions"), "Languages and contributions"),
    ("twitter", (638, 286, 242, 174), ("twitter",), "@SumitSainifzxs on X"),
]


def write_region(name, bounds, groups, title):
    root = ET.parse(SOURCE).getroot()
    x, y, width, height = bounds
    root.set("viewBox", f"{x} {y} {width} {height}")
    root.set("width", str(width))
    root.set("height", str(height))
    root.set("aria-label", title)
    root.find(f"{{{NS}}}title").text = title

    for element in list(root):
        if element.tag == f"{{{NS}}}g" and element.get("id") not in groups:
            root.remove(element)
        elif element.tag in (f"{{{NS}}}defs", f"{{{NS}}}style") and "collector" not in groups:
            root.remove(element)

    if "collector" in groups and y < 286:
        # Only the bottom region needs the three language logo paths.
        for parent in root.iter():
            for child in list(parent):
                if child.get("id") == "powers" or child.tag == f"{{{NS}}}symbol":
                    parent.remove(child)

    ET.indent(root, space="  ")
    (OUTPUT / f"{name}.svg").write_text(ET.tostring(root, encoding="unicode") + "\n", encoding="utf-8")


if __name__ == "__main__":
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for region in REGIONS:
        write_region(*region)
