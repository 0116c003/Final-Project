## ADDED Requirements
### Requirement: IEEE conference manuscript
The project SHALL include an editable IEEEtran conference manuscript and a reproducible compiled draft.

#### Scenario: Compile the manuscript
- **WHEN** main.tex is compiled with pdfLaTeX in an IEEEtran-enabled environment
- **THEN** compilation succeeds and produces a double-column conference paper with resolved references.

### Requirement: Accurate project status
The manuscript SHALL distinguish implemented calculator functionality from planned agent, retrieval, logging, and MCP functionality.

#### Scenario: No measured evaluation results
- **WHEN** no measured meal benchmark or user study is available
- **THEN** the manuscript presents the evaluation protocol without invented numerical results.

### Requirement: Traceable evidence
The manuscript SHALL include source references and explain evidence provenance, units, and uncertainty handling.

#### Scenario: Missing nutrition source
- **WHEN** a proposed retrieval operation cannot find a reliable match
- **THEN** the design specifies transparent unknown output or clarification rather than fabricated nutrient values.

### Requirement: MCP-assisted authoring trace
The submission SHALL document actual MCP-assisted authoring operations, including tool names and outcomes, without credentials.

#### Scenario: Authorized MCP client available
- **WHEN** the author connects an authorized repository MCP server and reads project files
- **THEN** the author records the actual successful calls and reviews the manuscript and specification changes.

#### Scenario: MCP client unavailable
- **WHEN** no MCP connection is available
- **THEN** the author marks MCP execution pending and does not claim it occurred.
