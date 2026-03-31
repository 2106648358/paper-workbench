# Abstract Writing Specification

## Overview
摘要撰写能力，确保论文中英文摘要符合学术写作规范。

## Requirements

### Requirement: Create structured Chinese abstract
The system SHALL create a Chinese abstract that follows academic writing standards with clear structure.

#### Scenario: Abstract structure
- **WHEN** creating Chinese abstract
- **THEN** abstract contains four parts: 目的、方法、结果、结论
- **AND** each part is clearly labeled
- **AND** content is accurate and concise

#### Scenario: Abstract length
- **WHEN** Chinese abstract is created
- **THEN** length is within one page
- **AND** word count is between 300-500 characters

### Requirement: Create corresponding English abstract
The system SHALL create an English abstract that corresponds to the Chinese abstract.

#### Scenario: Content correspondence
- **WHEN** English abstract is created
- **THEN** it covers the same four parts as Chinese abstract
- **AND** key findings and numbers match exactly

#### Scenario: Academic English style
- **WHEN** writing English abstract
- **THEN** use standard academic English expressions
- **AND** avoid direct translation from Chinese
- **AND** grammar and expressions are idiomatic

### Requirement: Follow academic writing style
The system SHALL ensure abstract follows academic writing conventions.

#### Scenario: Objective tone
- **WHEN** writing abstract
- **THEN** use third-person perspective
- **AND** avoid first-person pronouns
- **AND** use passive voice where appropriate

#### Scenario: Precise language
- **WHEN** reporting results
- **THEN** include specific numbers and P-values
- **AND** use precise terminology
- **AND** avoid vague expressions