# 2b. Key output — draft

Source of truth for section 2b. `tools/fill_2a.py` copies the culture box below into the Word form.

## Culture and standards box (max. 50 words)

In computer security and systems, peer-reviewed conference papers on large prototypes built by teams are the main output. The first author leads the work, usually a PhD student; the last author supervises it. Discovered vulnerabilities, once confirmed by the vendor, receive a CVE identifier: public evidence of real-world security impact.

(Decision 2026-10-08: no venue names or "Big Four/Five" wording, to avoid NWO's ban on rank/reputation terms for conferences.)

## Key outputs

Format per KO (parsed by tools/fill_2a.py): Open Access must be exactly Yes or No to be filled (anything else leaves the dropdown empty); Type and Indicators must match the form's dropdown text exactly; Indicators separated by " ; ". Metadata (authors, pages, DOIs) from Crossref, 2026-10-09. URL2 = optional second link to a free copy (form allows one extra open-access link); KO1–KO5, KO7, KO8 use the PDFs on the user's website (checked 2026-10-09) or arXiv. KO10 is ORCA (user, 2026-10-09); ReMon (USENIX ATC 2016) dropped.

### KO1
- Open Access: Yes
- Reference: **Voulimeneas, Alexios**; Song, Dokyung; Parzefall, Fabian; Na, Yeoul; Larsen, Per; Franz, Michael; Volckaert, Stijn. Distributed Heterogeneous N-Variant Execution. Detection of Intrusions and Malware, and Vulnerability Assessment (DIMVA 2020), Lecture Notes in Computer Science 12223, 217–237, 2020, Springer.
- URL: https://doi.org/10.1007/978-3-030-52683-2_11
- URL2: https://alexios-voulimeneas.github.io/papers/dimva20-paper27-final.pdf
- Type: Conference paper
- Indicators: Originality/novelty
- Motivation: As first author, I designed and built the first N-variant execution system that runs diversified copies of a program on machines with different hardware architectures, so that a single exploit cannot compromise all copies at once. I led the design, implementation, evaluation and writing. This work formed the core of my PhD thesis and the foundation of my later work on performance and availability (KO2, KO3).

### KO2
- Open Access: Yes
- Reference: **Voulimeneas, Alexios**; Song, Dokyung; Larsen, Per; Franz, Michael; Volckaert, Stijn. dMVX: Secure and Efficient Multi-Variant Execution in a Distributed Setting. Proceedings of the 14th European Workshop on Systems Security (EuroSec 2021), 41–47, 2021, ACM.
- URL: https://doi.org/10.1145/3447852.3458714
- URL2: https://arxiv.org/abs/2011.02091
- Type: Conference paper
- Indicators: Originality/novelty ; Academic awards, prizes and/or grants directly related to this output
- Motivation: Building on KO1, I introduced novel operating-system abstractions that reduce the run-time overhead of distributed multi-variant execution to single-digit percentages. As first author, I led the design, implementation and writing. These results motivated a proposal to the US Office of Naval Research that I co-wrote with my PhD advisor; it was funded and supported the PhD of the first author of KO3.

### KO3
- Open Access: Yes
- Reference: Rösti, André; Volckaert, Stijn; Franz, Michael; **Voulimeneas, Alexios**. I'll Be There for You! Perpetual Availability in the A8 MVX System. 2024 Annual Computer Security Applications Conference (ACSAC 2024), 520–533, 2024, IEEE.
- URL: https://doi.org/10.1109/ACSAC63791.2024.00052
- URL2: https://alexios-voulimeneas.github.io/papers/a8acsac2024.pdf
- Type: Conference paper
- Indicators: Academic awards, prizes and/or grants directly related to this output ; Mass media coverage ; Reproducibility
- Motivation: Multi-variant execution stops attacks by terminating the program, which makes it unusable for services that must stay online. A8 keeps protected services running while under attack. As last author, I shaped the project and guided its design and evaluation; the first author is a student I co-supervised at UC Irvine from MSc to PhD graduation. The paper received the Distinguished Paper Award with Artifact and was covered by the Dutch trade magazine Security Management.

### KO4
- Open Access: Yes
- Reference: **Voulimeneas, Alexios**; Vinck, Jonas; Mechelinck, Ruben; Volckaert, Stijn. You Shall Not (by)Pass! Practical, Secure, and Fast PKU-based Sandboxing. Proceedings of the Seventeenth European Conference on Computer Systems (EuroSys 2022), 266–282, 2022, ACM.
- URL: https://doi.org/10.1145/3492321.3519560
- URL2: https://alexios-voulimeneas.github.io/papers/cerberus.pdf
- Type: Conference paper
- Indicators: Academic invitations directly related to this output ; Industry use/interest
- Motivation: Intel's memory protection keys enable fast isolation within a process, but existing sandboxes built on them could be bypassed through the operating system. As first author, I designed and built a sandbox that closes these bypasses while keeping overheads low. The work led to invited talks at Intel Labs, the designers of the hardware feature, and at ORCA (KO10). It directly underpins the isolation layer of ACCESS.

### KO5
- Open Access: Yes
- Reference: Vinck, Jonas; Jacobs, Adriaan; **Voulimeneas, Alexios**; Volckaert, Stijn. Divide and Conquer: Introducing Partial Multi-Variant Execution. 2025 IEEE 10th European Symposium on Security and Privacy (EuroS&P 2025), 1049–1066, 2025, IEEE.
- URL: https://doi.org/10.1109/EuroSP63326.2025.00064
- URL2: https://alexios-voulimeneas.github.io/papers/eurosp2025pmvx.pdf
- Type: Conference paper
- Indicators: Originality/novelty
- Motivation: This paper introduced partial multi-variant execution: only the risky components of an application are replicated and monitored, which combines compartmentalization with multi-variant execution and greatly reduces overhead. I designed its compartmentalization approach and co-supervised the first author. Deciding which components to isolate, and how, is exactly the question ACCESS will answer automatically.

### KO6
- Open Access: Yes
- Reference: Jung, Joonkyo; Jang, Jisoo; Jo, Yongwan; Vinck, Jonas; **Voulimeneas, Alexios**; Volckaert, Stijn; Song, Dokyung. Moneta: Ex-Vivo GPU Driver Fuzzing by Recalling In-Vivo Execution States. Network and Distributed System Security Symposium (NDSS 2025), 2025, Internet Society.
- URL: https://doi.org/10.14722/ndss.2025.230218
- Type: Conference paper
- Indicators: Industry use/interest ; Academic collaboration and/or interdisciplinary engagement
- Motivation: GPU drivers run with kernel privileges but are hard to test. Moneta records driver states on real devices and replays them for fuzzing. It found ten previously unknown bugs in the NVIDIA, AMD and ARM Mali drivers; all were confirmed by the vendors and five were assigned CVEs. In this collaboration between Yonsei University and KU Leuven, I contributed the system call interposition part of the approach.

### KO7
- Open Access: Yes
- Reference: Jacobs, Adriaan; Gülmez, Merve; Andries, Alicia; Volckaert, Stijn; **Voulimeneas, Alexios**. System Call Interposition Without Compromise. 2024 54th Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN 2024), 183–194, 2024, IEEE.
- URL: https://doi.org/10.1109/DSN58291.2024.00030
- URL2: https://alexios-voulimeneas.github.io/papers/2024-lazypoline.pdf
- Type: Conference paper
- Indicators: Originality/novelty
- Motivation: System call interposition lets defences observe and control how programs interact with the operating system, but existing techniques trade off efficiency, completeness and compatibility. Our tool, lazypoline, achieves all three. As last author, I proposed the idea, contributed to the implementation and guided the first author, a KU Leuven PhD student whom I had previously supervised during their MSc.

### KO8
- Open Access: Yes
- Reference: Gómez Moreno, Jesús María; Moutafis, Vissarion; Dionysiou, Antreas; Kuipers, Fernando; Smaragdakis, Georgios; Coppens, Bart; **Voulimeneas, Alexios**. Clair Obscur: The Light and Shadow of System Call Interposition – From Pitfalls to Solutions with K23. Proceedings of the 26th International Middleware Conference (Middleware 2025), 241–255, 2025, ACM.
- URL: https://doi.org/10.1145/3721462.3770772
- URL2: https://alexios-voulimeneas.github.io/papers/K23_camera_ready.pdf
- Type: Conference paper
- Indicators: Academic invitations directly related to this output ; Academic collaboration and/or interdisciplinary engagement
- Motivation: Following KO7, we showed that widely used system call interposition techniques have subtle pitfalls that attackers can exploit, and designed K23, which avoids them without sacrificing performance. The first author is my first PhD student at TU Delft, and I led the project as senior author, together with colleagues at TU Delft and Ghent University. The work led to invited talks at the University of Lisbon and INESC-ID, the University of Athens, Ghent University and ORCA.

### KO9
- Open Access: No
- Reference: Gaidis, Alexander J.; Patmanidis, Ioulios; Shapiro, Isabelle; Portokalidis, Georgios; **Voulimeneas, Alexios**; Kemerlis, Vasileios P. IBTpoline: Flexible, Robust, and Intel IBT-compliant System Call Hooking. USENIX Annual Technical Conference (USENIX ATC 2026), USENIX Association, 2026. Accepted, to appear.
- URL: [CHECK: TODO – public preprint or USENIX page if available by 3 Nov; otherwise leave empty]
- Type: Conference paper
- Indicators: Originality/novelty ; Academic collaboration and/or interdisciplinary engagement
- Motivation: The fastest system call interposition techniques, including KO7 and KO8, break on recent processors that enforce Intel's hardware control-flow protection. IBTpoline is the first such technique compatible with this protection, adding only 1.49% overhead in the worst case, and can lock its hooks so that even an attacker with full memory access cannot bypass them. Brown University and the IMDEA Software Institute invited me to this collaboration because of my expertise in system call interposition; I proposed the core idea and supervised the TU Delft MSc student who is its second author.

### KO10
- Open Access: No
- Reference: Member of the Technical Steering Committee, Open Robust Compartmentalization Alliance (ORCA), Linux Foundation, 2026–present.
- URL: https://orca-lf.org/
- Type: Outreach/public engagement/advocacy, other
- Indicators: Industry use/interest ; Stakeholder involvement ; Academic collaboration and/or interdisciplinary engagement
- Motivation: The Linux Foundation launched ORCA in November 2025 as an open, vendor-neutral home for bringing practical isolation and compartmentalization into everyday software. I am a founding member and was elected to its five-member Technical Steering Committee, alongside researchers from New York University, MIT Lincoln Laboratory, the University of Florida and the University of Utah. Together, we organise talks, foster collaborations between academia and industry, and work to accelerate the adoption of compartmentalization. This role gives ACCESS a direct path from research to adoption.

## Parking lot

- ReMon (USENIX ATC 2016, 3rd author) was the old KO10; dropped for ORCA. URL if ever needed: https://www.usenix.org/conference/atc16/technical-sessions/presentation/volckaert
- Sharing is Caring (EuroSys 2022, 4th author) was KO3 until 2026-10-09; replaced by IBTpoline (new KO9), KOs renumbered. Old entry:

- Open Access: [CHECK]
- Reference: Vinck, Jonas; Abrath, Bert; Coppens, Bart; **Voulimeneas, Alexios**; De Sutter, Bjorn; Volckaert, Stijn. Sharing is Caring: Secure and Efficient Shared Memory Support for MVEEs. Proceedings of the Seventeenth European Conference on Computer Systems (EuroSys 2022), 99–116, 2022, ACM.
- URL: https://doi.org/10.1145/3492321.3519558
- Type: Conference paper
- Indicators: Academic collaboration and/or interdisciplinary engagement
- Motivation: Multi-variant execution could not protect programs whose threads communicate through shared memory, which excludes much real-world software. This paper supports such programs securely and efficiently. In this collaboration between KU Leuven and Ghent University, I contributed to [CHECK: your role, e.g. the security design and evaluation].
