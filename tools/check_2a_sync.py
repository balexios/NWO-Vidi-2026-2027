"""Compare section 2a in the Word draft with drafts/2a_academic_profile_draft.md.

Run before tools/fill_2a.py, which rebuilds 2a from the .md and would discard edits made in Word.
Only text is compared (bold/italic/colour changes are not detected).
"""
import re, subprocess, difflib, sys

PROJ = "/Users/dreamer/NWO-Vidi-2026-2027"
DOCX = f"{PROJ}/drafts/Vidi-2026-Pre-proposal-Voulimeneas.docx"
MD = f"{PROJ}/drafts/2a_academic_profile_draft.md"

txt = subprocess.run(["textutil", "-convert", "txt", "-stdout", DOCX],
                     capture_output=True, text=True, check=True).stdout
d = txt.split("Section 2a1. General academic profile", 1)[1].split("Word count 2a", 1)[0]
docx_paras = [l.strip() for l in d.splitlines()
              if l.strip() and l.strip() != "Section 2a2. Leadership and mentorship"]

md = open(MD, encoding="utf-8").read()
s = md.split("## 2a1. General academic profile", 1)[1]
s1, s2 = s.split("## 2a2. Leadership and mentorship", 1)
s2 = s2.split("\n## ", 1)[0]
md_paras = []
for blk in (s1, s2):
    for p in re.split(r"\n\s*\n", blk):
        p = p.strip().replace("\n", " ")
        if p and not p.startswith("![") and not p.startswith("(to be written"):
            md_paras.append(p.replace("**", "").strip("*"))

diff = list(difflib.unified_diff(md_paras, docx_paras, "markdown", "word", lineterm="", n=0))
if diff:
    print("\n".join(diff))
    sys.exit("Word and .md differ - port the Word edits into the .md before running fill_2a.py.")
print("In sync: section 2a text in Word matches the .md.")
