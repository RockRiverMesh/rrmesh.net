"""Stash the theme.logo SVG content into config.extra.logo_svg.

Lets the header partial render the logo inline (instead of as <img>) so
CSS can stroke its paths directly. Other contexts (e.g. the drawer)
keep using the standard <img> render.
"""
import re
from pathlib import Path


def on_config(config, **_):
    logo = config["theme"].get("logo")
    if not logo or not str(logo).lower().endswith(".svg"):
        return
    svg_path = Path(config["docs_dir"]) / logo
    if not svg_path.exists():
        return
    content = svg_path.read_text(encoding="utf-8")
    # XML declaration is invalid inside HTML
    content = re.sub(r"<\?xml[^?]*\?>\s*", "", content)
    config["extra"]["logo_svg"] = content
