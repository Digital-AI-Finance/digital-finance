"""
Compile all LaTeX lesson slides to PDF
Handles 48 lessons across 4 modules with automatic temp file cleanup
"""

import subprocess
from pathlib import Path
import re
from datetime import datetime

def find_lesson_files(base_dir):
    """Find all lesson_*.tex files in module folders"""
    lessons = []
    modules = [
        'module_01_fintech',
        'module_02_blockchain',
        'module_03_ai_ml',
        'module_04_traditional'
    ]

    for module in modules:
        module_path = base_dir / module
        if module_path.exists():
            # Find all *lesson_*.tex files (with timestamps)
            lesson_files = sorted(module_path.glob('*lesson_*.tex'))
            for lesson_file in lesson_files:
                lessons.append({
                    'path': lesson_file,
                    'module': module,
                    'name': lesson_file.stem
                })

    return lessons

def compile_latex(tex_file):
    """Compile a single LaTeX file to PDF"""
    work_dir = tex_file.parent

    # Run pdflatex twice for proper references
    for run in range(2):
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-output-directory=.', tex_file.name],
            cwd=work_dir,
            capture_output=True,
            text=True,
            timeout=60
        )

    # Check if PDF was created
    pdf_file = tex_file.with_suffix('.pdf')
    success = pdf_file.exists()

    return success, result.stdout, result.stderr

def move_temp_files(tex_file):
    """Move temporary LaTeX files to temp/ subfolder"""
    work_dir = tex_file.parent
    temp_dir = work_dir / 'temp'
    temp_dir.mkdir(exist_ok=True)

    # Temporary file extensions to move
    temp_extensions = ['.aux', '.log', '.nav', '.snm', '.toc', '.out', '.vrb']

    moved_files = []
    for ext in temp_extensions:
        temp_file = tex_file.with_suffix(ext)
        if temp_file.exists():
            dest = temp_dir / temp_file.name
            temp_file.rename(dest)
            moved_files.append(temp_file.name)

    return moved_files

def main():
    base_dir = Path(__file__).parent

    print("="*80)
    print("COMPILING ALL DIGITAL FINANCE LESSON SLIDES")
    print("="*80)
    print(f"Base directory: {base_dir}")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Find all lesson files
    lessons = find_lesson_files(base_dir)
    print(f"Found {len(lessons)} lesson files to compile")
    print()

    # Track results
    results = {
        'success': [],
        'failed': [],
        'errors': {}
    }

    # Compile each lesson
    for i, lesson in enumerate(lessons, 1):
        tex_file = lesson['path']
        module = lesson['module']
        name = lesson['name']

        print(f"[{i}/{len(lessons)}] Compiling {module}/{name}.tex ... ", end='', flush=True)

        try:
            success, stdout, stderr = compile_latex(tex_file)

            if success:
                # Move temp files
                moved = move_temp_files(tex_file)
                print(f"SUCCESS (moved {len(moved)} temp files)")
                results['success'].append(f"{module}/{name}")
            else:
                print("FAILED")
                results['failed'].append(f"{module}/{name}")
                # Extract error from log
                error_lines = [line for line in stdout.split('\n') if 'error' in line.lower()]
                results['errors'][f"{module}/{name}"] = error_lines[:5] if error_lines else ["Unknown error"]

        except subprocess.TimeoutExpired:
            print("TIMEOUT")
            results['failed'].append(f"{module}/{name}")
            results['errors'][f"{module}/{name}"] = ["Compilation timeout (>60s)"]
        except Exception as e:
            print(f"ERROR: {str(e)}")
            results['failed'].append(f"{module}/{name}")
            results['errors'][f"{module}/{name}"] = [str(e)]

    # Print summary
    print()
    print("="*80)
    print("COMPILATION SUMMARY")
    print("="*80)
    print(f"Total files: {len(lessons)}")
    print(f"Successful: {len(results['success'])}")
    print(f"Failed: {len(results['failed'])}")
    print()

    if results['success']:
        print("SUCCESSFUL COMPILATIONS:")
        for lesson in results['success']:
            print(f"  ✓ {lesson}")
        print()

    if results['failed']:
        print("FAILED COMPILATIONS:")
        for lesson in results['failed']:
            print(f"  ✗ {lesson}")
            if lesson in results['errors']:
                for error in results['errors'][lesson]:
                    print(f"      {error}")
        print()

    # Generate detailed report
    report_file = base_dir / f"compilation_report_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("DIGITAL FINANCE LESSON SLIDES - COMPILATION REPORT\n")
        f.write("="*80 + "\n")
        f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total files: {len(lessons)}\n")
        f.write(f"Successful: {len(results['success'])}\n")
        f.write(f"Failed: {len(results['failed'])}\n\n")

        if results['success']:
            f.write("SUCCESSFUL COMPILATIONS:\n")
            for lesson in results['success']:
                f.write(f"  ✓ {lesson}\n")
            f.write("\n")

        if results['failed']:
            f.write("FAILED COMPILATIONS:\n")
            for lesson in results['failed']:
                f.write(f"  ✗ {lesson}\n")
                if lesson in results['errors']:
                    for error in results['errors'][lesson]:
                        f.write(f"      {error}\n")
            f.write("\n")

    print(f"Detailed report saved to: {report_file}")
    print()

    return len(results['success']), len(results['failed'])

if __name__ == '__main__':
    success_count, failed_count = main()
    exit(0 if failed_count == 0 else 1)
