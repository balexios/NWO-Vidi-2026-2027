"""Insert section 2a (from the markdown draft) into the Vidi pre-proposal docx.

**bold** -> bold run, [CHECK ...] -> red run. Everything else Calibri 9.5pt black.
A paragraph of the form ![](path/to/image.png){width_cm} -> centred image (path relative
to the project folder; default width 12 cm).
"""
import re, shutil, sys, zipfile, os, struct
from xml.sax.saxutils import escape

PROJ = "/Users/dreamer/NWO-Vidi-2026-2027"
DOCX = f"{PROJ}/drafts/Vidi-2026-Pre-proposal-Voulimeneas.docx"
MD = f"{PROJ}/drafts/2a_academic_profile_draft.md"

md = open(MD, encoding="utf-8").read()
s1 = md.split("## 2a1. General academic profile", 1)[1]
s1, s2 = s1.split("## 2a2. Leadership and mentorship", 1)
s2 = s2.split("\n## ", 1)[0]  # stop at References / Parking lot
paras = lambda s: [p.strip().replace("\n", " ") for p in re.split(r"\n\s*\n", s)
                   if p.strip() and not p.strip().startswith("(to be written")]
P1, P2 = paras(s1), paras(s2)
IMG_RE = re.compile(r"^!\[[^\]]*\]\(([^)]+)\)(?:\{([\d.]+)(?:,(\d+))?\})?$")  # {width_cm,words_in_figure}
CAP_RE = re.compile(r"^\*([^*].*[^*])\*$")  # *whole paragraph in single stars* -> centred italic caption
IMAGES = []  # (rel_id, zip_name, bytes)

def image_xml(path, width_cm):
    data = open(os.path.join(PROJ, path), "rb").read()
    w, h = struct.unpack(">II", data[16:24])  # PNG header
    n = len(IMAGES) + 1
    rid, name = f"rIdFig{n}", f"word/media/fig{n}.png"
    IMAGES.append((rid, name, data))
    cx = int(width_cm * 360000); cy = int(cx * h / w)
    A = "http://schemas.openxmlformats.org/drawingml/2006/main"
    PIC = "http://schemas.openxmlformats.org/drawingml/2006/picture"
    return ('<w:p><w:pPr><w:spacing w:before="120" w:after="120"/><w:jc w:val="center"/></w:pPr><w:r><w:drawing>'
            f'<wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="{cx}" cy="{cy}"/>'
            f'<wp:docPr id="{9000 + n}" name="Figure {n}"/>'
            f'<wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="{A}" noChangeAspect="1"/></wp:cNvGraphicFramePr>'
            f'<a:graphic xmlns:a="{A}"><a:graphicData uri="{PIC}"><pic:pic xmlns:pic="{PIC}">'
            f'<pic:nvPicPr><pic:cNvPr id="0" name="fig{n}.png"/><pic:cNvPicPr/></pic:nvPicPr>'
            f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
            f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
            '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic>'
            '</wp:inline></w:drawing></w:r></w:p>')

def run(text, bold=False, red=False, italic=False):
    rpr = ('<w:rPr><w:rFonts w:ascii="Calibri" w:eastAsia="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>'
           + ('<w:b/><w:bCs/>' if bold else '') + ('<w:i/><w:iCs/>' if italic else '')
           + f'<w:color w:val="{"FF0000" if red else "000000"}"/>'
           + '<w:sz w:val="19"/><w:szCs w:val="19"/><w:lang w:val="en-GB"/></w:rPr>')
    return f'<w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'

def para_xml(text, ppr):
    m = IMG_RE.match(text)
    if m:
        return image_xml(m.group(1), float(m.group(2) or 12))
    m = CAP_RE.match(text)
    if m:
        return ('<w:p><w:pPr><w:spacing w:after="120"/><w:jc w:val="center"/></w:pPr>'
                + run(m.group(1), italic=True) + '</w:p>')
    return f"<w:p>{ppr}{runs_xml(text)}</w:p>"

def runs_xml(text):
    out = []
    for tok in re.split(r"(\*\*.+?\*\*|\[CHECK[^\]]*\])", text):
        if not tok:
            continue
        if tok.startswith("**"):
            out.append(run(tok[2:-2], bold=True))
        elif tok.startswith("[CHECK"):
            out.append(run(tok, red=True))
        else:
            out.append(run(tok))
    return "".join(out)

def fig_words(ps):
    return sum(int(m.group(3) or 0) for m in map(IMG_RE.match, ps) if m)

def words(ps):
    t = " ".join(re.sub(r"\[CHECK[^\]]*\]", "", p).replace("**", "").strip("*") for p in ps if not IMG_RE.match(p))
    return len(t.split())

def text_index(x):
    """Concatenated w:t text plus, per char, the xml offset of its w:t element."""
    chars, offs = [], []
    for m in re.finditer(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", x):
        for c in m.group(1):
            chars.append(c); offs.append(m.start())
    return "".join(chars), offs

def insert_after_heading(x, heading, ps):
    txt, offs = text_index(x)
    k = txt.rfind(heading)
    if k < 0:
        sys.exit(f"Heading not found: {heading!r}")
    pos = x.find("</w:p>", offs[k]) + len("</w:p>")
    m = re.compile(r"<w:p[ >]").search(x, pos)
    start = m.start(); end = x.find("</w:p>", start) + len("</w:p>")
    target = x[start:end]
    pm = re.search(r"<w:pPr>.*?</w:pPr>", target)
    ppr = pm.group(0) if pm else ""
    empty = "<w:t" not in target and not re.search(r"<w:p[ >]", target[4:])
    blank = f"<w:p>{ppr}</w:p>"
    new = ""
    for i, p in enumerate(ps):
        cur = para_xml(p, ppr)
        # no blank spacer paragraph around images
        if i and not IMG_RE.match(p) and not IMG_RE.match(ps[i - 1]):
            new += blank
        new += cur
    if not ps:
        return x
    if empty:
        return x[:start] + new + x[end:]
    return x[:start] + new + x[start:]

if os.path.exists(f"{PROJ}/drafts/~$di-2026-Pre-proposal-Voulimeneas.docx"):
    sys.exit("The draft is open in Word - close it first, then rerun.")

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "preproposal_base_before_2a.docx")
shutil.copy(DOCX, DOCX + ".bak")
zin = zipfile.ZipFile(BASE)  # rebuild 2a from the version without section 2a
x = zin.read("word/document.xml").decode("utf-8")
# later heading first so earlier offsets stay valid
x = insert_after_heading(x, "Section 2a2. Leadership and mentorship", P2)
x = insert_after_heading(x, "Section 2a1. General academic profile", P1)


# fill the "Word count (section 2a1 + 2a2)" field; NWO counts text inside figures too
TOTAL = words(P1) + words(P2) + fig_words(P1) + fig_words(P2)
k = x.find("<w:t>Word count (section 2a</w:t>")
if k < 0:
    sys.exit("Word-count field for 2a not found")
c0 = x.rfind("<w:sdtContent>", 0, k) + len("<w:sdtContent>")
c1 = x.find("</w:sdtContent>", k)
x = x[:c0] + run(str(TOTAL)) + x[c1:]
p = x.rfind("<w:showingPlcHdr/>", 0, c0)
if p > x.rfind("<w:sdt>", 0, c0):  # drop placeholder flag of this field only
    x = x[:p] + x[p + len("<w:showingPlcHdr/>"):]

# 2b culture-and-standards box, from drafts/2b_key_outputs_draft.md (first paragraph of that section)
md2b = open(f"{PROJ}/drafts/2b_key_outputs_draft.md", encoding="utf-8").read()
CULTURE = md2b.split("## Culture and standards box", 1)[1].split("\n", 1)[1].strip().split("\n\n", 1)[0].replace("\n", " ")
k = x.find("optional in max. 50 words]")
m = re.compile(r"<w:p [^>]*>(<w:pPr>.*?</w:pPr>)</w:p>").search(x, x.find("<w:tc>", k))
if not m or "<w:t" in m.group(0):
    sys.exit("Culture box not found or not empty")
x = x[:m.start()] + f"<w:p>{m.group(1)}{run(CULTURE)}</w:p>" + x[m.end():]

# 2b key outputs, from the "## Key outputs" section of the 2b draft (### KO<n> blocks with "- Field: value" lines)
def set_sdt(b, placeholder, value):
    """Replace the content of the content control showing `placeholder` with `value`."""
    i = b.find(f">{placeholder}</w:t>")
    if i < 0:
        sys.exit(f"Field not found: {placeholder!r}")
    s0 = b.rfind("<w:sdt>", 0, i)
    c0 = b.find("<w:sdtContent>", s0) + len("<w:sdtContent>")
    c1 = b.find("</w:sdtContent>", i)
    head = b[s0:c0].replace("<w:showingPlcHdr/>", "")
    return b[:s0] + head + run(value) + b[c1:]

def fill_after(b, label, text):
    """Put `text` in the (empty) paragraph of the table cell after the cell holding `label`."""
    i = b.find(f">{label}</w:t>")
    tc = b.find("<w:tc>", i)
    pe = b.find("</w:p>", tc)
    if i < 0 or re.search(r"<w:t[ >]", b[tc:pe]):
        sys.exit(f"Empty field after {label!r} not found")
    return b[:pe] + runs_xml(text) + b[pe:]

kos_md = md2b.split("## Key outputs", 1)[1].split("\n## ", 1)[0]
parts = re.split(r"^### KO(\d+)\s*$", kos_md, flags=re.M)
KOS = {int(n): dict(re.findall(r"^- ([A-Za-z0-9 ]+): (.+)$", body, re.M)) for n, body in zip(parts[1::2], parts[2::2])}
MOTIV_WORDS = 0
for n, f in sorted(KOS.items()):
    i = x.find(f">Key output {n}<")
    j = x.find(f">Key output {n + 1}<") if n < 10 else x.find(">Word count 2b")
    b = x[i:j]
    if f.get("Open Access") in ("Yes", "No"):
        b = set_sdt(b, "Yes/No", f["Open Access"])
    b = fill_after(b, "Reference:", f["Reference"])
    url_xml = runs_xml(f["URL"])
    if f.get("URL2"):  # second link to an open-access copy (allowed by the form)
        url_xml += '<w:r><w:br/></w:r>' + runs_xml(f["URL2"])
    ui = b.find(">URL:</w:t>"); tc = b.find("<w:tc>", ui); pe = b.find("</w:p>", tc)
    if ui < 0 or re.search(r"<w:t[ >]", b[tc:pe]):
        sys.exit("Empty field after 'URL:' not found")
    b = b[:pe] + url_xml + b[pe:]
    b = set_sdt(b, "Choose an output type", f["Type"])
    inds = [s.strip() for s in f.get("Indicators", "").split(" ; ") if s.strip()]
    for ph, val in zip(["Choose an indicator", "Optional: choose a second indicator",
                        "Optional: choose a third indicator"], inds):
        b = set_sdt(b, ph, val)
    b = fill_after(b, "Motivation:", f["Motivation"])
    MOTIV_WORDS += len(re.sub(r"\[CHECK[^\]]*\]", "", f["Motivation"]).replace("**", "").split())
    x = x[:i] + b + x[j:]

if KOS:  # 2b word-count field: motivations only (references, URLs, types and indicators excluded)
    k = x.find(">Word count (section 2b ")
    c0 = x.rfind("<w:sdtContent>", 0, k) + len("<w:sdtContent>")
    c1 = x.find("</w:sdtContent>", k)
    x = x[:c0] + run(str(MOTIV_WORDS)) + x[c1:]
    p = x.rfind("<w:showingPlcHdr/>", 0, c0)
    if p > x.rfind("<w:sdt>", 0, c0):
        x = x[:p] + x[p + len("<w:showingPlcHdr/>"):]

# 4d. Current appointment (user, 2026-10-09: 1.0 FTE contract, 40% research / 40% teaching / 20% management)
CURRENT = {"position": "Assistant professor", "type": "Position: Permanent", "start": "15-9-2023",  # contract "Ingangsdatum"
           "fte": "1.0", "research_fte": "0.4", "institution": "Delft University of Technology (TU Delft)"}
a = x.find(">Current appointment<")
r0 = x.find("</w:tr>", a) + len("</w:tr>")          # skip the header row
r1 = x.find("</w:tr>", r0) + len("</w:tr>")
row = set_sdt(x[r0:r1], "Please select from dropdown", CURRENT["position"])
row = set_sdt(row, "Please select from dropdown)", CURRENT["type"])
row = set_sdt(row, "Start date", CURRENT["start"])
row = row.replace('<w:date><w:dateFormat w:val="d-M-yyyy"/>', '<w:date w:fullDate="2023-09-15T00:00:00Z"><w:dateFormat w:val="d-M-yyyy"/>', 1)
cells = [m.start() for m in re.finditer(r"<w:tc>", row)]
for col, val in reversed(list(zip([3, 4, 5], [CURRENT["fte"], CURRENT["research_fte"], CURRENT["institution"]]))):
    pe = row.find("</w:p>", cells[col])
    if re.search(r"<w:t[ >]", row[cells[col]:pe]):
        sys.exit(f"4d cell {col} not empty")
    row = row[:pe] + runs_xml(val) + row[pe:]
x = x[:r0] + row + x[r1:]

# Section 3 key words and section 4 details (2026-10-09; sources: CV, eScholarship, user). [CHECK ...] = red.
KEYWORDS = "Compartmentalization, software security, isolation, dynamic analysis, operating systems"
S4 = {"Title(s), initial(s), surname(s):": "Dr. A. Voulimeneas",
      "University/College of higher education:": "University of California, Irvine (United States)",
      "Thesis title:": "Building the Next Generation of Security Focused NVX Systems: Overcoming Limitations of N-Variant Execution",
      "Host institution:": "Delft University of Technology (TU Delft)",
      "Research group:": "Cybersecurity group, Department of Intelligent Systems, Faculty of Electrical Engineering, Mathematics and Computer Science"}
SUPERVISOR = "Prof. M. Franz"
PAST = {"position": "Postdoctoral researcher", "fte": "1.0", "research_fte": "1.0",  # user
        "institution": "KU Leuven (Belgium)"}
SIGN_NAME, SIGN_PLACE = "A. Voulimeneas", "Delft"

# Section 3 title: whole title underlined (NWO rule), letters forming ACCESS in bold.
TITLE = [("ACCESS – ", 0), ("A", 1), ("dvan", 0), ("c", 1), ("ed ", 0), ("C", 1), ("ompartm", 0), ("e", 1),
         ("ntalization for ", 0), ("S", 1), ("ecure ", 0), ("S", 1), ("oftware", 0)]
k = x.find(">Title:<"); c0 = x.find("<w:sdtContent>", k) + len("<w:sdtContent>"); c1 = x.find("</w:sdtContent>", c0)
x = x[:c0] + "".join(run(t, bold=b).replace("<w:color ", '<w:u w:val="single"/><w:color ', 1) for t, b in TITLE) + x[c1:]
x = set_sdt(x, "Key words separated by commas (same as in ISAAC)", KEYWORDS)
IDEA = open(f"{PROJ}/drafts/3_research_idea_draft.md", encoding="utf-8").read().split("\n## Research idea\n", 1)[1].strip().replace("\n", " ")
IDEA_WORDS = len(IDEA.split())
x = set_sdt(x, "Research idea (same as ‘Abstract’ in ISAAC)", IDEA)
k = x.rfind("<w:sdt>", 0, x.find(">Word count (section 3 "))
x = x[:k] + set_sdt(x[k:], "excluding title and key words", str(IDEA_WORDS))
for label, val in S4.items():
    x = fill_after(x, label, val)
k = x.find("Date of PhD award")                       # PhD award 12 June 2020 (user)
x = x[:k] + set_sdt(x[k:], "Choose the date", "12-6-2020").replace(
    '<w:date><w:dateFormat w:val="d-M-yyyy"/>', '<w:date w:fullDate="2020-06-12T00:00:00Z"><w:dateFormat w:val="d-M-yyyy"/>', 1)
k = x.find(">Promotor(")                               # supervisor label is split over several runs
tc = x.find("<w:tc>", k); pe = x.find("</w:p>", tc)
assert not re.search(r"<w:t[ >]", x[tc:pe]), "supervisor cell not empty"
x = x[:pe] + runs_xml(SUPERVISOR) + x[pe:]

a = x.find(">Past appointments<")
r0 = x.find("</w:tr>", a) + len("</w:tr>"); r1 = x.find("</w:tr>", r0) + len("</w:tr>")
row = set_sdt(x[r0:r1], "Please select from dropdown", PAST["position"])
for ph, shown, iso in (("date", "1-9-2020", "2020-09-01"), ("End date", "31-8-2023", "2023-08-31")):  # user
    d = row.find(f">{ph}</w:t>"); s0 = row.rfind("<w:sdt>", 0, d)   # start-date placeholder is split: "S","tart ","date"
    row = row[:s0] + set_sdt(row[s0:], ph, shown).replace(
        '<w:date><w:dateFormat', f'<w:date w:fullDate="{iso}T00:00:00Z"><w:dateFormat', 1)
cells = [m.start() for m in re.finditer(r"<w:tc>", row)]
for col, val in reversed(list(zip([3, 4, 5], [PAST["fte"], PAST["research_fte"], PAST["institution"]]))):
    pe = row.find("</w:p>", cells[col])
    row = row[:pe] + runs_xml(val) + row[pe:]
x = x[:r0] + row + x[r1:]

e = x.find("xtension clause")
x = x[:e] + set_sdt(x[e:], "Yes/No", "No")               # PhD 2020: within the Vidi window

for label, val in (("Initial(s) and surname(s)</w:t>", SIGN_NAME), (">Place: </w:t>", SIGN_PLACE)):
    k = x.find(label); pe = x.find("</w:p>", k)
    x = x[:pe] + runs_xml(val) + x[pe:]

rels = zin.read("word/_rels/document.xml.rels").decode("utf-8")
ctypes = zin.read("[Content_Types].xml").decode("utf-8")
IMG_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image"
for rid, name, _ in IMAGES:
    rels = rels.replace("</Relationships>",
                        f'<Relationship Id="{rid}" Type="{IMG_REL}" Target="{name[5:]}"/></Relationships>')
if IMAGES and 'Extension="png"' not in ctypes:
    ctypes = ctypes.replace("<Default ", '<Default Extension="png" ContentType="image/png"/><Default ', 1)

tmp = DOCX + ".tmp"
with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        data = {"word/document.xml": x.encode("utf-8"),
                "word/_rels/document.xml.rels": rels.encode("utf-8"),
                "[Content_Types].xml": ctypes.encode("utf-8")}.get(item.filename) or zin.read(item.filename)
        zout.writestr(item, data)
    for _, name, data in IMAGES:
        zout.writestr(name, data)
zin.close()
os.replace(tmp, DOCX)
w1, w2 = words(P1), words(P2)
f1, f2 = fig_words(P1), fig_words(P2)
print(f"Done. 2a1: {w1} words, 2a2: {w2} words, total {w1 + w2} / 1200 (red [CHECK] notes excluded).")
if f1 or f2:
    print(f"Including text inside figures ({f1 + f2} words): 2a1: {w1 + f1}, 2a2: {w2 + f2}, "
          f"total {w1 + w2 + f1 + f2} / 1200.")
if KOS:
    print(f"2b: key outputs {sorted(KOS)} filled, motivations {MOTIV_WORDS} / 700 words (red [CHECK] notes excluded).")
print(f"Backup of previous version: {DOCX}.bak")
print(f"3: research idea {IDEA_WORDS} / 150 words.")
