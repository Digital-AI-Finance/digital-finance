#!/usr/bin/env python3
"""
Simple organization: just copy existing files to slides/ and docs/
Skip compilation - do that separately if needed.
"""

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


def create_slides_folder():
    """
    Create slides/ folder and copy all .tex and .pdf files.
    Organized by module.
    """
    print("="*70)
    print("CREATING SLIDES/ FOLDER STRUCTURE")
    print("="*70)

    slides_dir = BASE_DIR / "slides"
    slides_dir.mkdir(exist_ok=True)

    copied_files = []

    for module in MODULES:
        module_path = BASE_DIR / module
        if not module_path.exists():
            print(f"\nSkipping {module} (not found)")
            continue

        # Create module folder in slides/
        slides_module_dir = slides_dir / module
        slides_module_dir.mkdir(exist_ok=True)

        print(f"\n{module}:")

        # Copy .tex and .pdf files
        tex_count = 0
        pdf_count = 0

        for file_path in sorted(module_path.glob("lesson_*.*")):
            if file_path.parent.name in ['previous', 'temp']:
                continue

            if file_path.suffix in ['.tex', '.pdf']:
                dest_path = slides_module_dir / file_path.name
                try:
                    shutil.copy2(file_path, dest_path)
                    copied_files.append(str(dest_path.relative_to(BASE_DIR)))

                    if file_path.suffix == '.tex':
                        tex_count += 1
                    else:
                        pdf_count += 1
                except Exception as e:
                    print(f"  ERROR copying {file_path.name}: {e}")

        print(f"  Copied {tex_count} TEX files, {pdf_count} PDF files")

    print(f"\nTotal: {len(copied_files)} files copied to slides/")
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
        for pdf_path in sorted(module_path.glob("lesson_*.pdf")):
            if pdf_path.parent.name in ['previous', 'temp']:
                continue

            dest_path = docs_module_dir / pdf_path.name
            try:
                shutil.copy2(pdf_path, dest_path)
                copied_pdfs.append(str(dest_path.relative_to(BASE_DIR)))
                pdf_count += 1
            except Exception as e:
                print(f"  ERROR copying {pdf_path.name}: {e}")

        print(f"  Copied {pdf_count} PDFs")

    print(f"\nTotal: {len(copied_pdfs)} PDFs copied to docs/slides/")
    return copied_pdfs


def list_missing_pdfs():
    """List .tex files that don't have corresponding PDFs."""
    print("\n" + "="*70)
    print("CHECKING FOR MISSING PDFS")
    print("="*70)

    missing = []

    for module in MODULES:
        module_path = BASE_DIR / module
        if not module_path.exists():
            continue

        module_missing = []

        for tex_path in sorted(module_path.glob("lesson_*.tex")):
            if tex_path.parent.name in ['previous', 'temp']:
                continue

            pdf_path = tex_path.with_suffix('.pdf')
            if not pdf_path.exists():
                module_missing.append(tex_path.name)
                missing.append(str(tex_path.relative_to(BASE_DIR)))

        if module_missing:
            print(f"\n{module}: {len(module_missing)} missing PDFs")
            for name in module_missing:
                print(f"  - {name}")

    if not missing:
        print("\nAll .tex files have corresponding PDFs!")
    else:
        print(f"\nTotal: {len(missing)} .tex files need compilation")

    return missing


def main():
    """Execute all tasks."""
    print("\n" + "="*70)
    print("SLIDES ORGANIZATION (WITHOUT COMPILATION)")
    print("="*70)
    print(f"Base directory: {BASE_DIR}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Create slides/ folder
    slides_files = create_slides_folder()

    # Update docs/slides/ with PDFs
    docs_pdfs = update_docs_pdfs()

    # List missing PDFs
    missing = list_missing_pdfs()

    print("\n" + "="*70)
    print("COMPLETE")
    print("="*70)
    print(f"Slides folder: {len(slides_files)} files")
    print(f"Docs PDFs: {len(docs_pdfs)} files")
    print(f"Missing PDFs: {len(missing)} files")
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if missing:
        print("\nNOTE: Some .tex files need compilation.")
        print("Run pdflatex manually on these files if needed.")

    print("="*70 + "\n")


if __name__ == "__main__":
    main()
