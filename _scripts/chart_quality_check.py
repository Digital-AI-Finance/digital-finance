"""
Chart Quality Check for Digital Finance Course
Verifies all 462 charts are present, valid, and properly referenced
"""

from pathlib import Path
import re
import os

BASE_DIR = Path(r"D:\Joerg\Research\slides\DigitalFinance_3")
MODULES = [
    "module_01_fintech",
    "module_02_blockchain",
    "module_03_ai_ml",
    "module_04_traditional"
]


def check_chart_quality():
    """Comprehensive chart quality check"""
    print("=" * 80)
    print("CHART QUALITY CHECK")
    print("=" * 80)
    print()

    results = {
        'referenced': [],
        'missing': [],
        'orphaned': [],
        'empty': [],
        'small': [],  # Suspiciously small files
    }

    # 1. Find all referenced charts in .tex files
    all_references = []
    for module in MODULES:
        module_path = BASE_DIR / module
        tex_files = list(module_path.glob("lesson_*.tex"))

        for tex_file in tex_files:
            content = tex_file.read_text(encoding='utf-8', errors='ignore')

            # Find all includegraphics references
            matches = re.findall(r'\\includegraphics\[[^\]]*\]\{([^}]+)\}', content)

            for match in matches:
                # Resolve path relative to module folder
                if match.startswith('figures/'):
                    chart_path = module_path / match
                else:
                    chart_path = module_path / match

                all_references.append({
                    'tex_file': tex_file.name,
                    'module': module,
                    'reference': match,
                    'full_path': chart_path,
                })

    results['referenced'] = all_references
    print(f"Total chart references found: {len(all_references)}")

    # 2. Check which referenced charts are missing
    for ref in all_references:
        if not ref['full_path'].exists():
            results['missing'].append(ref)

    print(f"Missing chart files: {len(results['missing'])}")

    # 3. Find all chart PDFs on disk
    all_chart_pdfs = []
    for module in MODULES:
        figures_path = BASE_DIR / module / "figures"
        if figures_path.exists():
            for pdf in figures_path.rglob("*.pdf"):
                all_chart_pdfs.append(pdf)

    print(f"Total chart PDFs on disk: {len(all_chart_pdfs)}")

    # 4. Find orphaned charts (exist but not referenced)
    referenced_paths = set(ref['full_path'].resolve() for ref in all_references)

    for pdf in all_chart_pdfs:
        if pdf.resolve() not in referenced_paths:
            results['orphaned'].append(pdf)

    print(f"Orphaned charts (not referenced): {len(results['orphaned'])}")

    # 5. Check for empty or suspiciously small files
    for pdf in all_chart_pdfs:
        size = pdf.stat().st_size
        if size == 0:
            results['empty'].append((pdf, size))
        elif size < 1000:  # Less than 1KB
            results['small'].append((pdf, size))

    print(f"Empty chart files: {len(results['empty'])}")
    print(f"Suspiciously small (<1KB): {len(results['small'])}")

    # Detailed reports
    print()
    print("-" * 80)
    print("MISSING CHARTS")
    print("-" * 80)

    if results['missing']:
        for ref in results['missing'][:20]:
            print(f"  {ref['tex_file']}: {ref['reference']}")
        if len(results['missing']) > 20:
            print(f"  ... and {len(results['missing'])-20} more")
    else:
        print("  None - all referenced charts exist!")

    print()
    print("-" * 80)
    print("ORPHANED CHARTS (not referenced in any .tex)")
    print("-" * 80)

    if results['orphaned']:
        for pdf in results['orphaned'][:20]:
            rel_path = pdf.relative_to(BASE_DIR)
            print(f"  {rel_path}")
        if len(results['orphaned']) > 20:
            print(f"  ... and {len(results['orphaned'])-20} more")
    else:
        print("  None - all charts are referenced!")

    print()
    print("-" * 80)
    print("EMPTY/SMALL FILES")
    print("-" * 80)

    if results['empty'] or results['small']:
        for pdf, size in results['empty']:
            print(f"  [EMPTY] {pdf.relative_to(BASE_DIR)}")
        for pdf, size in results['small']:
            print(f"  [SMALL {size}B] {pdf.relative_to(BASE_DIR)}")
    else:
        print("  None - all chart files have valid size!")

    # Charts by module
    print()
    print("-" * 80)
    print("CHARTS BY MODULE")
    print("-" * 80)

    for module in MODULES:
        module_refs = [r for r in all_references if r['module'] == module]
        module_pdfs = [p for p in all_chart_pdfs if module in str(p)]
        print(f"  {module}: {len(module_refs)} references, {len(module_pdfs)} PDFs")

    # Summary
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)

    issues = len(results['missing']) + len(results['empty']) + len(results['small'])
    if issues == 0:
        print("All charts verified successfully!")
        print(f"  - {len(all_references)} chart references")
        print(f"  - {len(all_chart_pdfs)} PDF files")
        print(f"  - {len(results['orphaned'])} orphaned (can be cleaned up)")
    else:
        print(f"Found {issues} issues to fix:")
        if results['missing']:
            print(f"  - {len(results['missing'])} missing charts")
        if results['empty']:
            print(f"  - {len(results['empty'])} empty files")
        if results['small']:
            print(f"  - {len(results['small'])} suspiciously small files")

    return results


if __name__ == "__main__":
    check_chart_quality()
