# 3. Research idea — draft

Source of truth for section 3 (max. 150 words, plain text, no references except key outputs). `tools/fill_2a.py` copies the paragraph under "## Research idea" into the form and fills the word count. Must be identical to the ISAAC abstract.

Based on the user's text (2026-10-09), shortened to fit 150 words and aligned with the 2a1 framing.

## Research idea

Software bugs are unavoidable, and a single exploited bug can compromise an entire system. Compartmentalization, which confines each component of an application to only the resources it needs, has long promised to contain such compromises, yet is rarely deployed in practice. Two obstacles stand in the way. First, strong isolation typically depends on specialised hardware, kernel modifications or intrusive software changes, limiting portability. Second, deciding where compartment boundaries should lie, and which resources each compartment may access, is a manual, ad hoc process that does not scale to large or evolving codebases. ACCESS tackles both. It uses static and dynamic analysis to automatically derive compartment boundaries and the resources each compartment requires, such as memory, files, system calls and network sockets. It then enforces exactly these permissions through a portable isolation layer built on commodity hardware and software. Together, these advances will make robust compartmentalization practical for everyday software.
