# Skill Creator for Opencode

This is an Opencode-compatible version of the skill-creator tool. It helps you create, test, and improve skills for Opencode.

## Installation

The skill is installed at: `.opencode/skills/skill-creator/`

## Usage

### Creating a New Skill

1. Tell the AI agent: "I want to create a skill for [your task]"
2. The agent will help you:
   - Define what the skill should do
   - Write the SKILL.md file
   - Create test cases
   - Run evaluations
   - Iterate based on results

### Running Test Cases

Test cases are stored in `evals/evals.json`. Run them using:

```bash
python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
```

### Launching the Review Viewer

After running test cases, launch the review viewer:

```bash
python eval-viewer/generate_review.py \
  <workspace>/iteration-N \
  --skill-name "my-skill" \
  --benchmark <workspace>/iteration-N/benchmark.json \
  --static <workspace>/iteration-N/review.html
```

Open the generated `review.html` in your browser to see results and leave feedback.

### Packaging a Skill

When your skill is complete, package it:

```bash
python -m scripts.package_skill <path/to/skill-folder>
```

## Limitations (vs ClaudeCode version)

1. **Description Optimization**: The automated description optimization (`run_loop.py`) uses a simplified keyword-matching approach instead of AI-powered optimization, because Opencode doesn't have an equivalent to `claude -p`.

2. **Subagent Execution**: Test cases are run sequentially instead of in parallel.

3. **Browser Integration**: The viewer generates static HTML files instead of running a local server.

## Directory Structure

```
skill-creator/
├── SKILL.md              # This skill's definition
├── scripts/              # Python scripts
│   ├── run_eval.py       # Run trigger evaluations
│   ├── run_loop.py       # Optimization loop
│   ├── improve_description.py  # Description improvement
│   ├── package_skill.py  # Package skills
│   ├── aggregate_benchmark.py  # Aggregate results
│   └── ...
├── eval-viewer/          # HTML viewer for results
├── agents/               # Subagent instructions
│   ├── grader.md
│   ├── comparator.md
│   └── analyzer.md
├── references/           # Documentation
│   └── schemas.md
└── assets/               # Templates
    └── eval_review.html
```

## Configuration

Add skill permissions to your `opencode.json`:

```json
{
  "permission": {
    "skill": {
      "skill-creator": "allow"
    }
  }
}
```

## Getting Help

Use this skill by asking:
- "Help me create a new skill for X"
- "How do I test my skill?"
- "Run the evaluation viewer"
- "Package my skill"
