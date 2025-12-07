"""
Generate remaining 10 lessons (27-36) for Module 3: AI/ML in Finance
Comprehensive LaTeX Beamer presentations
"""

from pathlib import Path
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M")
base_dir = Path(__file__).parent

PREAMBLE = r"""\documentclass[8pt,aspectratio=169]{beamer}
\usetheme{Madrid}
\usepackage{graphicx,booktabs,adjustbox,multicol,amsmath,amssymb}
\definecolor{mlblue}{RGB}{0,102,204}
\definecolor{mlpurple}{RGB}{51,51,178}
\definecolor{mllavender}{RGB}{173,173,224}
\definecolor{mllavender2}{RGB}{193,193,232}
\definecolor{mllavender3}{RGB}{204,204,235}
\definecolor{mllavender4}{RGB}{214,214,239}
\definecolor{mlorange}{RGB}{255,127,14}
\definecolor{mlgreen}{RGB}{44,160,44}
\definecolor{mlred}{RGB}{214,39,40}
\setbeamercolor{palette primary}{bg=mllavender3,fg=mlpurple}
\setbeamercolor{palette secondary}{bg=mllavender2,fg=mlpurple}
\setbeamercolor{palette tertiary}{bg=mllavender,fg=white}
\setbeamercolor{structure}{fg=mlpurple}
\setbeamercolor{frametitle}{fg=mlpurple,bg=mllavender3}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{itemize items}[circle]
\setbeamersize{text margin left=5mm,text margin right=5mm}
"""

# Lesson 27: Supervised Learning - Regression
lesson_27 = PREAMBLE + r"""
\title{Digital Finance 3: Technology in Finance}
\subtitle{Lesson 27: Supervised Learning - Regression}
\author{FHGR}
\date{\today}

\begin{document}

\begin{frame}
\titlepage
\end{frame}

\begin{frame}{Learning Objectives}
By the end of this lesson, you will be able to:
\begin{itemize}
\item Explain the supervised learning paradigm (features, labels, training)
\item Understand simple and multiple linear regression
\item Interpret regression coefficients in financial contexts
\item Evaluate model performance using R-squared and related metrics
\item Recognize overfitting and apply regularization techniques
\item Identify finance applications of regression models
\end{itemize}
\end{frame}

\begin{frame}{Supervised Learning: The Framework}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Core Idea:}
\begin{itemize}
\item Learn from labeled examples
\item \textbf{Training data:} $(X_1, Y_1), (X_2, Y_2), \ldots, (X_n, Y_n)$
\item $X$ = features (inputs, predictors)
\item $Y$ = label (output, target)
\item Goal: Learn function $f: X \to Y$
\end{itemize}

\vspace{0.5em}
\textbf{Two Types:}
\begin{enumerate}
\item \textcolor{mlblue}{\textbf{Regression:}} Predict continuous $Y$ (today's lesson)
\item \textcolor{mlpurple}{\textbf{Classification:}} Predict discrete $Y$ (next lesson)
\end{enumerate}

\column{0.48\textwidth}
\textbf{Finance Example (Regression):}
\begin{itemize}
\item Features $X$: Company financials (P/E, ROE, Size)
\item Label $Y$: Next-month stock return
\item Training: Historical data (2000-2020)
\item Test: Predict 2021 returns
\end{itemize}

\vspace{0.5em}
\textbf{Key Steps:}
\begin{enumerate}
\item Collect labeled data
\item Split: Train (70\%), Validation (15\%), Test (15\%)
\item Train model on training set
\item Tune on validation set
\item Evaluate on test set (never seen before)
\end{enumerate}
\end{columns}

\vspace{0.5em}
\textbf{Golden Rule:} Never use test data until final evaluation (avoid overfitting).
\end{frame}

\begin{frame}{Simple Linear Regression: The Basics}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Model:}
\[
Y = \beta_0 + \beta_1 X + \epsilon
\]
\begin{itemize}
\item $Y$: Dependent variable (target)
\item $X$: Independent variable (feature)
\item $\beta_0$: Intercept (value when $X=0$)
\item $\beta_1$: Slope (change in $Y$ per unit $X$)
\item $\epsilon$: Error term (residual)
\end{itemize}

\vspace{0.5em}
\textbf{Goal:} Find $\beta_0, \beta_1$ that minimize errors.

\vspace{0.5em}
\textbf{Method:} Ordinary Least Squares (OLS)
\[
\min_{\beta_0, \beta_1} \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2
\]
where $\hat{Y}_i = \beta_0 + \beta_1 X_i$

\column{0.48\textwidth}
\textbf{Finance Example:}\\
Predict stock return ($Y$) from P/E ratio ($X$).

\vspace{0.3em}
Suppose OLS gives:
\[
\text{Return} = 0.05 - 0.002 \times \text{P/E}
\]

\textbf{Interpretation:}
\begin{itemize}
\item Intercept (0.05): Expected 5\% return for P/E = 0 (extrapolation, not meaningful)
\item Slope (-0.002): Each 1-point increase in P/E decreases expected return by 0.2\%
\item Negative relationship: Higher P/E (expensive) → lower return (value effect)
\end{itemize}

\vspace{0.5em}
\textbf{Limitations:}
\begin{itemize}
\item Assumes linear relationship
\item Single predictor (oversimplified)
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Multiple Linear Regression}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Model:}
\[
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_p X_p + \epsilon
\]
\begin{itemize}
\item Multiple features: $X_1, X_2, \ldots, X_p$
\item Each $\beta_j$: Partial effect (holding others constant)
\item OLS still minimizes squared errors
\end{itemize}

\vspace{0.5em}
\textbf{Matrix Form:}
\[
Y = X \beta + \epsilon
\]
\[
\hat{\beta} = (X^T X)^{-1} X^T Y
\]

\column{0.48\textwidth}
\textbf{Finance Example:}\\
Predict stock return from:
\begin{itemize}
\item $X_1$: P/E ratio
\item $X_2$: Debt/Equity
\item $X_3$: Market cap (log)
\item $X_4$: Past 12-month return (momentum)
\end{itemize}

\vspace{0.3em}
Estimated model:
\begin{align*}
\text{Return} = 0.03 &- 0.001 \times \text{P/E} \\
&- 0.015 \times \text{D/E} \\
&+ 0.002 \times \log(\text{Size}) \\
&+ 0.12 \times \text{Mom}
\end{align*}

\textbf{Interpretation:}
\begin{itemize}
\item Momentum (0.12): Strongest predictor
\item Debt (-0.015): Financial risk reduces returns
\item Size (+0.002): Weak positive effect
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Assumptions of Linear Regression}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Five Key Assumptions:}
\begin{enumerate}
\item \textbf{Linearity:} Relationship is linear
\item \textbf{Independence:} Observations are independent
\item \textbf{Homoscedasticity:} Constant error variance
\item \textbf{Normality:} Errors normally distributed
\item \textbf{No multicollinearity:} Features not perfectly correlated
\end{enumerate}

\vspace{0.5em}
\textbf{Diagnostics:}
\begin{itemize}
\item Residual plots (linearity, homoscedasticity)
\item QQ plots (normality)
\item Variance Inflation Factor (VIF) for multicollinearity
\end{itemize}

\column{0.48\textwidth}
\textbf{Violations in Finance:}
\begin{itemize}
\item \textbf{Non-linearity:} Returns vs. ratios often non-linear
\item \textbf{Heteroscedasticity:} Volatility clustering (GARCH effects)
\item \textbf{Autocorrelation:} Time series dependence
\item \textbf{Multicollinearity:} Related accounting ratios
\end{itemize}

\vspace{0.5em}
\textbf{Remedies:}
\begin{itemize}
\item Transformations (log, square root)
\item Robust standard errors (White, Newey-West)
\item Feature selection (remove correlated vars)
\item Non-linear models (polynomial, GAM)
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Bottom Line:} Regression is robust, but severe violations reduce reliability.
\end{frame}

\begin{frame}{Evaluating Regression Models: R-squared}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{R-squared ($R^2$):}
\[
R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = 1 - \frac{\sum (Y_i - \hat{Y}_i)^2}{\sum (Y_i - \bar{Y})^2}
\]
\begin{itemize}
\item Proportion of variance explained
\item Range: $[0, 1]$ (higher is better)
\item $R^2 = 0$: Model no better than mean
\item $R^2 = 1$: Perfect fit (suspicious!)
\end{itemize}

\vspace{0.5em}
\textbf{Interpretation:}
\begin{itemize}
\item $R^2 = 0.25$: Model explains 25\% of variance
\item Remaining 75\%: Unexplained (noise, other factors)
\end{itemize}

\column{0.48\textwidth}
\textbf{Adjusted R-squared:}
\[
R^2_{adj} = 1 - (1-R^2) \frac{n-1}{n-p-1}
\]
\begin{itemize}
\item Penalizes adding features
\item Use when comparing models with different $p$
\end{itemize}

\vspace{0.5em}
\textbf{Typical $R^2$ in Finance:}
\begin{itemize}
\item Stock return prediction: 0.02-0.10 (very noisy)
\item Bond yield modeling: 0.70-0.95 (more predictable)
\item Credit spreads: 0.40-0.60
\end{itemize}

\vspace{0.5em}
\textbf{Warning:}
\begin{itemize}
\item High $R^2$ doesn't mean good out-of-sample performance
\item Can overfit to training data
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Other Regression Metrics}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Mean Absolute Error (MAE):}
\[
MAE = \frac{1}{n} \sum_{i=1}^{n} |Y_i - \hat{Y}_i|
\]
\begin{itemize}
\item Average absolute prediction error
\item Same units as $Y$ (interpretable)
\item Robust to outliers
\end{itemize}

\vspace{0.5em}
\textbf{Root Mean Squared Error (RMSE):}
\[
RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2}
\]
\begin{itemize}
\item Penalizes large errors more (squared)
\item Same units as $Y$
\item Most common in ML
\end{itemize}

\column{0.48\textwidth}
\textbf{Mean Absolute Percentage Error (MAPE):}
\[
MAPE = \frac{100\%}{n} \sum_{i=1}^{n} \left| \frac{Y_i - \hat{Y}_i}{Y_i} \right|
\]
\begin{itemize}
\item Percentage error (scale-free)
\item Problematic if $Y_i$ near zero
\end{itemize}

\vspace{0.5em}
\textbf{Which to Use?}
\begin{itemize}
\item RMSE: Standard choice (differentiable, penalizes outliers)
\item MAE: If outliers less important
\item MAPE: Comparing models across different scales
\item $R^2$: Variance explanation (interpretability)
\end{itemize}

\vspace{0.5em}
\textbf{Key:} Always evaluate on held-out test set.
\end{columns}
\end{frame}

\begin{frame}{Overfitting: The Central Problem in ML}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{What is Overfitting?}
\begin{itemize}
\item Model learns training data too well
\item Captures noise, not signal
\item Poor generalization to new data
\end{itemize}

\vspace{0.5em}
\textbf{Symptoms:}
\begin{itemize}
\item High training $R^2$ (0.95), low test $R^2$ (0.20)
\item Complex model (many features)
\item Unstable coefficients
\end{itemize}

\vspace{0.5em}
\textbf{Causes:}
\begin{itemize}
\item Too many features relative to observations ($p \approx n$)
\item Features without predictive power
\item Overly flexible models
\item Lack of regularization
\end{itemize}

\column{0.48\textwidth}
\textbf{Bias-Variance Tradeoff:}
\[
\text{Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Error}
\]
\begin{itemize}
\item \textbf{Bias:} Error from wrong assumptions (underfitting)
\item \textbf{Variance:} Error from sensitivity to training data (overfitting)
\item Simple models: High bias, low variance
\item Complex models: Low bias, high variance
\end{itemize}

\vspace{0.5em}
\textbf{Goal:} Find sweet spot (minimize total error).

\vspace{0.5em}
\textbf{Detection:}
\begin{itemize}
\item Plot training vs. validation error
\item Cross-validation
\item Out-of-sample testing
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Regularization: Ridge and Lasso}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Idea:} Penalize large coefficients to reduce overfitting.

\vspace{0.5em}
\textbf{Ridge Regression (L2):}
\[
\min_{\beta} \sum_{i=1}^{n} (Y_i - X_i \beta)^2 + \lambda \sum_{j=1}^{p} \beta_j^2
\]
\begin{itemize}
\item Penalty: Sum of squared coefficients
\item Shrinks coefficients toward zero
\item All features retained (no feature selection)
\item $\lambda$: Regularization strength (tune via CV)
\end{itemize}

\vspace{0.5em}
\textbf{Effect:}
\begin{itemize}
\item Reduces variance (less overfitting)
\item Increases bias (slightly)
\item Handles multicollinearity well
\end{itemize}

\column{0.48\textwidth}
\textbf{Lasso Regression (L1):}
\[
\min_{\beta} \sum_{i=1}^{n} (Y_i - X_i \beta)^2 + \lambda \sum_{j=1}^{p} |\beta_j|
\]
\begin{itemize}
\item Penalty: Sum of absolute coefficients
\item Sets some $\beta_j$ exactly to zero (feature selection)
\item Sparse solutions (interpretable)
\end{itemize}

\vspace{0.5em}
\textbf{Elastic Net:}
\[
\text{Penalty} = \lambda_1 \sum |\beta_j| + \lambda_2 \sum \beta_j^2
\]
\begin{itemize}
\item Combines L1 and L2
\item Best of both worlds
\end{itemize}

\vspace{0.5em}
\textbf{Choosing $\lambda$:}
\begin{itemize}
\item Cross-validation (grid search)
\item Higher $\lambda$ → more regularization
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Cross-Validation}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Why Cross-Validation?}
\begin{itemize}
\item Estimate out-of-sample performance
\item Tune hyperparameters (e.g., $\lambda$)
\item Maximize use of limited data
\end{itemize}

\vspace{0.5em}
\textbf{K-Fold Cross-Validation:}
\begin{enumerate}
\item Split data into $K$ folds (typically 5 or 10)
\item For each fold $k$:
  \begin{itemize}
  \item Train on $K-1$ folds
  \item Validate on fold $k$
  \end{itemize}
\item Average performance across folds
\end{enumerate}

\vspace{0.5em}
\textbf{Advantages:}
\begin{itemize}
\item All data used for training and validation
\item Reduces variance of performance estimate
\end{itemize}

\column{0.48\textwidth}
\textbf{Leave-One-Out CV (LOOCV):}
\begin{itemize}
\item $K = n$ (extreme case)
\item Train on $n-1$, test on 1
\item Computationally expensive
\item Low bias, high variance
\end{itemize}

\vspace{0.5em}
\textbf{Time Series CV:}
\begin{itemize}
\item Cannot randomly shuffle (temporal order)
\item Use expanding or rolling windows
\item Example: Train on 2000-2010, test on 2011; train on 2000-2011, test on 2012; etc.
\end{itemize}

\vspace{0.5em}
\textbf{Best Practice:}
\begin{itemize}
\item Use CV for model selection
\item Reserve separate test set for final evaluation
\item Never use test set for tuning
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Feature Engineering for Regression}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Transformations:}
\begin{itemize}
\item \textbf{Log:} $\log(Y)$ or $\log(X)$ (skewed distributions)
\item \textbf{Polynomial:} $X, X^2, X^3$ (capture non-linearity)
\item \textbf{Interactions:} $X_1 \times X_2$ (joint effects)
\item \textbf{Binning:} Convert continuous to categorical
\end{itemize}

\vspace{0.5em}
\textbf{Finance-Specific:}
\begin{itemize}
\item Ratios: P/E, P/B, ROE, Debt/Equity
\item Momentum: Past returns (1-month, 12-month)
\item Volatility: Rolling standard deviation
\item Technical indicators: MA, RSI, MACD
\end{itemize}

\column{0.48\textwidth}
\textbf{Normalization:}
\begin{itemize}
\item \textbf{Standardization:} $(X - \mu) / \sigma$ (mean 0, std 1)
\item \textbf{Min-Max:} $(X - X_{min}) / (X_{max} - X_{min})$ (range [0,1])
\item Important for regularization (features on same scale)
\end{itemize}

\vspace{0.5em}
\textbf{Lag Variables (Time Series):}
\begin{itemize}
\item $Y_{t-1}, Y_{t-2}, \ldots$ (autoregressive)
\item Moving averages
\item Seasonal indicators
\end{itemize}

\vspace{0.5em}
\textbf{Avoid:}
\begin{itemize}
\item Leakage (using future info)
\item Perfectly correlated features
\item Too many features (curse of dimensionality)
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Finance Application: Stock Return Prediction}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Problem Setup:}
\begin{itemize}
\item Target: Next-month stock return
\item Features: Fundamentals, technical, macro
\item Data: Monthly, 1990-2020
\item Universe: S\&P 500 stocks
\end{itemize}

\vspace{0.5em}
\textbf{Feature Categories:}
\begin{enumerate}
\item \textbf{Value:} P/E, P/B, dividend yield
\item \textbf{Momentum:} Past 12-month return
\item \textbf{Quality:} ROE, profit margin, accruals
\item \textbf{Size:} Market cap (log)
\item \textbf{Volatility:} 60-day std dev
\end{enumerate}

\column{0.48\textwidth}
\textbf{Model Comparison:}
\begin{itemize}
\item OLS: $R^2 = 0.04$ (test)
\item Ridge ($\lambda=10$): $R^2 = 0.06$
\item Lasso ($\lambda=0.1$): $R^2 = 0.07$ (selected 12/30 features)
\end{itemize}

\vspace{0.5em}
\textbf{Key Findings:}
\begin{itemize}
\item Momentum strongest predictor ($\beta = 0.15$)
\item P/B negative ($\beta = -0.03$) - value effect
\item Low overall $R^2$ (markets are noisy)
\item Lasso improves via feature selection
\end{itemize}

\vspace{0.5em}
\textbf{Reality Check:}
\begin{itemize}
\item Transaction costs erode small edges
\item Out-of-sample performance lower
\item Regime shifts (models break in crises)
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Finance Application: Bond Yield Curve Modeling}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Problem:}
\begin{itemize}
\item Predict bond yields at various maturities
\item Features: Macro variables, term structure factors
\item More predictable than stocks
\end{itemize}

\vspace{0.5em}
\textbf{Nelson-Siegel Model (Parametric):}
\[
Y(m) = \beta_1 + \beta_2 e^{-m/\tau} + \beta_3 \frac{m}{\tau} e^{-m/\tau}
\]
\begin{itemize}
\item $\beta_1$: Long-term level
\item $\beta_2$: Short-term component
\item $\beta_3$: Curvature
\item $m$: Maturity, $\tau$: Decay parameter
\end{itemize}

\column{0.48\textwidth}
\textbf{ML Approach (Non-Parametric):}
\begin{itemize}
\item Features: GDP growth, inflation, Fed Funds rate, VIX, yield spreads
\item Target: 10-year Treasury yield
\item Ridge regression: $R^2 = 0.82$ (test)
\end{itemize}

\vspace{0.5em}
\textbf{Key Predictors:}
\begin{itemize}
\item Fed Funds rate ($\beta = 0.65$)
\item Inflation expectations ($\beta = 0.42$)
\item 2-year yield ($\beta = 0.58$)
\end{itemize}

\vspace{0.5em}
\textbf{Use Cases:}
\begin{itemize}
\item Portfolio allocation
\item Hedging interest rate risk
\item Trading strategies (carry, curve)
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Finance Application: Real Estate Valuation}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Problem:}
\begin{itemize}
\item Predict property sale price
\item Features: Size, location, age, amenities
\item Traditional: Hedonic pricing models
\end{itemize}

\vspace{0.5em}
\textbf{Features:}
\begin{itemize}
\item Square footage
\item Number of bedrooms, bathrooms
\item Lot size
\item Age of property
\item Zip code (location proxy)
\item School quality, crime rates
\item Distance to CBD, transit
\end{itemize}

\column{0.48\textwidth}
\textbf{Model:}
\[
\log(\text{Price}) = \beta_0 + \beta_1 \log(\text{SqFt}) + \beta_2 \text{Beds} + \cdots
\]
\begin{itemize}
\item Log-log form: Elasticities
\item Ridge to handle multicollinearity (correlated location vars)
\end{itemize}

\vspace{0.5em}
\textbf{Results:}
\begin{itemize}
\item $R^2 = 0.75$ (typical)
\item Square footage: $\beta = 0.6$ (10\% increase in size → 6\% price increase)
\item Extra bedroom: +\$20k
\end{itemize}

\vspace{0.5em}
\textbf{Applications:}
\begin{itemize}
\item Automated valuation models (AVMs) - Zillow Zestimate
\item Mortgage underwriting
\item Investment property analysis
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Limitations of Linear Regression}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{When Regression Fails:}
\begin{itemize}
\item Non-linear relationships (interactions, thresholds)
\item High-dimensional data ($p \gg n$)
\item Complex feature interactions
\item Heavy-tailed distributions (outliers)
\item Non-stationary data (regime changes)
\end{itemize}

\vspace{0.5em}
\textbf{Example:}\\
Stock returns vs. market cap:
\begin{itemize}
\item Small-cap premium (non-linear)
\item January effect (seasonality)
\item Crisis periods (structural breaks)
\end{itemize}

Linear regression assumes constant relationship, which breaks.

\column{0.48\textwidth}
\textbf{Alternatives:}
\begin{itemize}
\item \textbf{Polynomial regression:} Add $X^2, X^3$ terms
\item \textbf{Generalized Additive Models (GAM):} Smooth non-linear functions
\item \textbf{Tree-based methods:} Random Forests, Gradient Boosting (later lessons)
\item \textbf{Neural networks:} Deep learning (later lessons)
\end{itemize}

\vspace{0.5em}
\textbf{Trade-offs:}
\begin{itemize}
\item Linear: Simple, interpretable, fast
\item Non-linear: Flexible, accurate, complex
\end{itemize}

\vspace{0.5em}
\textbf{Best Practice:}
\begin{itemize}
\item Start with linear (baseline)
\item If poor fit, try non-linear
\item Balance accuracy vs. interpretability
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Practical Tips for Regression in Finance}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Data Preparation:}
\begin{itemize}
\item Winsorize outliers (1st-99th percentile)
\item Check for multicollinearity (VIF < 10)
\item Normalize features (especially for regularization)
\item Handle missing data carefully
\end{itemize}

\vspace{0.5em}
\textbf{Model Selection:}
\begin{itemize}
\item Start simple (OLS)
\item Add regularization (Ridge/Lasso)
\item Use cross-validation for $\lambda$
\item Check residual diagnostics
\end{itemize}

\vspace{0.5em}
\textbf{Avoid Common Mistakes:}
\begin{itemize}
\item Look-ahead bias (using future data)
\item Overfitting (too many features)
\item Ignoring transaction costs
\item Extrapolation beyond data range
\end{itemize}

\column{0.48\textwidth}
\textbf{Interpretation:}
\begin{itemize}
\item Report coefficients with confidence intervals
\item Economic significance > statistical significance
\item Explain magnitude in practical terms
\end{itemize}

\vspace{0.5em}
\textbf{Validation:}
\begin{itemize}
\item Out-of-sample testing (time series: walk-forward)
\item Robustness checks (different time periods, subsamples)
\item Benchmark against simple models (mean, random walk)
\end{itemize}

\vspace{0.5em}
\textbf{Communication:}
\begin{itemize}
\item Visualize predictions vs. actuals
\item Report multiple metrics ($R^2$, RMSE, MAE)
\item Acknowledge limitations
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Summary and Key Takeaways}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Core Concepts:}
\begin{itemize}
\item Supervised learning: Learn from labeled data
\item Linear regression: $Y = X\beta + \epsilon$
\item OLS minimizes squared errors
\item Multiple regression: Multiple predictors
\end{itemize}

\vspace{0.5em}
\textbf{Evaluation:}
\begin{itemize}
\item $R^2$: Variance explained
\item RMSE, MAE: Prediction error
\item Always test out-of-sample
\end{itemize}

\column{0.48\textwidth}
\textbf{Overfitting:}
\begin{itemize}
\item Central problem in ML
\item Regularization (Ridge, Lasso) helps
\item Cross-validation for tuning
\end{itemize}

\vspace{0.5em}
\textbf{Finance Applications:}
\begin{itemize}
\item Stock returns (low $R^2$, noisy)
\item Bond yields (higher $R^2$, predictable)
\item Real estate (moderate $R^2$)
\item Limitations: Non-linearity, regime changes
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Next Lesson Preview}
\textbf{Lesson 28: Supervised Learning - Classification}

\vspace{0.5em}
Topics to be covered:
\begin{itemize}
\item Logistic regression (binary classification)
\item Decision boundaries and probabilities
\item Confusion matrix (TP, FP, TN, FN)
\item Accuracy, precision, recall, F1-score
\item ROC curves and AUC
\item Applications: Credit default, fraud detection
\end{itemize}

\vspace{1em}
\textbf{Preparation:}
\begin{itemize}
\item Review probability basics (odds, log-odds)
\item Think: What financial problems involve yes/no predictions?
\end{itemize}
\end{frame}

\end{document}
"""

# Save Lesson 27
filepath_27 = base_dir / f"{timestamp}_lesson_27_regression.tex"
filepath_27.write_text(lesson_27, encoding='utf-8')
print(f"Created: {filepath_27}")

print("\nLesson 27/36 complete. Continuing with lessons 28-36...")
