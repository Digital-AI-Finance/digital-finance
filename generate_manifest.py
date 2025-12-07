#!/usr/bin/env python3
"""
Generate file manifest for GitHub deployment.
"""

import os
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(r"D:\Joerg\Research\slides\DigitalFinance_3")

# Patterns to exclude
EXCLUDE_PATTERNS = [
    'temp/',
    'previous/',
    '__pycache__/',
    '.aux',
    '.log',
    '.nav',
    '.snm',
    '.toc',
    '.out',
    'manifest.txt',
    'reorganize_for_github.py',
    'compile_all_pdfs.py',
    'organize_slides_simple.py',
    'generate_manifest.py',
    'nul',
    '.pyc'
]


def should_exclude(path_str):
    """Check if path should be excluded."""
    for pattern in EXCLUDE_PATTERNS:
        if pattern in path_str:
            return True
    return False


def generate_manifest():
    """Generate manifest.txt listing all files to be committed."""
    print("="*70)
    print("GENERATING FILE MANIFEST")
    print("="*70)

    manifest_path = BASE_DIR / "manifest.txt"

    files_to_commit = []

    # Walk through all files
    for root, dirs, files in os.walk(BASE_DIR):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if not any(excl.rstrip('/') in d for excl in EXCLUDE_PATTERNS)]

        for file in files:
            file_path = Path(root) / file
            rel_path = file_path.relative_to(BASE_DIR)
            rel_path_str = str(rel_path).replace('\\', '/')

            # Skip excluded files
            if should_exclude(rel_path_str):
                continue

            files_to_commit.append(rel_path_str)

    # Sort files
    files_to_commit.sort()

    # Group by category
    categories = {
        'Module 01 - FinTech': [],
        'Module 02 - Blockchain': [],
        'Module 03 - AI/ML': [],
        'Module 04 - Traditional': [],
        'Slides (Organized)': [],
        'Assessments': [],
        'Syllabus': [],
        'Demos': [],
        'Charts': [],
        'Docs (GitHub Pages)': [],
        'Other': []
    }

    for file_path in files_to_commit:
        if file_path.startswith('module_01_fintech/'):
            categories['Module 01 - FinTech'].append(file_path)
        elif file_path.startswith('module_02_blockchain/'):
            categories['Module 02 - Blockchain'].append(file_path)
        elif file_path.startswith('module_03_ai_ml/'):
            categories['Module 03 - AI/ML'].append(file_path)
        elif file_path.startswith('module_04_traditional/'):
            categories['Module 04 - Traditional'].append(file_path)
        elif file_path.startswith('slides/'):
            categories['Slides (Organized)'].append(file_path)
        elif file_path.startswith('assessments/'):
            categories['Assessments'].append(file_path)
        elif file_path.startswith('syllabus/'):
            categories['Syllabus'].append(file_path)
        elif file_path.startswith('demos/'):
            categories['Demos'].append(file_path)
        elif file_path.startswith('charts/'):
            categories['Charts'].append(file_path)
        elif file_path.startswith('docs/'):
            categories['Docs (GitHub Pages)'].append(file_path)
        else:
            categories['Other'].append(file_path)

    # Write manifest
    with open(manifest_path, 'w', encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write("DIGITAL FINANCE COURSE - FILE MANIFEST FOR GITHUB\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*70 + "\n\n")
        f.write("REPOSITORY STRUCTURE:\n")
        f.write("-" * 70 + "\n")
        f.write("module_XX/       - Source files (TEX, PDF, scripts)\n")
        f.write("slides/          - Organized lesson files by module\n")
        f.write("demos/           - Python demos and examples\n")
        f.write("charts/          - Chart generation scripts\n")
        f.write("assessments/     - Rubrics and guidelines\n")
        f.write("syllabus/        - Syllabus documents\n")
        f.write("docs/            - GitHub Pages website\n")
        f.write("  slides/        - PDFs for online viewing\n")
        f.write("\n")

        total_files = 0
        for category, files in categories.items():
            if files:
                f.write(f"\n{category} ({len(files)} files)\n")
                f.write("-" * 70 + "\n")
                for file_path in files[:50]:  # Limit to first 50 per category
                    f.write(f"  {file_path}\n")
                if len(files) > 50:
                    f.write(f"  ... and {len(files) - 50} more files\n")
                total_files += len(files)

        f.write("\n" + "="*70 + "\n")
        f.write(f"TOTAL FILES FOR GITHUB: {total_files}\n")
        f.write("="*70 + "\n")

        # Add notes
        f.write("\nNOTES:\n")
        f.write("-" * 70 + "\n")
        f.write("- Excluded: temp/, previous/, compilation artifacts\n")
        f.write("- Module folders contain source TEX and some compiled PDFs\n")
        f.write("- slides/ folder contains organized lesson files\n")
        f.write("- docs/slides/ contains PDFs for GitHub Pages deployment\n")
        f.write("- 31 TEX files need compilation (missing PDFs)\n")
        f.write("\n")

    print(f"\nGenerated: {manifest_path}")
    print(f"Total files: {total_files}")

    # Print summary
    print("\nFile count by category:")
    for category, files in categories.items():
        if files:
            print(f"  {category}: {len(files)} files")

    return manifest_path, total_files


def main():
    """Main execution."""
    print("\n" + "="*70)
    print("MANIFEST GENERATOR")
    print("="*70)
    print(f"Base directory: {BASE_DIR}")

    manifest_path, total_files = generate_manifest()

    print("\n" + "="*70)
    print("COMPLETE")
    print("="*70)
    print(f"Manifest: {manifest_path}")
    print(f"Total files: {total_files}")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
