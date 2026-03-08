#!/usr/bin/env python3
"""Improve a skill description based on eval results.

Simplified version for opencode. The full version uses claude -p which
is not available in opencode. This version provides a basic implementation
that can be used as a reference or extended with opencode-specific APIs.
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from utils import parse_skill_md


def improve_description(
    skill_name: str,
    skill_content: str,
    current_description: str,
    eval_results: dict,
    history: list[dict],
    model: str,
    test_results: dict | None = None,
    log_dir: Path | None = None,
    iteration: int | None = None,
) -> str:
    """Generate an improved description based on eval results.
    
    Note: This is a simplified implementation for opencode.
    The original version uses claude -p for AI-powered improvement.
    This version provides basic keyword-based optimization.
    
    For full AI-powered improvement, use opencode directly with the skill.
    """
    failed_triggers = [
        r for r in eval_results["results"]
        if r["should_trigger"] and not r["pass"]
    ]
    false_triggers = [
        r for r in eval_results["results"]
        if not r["should_trigger"] and not r["pass"]
    ]
    
    # Extract keywords from failed triggers
    failed_keywords = set()
    for r in failed_triggers:
        words = r["query"].lower().split()
        failed_keywords.update(w for w in words if len(w) > 3)
    
    # Extract keywords from false triggers
    false_keywords = set()
    for r in false_triggers:
        words = r["query"].lower().split()
        false_keywords.update(w for w in words if len(w) > 3)
    
    # Build improved description
    base_description = current_description
    
    # Add failed trigger keywords if missing
    for keyword in list(failed_keywords)[:5]:
        if keyword not in base_description.lower():
            base_description += f" Use for {keyword.replace('-', ' ')} tasks."
            break
    
    # Trim if over limit
    if len(base_description) > 1000:
        base_description = base_description[:1000]
    
    print(f"Improved description (simplified): {base_description[:100]}...", file=sys.stderr)
    
    return base_description


def main():
    parser = argparse.ArgumentParser(description="Improve a skill description based on eval results")
    parser.add_argument("--eval-results", required=True, help="Path to eval results JSON")
    parser.add_argument("--skill-path", required=True, help="Path to skill directory")
    parser.add_argument("--history", default=None, help="Path to history JSON")
    parser.add_argument("--model", required=True, help="Model for improvement")
    parser.add_argument("--verbose", action="store_true", help="Print progress")
    args = parser.parse_args()

    skill_path = Path(args.skill_path)
    if not (skill_path / "SKILL.md").exists():
        print(f"Error: No SKILL.md found at {skill_path}", file=sys.stderr)
        sys.exit(1)

    eval_results = json.loads(Path(args.eval_results).read_text())
    history = []
    if args.history:
        history = json.loads(Path(args.history).read_text())

    name, _, content = parse_skill_md(skill_path)
    current_description = eval_results["description"]

    if args.verbose:
        print(f"Current: {current_description}", file=sys.stderr)
        print(f"Score: {eval_results['summary']['passed']}/{eval_results['summary']['total']}", file=sys.stderr)

    new_description = improve_description(
        skill_name=name,
        skill_content=content,
        current_description=current_description,
        eval_results=eval_results,
        history=history,
        model=args.model,
    )

    if args.verbose:
        print(f"Improved: {new_description}", file=sys.stderr)

    output = {
        "description": new_description,
        "history": history + [{
            "description": current_description,
            "passed": eval_results["summary"]["passed"],
            "failed": eval_results["summary"]["failed"],
            "total": eval_results["summary"]["total"],
            "results": eval_results["results"],
        }],
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
