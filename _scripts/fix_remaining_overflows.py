"""
Fix remaining overflow issues in specific lessons.
More aggressive width reductions for problematic frames.
"""
import re
from pathlib import Path

BASE = Path(r'D:\Joerg\Research\slides\DigitalFinance_3\module_01_fintech')


def fix_lesson_03():
    """Fix remaining overflows in lesson_03_mobile_wallets.tex"""
    tex_path = BASE / 'lesson_03_mobile_wallets.tex'
    content = tex_path.read_text(encoding='utf-8')

    fixes = [
        # Apple Pay Architecture - reduce from 0.72 to 0.65
        (r'includegraphics\[width=0\.72\\textwidth\]\{figures/apple_pay_flow',
         r'includegraphics[width=0.65\\textwidth]{figures/apple_pay_flow'),
        # M-Pesa Ecosystem - reduce from 0.75 to 0.65
        (r'includegraphics\[width=0\.75\\textwidth\]\{figures/mpesa_ecosystem',
         r'includegraphics[width=0.65\\textwidth]{figures/mpesa_ecosystem'),
        # QR vs NFC - reduce from 0.68 to 0.62
        (r'includegraphics\[width=0\.68\\textwidth\]\{figures/qr_vs_nfc',
         r'includegraphics[width=0.62\\textwidth]{figures/qr_vs_nfc'),
        # Global wallet share - reduce from 0.72 to 0.60
        (r'includegraphics\[width=0\.72\\textwidth\]\{figures/global_wallet_share',
         r'includegraphics[width=0.58\\textwidth]{figures/global_wallet_share'),
        # Mobile wallet security - reduce from 0.70 to 0.62
        (r'includegraphics\[width=0\.70\\textwidth\]\{figures/mobile_wallet_security',
         r'includegraphics[width=0.62\\textwidth]{figures/mobile_wallet_security'),
    ]

    for pattern, replacement in fixes:
        content = re.sub(pattern, replacement, content)

    tex_path.write_text(content, encoding='utf-8')
    print(f"Fixed: lesson_03_mobile_wallets.tex")


def fix_lesson_12():
    """Fix remaining overflow in lesson_12_business_models.tex"""
    tex_path = BASE / 'lesson_12_business_models.tex'
    content = tex_path.read_text(encoding='utf-8')

    fixes = [
        # Network effects types - reduce
        (r'includegraphics\[width=0\.72\\textwidth\]\{figures/network_effects_types',
         r'includegraphics[width=0.62\\textwidth]{figures/network_effects_types'),
    ]

    for pattern, replacement in fixes:
        content = re.sub(pattern, replacement, content)

    tex_path.write_text(content, encoding='utf-8')
    print(f"Fixed: lesson_12_business_models.tex")


def main():
    print("=" * 70)
    print("FIXING REMAINING OVERFLOW ISSUES")
    print("=" * 70)

    fix_lesson_03()
    fix_lesson_12()

    print("\n" + "=" * 70)
    print("DONE - Re-run analyze_overflow_detailed.py to verify")
    print("=" * 70)


if __name__ == '__main__':
    main()
