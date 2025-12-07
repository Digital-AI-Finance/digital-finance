# Quick Start Guide - Python Demo Scripts

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

Required packages: numpy, scipy, matplotlib

## Running Individual Scripts

Navigate to any script folder and run:

```bash
# Example: Hash Demonstration
cd module_02_blockchain/hash_demonstration
python hash_demonstration.py
```

Output PDF will be saved in the same directory.

## Running All Scripts

Execute all 9 demos at once:

```bash
python run_all_demos.py
```

This will run all scripts sequentially and provide a summary report.

## Script Locations

### Module 2: Blockchain (3 scripts)

```bash
module_02_blockchain/hash_demonstration/hash_demonstration.py
module_02_blockchain/block_structure/block_structure_viz.py
module_02_blockchain/impermanent_loss/defi_impermanent_loss.py
```

### Module 3: AI/ML (4 scripts)

```bash
module_03_ai_ml/linear_regression/linear_regression_demo.py
module_03_ai_ml/classification/classification_demo.py
module_03_ai_ml/sentiment/sentiment_analysis_demo.py
module_03_ai_ml/var_calculation/var_calculation.py
```

### Module 4: Traditional Finance (2 scripts)

```bash
module_04_traditional/order_book/order_book_simulation.py
module_04_traditional/efficient_frontier/portfolio_efficient_frontier.py
```

## Expected Outputs

Each script produces:
- Publication-quality PDF (300 DPI)
- Detailed console output with statistics
- Reproducible results (fixed random seeds)

## Typical Execution Times

- Individual scripts: 3-7 seconds each
- All scripts together: ~50 seconds total

## Troubleshooting

If a script fails:
1. Check that all dependencies are installed
2. Verify Python version (3.8+)
3. Check file paths (should run from script directory or use absolute paths)
4. Review console output for specific error messages

## For Instructors

- Scripts are observational demos (students watch)
- Each demo takes 2-5 minutes to run and explain
- Console output includes educational explanations
- All visualizations use grayscale-friendly colors
- No external data or API keys required

## File Structure After Running

```
python_demos/
├── module_02_blockchain/
│   ├── hash_demonstration/
│   │   ├── hash_demonstration.py
│   │   └── hash_demonstration.pdf  (generated)
│   └── ...
├── module_03_ai_ml/
│   └── ...
└── module_04_traditional/
    └── ...
```

## Documentation

- README.md - Detailed documentation of all scripts
- SCRIPT_SUMMARY.md - Execution summary with output statistics
- QUICK_START.md - This file
- requirements.txt - Python dependencies

## Support

For questions or issues, refer to:
1. Individual script docstrings (at top of each .py file)
2. README.md for detailed descriptions
3. SCRIPT_SUMMARY.md for expected outputs
