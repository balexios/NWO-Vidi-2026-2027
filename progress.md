# NWO Vidi 2026 pre-proposal – progress log

Handover file. A new session should read this file first, then `drafts/2a_academic_profile_draft.md`.
Last updated: 2026-10-07.

## 1. The application
- **Applicant:** A. Voulimeneas, assistant professor at TU Delft. Cybersecurity (CYS) section, Dept. of Intelligent Systems, EEMCS. Tenured since 15 March 2025. PhD UC Irvine, 2020 (advisor M. Franz). Postdoc KU Leuven, 2020–2023 (S. Volckaert).
- **Scheme:** NWO Talent Programme, Vidi 2026. Grant of up to EUR 850k.
- **Deadlines:**
  - Pre-proposal: **3 Nov 2026, 14:00:00 CET**, submitted in ISAAC. Start the submission at least 1 day early.
  - Full proposal: 6 Apr 2027, 14:00 CEST.
- **Domain chosen:** Science (ENW), *Computer and information sciences* panel. This choice is final once submitted. No interviews in ENW.
- **Project:** ACCESS – Advanced Compartmentalization for Secure Software. The project:
  - uses static and dynamic analysis to infer compartment boundaries and the resources each compartment needs (memory, files, syscalls, sockets);
  - enforces these per-compartment profiles through a platform-agnostic isolation abstraction built on commodity hardware and software primitives.
- **Pre-proposal assessment:** only "quality of the researcher" (100%), based on the evidence-based CV in section 2. The research idea (section 3) is used only to check that the CV and the idea fit together.

## 2. Folder layout
| Path | What |
|---|---|
| `nwo-documents/` | Official NWO files: call PDF, pre-proposal form, embedding guarantee form, literature-list template. Keep these untouched. |
| `drafts/Vidi-2026-Pre-proposal-Voulimeneas.docx` | **Working copy of the pre-proposal form.** This is the file being filled in. |
| `drafts/2a_academic_profile_draft.md` | **Source text for section 2a.** It also holds the provisional key-output list, the reference list, and a "parking lot" of old paragraphs. |
| `tools/fill_2a.py` | Rebuilds section 2a in the working docx from the .md file (see section 6). |
| `tools/preproposal_base_before_2a.docx` | Clean base: the working docx with title, 1a and 1b filled in but 2a empty. Used by `fill_2a.py`. |
| `Voulimeneas_Alexios_academic_CV.pdf` | Applicant's full CV (current as of 18 Jul 2026). Source of facts. |
| `other-vinis/Harm_griffioen_pre_proposal.pdf` | Example **Veni** 2024 pre-proposal by a TU Delft CYS colleague. **The user considers this the main model.** |
| `other-vinis/Veni pre-proposal form 2025_revised.pdf` | Second example. **Not yet read.** |

## 3. Key rules from the call and form (to respect while writing)
- **Formatting:**
  - English only.
  - Calibri, black, 9.5 pt, single line spacing, 2.5 cm margins.
  - Delete the explanatory-note boxes before making the PDF.
  - Submit as a PDF without security.
- **Personal details:** initials and surname only, no first names.
- **2a, academic profile:** max **1200 words** in total, covering 2a1 (general academic profile) and 2a2 (leadership and mentorship). Word counts include references, footnotes and text in figures. Figures are allowed in 2a.
- **2b, key outputs:**
  - Max 10 outputs and **700 words** for the motivations.
  - Up to 3 quality indicators per output.
  - One URL per output (a DOI is preferred).
  - Only output that is published or unconditionally accepted. Preprints are allowed only if they are in an open repository and the venue is not named.
- **Section 3, research idea:**
  - Max **150 words**, plain text only, no references.
  - Title underlined, plus up to 5 keywords.
  - Title, keywords and research idea must match ISAAC exactly.
- **Not allowed anywhere:**
  - acceptance rates, h-index, journal impact factors, rankings
  - words like "top-tier", "prestigious", "leading" applied to venues
  - totals of publications, funding or prizes (totals of supervised students ARE allowed)
  - URLs, except in the 2b URL fields
  - mentioning output that is not in the key-output list
- **Mandatory annex:** the Embedding Guarantee, on NWO's template and signed by the dean. Start this early.
- **Optional annexes:**
  - literature list for referees (max 10 papers)
  - up to 3 non-referees, entered in ISAAC
- **Vidi submission limit:** an applicant may submit a Vidi only twice in total.
- **Typo in the call:** section 3.2.1 says "October 1, 2028". The correct date is 2018.

## 4. Status per section of the form
| Section | Status |
|---|---|
| Title | **Done** in docx: "ACCESS - Advanced Compartmentalization for Secure Software". The acronym letters are underlined (A, c in Advan**c**ed, C, e in Compartm**e**ntalization, S, S). Note: the form asks for the *whole* title underlined. We offered bolding the acronym letters instead; the user has not decided. |
| 1a Domain | **Done**: Science (ENW) - Computer and information sciences. |
| 1b Fields | **Done**: main 1.02.08 Security & privacy; second 1.02.05 Computer systems, architectures, networks; third 1.02.09 Software engineering, programming languages, formal methods. Fourth is still the placeholder; delete it in the final version. In ISAAC, enter the names only, without the codes. |
| 2a1 | **In progress.** Only the "Research vision" paragraph (135 words) is agreed and in the docx. |
| 2a2 | Not started in the docx. Leadership inventory done (see section 5). |
| 2b Key outputs | Provisional list of 10 in the .md file. Not discussed or agreed yet. |
| 3 Research idea | Two candidate versions exist (see section 5). Neither is chosen or in the docx yet. Keywords not chosen. |
| 4 Admin | Not started. |
| Embedding guarantee | Not started. Needs the TU Delft dean's signature. |
| Literature list | Not started (optional). |

## 5. Decisions, content and user preferences so far
**User preferences (important):**
- Do not spend long on compliance checking. The user wants to work on content and framing.
- Work **section by section, one paragraph at a time.** Write a paragraph, let the user react, then put it in the Word file.
- Put unknowns or facts to verify as **red `[CHECK ...]` placeholders** in the text. The user will fix them later.
- Make the narrative **Netherlands-specific**, using Dutch cases of bugs and attacks.
- **No citation markers in the form text.** Decided 2026-10-07: the form cites only key outputs (KO1…KO10). External sources (e.g. the Dutch cases) are kept in the "Sources" section of the .md, for fact-checking only. A separate reference file cannot be submitted, because NWO allows no extra annexes.
- The user did not like the first full draft of 2a. It was too generic, and some 2a1 parts read as leadership (group size, "what a Vidi will enable"). **Keep 2a1 about the research path (PhD → postdoc → TU Delft) and move team and leadership content into 2a2.**

**Agreed 2a1 opening (in the docx):**
- Three Dutch cases (no citation markers in the text):
  - COATHANGER: Ministry of Defence network breached via a FortiGate memory-safety bug
  - Citrix 2020: NCSC-NL urged organisations to switch off their Citrix servers
  - CrowdStrike 2024: a faulty update made KLM largely suspend flights at Schiphol
- Personal story, added at the user's request in the style of Griffioen: the user didn't plan to stay in academia during the PhD, did internships at Oracle Labs (2017) and Apple (2019), then chose academia (KU Leuven, then TU Delft). The user accepted the reason text and removed the red note. "I did not plan to stay in academia: I wanted to protect real systems" is in bold. Paragraph is 217 words.
- If the user edits the docx directly, read the docx text with textutil and sync the .md before rerunning fill_2a.py.
- Belief, in bold: "I believe we must stop assuming that software can be made bug-free, and instead build systems that remain safe when bugs are triggered or exploited."
- Central question, in bold: "how can we build trustworthy systems from untrustworthy software?"

**Second 2a1 paragraph (drafted 2026-10-07, from the user's outline):** "Detecting and surviving attacks at run time".
- The unifying method is dynamic analysis: tracing execution at run time. This covers MVX, sandboxing and fuzzing.
- Content: comprehensive defences that rule out classes of attacks (KO1); then performance (KO2), compatibility via shared memory (KO3), and availability (KO4, A8: Distinguished Paper Award plus Dutch media coverage).
- **KOs are now numbered in order of first citation.** See the table in the .md.
- Confirmed: KO1 = dMon (DIMVA 2020, Distributed Heterogeneous NVX); KO2 = dMVX (EuroSec 2021). ATC 2016 is back among the unnumbered candidates.
- Target for 2a1 is now ~700 words, which leaves ~450–500 words for 2a2.
- The user removed this paragraph's heading and changed "the most effective" to "an effective" approach.

**Third 2a1 paragraph (in the docx):** dynamic analysis across the whole software and hardware stack.
- Component isolation: KO5, PKU sandbox (bold sentence).
- GPU driver bug finding: KO6, Moneta ("found previously unknown, security-critical vulnerabilities" in bold). The red note was removed at the user's request; numbers of bugs/CVEs could be added later.
- Fundamental tools: KO7, lazypoline (DSN 2024); KO8, K23 (Middleware 2025).
- 2a1 is at 435 words. Intel Labs invited talk added after KO5.

**Fourth 2a1 paragraph (in the docx): open science and recognition.**
- Bold "I believe in open science": we open-source our systems. No specific KO references, at the user's request.
- Programme committees: IEEE S&P, USENIX Security, ACM CCS, EuroSys.
- Reviewer awards at CCS, ASIA CCS and EuroSys.
- ORCA was removed at the user's request. It could still go in 2a2 if the user wants.

**Fifth 2a1 paragraph (in the docx): teaching.**
- "I also enjoy teaching", in the style of Griffioen.
- Developed and teaches Systems Security and Computer Security at TU Delft.
- Optional red [CHECK]: student numbers or evaluations.
- 2a1 is at 554 words.

**Sixth and final 2a1 paragraph (in the docx): "Future vision."**
- Modelled on a Veni "Future Vision" example the user pasted.
- Content: why compartmentalization is not deployed (hardware dependence; manual boundaries); ACCESS builds on dynamic analysis (KO1–KO3, KO6–KO8) and isolation (KO4 A8, KO5 PKU sandbox, KO9 ReMon). This grouping was chosen by the user.
- KO9 = ReMon (USENIX ATC 2016). Only KO10 is still free.
- Later, at the user's request, the KO references were removed from the Future vision paragraph. KO9 is no longer cited in 2a, but stays as a key output in 2b.
- Bold closing sentence: the Vidi lets the user expand the group and establish a distinctive research programme under their leadership.
- **The 2a1 target was raised to 750–800 words.** 2a1 is now at 762 words, so 2a2 has about 440 words.
- Teaching paragraph expanded: lab assistant at AUEB, TA at UC Irvine, the TU Delft courses (red note removed at the user's request), and advising students in Athens on graduate studies.
- Future vision now opens with: "Over the past decade, the research community, including my own work, has greatly advanced the techniques for building trustworthy systems." Then, in bold: "Yet security, performance and usability limitations of existing techniques still hold back their adoption in practice." Compartmentalization is the prime example.
- The KO5 sentence now says the isolation is built "using commodity hardware primitives".
- Recognition paragraph: invited talks added (IMDEA Software, INESC-ID/University of Lisbon, and Télécom SudParis at IP Paris; the user first said "Inria" but meant this talk).
- **Decision:** the user's leadership in reproducibility (ACM REP General Chair, SOSP artifact-evaluation chair, etc.) goes in **2a2, not 2a1**.

**Planned structure for the rest of 2a1** (proposed; the user has not confirmed yet). Each career stage answers part of the central question:
1. **PhD (UC Irvine):** *detect* compromise, through multi-variant execution (MVX). KO8 (ATC 2016), KO7 (DIMVA 2020, first author). Insight: the application–OS boundary is where policy is best enforced.
2. **Postdoc (KU Leuven):** *contain* compromise, through in-process isolation. KO1 (EuroSys 2022, PKU sandbox, first author). KO2 (DSN 2024, syscall interposition).
3. **TU Delft:** *control what compromised code can do*, through syscall mediation. KO3 (Middleware 2025, K23, own PhD student first author). KO4 (ACSAC 2024 Distinguished Paper). Space/ESA as the societal domain (KO10).
4. **ACCESS:** confine each component automatically.
5. Then: recognition and citizenship (programme committees, reviewer awards), ORCA steering committee, open science and reproducibility (ACM REP General Chair, SOSP artifact-evaluation chair).

The old paragraphs in the .md "parking lot" can be mined for this.

**Lessons from the Griffioen example (the user's main model):**
- Open with a societal hook and the personal story.
- Put the key insight sentences in **bold**.
- Give concrete numbers (attacks, % improvement).
- Name stakeholders (ministries, companies).
- Use a figure in 2a.
- Reference key outputs inline.
- **Do not copy** its ranking language ("largest academic security conference"), which is not allowed.
- It is a Veni, so it has no 2a2. Vidi needs a real leadership story.

**Leadership inventory for 2a2** (from the CV, discussed with the user):
- **Strong:**
  - 2 PhD students at TU Delft (main supervisor)
  - co-hosted MSCA postdoc (with G. Smaragdakis)
  - 11 completed MSc theses (KU Leuven, TU Braunschweig, TU Delft) plus 1 ongoing
  - **Outcomes:** a KU Leuven MSc student later became first author of the DSN 2024 paper; a 2025 MSc student continued as the user's PhD student; the first PhD student is first author of K23
  - senior/last author on Middleware 2025, ACSAC 2024, DSN 2024 and 3S 2024
  - started a new space-security line (ESA visit, CubeSat/space MSc theses)
- **Organisational:**
  - General Chair, ACM REP 2026
  - Artifact Evaluation Chair, SOSP 2026
  - ORCA Technical Steering Committee
  - Treasurer, CCS 2026
  - Proceedings Chair, EuroSys and HotOS
- **Weaker or belongs elsewhere:** course development (only relevant to 2a2 as recruitment); ONR HONEY-MON (contributed, not PI); programme committees, awards and talks (these go in 2a1).
- **Missing; only the user can supply:** their leadership and mentoring *vision and practice* (supervision style, career support, group culture).

**Research idea (section 3), candidate versions:**
- (a) A shortened technical version, 140 words.
- (b) A version opening with the bigger context, 142 words: "Modern society runs on software assembled from millions of lines of code…" ending with "…making least privilege practical for everyday software."
- These were given in chat and are not saved anywhere. If needed, regenerate them from the abstract in the user's original text, staying under 150 words.
- Possible extra framing for the full proposal: the EU Cyber Resilience Act and "secure by design".
- Suggested keywords: software compartmentalization, isolation, least privilege, program analysis, systems security.

**Provisional key outputs:** see the table in `drafts/2a_academic_profile_draft.md`. Open question: replace KO9 (NDSS 2025, 5th author) with the CCS 2022 fitness-tracking privacy paper (runner-up for the CNIL-Inria award)?

## 6. How to update the Word file
- **First run `python3 -I tools/check_2a_sync.py`.** It compares the 2a text in Word against the .md and lists any edits the user made in Word. Port those into the .md, then run fill_2a.py.
- Edit the 2a1 and 2a2 sections in `drafts/2a_academic_profile_draft.md`, then run:
  `python3 -I tools/fill_2a.py`
- What the script does:
  - Starts from `tools/preproposal_base_before_2a.docx` and inserts the 2a1 and 2a2 paragraphs from the .md file into `drafts/Vidi-2026-Pre-proposal-Voulimeneas.docx`, keeping a `.bak` of the previous version.
  - Turns `**bold**` into bold and `[CHECK ...]` into red text. Everything else is Calibri 9.5 pt, black.
  - Ignores "(to be written)" placeholders and anything after the next `## ` heading (References, Parking lot).
  - Prints word counts.
- **Caveat:** the script rebuilds 2a from the base, so any manual edits the user makes to 2a in Word are lost. Ask first, and port those edits into the .md.
- **Caveat:** if the title or section 1/3/4 fields are later changed in the docx, regenerate the base first (a copy of the docx with 2a empty), or extend the script.
- **Word must be closed.** The script refuses to run if the lock file `drafts/~$di-2026-Pre-proposal-Voulimeneas.docx` exists. The user often has the file open; ask them to close it (Cmd+W).
- No LibreOffice is installed, so the docx cannot be rendered to check the layout. Use `textutil -convert txt -stdout <docx>` to check the text.
- The docx dropdowns (domain, research fields, output types, quality indicators) are content controls. Set them by replacing the `<w:t>` text with one of the listed `w:displayText` values.

## 7. Next steps
1. Write the PhD paragraph of 2a1, following the plan in section 5. Show it to the user, then put it into the docx.
2. Continue with the postdoc and TU Delft paragraphs, then recognition and open science.
3. Get concrete numbers and impact facts from the user (red placeholders), e.g. PKU-sandbox overhead, K23 adoption or affected tools, open-source artifacts.
4. Draft 2a2 from the leadership inventory, with the user's own leadership vision.
5. Decide the 10 key outputs and write the 2b motivations (700 words).
6. Choose and insert the research idea, title formatting and keywords.
7. Fill in section 4 (PhD date, host group, appointments with FTE), the embedding guarantee and the literature list.
8. Read `other-vinis/Veni pre-proposal form 2025_revised.pdf`.

## 8. Change log (latest at the bottom)
- 2026-10-07: "Compartmentalization" is now introduced early, in the KO5 sentence: "compartmentalization techniques that isolate specific application components using commodity hardware primitives… (KO5, KO6)".
  - KO6 = Divide and Conquer: Partial MVX (Euro S&P 2025).
  - **KOs renumbered:** KO7 Moneta, KO8 lazypoline, KO9 K23, KO10 ReMon (not cited in 2a). All 10 slots are now used. The current table in the .md is authoritative; older KO numbers mentioned earlier in this file are outdated.
  - The Intel sentence now reads "Our sandbox design (KO5) led to an invited talk at Intel Labs…".
  - 2a1 is at 801 words.
- 2026-10-07: Added a figure of the user's general research approach: `figures/dynamic_analysis_overview.png`, copied from the user's PNG in the project root.
  - It shows dynamic analysis feeding attack prevention, attack containment and bug discovery.
  - Placed in 2a1 right after the "To build such systems… effective approach…" paragraph, 12 cm wide, centred.
  - No caption and no in-text reference, at the user's request.
  - In the .md it is the line `![](figures/dynamic_analysis_overview.png){12}`; `tools/fill_2a.py` now supports this syntax.
  - **Text inside the figure counts toward the word limit: about 88 words.** Real 2a1 total is therefore about 890 words, leaving about 310 for 2a2. The script's printed count excludes the figure text.
- 2026-10-07: Caption added below the figure: *Figure 1: My approach to building trustworthy systems*.
  - The .md line is `*…*`, which `fill_2a.py` renders as a centred italic caption.
  - The figure line is now `{12,88}` (width in cm, words inside the figure). The script prints counts both without and with figure text.
  - **Current count: 2a1 is 809 words of text, 897 including the figure. About 303 words are left for 2a2.**
- 2026-10-07: The open-science/recognition and teaching paragraphs were merged into one.
  - Removed: Télécom SudParis talk; early lab-assistant and TA work. Kept: Athens advising sentence.
  - **2a1 is now 756 words of text, 844 including the figure. About 356 words are left for 2a2.**
- 2026-10-07: Future vision now names the security barriers too.
  - Lightweight commodity isolation can often be bypassed (this ties to KO5).
  - Manually defined compartments are laborious and often over-privileged.
  - ACCESS derives "tight" compartments and enforces them "securely".
  - **2a1 is now 775 words of text, 863 including the figure. About 337 words are left for 2a2.**
- 2026-10-07: Space cuts applied.
  - Removed: the Citrix case (the opening now has COATHANGER plus "In the same year…" KLM); the open-source sentence (completely, at the user's request); the Athens advising sentence.
  - Tightened the Future vision opening to: "Techniques for building trustworthy systems have advanced greatly, including through my own work."
  - **2a1 is now 702 words of text, 790 including the figure. About 410 words are left for 2a2.**
- 2026-10-07: Removed the "Research vision." heading from the first 2a1 paragraph. The "Future vision." heading is still there.
- 2026-10-07: Removed the "Future vision." heading as well. 2a1 has no paragraph headings now.
- 2026-10-07: Programme committees now described as "systems and security conferences of all sizes, from IEEE S&P, USENIX Security, ACM CCS and EuroSys to specialised venues such as RAID and EuroSec".
- 2026-10-07: The user edited the caption in Word to *Figure 1: My research approach*. Synced to the .md. (Before rerunning fill_2a.py, always diff the docx 2a text against the .md to catch edits made in Word.)
- 2026-10-08: **2a2 first draft written from the user's outline** (230 words). Three paragraphs:
  1. Collaborative and reproducible research: ACM REP 2026 General Chair, SOSP 2026 artifact-evaluation chair, ORCA steering committee; "we release all our systems as open source".
  2. Mentoring approach: 2 PhD students and a co-hosted MSCA postdoc (with G. Smaragdakis). Gives mentees access to the user's network and encourages their own collaborations. Weekly meetings, individual and group. Motto (bold): "My goal is not to find PhD students or postdocs, but to train independent scientists with whom I build long-standing collaborations."
  3. Evidence: more than ten MSc theses (TU Delft, KU Leuven, TU Braunschweig). A KU Leuven MSc student became first author of KO8; a TU Delft MSc student continued as PhD student; the first PhD student is first author of KO9.
  - **Totals: 941 words of text, 1029 including the figure. About 171 words are left.**
  - Possible additions: plans for the Vidi team (developing the postdoc toward independence), group culture and inclusiveness.
- 2026-10-08: 2a2 extended with two paragraphs.
  - (1) **Vidi team plans:** red [CHECK] for team composition. PhD students on complementary parts (analysis vs isolation), working in pairs. The postdoc is prepared for independence (co-supervision, leading parts, own grant proposals).
  - (2) **Group culture:** bold "open and inclusive place where everyone feels safe to share ideas and mistakes". Honest feedback; mentees present their own work and are first authors on papers they drive; stays at collaborators' labs and in industry.
  - **Totals: 2a2 is 365 words. 2a is 1076 words of text, 1164 including the figure, out of 1200.** Filling the red CHECK adds about 6 words, giving about 1170.
  - **2a is complete in a first full draft.** Next: 2b key-output motivations (700 words), then section 3 and section 4.
- 2026-10-08: Vidi team = one PhD student and one postdoc (confirmed by the user; red note removed). "Working in pairs" became "They will work closely together, so that each learns from the other's expertise." No red notes remain in 2a.
- 2026-10-08: ORCA sentence in 2a2 expanded: "…under the Linux Foundation that aims to bring compartmentalization from research into widely used software, the very goal of ACCESS." **Totals: 1096 words of text, 1184 including the figure, out of 1200.**
- 2026-10-08: First 2a2 paragraph restructured. Reproducibility efforts are now listed: ACM REP 2026 General Chair, SOSP 2026 artifact-evaluation chair, AE committees of OSDI/PLDI/EuroSys/USENIX Security. Then the open-source sentence, then ORCA in its own sentence. **Totals: 1111 words of text, 1199 including the figure, out of 1200 — at the limit; any additions now need cuts.**
- 2026-10-08 (applied to docx; 2a total 1112 words text, 1200 incl. figure): The MSc paragraph in 2a2 now gives career outcomes instead of publication outcomes. A KU Leuven MSc student became a PhD student there; a TU Delft MSc student became the user's PhD student; the co-hosted MSCA postdoc obtained a faculty position at TU Delft. KO8 and KO9 are no longer cited in 2a2 (still cited in 2a1).
- 2026-10-08: Compliance check of 2a against the form's allowed/not-allowed table and call section 4.3.4 (DORA). No violations found (no rank terms, no publication/grant totals, no URLs, no non-KO outputs, figure text OK). Soft points to substantiate: 'billions of phones and computers' (KO7) could name the driver vendors; reviewer awards are listed per venue (allowed, not a total).
- 2026-10-08: The 2a word-count field in the docx is now filled automatically by tools/fill_2a.py with text + figure words (form p.1: 'Word counts include all text ... text in tables and figures'). Current value: 1200.
- 2026-10-08: 2b culture box filled (41/50 words): conference papers are the main output; author order (first = lead, last = supervising senior). Deliberately no venue names or 'Big Four/Five' (rank/reputation terms not allowed). Text lives in drafts/2b_key_outputs_draft.md; tools/fill_2a.py now also fills this box.
- 2026-10-08: Culture box extended to 49/50 words (adds 'open-source software and industry collaborations are also recognised outputs'). User wants ORCA as a key output, following Lilika's Veni (other-vinis/Veni pre-proposal form 2025_revised.pdf = Lilika's; KO8 F+Cube mentoring, KO9 PC membership). Draft ORCA KO10 in drafts/2b_key_outputs_draft.md; proposed to drop ReMon (old KO10). Pending user confirmation + [CHECK] facts. If adopted, add '(KO10)' after ORCA in 2a2 and cut one word to stay at 1200.
- 2026-10-08: ORCA-as-KO is ON HOLD (user: not yet); ReMon stays KO10 for now. Culture box rewritten (50/50 words, in docx): conference papers on large team-built prototypes; author order (first = lead, usually PhD student; last = supervisor); CVEs as public evidence of real-world impact. Artifact-badge point dropped by user. KO7 (Moneta) motivation should cite CVE numbers to match the box.
- 2026-10-09: 2a2 now mentions the UC Irvine mentee (A. Rösti, co-supervised with M. Franz from MSc to PhD graduation; first author of KO4/A8). To fit, trimmed: 'very' goal; 'involved in several efforts for' -> 'contribute to'; network sentence shortened; 'so that each learns' -> 'and learn from each other's'; dropped 'they'. 2a now 1108 text / 1196 incl. figure.
- 2026-10-09: 2b KO1–KO9 drafted in drafts/2b_key_outputs_draft.md (references + DOIs from Crossref, type, indicators, motivations ~60 words each) and filled into the docx by tools/fill_2a.py (now also fills KO blocks + 2b word count; motivations 530/700). Many red [CHECK]s: open access status (only KO7/NDSS set to Yes), your role in KO3/KO6/KO7, dMVX key result, Moneta CVE numbers, Dutch media outlet for KO4, lazypoline reuse, 'first system' claim KO1, KO5 published title. KO10 (ReMon) left empty; ORCA alternative is in the parking lot.
- 2026-10-09: ORCA is now KO10 (ReMon dropped; noted in 2b parking lot). KO10 entry in drafts/2b_key_outputs_draft.md (Type: Outreach/public engagement/advocacy, other; OA No; URL [CHECK]). 2a2 now cites '(KO10)' after ORCA (2a = 1197 incl. figure). DOCX NOT YET UPDATED (Word was open) - run check_2a_sync.py (will show the expected KO10 diff) then fill_2a.py.
- 2026-10-09: KO10 URL = https://orca-lf.org/ (homepage lists the 5-member TSC incl. the user, with NYU, MIT Lincoln Lab, U Florida, U Utah/US Ignite). KO10 motivation updated accordingly (in .md; docx pending, Word was open).
- 2026-10-09: Sharing is Caring (old KO3) replaced by IBTpoline (USENIX ATC 2026, accepted; Gaidis, Patmanidis, Shapiro, Portokalidis, Voulimeneas, Kemerlis). KOs renumbered in first-citation order: KO1 dMon, KO2 dMVX, KO3 A8, KO4 PKU sandbox, KO5 Partial MVX, KO6 Moneta, KO7 lazypoline, KO8 K23, KO9 IBTpoline, KO10 ORCA. 2a1 'compatibility ... shared memory (KO3)' clause removed; tools sentence now (KO7–KO9). IBTpoline URL is a TODO for the user. DOCX PENDING (Word open).
- 2026-10-09: KO9 IBTpoline motivation: user proposed the core idea, supervised TU Delft MSc student I. Patmanidis (2nd author); invited by Brown/IMDEA because of syscall-interposition expertise. DOCX PENDING (Word open).
- 2026-10-09: KO1 confirmed by user as the first such system; motivation now says 'the first N-variant execution system...'. Docx updated.
- 2026-10-09: KO2 motivation rewritten: novel OS abstractions cut distributed MVX overhead to single-digit %; results motivated a DARPA proposal co-written with PhD advisor, funded, supported PhD of KO3's first author. Indicators: Originality/novelty + grant directly related. Funder confirmed: ONR (HONEY-MON), not DARPA. DOCX PENDING (Word open).
- 2026-10-09: Docx updated with KO2 (ONR) changes. 2a 1183/1200 incl. figure; 2b motivations 693/700 - remaining [CHECK]s will need cuts elsewhere.
- 2026-10-09: KO3 (A8) motivation: user OK with 'covered by Dutch media' without naming the outlet; [CHECK] removed. Docx updated (2b 692/700).
- 2026-10-09: KO9 IBTpoline: no DOI/pages before deadline -> reference ends 'Accepted, to appear.'; Open Access set to No (must be freely accessible by deadline to mark Yes); URL = public preprint/USENIX page if available, else leave empty. Keep acceptance email as proof (NWO may ask). DOCX PENDING (Word open).
- 2026-10-09: KO5 (Partial MVX) role: user designed the compartmentalization approach and co-supervised the first author. 2b motivations now 699/700 - FULL; any further additions need cuts.
- 2026-10-09: KO7 (lazypoline): user proposed the idea and contributed to the implementation; open-source/reuse sentence and 'Reuse' indicator dropped.
- 2026-10-09: KO6 Moneta facts from paper (~/Downloads/2025-218-paper.pdf): 10 previously unknown bugs (5 NVIDIA, 3 AMD Radeon, 2 ARM Mali), all vendor-confirmed, 5 CVEs. User contributed the system call interposition part. STYLE: always 'system call interposition' (no hyphen) - applied everywhere. Trims to fit 2b (697/700): KO3 'recognising both...' removed; KO4 ORCA description -> '(KO10)'; KO9 'which modern Linux systems increasingly enable' removed; KO10 'which sets its technical direction' removed; KO6 'operating-system kernel' -> 'kernel'. Docx updated.
- 2026-10-09: Removed 'billions of devices/phones and computers' overclaim (user). 2a1 now: '...security-critical vulnerabilities in NVIDIA, AMD and ARM drivers (KO6).' KO6: 'GPU drivers run with kernel privileges but are hard to test.' DOCX PENDING (Word open); 2a ~1179, 2b ~694.
- 2026-10-09: KO10 ORCA motivation rewritten: user is a founding member, elected to the 5-member TSC; TSC organises talks, fosters academia-industry collaborations, works to accelerate adoption. Invited-talk sentence dropped from KO10 (talks still in KO4/KO8). 2b 693/700.
- 2026-10-09: 2a2 ORCA sentence: 'founding member of ORCA (KO10) and was elected to its Technical Steering Committee. This industry–academia initiative...'

## 2026-10-09 — "Dutch media" → "a Dutch online magazine"
- KO3 coverage was in an online magazine; wording changed in 2a1 and KO3 motivation (2a and 2b md + Word).
- Named the outlet: "the Dutch trade magazine Security Management" (securitymanagement.nl, 3 Jun 2025, "Baanbrekend onderzoek versterkt cybersecurity").

## 2026-10-09 — Open access
- KO1–KO5, KO7, KO8 set to Open Access: Yes; second URL (URL2) added pointing to website PDFs (KO2: arXiv), all checked to load and match titles. fill_2a.py supports URL2 (line break in URL cell). 2b count unchanged (697; counts motivations only, URLs excluded).

## 2026-10-09 — Open access
- KO1–KO5, KO7, KO8 set to Open Access: Yes; second link (URL2 in the md) added under the DOI, pointing to the PDFs on the user's website (KO2: arXiv). All links checked to load and match the paper titles.
- fill_2a.py supports URL2 (line break in the URL cell). First version reused variable `i` and corrupted the docx; fixed and validated (XML OK).
- 2b count unchanged at 697: only motivations are counted, so URLs, references, types and indicators are excluded.
- 2a2: "ACM REP 2026" spelled out as "the 2026 ACM Conference on Reproducibility and Replicability" (2a now 1191/1200).
- 2a2 Vidi paragraph: "They will work closely together and with my international collaborators, learning from each other's expertise." (no names, per user).
- 2a2 Vidi sentence: "with my other students and collaborators" (dropped "international").
- KO7 motivation: no longer implies lazypoline was an MSc thesis project; now "guided the first author, a KU Leuven PhD student whom I had previously supervised during their MSc."
- KO8: added invited talk at Ghent University (2b 698/700).
- 4d current appointment added to fill_2a.py: Assistant professor, Position: Permanent, 1.0 FTE, 0.4 FTE research (40/40/20 research/teaching/management, per user), TU Delft. Start date still needed. Applied to Word.
- 4d: TU Delft start date 15-9-2023 (contract "Ingangsdatum", per user).

## 2026-10-09 — Section 3 key words and section 4 filled (fill_2a.py)
- Key words (proposed): Compartmentalization, software security, isolation, dynamic analysis, operating systems.
- 4a Dr. A. Voulimeneas; 4b UC Irvine, Prof. M. Franz, thesis title from eScholarship; PhD award date still open.
- 4c TU Delft, Cybersecurity group, Dept. Intelligent Systems, EEMCS.
- 4d past row: Postdoctoral researcher, KU Leuven; dates and FTEs still [CHECK].
- Extension clause: No. Signature: A. Voulimeneas, Delft; date left for submission day.
- Not touched: research idea (user), fourth research-field placeholder, title formatting (only acronym letters underlined; NWO asks for underlined title; hyphen vs en dash).
- 4b PhD award date: 12-6-2020 (user).
- 4d KU Leuven postdoc: 1-9-2020 to 31-8-2023 (user). FTEs still [CHECK].
- 4d KU Leuven postdoc: 1-9-2020 to 31-8-2023, 1.0 FTE, 1.0 FTE research (user). Section 4d complete.
- Section 3 title: whole title underlined (NWO rule), acronym letters A,c,C,e,S,S bold (user asked for bold).
- Title dash changed to en dash ("ACCESS – Advanced…") to match the contract-office email; use the same in ISAAC.

## 2026-10-09 — Section 3 research idea
- Drafted from user text, cut to 149/150 words: drafts/3_research_idea_draft.md (source of truth); fill_2a.py fills it and the section 3 word count. Must be identical to ISAAC abstract. (First run corrupted the docx through a wrong sdt search start; fixed and validated.)

## 2026-10-09 — Literature list for referees (optional annex)
- 10 items chosen by user (7 external + KO8, KO4, KO5): drafts/literature_list_draft.md -> tools/fill_literature.py -> drafts/Vidi-2026-Literature-list-Voulimeneas.docx (NWO template). Save as PDF and upload in ISAAC.
- OpenBSD paper: Ai, Zhang, Lefeuvre, Seltzer, CCS 2026 (accepted; from first author site). IUBIK co-authored by Kemerlis/Gaidis (KO9 co-authors).
- Lit. list [5]: authors and ACM reference (CCS 2026, The Hague, DOI 10.1145/3830454.3846768) from the camera-ready PDF; preprint link https://owl.eu.com/papers/openbsd-civs-ccs26.pdf added.
- Lit. list: all links checked; removed CCS 2026 DOI for [5] (not yet registered), kept author PDF link.
