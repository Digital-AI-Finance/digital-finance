"""
Master Script to Run All Demo Scripts

This script executes all 9 demonstration scripts in sequence and generates
a summary report.

Author: BSc Digital Finance Course
Date: 2025-12-07
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime

# Define all demo scripts
DEMOS = [
    # Module 2: Blockchain
    ("Module 2: Hash Demonstration",
     "module_02_blockchain/hash_demonstration/hash_demonstration.py"),
    ("Module 2: Block Structure",
     "module_02_blockchain/block_structure/block_structure_viz.py"),
    ("Module 2: Impermanent Loss",
     "module_02_blockchain/impermanent_loss/defi_impermanent_loss.py"),

    # Module 3: AI/ML
    ("Module 3: Linear Regression",
     "module_03_ai_ml/linear_regression/linear_regression_demo.py"),
    ("Module 3: Classification",
     "module_03_ai_ml/classification/classification_demo.py"),
    ("Module 3: Sentiment Analysis",
     "module_03_ai_ml/sentiment/sentiment_analysis_demo.py"),
    ("Module 3: VaR Calculation",
     "module_03_ai_ml/var_calculation/var_calculation.py"),

    # Module 4: Traditional Finance
    ("Module 4: Order Book",
     "module_04_traditional/order_book/order_book_simulation.py"),
    ("Module 4: Efficient Frontier",
     "module_04_traditional/efficient_frontier/portfolio_efficient_frontier.py"),
]

def run_demo(name, script_path):
    """Run a single demo script and return status."""
    print(f"\n{'='*70}")
    print(f"Running: {name}")
    print(f"Script: {script_path}")
    print(f"{'='*70}")

    script_full_path = Path(__file__).parent / script_path

    if not script_full_path.exists():
        print(f"ERROR: Script not found at {script_full_path}")
        return False

    try:
        # Run the script
        result = subprocess.run(
            [sys.executable, str(script_full_path)],
            capture_output=True,
            text=True,
            timeout=120  # 2 minute timeout per script
        )

        # Print output
        if result.stdout:
            print(result.stdout)

        if result.stderr:
            print("STDERR:", result.stderr)

        if result.returncode == 0:
            print(f"SUCCESS: {name}")
            return True
        else:
            print(f"FAILED: {name} (exit code {result.returncode})")
            return False

    except subprocess.TimeoutExpired:
        print(f"TIMEOUT: {name} took longer than 2 minutes")
        return False
    except Exception as e:
        print(f"ERROR: {name} - {str(e)}")
        return False

def main():
    """Run all demo scripts and generate summary."""
    print("="*70)
    print("BSc DIGITAL FINANCE - DEMO SCRIPT EXECUTOR")
    print("="*70)
    print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total scripts to run: {len(DEMOS)}")

    results = []
    start_time = datetime.now()

    # Run each demo
    for name, script_path in DEMOS:
        success = run_demo(name, script_path)
        results.append((name, script_path, success))

    end_time = datetime.now()
    duration = end_time - start_time

    # Print summary
    print("\n" + "="*70)
    print("EXECUTION SUMMARY")
    print("="*70)

    successful = sum(1 for _, _, success in results if success)
    failed = len(results) - successful

    print(f"\nTotal scripts: {len(results)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Success rate: {successful/len(results)*100:.1f}%")
    print(f"Total execution time: {duration.total_seconds():.1f} seconds")

    print("\nDetailed Results:")
    print("-"*70)
    for name, script_path, success in results:
        status = "PASS" if success else "FAIL"
        print(f"[{status}] {name}")

    if failed > 0:
        print("\nFailed scripts:")
        for name, script_path, success in results:
            if not success:
                print(f"  - {name}: {script_path}")

    print("\n" + "="*70)
    print(f"End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)

    # Return exit code
    return 0 if failed == 0 else 1

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
