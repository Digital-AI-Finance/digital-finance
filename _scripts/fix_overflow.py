"""
Fix overflow warnings in LaTeX lessons by adding \small to dense frames.
"""
import subprocess
from pathlib import Path
import re

BASE = Path(r'D:\Joerg\Research\slides\DigitalFinance_3')

LESSONS_WITH_OVERFLOW = [
    ('module_01_fintech', 'lesson_03_mobile_wallets.tex'),
    ('module_01_fintech', 'lesson_04_neobanks.tex'),
    ('module_01_fintech', 'lesson_05_open_banking.tex'),
    ('module_01_fintech', 'lesson_06_digital_identity.tex'),
    ('module_01_fintech', 'lesson_07_p2p_lending.tex'),
    ('module_01_fintech', 'lesson_08_robo_advisors.tex'),
    ('module_01_fintech', 'lesson_09_insurtech.tex'),
    ('module_01_fintech', 'lesson_10_regtech.tex'),
    ('module_01_fintech', 'lesson_11_regulatory_frameworks.tex'),
    ('module_01_fintech', 'lesson_12_business_models.tex'),
    ('module_02_blockchain', 'lesson_15_public_key_crypto.tex'),
    ('module_02_blockchain', 'lesson_16_proof_of_work.tex'),
    ('module_02_blockchain', 'lesson_17_proof_of_stake.tex'),
    ('module_02_blockchain', 'lesson_18_bitcoin_architecture.tex'),
    ('module_02_blockchain', 'lesson_19_ethereum_smart_contracts.tex'),
    ('module_02_blockchain', 'lesson_20_tokens.tex'),
    ('module_02_blockchain', 'lesson_21_defi.tex'),
    ('module_02_blockchain', 'lesson_22_stablecoins.tex'),
    ('module_02_blockchain', 'lesson_23_security.tex'),
    ('module_02_blockchain', 'lesson_24_regulation_future.tex'),
    ('module_04_traditional', 'lesson_42_risk_management.tex'),
    ('module_04_traditional', 'lesson_43_regtech_compliance.tex'),
    ('module_04_traditional', 'lesson_44_capital_markets_tech.tex'),
    ('module_04_traditional', 'lesson_45_derivatives_technology.tex'),
    ('module_04_traditional', 'lesson_47_data_vendors.tex'),
    ('module_04_traditional', 'lesson_48_cbdc_future.tex'),
]


def fix_overflow(tex_path):
    """Add \\scriptsize after \\begin{columns}[T] to reduce font size in dense frames"""
    content = tex_path.read_text(encoding='utf-8')
    original = content

    # Replace existing size commands with scriptsize
    content = content.replace('\\begin{columns}[T]\n\\small\n', '\\begin{columns}[T]\n\\scriptsize\n')
    content = content.replace('\\begin{columns}[T]\n\\footnotesize\n', '\\begin{columns}[T]\n\\scriptsize\n')

    # Also apply to any that don't have it yet
    if '\\begin{columns}[T]\n\\scriptsize' not in content:
        content = content.replace('\\begin{columns}[T]\n', '\\begin{columns}[T]\n\\scriptsize\n')

    if content != original:
        tex_path.write_text(content, encoding='utf-8')
        return True
    return False


def check_overflows(tex_path):
    """Count overflow warnings for a tex file"""
    result = subprocess.run(
        ['pdflatex', '-interaction=nonstopmode', str(tex_path)],
        cwd=tex_path.parent,
        capture_output=True,
        text=True,
        timeout=60
    )
    output = result.stdout + result.stderr
    return output.lower().count('overfull')


def main():
    print("=" * 70)
    print("FIXING OVERFLOW WARNINGS")
    print("=" * 70)

    fixed_count = 0
    for module, lesson in LESSONS_WITH_OVERFLOW:
        tex_path = BASE / module / lesson
        if tex_path.exists():
            if fix_overflow(tex_path):
                fixed_count += 1
                print(f'Fixed: {lesson}')
            else:
                print(f'No changes needed: {lesson}')

    print(f'\nTotal files modified: {fixed_count}')

    # Verify fixes
    print("\n" + "=" * 70)
    print("VERIFYING FIXES")
    print("=" * 70)

    remaining_issues = []
    for module, lesson in LESSONS_WITH_OVERFLOW:
        tex_path = BASE / module / lesson
        if tex_path.exists():
            overflows = check_overflows(tex_path)
            if overflows > 0:
                remaining_issues.append((lesson, overflows))
                print(f'{lesson}: {overflows} overflows remaining')
            else:
                print(f'{lesson}: OK')

    print("\n" + "=" * 70)
    if remaining_issues:
        print(f"SUMMARY: {len(remaining_issues)} lessons still have overflows")
    else:
        print("SUCCESS: All overflows fixed!")
    print("=" * 70)


if __name__ == '__main__':
    main()
