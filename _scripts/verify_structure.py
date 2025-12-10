#!/usr/bin/env python3
"""
Verify repository structure is ready for GitHub deployment.
"""

from pathlib import Path
from datetime import datetime

BASE_DIR = Path(r"D:\Joerg\Research\slides\DigitalFinance_3")

def check_structure():
    """Verify folder structure."""
    print("="*70)
    print("REPOSITORY STRUCTURE VERIFICATION")
    print("="*70)

    required_folders = {
        'module_01_fintech': 'FinTech source files',
        'module_02_blockchain': 'Blockchain source files',
        'module_03_ai_ml': 'AI/ML source files',
        'module_04_traditional': 'Traditional finance source files',
        'slides': 'Organized lesson files',
        'slides/module_01_fintech': 'FinTech slides',
        'slides/module_02_blockchain': 'Blockchain slides',
        'slides/module_03_ai_ml': 'AI/ML slides',
        'slides/module_04_traditional': 'Traditional slides',
        'docs': 'GitHub Pages root',
        'docs/slides': 'Web-ready PDFs',
        'demos': 'Python demos',
        'charts': 'Chart scripts',
        'assessments': 'Rubrics',
        'syllabus': 'Syllabus'
    }

    print("\nFOLDER STRUCTURE:")
    all_exist = True
    for folder, desc in required_folders.items():
        folder_path = BASE_DIR / folder
        exists = folder_path.exists()
        status = "OK" if exists else "MISSING"
        print(f"  [{status}] {folder:30s} - {desc}")
        if not exists:
            all_exist = False

    return all_exist


def check_files():
    """Check critical files exist."""
    print("\n" + "="*70)
    print("CRITICAL FILES")
    print("="*70)

    critical_files = {
        'README.md': 'Main documentation',
        'LICENSE': 'CC BY-NC-SA 4.0 license',
        'manifest.txt': 'File inventory',
        'REORGANIZATION_SUMMARY.md': 'Reorganization report',
        'NEXT_STEPS.md': 'Deployment guide',
        'docs/index.html': 'GitHub Pages home',
        'requirements.txt': 'Python dependencies',
    }

    all_exist = True
    for filename, desc in critical_files.items():
        file_path = BASE_DIR / filename
        exists = file_path.exists()
        status = "OK" if exists else "MISSING"
        print(f"  [{status}] {filename:35s} - {desc}")
        if not exists:
            all_exist = False

    return all_exist


def count_lessons():
    """Count lesson files."""
    print("\n" + "="*70)
    print("LESSON FILE COUNTS")
    print("="*70)

    modules = [
        'module_01_fintech',
        'module_02_blockchain',
        'module_03_ai_ml',
        'module_04_traditional'
    ]

    total_tex = 0
    total_pdf = 0
    total_missing = 0

    for module in modules:
        module_path = BASE_DIR / module
        if not module_path.exists():
            continue

        tex_files = list(module_path.glob("lesson_*.tex"))
        pdf_files = list(module_path.glob("lesson_*.pdf"))

        tex_count = len(tex_files)
        pdf_count = len(pdf_files)
        missing = tex_count - pdf_count

        total_tex += tex_count
        total_pdf += pdf_count
        total_missing += missing

        print(f"\n{module}:")
        print(f"  TEX files: {tex_count}")
        print(f"  PDF files: {pdf_count}")
        print(f"  Missing PDFs: {missing}")

    print(f"\nTOTAL:")
    print(f"  TEX files: {total_tex}")
    print(f"  PDF files: {total_pdf}")
    print(f"  Missing PDFs: {total_missing}")

    return total_tex, total_pdf, total_missing


def check_slides_folder():
    """Check slides/ folder organization."""
    print("\n" + "="*70)
    print("SLIDES FOLDER VERIFICATION")
    print("="*70)

    slides_dir = BASE_DIR / "slides"
    if not slides_dir.exists():
        print("  ERROR: slides/ folder not found")
        return False

    modules = [
        'module_01_fintech',
        'module_02_blockchain',
        'module_03_ai_ml',
        'module_04_traditional'
    ]

    total_files = 0
    for module in modules:
        module_path = slides_dir / module
        if not module_path.exists():
            print(f"  MISSING: slides/{module}/")
            continue

        tex_count = len(list(module_path.glob("lesson_*.tex")))
        pdf_count = len(list(module_path.glob("lesson_*.pdf")))
        total = tex_count + pdf_count
        total_files += total

        print(f"  {module}: {tex_count} TEX + {pdf_count} PDF = {total} files")

    print(f"\nTotal files in slides/: {total_files}")
    return total_files > 0


def check_docs_folder():
    """Check docs/ folder for GitHub Pages."""
    print("\n" + "="*70)
    print("DOCS FOLDER VERIFICATION (GitHub Pages)")
    print("="*70)

    docs_dir = BASE_DIR / "docs"
    if not docs_dir.exists():
        print("  ERROR: docs/ folder not found")
        return False

    # Check index.html
    index_html = docs_dir / "index.html"
    if index_html.exists():
        size = index_html.stat().st_size
        print(f"  OK: index.html ({size:,} bytes)")
    else:
        print("  MISSING: index.html")

    # Check slides PDFs
    docs_slides = docs_dir / "slides"
    if not docs_slides.exists():
        print("  ERROR: docs/slides/ folder not found")
        return False

    modules = [
        'module_01_fintech',
        'module_02_blockchain',
        'module_03_ai_ml',
        'module_04_traditional'
    ]

    total_pdfs = 0
    for module in modules:
        module_path = docs_slides / module
        if module_path.exists():
            pdf_count = len(list(module_path.glob("lesson_*.pdf")))
            total_pdfs += pdf_count
            print(f"  {module}: {pdf_count} PDFs")

    print(f"\nTotal PDFs in docs/slides/: {total_pdfs}")
    return total_pdfs > 0


def check_unwanted_files():
    """Check for files that should be excluded."""
    print("\n" + "="*70)
    print("UNWANTED FILES CHECK")
    print("="*70)

    unwanted_patterns = [
        '**/*.aux',
        '**/*.log',
        '**/*.nav',
        '**/*.snm',
        '**/*.toc',
        '**/*.out',
    ]

    unwanted_found = []

    for pattern in unwanted_patterns:
        files = list(BASE_DIR.glob(pattern))
        # Exclude temp/ and previous/ folders
        files = [f for f in files if 'temp' not in str(f) and 'previous' not in str(f)]

        if files:
            unwanted_found.extend(files)

    if unwanted_found:
        print(f"  WARNING: {len(unwanted_found)} unwanted files found (should be in temp/):")
        for f in unwanted_found[:10]:
            print(f"    {f.relative_to(BASE_DIR)}")
        if len(unwanted_found) > 10:
            print(f"    ... and {len(unwanted_found) - 10} more")
    else:
        print("  OK: No unwanted compilation artifacts found")

    return len(unwanted_found) == 0


def main():
    """Run all verifications."""
    print("\n" + "="*70)
    print("DIGITAL FINANCE REPOSITORY - PRE-DEPLOYMENT VERIFICATION")
    print("="*70)
    print(f"Location: {BASE_DIR}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Run checks
    structure_ok = check_structure()
    files_ok = check_files()
    tex_count, pdf_count, missing_count = count_lessons()
    slides_ok = check_slides_folder()
    docs_ok = check_docs_folder()
    no_unwanted = check_unwanted_files()

    # Summary
    print("\n" + "="*70)
    print("VERIFICATION SUMMARY")
    print("="*70)

    checks = [
        ("Folder structure", structure_ok),
        ("Critical files", files_ok),
        ("Slides folder", slides_ok),
        ("Docs folder", docs_ok),
        ("No unwanted files", no_unwanted),
    ]

    all_passed = all(result for _, result in checks)

    for check_name, result in checks:
        status = "PASS" if result else "FAIL"
        print(f"  [{status}] {check_name}")

    print(f"\nLesson Statistics:")
    print(f"  Total lessons: {tex_count}")
    print(f"  Compiled PDFs: {pdf_count}")
    print(f"  Missing PDFs: {missing_count}")
    print(f"  Completion: {(pdf_count/tex_count*100):.1f}%")

    print("\n" + "="*70)
    if all_passed and missing_count == 0:
        print("STATUS: READY FOR GITHUB DEPLOYMENT")
        print("All checks passed, all PDFs compiled!")
    elif all_passed:
        print("STATUS: READY FOR GITHUB DEPLOYMENT (with missing PDFs)")
        print(f"Structure is good, but {missing_count} PDFs need compilation.")
        print("Run: python compile_missing_pdfs.py")
    else:
        print("STATUS: NOT READY - Issues found")
        print("Review failures above and fix before deployment.")

    print("="*70)
    print("\nNext steps:")
    print("  1. Review NEXT_STEPS.md for deployment instructions")
    print("  2. Create .gitignore file")
    print("  3. Initialize git repository")
    print("  4. Push to GitHub")
    print("  5. Enable GitHub Pages")
    print("="*70 + "\n")

    return 0 if all_passed else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
