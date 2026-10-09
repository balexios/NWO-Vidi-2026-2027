"""Fill NWO's literature-list template from drafts/literature_list_draft.md."""
import re, sys, os, zipfile
from xml.sax.saxutils import escape

PROJ = "/Users/dreamer/NWO-Vidi-2026-2027"
TEMPLATE = f"{PROJ}/nwo-documents/Vidi-2026-Literature_list.docx"
OUT = f"{PROJ}/drafts/Vidi-2026-Literature-list-Voulimeneas.docx"
NAME = "Dr. A. Voulimeneas"
TITLE = "ACCESS – Advanced Compartmentalization for Secure Software"

if os.path.exists(f"{PROJ}/drafts/~$di-2026-Literature-list-Voulimeneas.docx"):
    sys.exit("The literature list is open in Word - close it first, then rerun.")
md = open(f"{PROJ}/drafts/literature_list_draft.md", encoding="utf-8").read().split("\n## List\n", 1)[1]
items = re.findall(r"^\d+\.\s+(.+)$", md, re.M)
assert 1 <= len(items) <= 10, len(items)

def run(text):
    return f'<w:r><w:t xml:space="preserve">{escape(text)}</w:t></w:r>'

PPR = '<w:pPr><w:spacing w:line="260" w:lineRule="exact"/></w:pPr>'
zin = zipfile.ZipFile(TEMPLATE)
x = zin.read("word/document.xml").decode("utf-8")
for label, val in (("<w:t>Applicant title(s), initial(s) and surname(s):</w:t></w:r>", NAME),
                   ("<w:t>:</w:t></w:r>", TITLE)):           # "Title of the proposal" + ":" runs
    k = x.find(label) + len(label)
    assert k > len(label), label
    x = x[:k] + run(" " + val) + x[k:]
k = x.find("<w:t>committee.</w:t></w:r></w:p>") + len("<w:t>committee.</w:t></w:r></w:p>")
lst = f"<w:p>{PPR}</w:p>" + "".join(
    f'<w:p><w:pPr><w:spacing w:after="120"/><w:ind w:left="397" w:hanging="397"/></w:pPr>{run(f"[{i}]")}<w:r><w:tab/></w:r>{run(t)}</w:p>'
    for i, t in enumerate(items, 1))
x = x[:k] + lst + x[k:]

tmp = OUT + ".tmp"
with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
    for it in zin.infolist():
        zout.writestr(it, x.encode("utf-8") if it.filename == "word/document.xml" else zin.read(it.filename))
os.replace(tmp, OUT)
print(f"Literature list: {len(items)} items -> {OUT}")
