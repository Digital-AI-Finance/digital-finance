# BSc Digital Finance - Python Demonstration Scripts

This repository contains observational demonstration scripts for the BSc Digital Finance course, organized by module.

## Overview

All scripts are self-contained, runnable with `python script.py`, and produce publication-quality PDF outputs. They use grayscale-friendly color schemes suitable for both digital display and print.

## Directory Structure

```
python_demos/
├── module_02_blockchain/
│   ├── hash_demonstration/
│   ├── block_structure/
│   └── impermanent_loss/
├── module_03_ai_ml/
│   ├── linear_regression/
│   ├── classification/
│   ├── sentiment/
│   └── var_calculation/
└── module_04_traditional/
    ├── order_book/
    └── efficient_frontier/
```

## Requirements

- Python 3.8+
- matplotlib
- numpy
- scipy

Install dependencies:
```bash
pip install -r requirements.txt
```

## Module 2: Blockchain

### 1. Hash Demonstration
**File:** `module_02_blockchain/hash_demonstration/hash_demonstration.py`

Demonstrates the SHA-256 avalanche effect - how small input changes produce drastically different hash outputs.

**Output:** Hamming distance chart and binary hash visualization

**Run:**
```bash
cd module_02_blockchain/hash_demonstration
python hash_demonstration.py
```

### 2. Block Structure Visualization
**File:** `module_02_blockchain/block_structure/block_structure_viz.py`

Visualizes how blocks are cryptographically linked in a blockchain.

**Output:** Block chain linking diagram with hash connections

**Run:**
```bash
cd module_02_blockchain/block_structure
python block_structure_viz.py
```

### 3. Impermanent Loss Calculator
**File:** `module_02_blockchain/impermanent_loss/defi_impermanent_loss.py`

Demonstrates impermanent loss in DeFi automated market makers (AMMs).

**Output:** IL curves and LP vs HODL comparison

**Run:**
```bash
cd module_02_blockchain/impermanent_loss
python defi_impermanent_loss.py
```

## Module 3: AI/ML

### 4. Linear Regression Demo
**File:** `module_03_ai_ml/linear_regression/linear_regression_demo.py`

Simple linear regression on market cap vs returns with residual analysis.

**Output:** Scatter plot with regression line and residual diagnostics

**Run:**
```bash
cd module_03_ai_ml/linear_regression
python linear_regression_demo.py
```

### 5. Classification Demo
**File:** `module_03_ai_ml/classification/classification_demo.py`

Binary classification for credit default prediction with confusion matrix.

**Output:** Decision boundary visualization and confusion matrix

**Run:**
```bash
cd module_03_ai_ml/classification
python classification_demo.py
```

### 6. Sentiment Analysis
**File:** `module_03_ai_ml/sentiment/sentiment_analysis_demo.py`

Rule-based sentiment analysis on financial news headlines.

**Output:** Sentiment scores over time and distribution analysis

**Run:**
```bash
cd module_03_ai_ml/sentiment
python sentiment_analysis_demo.py
```

### 7. VaR Calculation
**File:** `module_03_ai_ml/var_calculation/var_calculation.py`

Historical Value at Risk (VaR) calculation on simulated returns.

**Output:** Return distribution with VaR thresholds and portfolio scenarios

**Run:**
```bash
cd module_03_ai_ml/var_calculation
python var_calculation.py
```

## Module 4: Traditional Finance

### 8. Order Book Simulation
**File:** `module_04_traditional/order_book/order_book_simulation.py`

Simulates a limit order book and visualizes market depth.

**Output:** Order book depth chart and cumulative liquidity

**Run:**
```bash
cd module_04_traditional/order_book
python order_book_simulation.py
```

### 9. Efficient Frontier
**File:** `module_04_traditional/efficient_frontier/portfolio_efficient_frontier.py`

Modern Portfolio Theory - calculates and visualizes the efficient frontier.

**Output:** Efficient frontier with optimal portfolios

**Run:**
```bash
cd module_04_traditional/efficient_frontier
python portfolio_efficient_frontier.py
```

## Design Specifications

All visualizations follow these standards:
- Font size: 8pt (publication quality)
- Color scheme: Grayscale-friendly (prints well in B&W)
- Output format: PDF at 300 DPI
- Resolution: High-resolution for academic publications
- Style: Clean, minimal, information-dense

## Usage Notes

1. Each script is completely self-contained
2. All scripts use fixed random seeds for reproducibility
3. Outputs are saved in the same directory as the script
4. Scripts include detailed console output explaining results
5. No external data files required - all data is synthetic

## Author

BSc Digital Finance Course
Date: 2025-12-07
