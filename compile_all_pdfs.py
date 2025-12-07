#!/usr/bin/env python3
"""
Compile all .tex files to PDFs and organize into slides/ folder.
"""

import os
import subprocess
import shutil
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(r"D:\Joerg\Research\slides\DigitalFinance_3")

MODULES = [
    "module_01_fintech",
    "module_02_blockchain",
    "module_03_ai_ml",
    "module_04_traditional"
]


def compile_tex_to_pdf(tex_file):
    """
    Compile a .tex file to PDF using pdflatex.
    Returns True if successful.
    """
    tex_path = Path(tex_file)

    if not tex_path.exists():
        print(f"  ERROR: {tex_path.name} not found")
        return False

    # Run pdflatex twice for proper references
    try:
        for run in [1, 2]:
            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', str(tex_path)],
                cwd=tex_path.parent,
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode != 0 and run == 2:
                print(f"  ERROR compiling {tex_path.name}")
                print(f"    {result.stderr[:200]}")
                return False

        # Check if PDF was created
        pdf_path = tex_path.with_suffix('.pdf')
        if pdf_path.exists():
            print(f"  SUCCESS: {tex_path.name} -> {pdf_path.name}")
            return True
        else:
            print(f"  ERROR: PDF not created for {tex_path.name}")
            return False

    except subprocess.TimeoutExpired:
        print(f"  TIMEOUT: {tex_path.name} took too long")
        return False
    except Exception as e:
        print(f"  ERROR: {tex_path.name} - {str(e)}")
        return False


def move_temp_files(module_path):
    """Move compilation temp files to temp/ folder."""
    temp_dir = module_path / "temp"
    temp_dir.mkdir(exist_ok=True)

    temp_extensions = ['.aux', '.log', '.nav', '.snm', '.toc', '.out']

    for ext in temp_extensions:
        for file_path in module_path.glob(f"*{ext}"):
            if file_path.parent.name != 'temp':
                dest = temp_dir / file_path.name
                shutil.move(str(file_path), str(dest))


def compile_all_modules():
    """Compile all .tex files in all modules."""
    print("="*70)
    print("COMPILING ALL TEX FILES TO PDF")
    print("="*70)

    stats = {
        'total': 0,
        'success': 0,
        'failed': 0,
        'skipped': 0
    }

    for module in MODULES:
        module_path = BASE_DIR / module
        if not module_path.exists():
            print(f"\nSkipping {module} (not found)")
            continue

        print(f"\n{module}:")
        print("-" * 70)

        # Find all .tex files (not in previous/ or temp/)
        tex_files = [f for f in module_path.glob("lesson_*.tex")
                     if f.parent.name not in ['previous', 'temp']]

        for tex_file in sorted(tex_files):
            stats['total'] += 1

            # Check if PDF already exists
            pdf_file = tex_file.with_suffix('.pdf')
            if pdf_file.exists():
                # Check if PDF is newer than TEX
                if pdf_file.stat().st_mtime > tex_file.stat().st_mtime:
                    print(f"  SKIP: {tex_file.name} (PDF up to date)")
                    stats['skipped'] += 1
                    continue

            # Compile
            if compile_tex_to_pdf(tex_file):
                stats['success'] += 1
            else:
                stats['failed'] += 1

        # Clean up temp files
        move_temp_files(module_path)

    print("\n" + "="*70)
    print("COMPILATION SUMMARY")
    print("="*70)
    print(f"Total files: {stats['total']}")
    print(f"Compiled: {stats['success']}")
    print(f"Failed: {stats['failed']}")
    print(f"Skipped (up to date): {stats['skipped']}")
    print("="*70)

    return stats


def create_slides_folder():
    """
    Create slides/ folder and copy all .tex and .pdf files.
    Organized by module.
    """
    print("\n" + "="*70)
    print("CREATING SLIDES/ FOLDER STRUCTURE")
    print("="*70)

    slides_dir = BASE_DIR / "slides"
    slides_dir.mkdir(exist_ok=True)

    copied_files = []

    for module in MODULES:
        module_path = BASE_DIR / module
        if not module_path.exists():
            continue

        # Create module folder in slides/
        slides_module_dir = slides_dir / module
        slides_module_dir.mkdir(exist_ok=True)

        print(f"\n{module}:")

        # Copy .tex and .pdf files
        for ext in ['.tex', '.pdf']:
            for file_path in module_path.glob(f"lesson_*{ext}"):
                if file_path.parent.name not in ['previous', 'temp']:
                    dest_path = slides_module_dir / file_path.name
                    shutil.copy2(file_path, dest_path)
                    copied_files.append(str(dest_path.relative_to(BASE_DIR)))
                    print(f"  Copied: {file_path.name}")

    print(f"\nCopied {len(copied_files)} files to slides/")
    return copied_files


def update_docs_pdfs():
    """
    Update docs/slides/ with all compiled PDFs.
    """
    print("\n" + "="*70)
    print("UPDATING DOCS/SLIDES/ WITH ALL PDFS")
    print("="*70)

    docs_slides_dir = BASE_DIR / "docs" / "slides"
    docs_slides_dir.mkdir(parents=True, exist_ok=True)

    copied_pdfs = []

    for module in MODULES:
        module_path = BASE_DIR / module
        if not module_path.exists():
            continue

        # Create module folder in docs/slides/
        docs_module_dir = docs_slides_dir / module
        docs_module_dir.mkdir(exist_ok=True)

        print(f"\n{module}:")

        # Copy all PDF files
        pdf_count = 0
        for pdf_path in module_path.glob("lesson_*.pdf"):
            if pdf_path.parent.name not in ['previous', 'temp']:
                dest_path = docs_module_dir / pdf_path.name
                shutil.copy2(pdf_path, dest_path)
                copied_pdfs.append(str(dest_path.relative_to(BASE_DIR)))
                pdf_count += 1

        print(f"  Copied {pdf_count} PDFs")

    print(f"\nTotal: {len(copied_pdfs)} PDFs copied to docs/slides/")
    return copied_pdfs


def main():
    """Execute all tasks."""
    print("\n" + "="*70)
    print("PDF COMPILATION AND ORGANIZATION")
    print("="*70)
    print(f"Base directory: {BASE_DIR}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Compile all PDFs
    stats = compile_all_modules()

    # Create slides/ folder
    slides_files = create_slides_folder()

    # Update docs/slides/ with PDFs
    docs_pdfs = update_docs_pdfs()

    print("\n" + "="*70)
    print("COMPLETE")
    print("="*70)
    print(f"Compiled: {stats['success']} PDFs")
    print(f"Failed: {stats['failed']} PDFs")
    print(f"Slides folder: {len(slides_files)} files")
    print(f"Docs PDFs: {len(docs_pdfs)} files")
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
