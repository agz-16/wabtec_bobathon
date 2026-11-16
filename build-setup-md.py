#!/usr/bin/env python3
"""Generate docs/setup.md from docs/tracks/setup.html.

Usage:  python3 build-setup-md.py

docs/tracks/setup.html is the single source of truth for the Environment Setup
steps. docs/setup.md is a plain-markdown copy of it (linked from README.md),
so do not edit setup.md by hand; edit the track file and re-run this script.

The interactive IP address box becomes a sentence. Standard library only.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "docs" / "tracks" / "setup.html"
OUT = ROOT / "docs" / "setup.md"

SKIP_TAGS = {"svg", "button", "input", "script", "style"}
VOID = {"img", "br", "input", "hr", "meta", "link"}

SERVER_NOTE = (
    "Your instructor will give you the IP address of your server. Wherever this "
    "guide shows `<myIPaddress>`, use that address."
)


def fail(msg):
    print("ERROR: " + msg, file=sys.stderr)
    sys.exit(1)


class Node:
    def __init__(self, tag, attrs, parent):
        self.tag = tag
        self.attrs = attrs
        self.parent = parent
        self.children = []

    def has(self, cls):
        return cls in (self.attrs.get("class") or "").split()

    def elements(self):
        return [c for c in self.children if isinstance(c, Node)]

    def find(self, cls):
        for c in self.elements():
            if c.has(cls):
                return c
            hit = c.find(cls)
            if hit:
                return hit
        return None

    def find_all(self, cls):
        found = []
        for c in self.elements():
            if c.has(cls):
                found.append(c)
            found.extend(c.find_all(cls))
        return found

    def find_tag(self, tag):
        found = []
        for c in self.elements():
            if c.tag == tag:
                found.append(c)
            found.extend(c.find_tag(tag))
        return found


class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root", {}, None)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        node = Node(tag, dict(attrs), self.cur)
        self.cur.children.append(node)
        if tag not in VOID:
            self.cur = node

    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.children.append(data)


def collapse(text):
    return re.sub(r"\s+", " ", text.replace("\xa0", " ")).strip()


def raw_text(node):
    if isinstance(node, str):
        return node
    if node.tag in SKIP_TAGS:
        return ""
    return "".join(raw_text(c) for c in node.children)


def inline(node):
    out = []
    for c in node.children:
        if isinstance(c, str):
            out.append(c.replace("*", "\\*"))
            continue
        tag = c.tag
        if tag in SKIP_TAGS:
            continue
        if tag in ("strong", "b"):
            out.append("**" + inline(c).strip() + "**")
        elif tag in ("em", "i"):
            out.append("*" + inline(c).strip() + "*")
        elif tag == "code":
            out.append("`" + collapse(raw_text(c)) + "`")
        elif tag == "a":
            out.append("[%s](%s)" % (collapse(inline(c)).rstrip("↗").strip(), c.attrs.get("href", "")))
        elif tag == "br":
            out.append(" ")
        elif tag == "img":
            out.append("![%s](%s)" % (c.attrs.get("alt", ""), c.attrs.get("src", "")))
        else:
            out.append(inline(c))
    return "".join(out)


def para(node):
    return collapse(inline(node))


def table_block(table):
    heads = table.find_tag("th")
    aligns = ["center" in (h.attrs.get("style") or "") for h in heads]

    def cell(n):
        return para(n).replace("|", "\\|")

    lines = ["| " + " | ".join(cell(h) for h in heads) + " |",
             "|" + "|".join(":---:" if a else "---" for a in aligns) + "|"]
    for tr in table.find_tag("tr"):
        tds = [c for c in tr.elements() if c.tag == "td"]
        if tds:
            lines.append("| " + " | ".join(cell(td) for td in tds) + " |")
    return ("table", "\n".join(lines))


def block(node):
    """Return a list of (kind, text) blocks for one element."""
    if isinstance(node, str):
        return []
    if node.tag in SKIP_TAGS:
        return []
    if node.has("step-title") or node.has("uc-title") or node.has("step-num"):
        return []
    if node.has("detail-intro") or node.has("uc-desc") or node.has("step-desc") or node.tag == "p":
        text = para(node)
        return [("p", text)] if text else []
    if node.has("info-box") or node.has("warn-box"):
        return [("quote", "> " + para(node))]
    if node.has("step-screenshot"):
        img = node.find_tag("img")[0]
        out = [("img", "![%s](%s)" % (img.attrs.get("alt", ""), img.attrs.get("src", "")))]
        cap = node.find("step-screenshot-caption")
        if cap:
            out.append(("p", "*" + para(cap) + "*"))
        return out
    if node.has("step-prompt"):
        pre = node.find_tag("pre")[0]
        return [("code", "```\n" + raw_text(pre).strip("\n") + "\n```")]
    if node.has("server-ip-field"):
        return [("p", SERVER_NOTE)]
    if node.tag == "table":
        return [table_block(node)]
    if node.has("mode-steps"):
        return [("list", steps_block(node))]
    out = []
    for c in node.elements():
        out.extend(block(c))
    return out


def indent(text, n=3):
    pad = " " * n
    return "\n".join(pad + line if line.strip() else "" for line in text.split("\n"))


def steps_block(steps):
    """A numbered list. A step with no title is rendered flat (no number)."""
    parts = []
    for step in steps.elements():
        if not step.has("mode-step"):
            continue
        num = collapse(raw_text(step.find("step-num")))
        body = step.find("step-body")
        title = body.find("step-title")
        blocks = []
        for c in body.elements():
            blocks.extend(block(c))
        if title is None:
            parts.append("\n\n".join(t for _, t in blocks))
            continue
        head = "%s. **%s**" % (num, para(title))
        if blocks and blocks[0][0] == "p":
            head += " — " + blocks[0][1]
            blocks = blocks[1:]
        parts.append("\n\n".join([head] + [indent(t) for _, t in blocks]))
    return "\n\n".join(parts)


def main():
    if not SRC.is_file():
        fail("missing " + str(SRC))
    tree = Tree()
    tree.feed(SRC.read_text(encoding="utf-8"))
    card = tree.root.find("bubble-card")
    if card is None:
        fail("no .bubble-card found in " + str(SRC))

    title = collapse(raw_text(card.find("card-title")))
    intro = para(card.find("detail-intro"))

    md = [
        "<!-- Generated from docs/tracks/setup.html by build-setup-md.py. Do not edit by hand. -->",
        "# " + title,
        intro,
    ]
    for uc in card.find_all("use-case"):
        md.append("---")
        md.append("## " + collapse(raw_text(uc.find("uc-title"))))
        md.extend(t for _, t in block(uc.find("uc-body")))

    OUT.write_text("\n\n".join(md) + "\n", encoding="utf-8")
    print("Wrote %s (%d use-cases)" % (OUT, len(card.find_all("use-case"))))


if __name__ == "__main__":
    main()
