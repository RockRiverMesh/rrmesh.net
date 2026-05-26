"""Register a `qr` superfences block that renders the body as an inline QR SVG.

Usage in markdown:
    ```qr
    https://example.com/...
    ```

Options on the fence opener:
    alt="..."             Sets aria-label on the SVG (defaults to "QR code").
    width="200"           Sets the SVG width attribute. Mirrors to height if unset.
    height="200"          Sets the SVG height attribute. Mirrors to width if unset.
    link="true"           Wraps the SVG in <a href="<body>"> so the QR is clickable.
    link="https://..."    Wraps the SVG in <a href="<value>"> with an explicit target.
"""
import io
import re
from xml.sax.saxutils import quoteattr

import segno


_FG_PLACEHOLDER = "#fe0000"  # unlikely to appear elsewhere in segno output


def _svg(url: str, alt: str, width=None, height=None) -> str:
    buf = io.BytesIO()
    segno.make(url, error="m").save(
        buf,
        kind="svg",
        scale=8,
        border=2,
        xmldecl=False,
        svgns=False,
        dark=_FG_PLACEHOLDER,
    )
    svg = buf.getvalue().decode("utf-8")
    svg = svg.replace(_FG_PLACEHOLDER, "currentColor")
    intrinsic = re.search(r'\bwidth="(\d+)"\s+height="(\d+)"', svg)
    svg = svg.replace(
        "<svg ",
        f"<svg role=\"img\" aria-label={quoteattr(alt)} "
        f"viewBox=\"0 0 {intrinsic.group(1)} {intrinsic.group(2)}\" "
        f"style=\"color:var(--md-default-fg-color)\" ",
        1,
    )
    if width is not None:
        svg = re.sub(
            r'\bwidth="[^"]*"', f"width={quoteattr(str(width))}", svg, count=1
        )
    if height is not None:
        svg = re.sub(
            r'\bheight="[^"]*"', f"height={quoteattr(str(height))}", svg, count=1
        )
    return svg


def _validator(language, inputs, options, attrs, md):
    for key, value in inputs.items():
        options[key] = value
    return True


def _fence_format(source, language, css_class, options, md, **kwargs):
    url = source.strip()
    alt = options.get("alt", "QR code")
    width = options.get("width")
    height = options.get("height", width)
    if width is None and height is not None:
        width = height
    svg = _svg(url, alt, width=width, height=height)
    link = options.get("link")
    if not link or str(link).lower() in ("false", "no", "0"):
        return svg
    href = link if str(link).startswith(("http://", "https://", "/")) else url
    return f"<a href={quoteattr(href)} class=\"{css_class}-link\">{svg}</a>"


def on_config(config, **_):
    sf = config["mdx_configs"].setdefault("pymdownx.superfences", {})
    sf.setdefault("custom_fences", []).append(
        {
            "name": "qr",
            "class": "qr",
            "validator": _validator,
            "format": _fence_format,
        }
    )


