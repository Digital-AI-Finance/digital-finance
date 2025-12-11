"""
List all missing figure files in Module 02 lessons.
"""
import re
from pathlib import Path
from collections import defaultdict

BASE = Path(r'D:\Joerg\Research\slides\DigitalFinance_3\module_02_blockchain')
FIGURES_DIR = BASE / 'figures'


def main():
    missing_figures = []
    lessons = sorted(BASE.glob('lesson_*.tex'))

    for tex_path in lessons:
        content = tex_path.read_text(encoding='utf-8')

        pattern = r'\\includegraphics.*?\{([^}]+)\}'
        for match in re.finditer(pattern, content):
            fig_path = match.group(1)

            if not fig_path.endswith('.pdf'):
                fig_path_pdf = fig_path + '.pdf'
            else:
                fig_path_pdf = fig_path

            full_path = BASE / fig_path_pdf

            if not full_path.exists():
                fig_name = Path(fig_path).stem
                missing_figures.append({
                    'lesson': tex_path.name,
                    'figure': fig_path,
                    'name': fig_name,
                })

    print(f"Found {len(missing_figures)} missing figures:\n")

    by_lesson = defaultdict(list)
    for fig in missing_figures:
        by_lesson[fig['lesson']].append(fig['name'])

    for lesson, figs in sorted(by_lesson.items()):
        print(f"{lesson}: {len(figs)} missing")
        for f in figs:
            print(f"  - {f}")
        print()

    unique_names = sorted(set(f['name'] for f in missing_figures))
    print(f"\nUnique figures to generate: {len(unique_names)}")

    return missing_figures, unique_names


if __name__ == '__main__':
    missing, unique = main()
