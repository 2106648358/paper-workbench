# Three Line Table Format Specification

## Overview
三线表格式规范化能力，确保论文中的表格符合国家标准 GB/T 7713-1987 的三线表规范。

## Requirements

### Requirement: Set three-line table line widths
The system SHALL configure booktabs package to use standard line widths for three-line tables.

#### Scenario: Configure standard line widths
- **WHEN** document preamble is loaded
- **THEN** `\heavyrulewidth` is set to 1.5pt (top and bottom rules)
- **AND** `\lightrulewidth` is set to 0.75pt (mid rule)
- **AND** `\cmidrulewidth` is set to 0.4pt (for grouped tables)

### Requirement: Use only three horizontal lines
The system SHALL ensure each table contains only three horizontal lines: top rule, mid rule, and bottom rule.

#### Scenario: Standard three-line table
- **WHEN** a table is created
- **THEN** it has exactly one `\toprule` at the top
- **AND** exactly one `\midrule` below the header row
- **AND** exactly one `\bottomrule` at the bottom
- **AND** no additional `\midrule` between data rows

#### Scenario: Remove extra midrules
- **WHEN** a table contains multiple `\midrule` commands
- **THEN** only the one below the header row is kept
- **AND** other `\midrule` commands are removed

### Requirement: Handle wide tables
The system SHALL handle tables that are too wide for the page width by splitting into multiple rows.

#### Scenario: Split wide table into multiple rows
- **WHEN** a table has too many columns to fit page width
- **THEN** the table is split into multiple row groups
- **AND** each row group shows a subset of columns
- **AND** row groups are separated by a double-thin line (0.75pt)

#### Scenario: Use double-thin line for row separation
- **WHEN** wide table is split into multiple rows
- **THEN** `\midrule[0.75pt]` or custom `\doubleline` command is used between row groups

### Requirement: Handle long tables
The system SHALL handle tables with too many rows by displaying side by side.

#### Scenario: Display long table side by side
- **WHEN** a table has too many rows for page height
- **THEN** the table is split into two parts displayed side by side
- **AND** left and right parts are separated by double vertical line (0.75pt)

### Requirement: Add text description when data incomplete
The system SHALL add text description when three-line table format cannot fully display all data.

#### Scenario: Add supplementary text
- **WHEN** table format modification hides important grouping information
- **THEN** text description is added before or after the table
- **AND** the text explains the data structure clearly

### Requirement: Maintain logical flow
The system SHALL ensure table modifications do not break the logical flow of the text.

#### Scenario: Check surrounding text
- **WHEN** a table is modified
- **THEN** surrounding text paragraphs are reviewed for consistency
- **AND** references to table rows/columns remain accurate
- **AND** transitions between text and table remain smooth

### Requirement: Point-to-point modification
The system SHALL modify each table individually based on its specific characteristics.

#### Scenario: Analyze each table
- **WHEN** starting table optimization
- **THEN** each table is analyzed for its specific issues
- **AND** appropriate modification strategy is determined for each table
- **AND** modifications are applied table by table

#### Scenario: Verify each modification
- **WHEN** a table is modified
- **THEN** the modified table is checked for completeness
- **AND** data is not lost or corrupted
- **AND** table format is correct