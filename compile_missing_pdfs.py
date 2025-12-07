#!/usr/bin/env python3
"""
Compile all missing PDFs in batch mode.
This script compiles the 31 .tex files that don't have corresponding PDFs.
"""

import subprocess
import shutil
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(r"D:\Joerg\Research\slides\DigitalFinance_3")

# List of files that need compilation (from REORGANIZATION_SUMMARY.md)
MISSING_PDFS = {
    'module_02_blockchain': [
        'lesson_16_proof_of_work.tex',
        'lesson_17_proof_of_stake.tex',
        'lesson_18_bitcoin_architecture.tex',
        'lesson_19_ethereum_smart_contracts.tex',
        'lesson_20_tokens.tex',
        'lesson_21_defi.tex',
        'lesson_22_stablecoins.tex',
        'lesson_23_security.tex',
        'lesson_24_regulation_future.tex',
    ],
    'module_03_ai_ml': [
        'lesson_26_financial_data.tex',
        'lesson_27_regression.tex',
        'lesson_28_classification.tex',
        'lesson_29_algorithmic_trading_concepts.tex',
        'lesson_30_credit_scoring_and_risk_models.tex',
        'lesson_31_fraud_detection_and_aml.tex',
        'lesson_32_nlp_in_finance.tex',
        'lesson_33_robo-advisors_ml_aspects.tex',
        'lesson_34_market_prediction_limitations.tex',
        'lesson_35_explainability_and_bias.tex',
    ],
    'module_04_traditional': [
        'lesson_37_financial_markets.tex',
        'lesson_38_core_banking.tex',
        'lesson_39_payment_rails.tex',
        'lesson_40_electronic_trading.tex',
        'lesson_41_market_microstructure.tex',
        'lesson_42_risk_management.tex',
        'lesson_43_regtech_compliance.tex',
        'lesson_44_capital_markets_tech.tex',
        'lesson_45_derivatives_technology.tex',
        'lesson_46_wealth_management.tex',
        'lesson_47_data_vendors.tex',
        'lesson_48_cbdc_future.tex',
    ]
}


def compile_pdf(tex_path):
    """
    Compile a single .tex file to PDF.
    Returns True if successful.
    """
    if not tex_path.exists():
        return False, f"File not found: {tex_path}"

    try:
        # Run pdflatex twice for proper references
        for run in [1, 2]:
            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', str(tex_path)],
                cwd=tex_path.parent,
                capture_output=True,
                text=True,
                timeout=120
            )

            if result.returncode != 0 and run == 2:
                # Get last 500 chars of error
                error_msg = result.stdout[-500:] if result.stdout else "Unknown error"
                return False, error_msg

        # Check if PDF was created
        pdf_path = tex_path.with_suffix('.pdf')
        if pdf_path.exists():
            return True, "Success"
        else:
            return False, "PDF not created"

    except subprocess.TimeoutExpired:
        return False, "Compilation timeout (>120s)"
    except FileNotFoundError:
        return False, "pdflatex not found - install LaTeX distribution"
    except Exception as e:
        return False, str(e)


def clean_temp_files(module_path):
    """
    Move temp files to temp/ folder.
    Uses try/except to handle file locks.
    """
    temp_dir = module_path / "temp"
    temp_dir.mkdir(exist_ok=True)

    temp_exts = ['.aux', '.log', '.nav', '.snm', '.toc', '.out']
    moved = 0

    for ext in temp_exts:
        for file_path in module_path.glob(f"*{ext}"):
            if file_path.parent.name != 'temp':
                try:
                    dest = temp_dir / file_path.name
                    shutil.move(str(file_path), str(dest))
                    moved += 1
                except (PermissionError, OSError):
                    # File locked, skip
                    pass

    return moved


def update_docs_and_slides(module, tex_filename):
    """
    Copy compiled PDF to docs/ and slides/ folders.
    """
    pdf_filename = tex_filename.replace('.tex', '.pdf')
    source_pdf = BASE_DIR / module / pdf_filename

    if not source_pdf.exists():
        return False

    # Copy to docs/slides/
    docs_dest = BASE_DIR / "docs" / "slides" / module / pdf_filename
    docs_dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_pdf, docs_dest)

    # Copy to slides/
    slides_dest = BASE_DIR / "slides" / module / pdf_filename
    slides_dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_pdf, slides_dest)

    return True


def main():
    """Main compilation routine."""
    print("="*70)
    print("BATCH PDF COMPILATION")
    print("="*70)
    print(f"Base directory: {BASE_DIR}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    stats = {
        'total': 0,
        'success': 0,
        'failed': 0,
        'not_found': 0
    }

    failed_files = []

    for module, tex_files in MISSING_PDFS.items():
        print(f"\n{module.upper()}")
        print("-" * 70)

        module_path = BASE_DIR / module
        if not module_path.exists():
            print(f"  ERROR: Module directory not found")
            continue

        for tex_file in tex_files:
            stats['total'] += 1
            tex_path = module_path / tex_file

            print(f"  Compiling: {tex_file}...", end=" ")

            if not tex_path.exists():
                print("NOT FOUND")
                stats['not_found'] += 1
                failed_files.append((module, tex_file, "File not found"))
                continue

            success, message = compile_pdf(tex_path)

            if success:
                print("SUCCESS")
                stats['success'] += 1

                # Copy to docs and slides
                if update_docs_and_slides(module, tex_file):
                    print(f"    -> Copied to docs/ and slides/")
            else:
                print(f"FAILED")
                print(f"    Error: {message[:100]}")
                stats['failed'] += 1
                failed_files.append((module, tex_file, message[:200]))

        # Clean temp files
        moved = clean_temp_files(module_path)
        print(f"  Cleaned {moved} temp files")

    # Summary
    print("\n" + "="*70)
    print("COMPILATION SUMMARY")
    print("="*70)
    print(f"Total files:  {stats['total']}")
    print(f"Successful:   {stats['success']}")
    print(f"Failed:       {stats['failed']}")
    print(f"Not found:    {stats['not_found']}")

    if failed_files:
        print("\nFAILED FILES:")
        print("-" * 70)
        for module, filename, error in failed_files:
            print(f"  {module}/{filename}")
            print(f"    {error}\n")

    print("="*70)
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)

    # Return exit code
    return 0 if stats['failed'] == 0 else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
