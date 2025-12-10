#!/usr/bin/env python3
"""
Reorganize Digital Finance course files for GitHub deployment.

This script:
1. Renames timestamped .tex and .pdf files (removes timestamps)
2. Cleans temp files (.aux, .log, .nav, .snm, .toc, .out)
3. Creates docs/ folder structure for GitHub Pages
4. Restructures main folders
5. Generates file manifest
"""

import os
import shutil
import re
from pathlib import Path
from datetime import datetime

# Base directory
BASE_DIR = Path(r"D:\Joerg\Research\slides\DigitalFinance_3")

# Module directories
MODULES = [
    "module_01_fintech",
    "module_02_blockchain",
    "module_03_ai_ml",
    "module_04_traditional"
]

# Temp file extensions to clean
TEMP_EXTENSIONS = ['.aux', '.log', '.nav', '.snm', '.toc', '.out']

# Pattern to match timestamped files: YYYYMMDD_HHMM_filename.ext
TIMESTAMP_PATTERN = re.compile(r'^(\d{8}_\d{4})_(.+)$')


def ensure_directory(path):
    """Create directory if it doesn't exist."""
    path.mkdir(parents=True, exist_ok=True)
    return path


def rename_timestamped_files():
    """
    Rename .tex and .pdf files by removing timestamps.
    Keep originals in previous/ folder.
    """
    print("\n" + "="*70)
    print("TASK 1: Renaming timestamped files")
    print("="*70)

    renamed_files = []

    for module in MODULES:
        module_path = BASE_DIR / module
        if not module_path.exists():
            print(f"Skipping {module} (not found)")
            continue

        # Create previous/ folder in module
        previous_dir = ensure_directory(module_path / "previous")

        # Find all .tex and .pdf files
        for ext in ['.tex', '.pdf']:
            for file_path in module_path.glob(f"*{ext}"):
                # Skip if already in previous/ or temp/
                if file_path.parent.name in ['previous', 'temp']:
                    continue

                filename = file_path.name
                match = TIMESTAMP_PATTERN.match(filename)

                if match:
                    timestamp = match.group(1)
                    clean_name = match.group(2)
                    new_path = module_path / clean_name

                    # Backup to previous/
                    backup_path = previous_dir / filename
                    shutil.copy2(file_path, backup_path)

                    # Rename (or copy if file exists)
                    if new_path.exists():
                        print(f"  WARNING: {clean_name} already exists, keeping timestamped version in previous/")
                        file_path.unlink()  # Remove timestamped version
                    else:
                        file_path.rename(new_path)
                        renamed_files.append({
                            'old': filename,
                            'new': clean_name,
                            'module': module,
                            'backup': str(backup_path)
                        })
                        print(f"  {module}: {filename} -> {clean_name}")

    print(f"\nRenamed {len(renamed_files)} files")
    return renamed_files


def clean_temp_files():
    """
    Clean temporary LaTeX compilation files.
    Move to temp/ folder instead of deleting.
    """
    print("\n" + "="*70)
    print("TASK 2: Cleaning temp files")
    print("="*70)

    cleaned_files = []

    for module in MODULES:
        module_path = BASE_DIR / module
        if not module_path.exists():
            continue

        # Create temp/ folder in module
        temp_dir = ensure_directory(module_path / "temp")

        # Find and move temp files
        for ext in TEMP_EXTENSIONS:
            for file_path in module_path.glob(f"*{ext}"):
                # Skip if already in temp/
                if file_path.parent.name == 'temp':
                    continue

                dest_path = temp_dir / file_path.name
                shutil.move(str(file_path), str(dest_path))
                cleaned_files.append(str(file_path.relative_to(BASE_DIR)))
                print(f"  Moved: {file_path.name} -> temp/")

        # Also clean __pycache__ directories
        for pycache in module_path.rglob("__pycache__"):
            shutil.rmtree(pycache)
            cleaned_files.append(str(pycache.relative_to(BASE_DIR)))
            print(f"  Removed: {pycache.relative_to(module_path)}")

    print(f"\nCleaned {len(cleaned_files)} temp files/folders")
    return cleaned_files


def create_docs_structure():
    """
    Create docs/ folder structure for GitHub Pages.
    Copy PDFs to appropriate module folders.
    """
    print("\n" + "="*70)
    print("TASK 3: Creating docs/ folder structure")
    print("="*70)

    docs_dir = ensure_directory(BASE_DIR / "docs")
    slides_dir = ensure_directory(docs_dir / "slides")

    copied_pdfs = []

    for module in MODULES:
        module_path = BASE_DIR / module
        if not module_path.exists():
            continue

        # Create module folder in docs/slides/
        docs_module_dir = ensure_directory(slides_dir / module)

        # Copy all PDF files (non-timestamped names now)
        for pdf_path in module_path.glob("*.pdf"):
            # Skip if in previous/ or temp/
            if pdf_path.parent.name in ['previous', 'temp']:
                continue

            dest_path = docs_module_dir / pdf_path.name
            shutil.copy2(pdf_path, dest_path)
            copied_pdfs.append({
                'source': str(pdf_path.relative_to(BASE_DIR)),
                'dest': str(dest_path.relative_to(BASE_DIR))
            })
            print(f"  Copied: {pdf_path.name} -> docs/slides/{module}/")

    print(f"\nCopied {len(copied_pdfs)} PDFs to docs/slides/")
    return copied_pdfs


def restructure_main_folders():
    """
    Ensure clean folder structure:
    - Rename python_demos -> demos
    - Verify other folders exist
    """
    print("\n" + "="*70)
    print("TASK 4: Restructuring main folders")
    print("="*70)

    actions = []

    # Rename python_demos -> demos
    python_demos = BASE_DIR / "python_demos"
    demos = BASE_DIR / "demos"

    if python_demos.exists() and not demos.exists():
        python_demos.rename(demos)
        actions.append("Renamed: python_demos -> demos")
        print("  Renamed: python_demos -> demos")
    elif demos.exists():
        print("  demos/ already exists")
    else:
        print("  WARNING: python_demos/ not found")

    # Verify other folders
    expected_folders = {
        'slides': 'Will be populated manually',
        'demos': 'Python demos and examples',
        'charts': 'Chart generation scripts',
        'assessments': 'Rubrics and guidelines',
        'syllabus': 'Syllabus documents',
        'docs': 'GitHub Pages site'
    }

    print("\nVerifying folder structure:")
    for folder, description in expected_folders.items():
        folder_path = BASE_DIR / folder
        status = "EXISTS" if folder_path.exists() else "MISSING"
        print(f"  [{status}] {folder}/ - {description}")

        if status == "MISSING" and folder == 'slides':
            print(f"    NOTE: {folder}/ should be created manually")

    return actions


def generate_file_manifest():
    """
    Generate manifest.txt listing all files to be committed.
    Excludes temp/, previous/, and system files.
    """
    print("\n" + "="*70)
    print("TASK 5: Generating file manifest")
    print("="*70)

    manifest_path = BASE_DIR / "manifest.txt"

    # Patterns to exclude
    exclude_patterns = [
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
        'nul'
    ]

    files_to_commit = []

    # Walk through all files
    for root, dirs, files in os.walk(BASE_DIR):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if not any(excl.rstrip('/') in d for excl in exclude_patterns)]

        for file in files:
            file_path = Path(root) / file
            rel_path = file_path.relative_to(BASE_DIR)
            rel_path_str = str(rel_path).replace('\\', '/')

            # Skip excluded files
            if any(excl in rel_path_str for excl in exclude_patterns):
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
        f.write("DIGITAL FINANCE COURSE - FILE MANIFEST\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*70 + "\n\n")

        total_files = 0
        for category, files in categories.items():
            if files:
                f.write(f"\n{category} ({len(files)} files)\n")
                f.write("-" * 70 + "\n")
                for file_path in files:
                    f.write(f"  {file_path}\n")
                total_files += len(files)

        f.write("\n" + "="*70 + "\n")
        f.write(f"TOTAL: {total_files} files\n")
        f.write("="*70 + "\n")

    print(f"Generated manifest.txt with {total_files} files")

    # Print summary
    print("\nFile count by category:")
    for category, files in categories.items():
        if files:
            print(f"  {category}: {len(files)} files")

    return manifest_path


def main():
    """Execute all reorganization tasks."""
    print("\n" + "="*70)
    print("DIGITAL FINANCE COURSE - GITHUB REORGANIZATION")
    print("="*70)
    print(f"Base directory: {BASE_DIR}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Execute tasks
    renamed = rename_timestamped_files()
    cleaned = clean_temp_files()
    copied = create_docs_structure()
    restructured = restructure_main_folders()
    manifest = generate_file_manifest()

    # Final summary
    print("\n" + "="*70)
    print("REORGANIZATION COMPLETE")
    print("="*70)
    print(f"Renamed files: {len(renamed)}")
    print(f"Cleaned temp files: {len(cleaned)}")
    print(f"Copied PDFs to docs/: {len(copied)}")
    print(f"Manifest generated: {manifest}")
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\nNext steps:")
    print("1. Review manifest.txt")
    print("2. Create slides/ folder manually if needed")
    print("3. Copy cleaned .tex and .pdf files to slides/ if desired")
    print("4. Review docs/index.html (created by other agent)")
    print("5. Initialize git repo and commit")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
