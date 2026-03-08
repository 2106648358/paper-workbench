#!/usr/bin/env python3
"""
Zotero Citation Formatter

Generate citations in various formats from Zotero items.

Usage:
    python cite.py <item_key> [--style apa|mla|chicago|ieee]
"""

import json
import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


def format_authors(authors, max_authors=3):
    """Format author list according to style."""
    if not authors:
        return "Unknown Author"
    
    if len(authors) <= max_authors:
        if len(authors) == 1:
            return authors[0].get("firstName", "") + " " + authors[0].get("lastName", "")
        elif len(authors) == 2:
            return (authors[0].get("firstName", "") + " " + authors[0].get("lastName", "") + 
                    " and " + 
                    authors[1].get("firstName", "") + " " + authors[1].get("lastName", ""))
        else:
            parts = [f"{a.get('firstName', '')} {a.get('lastName', '')}" for a in authors]
            return ", ".join(parts[:-1]) + ", and " + parts[-1]
    else:
        # More than max_authors, use et al.
        first = authors[0].get("firstName", "") + " " + authors[0].get("lastName", "")
        return f"{first} et al."


def format_citation(item, style="apa"):
    """Format a citation in the specified style."""
    creators = item.get("data", {}).get("creators", [])
    title = item.get("data", {}).get("title", "Untitled")
    date = item.get("data", {}).get("date", "n.d.")
    publication = item.get("data", {}).get("publicationTitle", "")
    volume = item.get("data", {}).get("volume", "")
    issue = item.get("data", {}).get("issue", "")
    pages = item.get("data", {}).get("pages", "")
    doi = item.get("data", {}).get("DOI", "")
    
    # Extract year from date
    year = date.split("-")[0] if date and len(date) >= 4 else "n.d."
    
    authors = format_authors(creators)
    
    if style == "apa":
        if len(creators) == 1:
            citation = f"{authors} ({year}). {title}."
            if publication:
                citation += f" {publication}"
            if volume:
                citation += f", {volume}"
            if issue:
                citation += f"({issue})"
            if pages:
                citation += f", {pages}"
            if doi:
                citation += f" https://doi.org/{doi}"
        else:
            citation = f"{authors} ({year}). {title}."
            if publication:
                citation += f" {publication}"
            if volume:
                citation += f", {volume}"
            if issue:
                citation += f"({issue})"
            if pages:
                citation += f", {pages}"
            if doi:
                citation += f" https://doi.org/{doi}"
    
    elif style == "mla":
        citation = f"{authors}. \"{title}.\""
        if publication:
            citation += f" {publication}"
        if year and year != "n.d.":
            citation += f", {year}"
        if volume:
            citation += f", vol. {volume}"
        if issue:
            citation += f", no. {issue}"
        if pages:
            citation += f", pp. {pages}"
        citation += "."
        if doi:
            citation += f" https://doi.org/{doi}"
    
    elif style == "chicago":
        citation = f"{authors}. \"{title}.\""
        if publication:
            citation += f" {publication}"
        if year and year != "n.d.":
            citation += f" ({year})"
        if volume:
            citation += f" {volume}"
        if issue:
            citation += f", no. {issue}"
        if pages:
            citation += f": {pages}"
        citation += "."
        if doi:
            citation += f" https://doi.org/{doi}"
    
    elif style == "ieee":
        citation = f"{authors}, \"{title},\""
        if publication:
            citation += f" {publication}"
        if volume:
            citation += f", vol. {volume}"
        if issue:
            citation += f", no. {issue}"
        if pages:
            citation += f", pp. {pages}"
        if year and year != "n.d.":
            citation += f", {year}"
        if doi:
            citation += f", doi: {doi}"
        citation += "."
    
    else:
        # Default format
        citation = f"{authors} ({year}). {title}. {publication}"
    
    return citation


def format_bibtex(item):
    """Generate BibTeX entry for an item."""
    creators = item.get("data", {}).get("creators", [])
    title = item.get("data", {}).get("title", "Untitled")
    date = item.get("data", {}).get("date", "n.d.")
    publication = item.get("data", {}).get("publicationTitle", "")
    volume = item.get("data", {}).get("volume", "")
    issue = item.get("data", {}).get("issue", "")
    pages = item.get("data", {}).get("pages", "")
    doi = item.get("data", {}).get("DOI", "")
    
    # Extract year
    year = date.split("-")[0] if date and len(date) >= 4 else "n.d."
    
    # Generate citation key
    if creators:
        first_author = creators[0].get("lastName", "unknown")
    else:
        first_author = "unknown"
    key = f"{first_author}{year}{title[:4].replace(' ', '')}".lower()
    key = "".join(c for c in key if c.isalnum())
    
    # Format authors for BibTeX
    author_list = []
    for c in creators:
        first = c.get("firstName", "")
        last = c.get("lastName", "")
        if first and last:
            author_list.append(f"{last}, {first}")
        elif last:
            author_list.append(last)
    
    authors_str = " and ".join(author_list) if author_list else "Unknown"
    
    bibtex = f"@article{{{key},\n"
    bibtex += f"  author = {{{authors_str}}},\n"
    bibtex += f"  title = {{{title}}},\n"
    if publication:
        bibtex += f"  journal = {{{publication}}},\n"
    if year and year != "n.d.":
        bibtex += f"  year = {{{year}}},\n"
    if volume:
        bibtex += f"  volume = {{{volume}}},\n"
    if issue:
        bibtex += f"  number = {{{issue}}},\n"
    if pages:
        bibtex += f"  pages = {{{pages}}},\n"
    if doi:
        bibtex += f"  doi = {{{doi}}},\n"
    bibtex += "}"
    
    return bibtex


def main():
    if len(sys.argv) < 2:
        print("Usage: python cite.py <item_key> [--style apa|mla|chicago|ieee|--bibtex]")
        print("Example: python cite.py ABC123 --style apa")
        sys.exit(1)
    
    item_key = sys.argv[1]
    style = "apa"
    
    if "--style" in sys.argv:
        idx = sys.argv.index("--style")
        if idx + 1 < len(sys.argv):
            style = sys.argv[idx + 1]
    
    # Fetch item from Zotero using subprocess to call the MCP tool
    print(f"Fetching item {item_key} from Zotero...", file=sys.stderr)
    
    # For now, use a placeholder - in practice, this would call the Zotero API
    # The actual implementation depends on how Zotero MCP is configured
    item_data = None
    
    if item_data is None:
        print(f"Error: Cannot fetch item {item_key}. Please provide item data as JSON via stdin.", file=sys.stderr)
        try:
            item_data = json.loads(sys.stdin.read())
        except (json.JSONDecodeError, Exception):
            print("Invalid JSON input or unable to fetch from Zotero.", file=sys.stderr)
            sys.exit(1)
    
    if style == "bibtex":
        print(format_bibtex(item_data))
    else:
        print(format_citation(item_data, style))


if __name__ == "__main__":
    main()
