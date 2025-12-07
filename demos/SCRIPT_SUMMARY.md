# Python Demo Scripts - Execution Summary

All 9 demonstration scripts have been successfully created and tested.

## Execution Status

| Module | Script | Status | Output |
|--------|--------|--------|--------|
| 2 - Blockchain | hash_demonstration.py | PASS | hash_demonstration.pdf |
| 2 - Blockchain | block_structure_viz.py | PASS | block_structure_viz.pdf |
| 2 - Blockchain | defi_impermanent_loss.py | PASS | defi_impermanent_loss.pdf |
| 3 - AI/ML | linear_regression_demo.py | PASS | linear_regression_demo.pdf |
| 3 - AI/ML | classification_demo.py | PASS | classification_demo.pdf |
| 3 - AI/ML | sentiment_analysis_demo.py | PASS | sentiment_analysis_demo.pdf |
| 3 - AI/ML | var_calculation.py | PASS | var_calculation.pdf |
| 4 - Traditional | order_book_simulation.py | PASS | order_book_simulation.pdf |
| 4 - Traditional | portfolio_efficient_frontier.py | PASS | portfolio_efficient_frontier.pdf |

## Key Features

All scripts include:
- Self-contained execution (no external data required)
- Fixed random seeds for reproducibility
- Publication-quality PDF output at 300 DPI
- Grayscale-friendly visualizations (print-safe)
- Font size: 8pt throughout
- Detailed console output with explanations
- Clear docstrings and comments
- Educational focus (observational demos)

## Script Highlights

### Module 2: Blockchain

1. **Hash Demonstration** - Shows avalanche effect with 256-bit binary visualization
2. **Block Structure** - Visual representation of blockchain linking with 4 blocks
3. **Impermanent Loss** - DeFi IL calculator with comparison to HODL strategy

### Module 3: AI/ML

4. **Linear Regression** - Market cap vs returns with residual diagnostics
5. **Classification** - Credit default prediction with confusion matrix
6. **Sentiment Analysis** - Rule-based sentiment on 15 financial headlines
7. **VaR Calculation** - Historical VaR with CVaR and portfolio scenarios

### Module 4: Traditional Finance

8. **Order Book** - Limit order book depth with market impact analysis
9. **Efficient Frontier** - MPT with 4 assets and optimal portfolio weights

## Dependencies

- numpy >= 1.21.0
- scipy >= 1.7.0
- matplotlib >= 3.4.0

Install: `pip install -r requirements.txt`

## Directory Structure

```
python_demos/
├── README.md
├── requirements.txt
├── SCRIPT_SUMMARY.md
├── module_02_blockchain/
│   ├── hash_demonstration/
│   │   ├── hash_demonstration.py
│   │   └── hash_demonstration.pdf
│   ├── block_structure/
│   │   ├── block_structure_viz.py
│   │   └── block_structure_viz.pdf
│   └── impermanent_loss/
│       ├── defi_impermanent_loss.py
│       └── defi_impermanent_loss.pdf
├── module_03_ai_ml/
│   ├── linear_regression/
│   │   ├── linear_regression_demo.py
│   │   └── linear_regression_demo.pdf
│   ├── classification/
│   │   ├── classification_demo.py
│   │   └── classification_demo.pdf
│   ├── sentiment/
│   │   ├── sentiment_analysis_demo.py
│   │   └── sentiment_analysis_demo.pdf
│   └── var_calculation/
│       ├── var_calculation.py
│       └── var_calculation.pdf
└── module_04_traditional/
    ├── order_book/
    │   ├── order_book_simulation.py
    │   └── order_book_simulation.pdf
    └── efficient_frontier/
        ├── portfolio_efficient_frontier.py
        └── portfolio_efficient_frontier.pdf
```

## Sample Output Statistics

### Hash Demonstration
- Demonstrates avalanche effect on 5 input variations
- Shows Hamming distances ranging from 0 to 138 bits changed
- Visualizes binary patterns for first 128 bits

### Block Structure
- Creates 4-block blockchain (Genesis + 3 transaction blocks)
- Each block contains 16-character hash (shortened for display)
- Shows cryptographic linking between consecutive blocks

### Impermanent Loss
- Calculates IL for price ratios from 0.1x to 10x
- Key examples: 2x price change = 5.72% IL, 5x = 25.46% IL
- Compares LP returns vs HODL strategy

### Linear Regression
- 100 synthetic data points (market cap vs returns)
- R-squared: 0.547 (moderate fit)
- Shows negative correlation (size effect)

### Classification
- 500 samples (80% non-default, 20% default)
- Achieves 77% accuracy with simple rule-based classifier
- High recall (89%) but lower precision (46%)

### Sentiment Analysis
- Analyzes 15 financial headlines
- Distribution: 47% positive, 40% negative, 13% neutral
- Uses simple lexicon-based approach

### VaR Calculation
- 1000 days of synthetic returns with fat tails
- 95% VaR: 2.45% daily loss on $1M portfolio = $24,462
- Shows VaR vs CVaR comparison

### Order Book
- 20 price levels each side
- Bid-ask spread: $0.20 (0.20%)
- 8,000+ shares total liquidity
- Market impact analysis for 6 order sizes

### Efficient Frontier
- 4 assets with realistic correlations
- 5000 random portfolios plotted
- Min variance portfolio: 8.41% return, 10.16% vol
- Max Sharpe: 0.89 (bond-heavy allocation)

## Usage Instructions

Each script can be run independently:

```bash
cd python_demos/module_0X_name/script_folder
python script_name.py
```

Output PDF will be saved in the same directory.

## Notes for Instructors

- All scripts are observational (students watch, do not code)
- Each takes 2-5 minutes to run and explain
- Console output includes educational explanations
- PDFs suitable for inclusion in slides
- No API keys or external data required
- Synthetic data clearly labeled as [SYNTHETIC] where applicable
