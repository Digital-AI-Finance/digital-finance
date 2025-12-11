"""
List all missing figure files in Module 01 lessons.
"""
import re
from pathlib import Path
from collections import defaultdict

BASE = Path(r'D:\Joerg\Research\slides\DigitalFinance_3\module_01_fintech')
FIGURES_DIR = BASE / 'figures'

LESSONS = [
    'lesson_03_mobile_wallets.tex',
    'lesson_04_neobanks.tex',
    'lesson_05_open_banking.tex',
    'lesson_06_digital_identity.tex',
    'lesson_07_p2p_lending.tex',
    'lesson_08_robo_advisors.tex',
    'lesson_09_insurtech.tex',
    'lesson_10_regtech.tex',
    'lesson_11_regulatory_frameworks.tex',
    'lesson_12_business_models.tex',
]


def main():
    missing_figures = []

    for lesson in LESSONS:
        tex_path = BASE / lesson
        content = tex_path.read_text(encoding='utf-8')

        # Find all includegraphics references using raw string
        pattern = r'\\includegraphics.*?\{([^}]+)\}'
        for match in re.finditer(pattern, content):
            fig_path = match.group(1)

            # Build full path
            if not fig_path.endswith('.pdf'):
                fig_path_pdf = fig_path + '.pdf'
            else:
                fig_path_pdf = fig_path

            full_path = BASE / fig_path_pdf

            if not full_path.exists():
                # Extract figure name for folder creation
                fig_name = Path(fig_path).stem
                missing_figures.append({
                    'lesson': lesson,
                    'figure': fig_path,
                    'name': fig_name,
                    'folder': str(FIGURES_DIR / fig_name)
                })

    print(f"Found {len(missing_figures)} missing figures:\n")

    # Group by lesson
    by_lesson = defaultdict(list)
    for fig in missing_figures:
        by_lesson[fig['lesson']].append(fig['name'])

    for lesson, figs in sorted(by_lesson.items()):
        print(f"{lesson}: {len(figs)} missing")
        for f in figs:
            print(f"  - {f}")
        print()

    # Output unique figure names for generation
    unique_names = sorted(set(f['name'] for f in missing_figures))
    print(f"\nUnique figures to generate: {len(unique_names)}")
    for name in unique_names:
        print(f"  {name}")

    return missing_figures, unique_names


if __name__ == '__main__':
    missing, unique = main()
