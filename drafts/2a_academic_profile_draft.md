# Section 2a – Academic profile (DRAFT v2)

Limit: 1200 words for 2a1 + 2a2 together. [CHECK] = fact to verify or fill in.

## Proposed key outputs referenced below (section 2b, provisional)

| KO | Output | Role |
|---|---|---|
| KO1 | dMon: Distributed Heterogeneous N-Variant Execution – DIMVA 2020 | 1st author |
| KO2 | dMVX: Secure and Efficient MVX in a Distributed Setting – EuroSec 2021 | 1st author |
| KO3 | Perpetual Availability in the A8 MVX – ACSAC 2024 (Distinguished Paper w/ Artifact; Security Management (NL trade magazine, 3 Jun 2025, securitymanagement.nl/baanbrekend-onderzoek-versterkt-cybersecurity/) coverage) | last author |
| KO4 | You Shall Not (by)Pass! PKU-based sandboxing – EuroSys 2022 | 1st author |
| KO5 | Divide and Conquer: Introducing Partial Multi-Variant Execution – Euro S&P 2025 | 3rd author |
| KO6 | Moneta: Ex-Vivo GPU Driver Fuzzing – NDSS 2025 | 5th author |
| KO7 | lazypoline: System Call Interposition Without Compromise – DSN 2024 | last author |
| KO8 | Clair Obscur / K23 – Middleware 2025 | last author (own PhD student 1st) |
| KO9 | IBTpoline: IBT-compliant System Call Hooking – USENIX ATC 2026 (accepted) | 5th author; proposed idea, supervised TU Delft MSc student (2nd author); invited by Brown/IMDEA for syscall-interposition expertise |
| KO10 | ORCA (Open Robust Compartmentalization Alliance, Linux Foundation) – Technical Steering Committee member, 2026– (replaced ReMon, USENIX ATC 2016, on 2026-10-09) | TSC member |

All 10 slots are now used. Dropped candidates: Sharing is Caring – EuroSys 2022 (4th; replaced by IBTpoline on 2026-10-09); Probabilistic Memory Safety – IEEE S&P magazine 2024 (2nd); Orbital Shield – IEEE 3S 2024 (last); CCS 2022 fitness-tracking privacy (CNIL-Inria runner-up);  open-source software (e.g. K23).

KO numbering rule: KOs are numbered in the order they are first cited in 2a.

---

## 2a1. General academic profile

In 2024, Dutch intelligence services revealed that state-sponsored attackers had entered a Ministry of Defence network by exploiting a single memory-safety bug in a commercial firewall. In the same year, a bug in a single security-software update forced KLM to largely suspend flights at Schiphol, without any attacker involved. Bugs are everywhere, and Dutch society depends on the software that contains them. When I started my PhD at UC Irvine, **I did not plan to stay in academia: I wanted to protect real systems**, and I spent time in industry at Oracle Labs (2017) and Apple (2019). These experiences showed me that industry mostly fixes bugs one at a time, under product deadlines, while the deeper problem, that a single bug can compromise an entire system, needs long-term research. This is why I chose an academic career, first at KU Leuven and, since 2023, at TU Delft. **I believe we must stop assuming that software can be made bug-free, and instead build systems that remain safe when bugs are triggered or exploited.** Every step of my research is driven by one central question: **how can we build trustworthy systems from untrustworthy software?**

**To build such systems, I found that an effective approach is to observe and control software while it runs**, tracing its execution with dynamic analysis. I first built comprehensive defences that rule out entire classes of known attacks by running diversified copies of a program side by side and detecting when their behaviour diverges (KO1). These strong security results motivated me to make such defences practical, improving their performance (KO2) and their availability, so that protected services keep running while under attack (KO3). One of our latest works in this area received a Distinguished Paper Award and was covered by the Dutch trade magazine Security Management (KO3).

![](figures/dynamic_analysis_overview.png){12,88}

*Figure 1: My research approach*

This line of research required a deep understanding of the whole software and hardware stack, which led me to design dynamic analysis techniques for different contexts. By monitoring applications at run time in a fine-grained way, **I designed and built compartmentalization techniques that isolate specific application components using commodity hardware primitives, containing the impact of bugs both securely and efficiently** (KO4, KO5). Our sandbox design (KO4) led to an invited talk at Intel Labs, the designers of the hardware feature it builds on. With my collaborators, we applied similar mechanisms to graphics drivers and **found previously unknown, security-critical vulnerabilities** in NVIDIA, AMD and ARM drivers (KO6). In parallel, we designed and built fundamental tools that improve the performance, security and compatibility of dynamic analysis in general (KO7–KO9).

My expertise is recognised by the research community: I regularly serve on the programme committees of systems and security conferences of all sizes, from IEEE S&P, USENIX Security, ACM CCS and EuroSys to specialised venues such as RAID and EuroSec, my reviewing received awards at CCS, ASIA CCS and EuroSys, and I have been invited to present my work at institutes across Europe, including IMDEA Software Institute, INESC-ID and the University of Lisbon. I also enjoy teaching: at TU Delft, I developed and teach Systems Security and Computer Security, which bring the latest research into the classroom and attract motivated students to research.

Techniques for building trustworthy systems have advanced greatly, including through my own work. **Yet security, performance and usability limitations of existing techniques still hold back their adoption in practice.** Compartmentalization is a prime example. By confining each component of an application to only the resources it needs, it could contain the impact of bugs like the ones above, yet it is rarely deployed: lightweight isolation mechanisms on commodity hardware can often be bypassed, strong isolation depends on specialised hardware or intrusive platform changes, and compartments are defined manually, a laborious process that often leaves them with more privileges than they need. My Vidi project, ACCESS, builds directly on my expertise in dynamic analysis and isolation to remove these barriers, automatically deriving tight compartments and enforcing them securely with a portable isolation layer built on commodity hardware. **The Vidi will allow me to expand my group into a team that makes compartmentalization practical for everyday software, establishing a distinctive research programme under my leadership.**

## 2a2. Leadership and mentorship

**I strongly believe in collaborative and reproducible research.** I contribute to open and reproducible science: I am General Chair of the 2026 ACM Conference on Reproducibility and Replicability, chair artifact evaluation at SOSP 2026, and have served on the artifact evaluation committees of OSDI, PLDI, EuroSys and USENIX Security. In my group, we release all our systems as open-source software. I am also a founding member of the Open Robust Compartmentalization Alliance (KO10) and was elected to its Technical Steering Committee. This industry–academia initiative under the Linux Foundation aims to bring compartmentalization from research into widely used software, the goal of ACCESS.

Today, important problems can only be tackled through collaboration, and **I aim to pass this mindset on to my mentees**. I currently supervise two PhD students and co-host a Marie Skłodowska-Curie postdoctoral fellow with G. Smaragdakis. I introduce them to my academic network and encourage them to establish collaborations of their own. I meet my mentees weekly, both individually and as a group, so that each receives personal guidance while learning from the others' work. **My goal is not to find PhD students or postdocs, but to train independent scientists with whom I build long-standing collaborations.**

I have also supervised more than ten MSc theses at TU Delft, KU Leuven and TU Braunschweig. My mentees have progressed in their careers: at UC Irvine, I co-supervised a student from MSc to PhD graduation, including our award-winning work (KO3); my MSc students at KU Leuven and TU Delft continued as PhD students, the latter with me; and the postdoctoral fellow I co-host has obtained a faculty position at TU Delft.

With a Vidi, I will expand my group with a PhD student and a postdoc working on complementary parts of ACCESS: program analysis to derive compartments, and isolation mechanisms to enforce them. They will work closely together and with my other students and collaborators, learning from each other's expertise. I will prepare the postdoc for an independent career by having them co-supervise PhD and MSc students, lead parts of the project and write their own grant proposals.

**I want my group to be an open and inclusive place where everyone feels safe to share ideas and mistakes.** We give each other honest, constructive feedback, my mentees present their own work at conferences, and lead the papers they drive as first authors. I also encourage them to spend time at my collaborators' labs and in industry, as my own internships shaped my career.

## Sources (for our own fact-checking only – NOT in the form; the form only cites key outputs KO1–KO10)

[1] MIVD and AIVD, advisory on the COATHANGER malware in a Dutch Ministry of Defence network (CVE-2022-42475), February 2024.
[2] NCSC-NL, advisory on Citrix ADC/Gateway vulnerability CVE-2019-19781, January 2020.
[3] NL Times, "200 flights canceled at Schiphol after Windows outage" (CrowdStrike update), 19 July 2024.

<!-- Verification links (NOT for the form):
[1] https://www.helpnetsecurity.com/2024/06/12/coathanger-fortigate/ ; https://securityaffairs.com/?p=158765
[2] https://computing.co.uk/news/3085055/dutch-ncsc-citrix-turn-off ; https://www.divd.nl/newsroom/articles/b6f6e14afadc/
[3] https://nltimes.nl/node/74093 ; https://nltimes.nl/2024/07/19/klm-cancellations-likely-weekend-disruption-nearly-resolved
-->

---

## Parking lot – earlier draft text (NOT in the form; reuse/rewrite as needed)

### Old 2a1 paragraphs

**PhD (UC Irvine, 2015–2020): making multi-variant execution practical.** With Prof. Franz, I worked on multi-variant execution (MVX), which runs diversified copies of a program in lockstep and detects attacks when they diverge. MVX offers strong guarantees but was considered too slow and restrictive for practical use. I co-developed a monitoring design that moves most security checks out of the kernel, substantially reducing overhead (KO8). As first author, I showed how variants can run across machines and even across different processor architectures (KO7), freeing MVX from the limits of a single machine. **This work taught me that the boundary between an application and the operating system is where security policy is best enforced**, a principle at the heart of ACCESS.

**Postdoc (KU Leuven, 2020–2023): from detection to isolation.** With Prof. Volckaert, I moved to isolation inside a single process. As first author, I showed that sandboxes built on Intel Memory Protection Keys, a commodity hardware feature, could be bypassed through the operating system, and **designed a sandbox that closes these holes while remaining fast** (KO1) [CHECK: add a concrete number, e.g. overhead or number of bypass classes closed]. This work established my expertise in compartmentalization built on commodity primitives, and led to invited talks at Intel Labs and the Open Robust Compartmentalization Alliance (ORCA). I co-led work on secure system call interposition (KO2), the mechanism ACCESS will use to mediate access to files, sockets and other operating-system resources, and contributed to work on memory safety, MVX and driver fuzzing (KO5, KO6, KO9), broadening my expertise in program analysis.

**Independent research line at TU Delft (2023–present).** Since joining TU Delft (tenured in 2025), I have built my own research line on practical compartmentalization and system call mediation. With my first PhD student, I showed that **widely used system call interposition techniques have subtle, exploitable pitfalls**, and designed K23, which avoids them without sacrificing performance (KO3) [CHECK: concrete impact, e.g. which tools/projects were affected or adopted fixes]. As senior author, I guided work that lets MVX-protected services survive attacks instead of crashing; it **received the ACSAC Distinguished Paper Award with Artifact** and was covered in the Dutch trade press (KO4). I also opened a domain with clear societal relevance: satellites increasingly run commercial off-the-shelf software, and as a visiting researcher at the European Space Agency (2025) I studied how isolation can protect them (KO10) [CHECK: ESA-linked MSc projects?].

**Recognition and academic citizenship.** I am regularly invited to the programme committees of the main security and systems conferences, including IEEE S&P, USENIX Security, ACM CCS and EuroSys. My reviewing received awards at CCS (2023), ASIA CCS (2023) and EuroSys (2022). I hold organisational roles as General Chair of ACM REP 2026, Artifact Evaluation Chair of SOSP 2026, Treasurer of CCS 2026, and Proceedings Chair of EuroSys and HotOS. In 2026 I **joined the Technical Steering Committee of ORCA**, a Linux Foundation alliance of industry and academia on compartmentalization, giving ACCESS a direct route to practitioners. I have given invited talks at universities and research institutes in Portugal, Spain, Belgium and Greece.

**Open science.** Reproducibility is central to how I work. My group releases its systems as open-source artifacts (KO3, KO4) [CHECK], and I help shape reproducibility practice in my field by leading artifact evaluation at SOSP and chairing ACM REP.

**International and industry experience.** Research positions in the USA, Belgium and the Netherlands, internships at Apple and Oracle Labs, and a visiting position at ESA have given me a network spanning academia, industry and agencies. My collaborators include researchers at KU Leuven, UC Irvine, TU Darmstadt and Ghent University.

**What a Vidi will enable.** My group currently has two PhD students and a co-hosted Marie Skłodowska-Curie postdoctoral fellow. ACCESS requires combining program analysis with isolation mechanisms, a scope no single PhD project can cover. **With a Vidi, I will grow my group into a team that tackles this agenda as a whole, making robust compartmentalization practical for everyday software.**

### Old 2a2 paragraphs

**Vision.** I see mentoring as helping each person find, and then own, a research problem. [CHECK: describe your actual practice, e.g.] I meet each student weekly, co-design their first project with them, and gradually hand over ownership, aiming for every PhD student to lead their own first-author papers and develop a visible profile of their own.

**Evidence.** I currently supervise two PhD students and co-host a Marie Skłodowska-Curie postdoctoral fellow, and I have supervised eleven completed MSc theses at three universities. Several of these led to research outcomes. An MSc student I supervised at KU Leuven became first author of KO2. At TU Delft, an MSc student I supervised continued as my PhD student, and my first PhD student is first author of KO3, our group's first major paper. MSc projects in my group range from memory-safe system call interposition to space-system security, letting students explore directions that feed into the group's agenda.

**Team building and collaboration.** I co-host the postdoctoral fellow with G. Smaragdakis, and our students collaborate across our groups within the TU Delft Cybersecurity section. I developed and teach two courses, Systems Security and Computer Security, which also bring motivated MSc students into my research. As General Chair of ACM REP and artifact evaluation chair at SOSP, I lead large volunteer teams of researchers, experience I bring into running a growing group.

**Plans.** [CHECK: inclusive culture, career development of team members, e.g.] With a Vidi, I will structure my group around complementary roles: the postdoc will be mentored toward independence by co-leading part of the project and supervising students, while PhD students will pair analysis and isolation expertise. Regular group meetings, shared infrastructure and joint artifact development will ensure knowledge transfer within the team.
