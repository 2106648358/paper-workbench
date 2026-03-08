---
name: skill-creator
description: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
compatibility: opencode
---

# Skill Creator

A skill for creating new skills and iteratively improving them.

## Core Workflow

1. Understand what the skill should do and how it should work
2. Write a draft of the skill
3. Create test prompts and run opencode-with-access-to-the-skill on them
4. Evaluate results with the user (qualitative and quantitative)
5. Rewrite based on feedback
6. Repeat until satisfied
7. Expand test set and test at larger scale

## Creating a Skill

### Capture Intent

Extract from conversation or ask:

1. What should this skill enable opencode to do?
2. When should this skill trigger? (user phrases/contexts)
3. What's the expected output format?
4. Should we set up test cases? (Skills with objectively verifiable outputs benefit from test cases)

### Write the SKILL.md

Fill in these components:

- **name**: Skill identifier (lowercase, alphanumeric, single hyphens)
- **description**: When to trigger AND what it does (1-1024 chars)
- **compatibility**: Required tools, dependencies (optional)
- **Body**: Instructions, patterns, examples

### Skill Anatomy

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/    - Executable code for deterministic/repetitive tasks
    ├── references/ - Docs loaded into context as needed
    └── assets/     - Files used in output (templates, icons, fonts)
```

### Progressive Disclosure

1. **Metadata** (name + description) - Always in context
2. **SKILL.md body** - In context when skill triggers (<500 lines ideal)
3. **Bundled resources** - As needed

**Key patterns:**
- Keep SKILL.md under 500 lines; add hierarchy if approaching limit
- Reference files clearly with guidance on when to read them
- For large reference files (>300 lines), include a table of contents

### Writing Patterns

**Defining output formats:**
```markdown
## Report structure
ALWAYS use this exact template:
# [Title]
## Executive summary
## Key findings
## Recommendations
```

**Examples pattern:**
```markdown
## Commit message format
**Example 1:**
Input: Added user authentication with JWT tokens
Output: feat(auth): implement JWT-based authentication
```

### Test Cases

After writing the skill draft, create 2-3 realistic test prompts. Save to `evals/evals.json`:

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's task prompt",
      "expected_output": "Description of expected result",
      "files": []
    }
  ]
}
```

See `references/schemas.md` for the full schema.

## Running and Evaluating Test Cases

### Workspace Organization

Results go in `<skill-name>-workspace/` as sibling to skill directory:
```
<workspace>/
├── iteration-1/
│   ├── eval-0/
│   │   ├── with_skill/
│   │   └── eval_metadata.json
│   └── benchmark.json
└── iteration-2/
```

### Step 1: Run Test Cases

Use opencode's Task tool to run test cases. For each test case:

**With-skill run:**
```
Execute this task:
- Skill path: <path-to-skill>
- Task: <eval prompt>
- Input files: <eval files if any>
- Save outputs to: <workspace>/iteration-<N>/eval-<ID>/with_skill/outputs/
```

**Baseline run** (for new skills):
- Same prompt, no skill path
- Save to `without_skill/outputs/`

Write `eval_metadata.json` for each test case:
```json
{
  "eval_id": 0,
  "eval_name": "descriptive-name-here",
  "prompt": "The user's task prompt",
  "assertions": []
}
```

### Step 2: Draft Assertions

While runs are in progress, draft quantitative assertions:
- Objectively verifiable
- Descriptive names
- Explained to user before committing

Update `eval_metadata.json` and `evals/evals.json` with assertions.

### Step 3: Grade and Aggregate

**Grade each run:**
- Use `agents/grader.md` for evaluation
- Save to `grading.json` with fields: `text`, `passed`, `evidence`

**Aggregate into benchmark:**
```bash
python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
```

### Step 4: Launch Viewer

```bash
python <skill-creator-path>/eval-viewer/generate_review.py \
  <workspace>/iteration-N \
  --skill-name "my-skill" \
  --benchmark <workspace>/iteration-N/benchmark.json \
  --static <workspace>/iteration-N/review.html
```

For iteration 2+, add `--previous-workspace <workspace>/iteration-<N-1>`.

Tell user: "I've generated a review page at `<path>`. Open it in your browser to see outputs and leave feedback."

### Step 5: Read Feedback

User clicks "Submit All Reviews" which saves `feedback.json`:

```json
{
  "reviews": [
    {"run_id": "eval-0-with_skill", "feedback": "the chart is missing axis labels", "timestamp": "..."},
    {"run_id": "eval-1-with_skill", "feedback": "", "timestamp": "..."}
  ],
  "status": "complete"
}
```

Empty feedback = user thought it was fine. Focus on specific complaints.

## Improving the Skill

### Improvement Principles

1. **Generalize from feedback** - Don't overfit to specific examples
2. **Keep instructions lean** - Remove what isn't pulling its weight
3. **Explain the why** - Help model understand reasoning
4. **Bundle repeated work** - If all test cases write similar scripts, bundle them in `scripts/`

### Iteration Loop

1. Apply improvements to skill
2. Rerun all test cases into `iteration-<N+1>/`
3. Launch viewer with `--previous-workspace`
4. Wait for user review
5. Read feedback, improve again, repeat

## Description Optimization

After creating/improving a skill, offer to optimize the description for better triggering.

### Step 1: Generate Eval Queries

Create 20 queries (mix of should-trigger and should-not-trigger):

```json
[
  {"query": "prompt text", "should_trigger": true},
  {"query": "another prompt", "should_trigger": false}
]
```

Use `assets/eval_review.html` template for user review.

### Step 2: Run Optimization Loop

```bash
python -m scripts.run_loop \
  --eval-set <path-to-trigger-eval.json> \
  --skill-path <path-to-skill> \
  --model <model-id> \
  --max-iterations 5 \
  --verbose
```

### Step 3: Apply Result

Take `best_description` from output and update SKILL.md frontmatter.

## Packaging

```bash
python -m scripts.package_skill <path/to/skill-folder>
```

Direct user to the resulting `.skill` file path for installation.

## Opencode-Specific Notes

### Subagent Usage

Use opencode's Task tool for parallel work:
- `@general` - General-purpose subagent for complex tasks
- `@explore` - Fast read-only exploration

### Tool Invocation

When the skill says "spawn a subagent", use:
```
Execute this task:
- Task: <description>
- Context: <relevant info>
```

### File Operations

All file paths should be absolute or relative to project root. On Windows, use proper path separators.

## Reference Files

- `agents/grader.md` - How to evaluate assertions
- `agents/comparator.md` - Blind A/B comparison
- `agents/analyzer.md` - Analyze benchmark results
- `references/schemas.md` - JSON schemas for evals, grading, etc.

---

## Quick Start

New user says "I want to make a skill for X":

1. Ask clarifying questions about intent, triggers, output format
2. Write draft SKILL.md
3. Create 2-3 test prompts
4. Run test cases with and without skill
5. Launch eval viewer for user review
6. Iterate based on feedback
7. Package and deliver
