"""
Generate all 12 Beamer slide decks for Module 3: AI and Machine Learning in Finance
"""

import os
from datetime import datetime

# Get timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M")

# Base directory
base_dir = r"D:\Joerg\Research\slides\DigitalFinance_3\module_03_ai_ml"

# Lesson definitions
lessons = [
    {
        "number": 25,
        "slug": "intro_ai_ml",
        "title": "Introduction to AI and Machine Learning",
        "subtitle": "Concepts, Definitions, and Financial Applications",
        "sections": [
            ("What is Artificial Intelligence?", [
                "Definition: Systems that mimic human intelligence",
                "Narrow AI vs. General AI (AGI)",
                "Machine Learning as a subset of AI",
                "Deep Learning as a subset of ML"
            ]),
            ("What is Machine Learning?", [
                "Learning from data without explicit programming",
                "Key components: Data, Algorithm, Model, Prediction",
                "Supervised vs. Unsupervised vs. Reinforcement Learning",
                "Training, Validation, Testing phases"
            ]),
            ("AI/ML Hierarchy", [
                "Artificial Intelligence (broadest)",
                "Machine Learning (data-driven)",
                "Deep Learning (neural networks)",
                "Financial applications at each level"
            ]),
            ("Applications in Finance", [
                "Credit scoring and risk assessment",
                "Fraud detection and AML",
                "Algorithmic trading",
                "Portfolio management",
                "Customer service (chatbots)",
                "Document processing and NLP"
            ]),
            ("Hype vs. Reality", [
                "Common misconceptions about AI",
                "What ML can do well in finance",
                "What ML cannot do (yet)",
                "Realistic expectations and limitations"
            ])
        ],
        "charts": [
            "AI/ML/DL hierarchy diagram (Venn diagram)",
            "ML workflow: Data → Training → Model → Prediction",
            "Supervised vs. Unsupervised learning comparison",
            "Finance AI applications by category",
            "Gartner Hype Cycle for AI in Finance"
        ]
    },
    {
        "number": 26,
        "slug": "financial_data",
        "title": "Financial Data for Machine Learning",
        "subtitle": "Types, Sources, Quality, and Privacy",
        "sections": [
            ("Structured vs. Unstructured Data", [
                "Structured: Tabular data (prices, transactions, balances)",
                "Semi-structured: JSON, XML (API responses)",
                "Unstructured: Text (news, reports), Images, Audio",
                "Challenges of each type for ML"
            ]),
            ("Data Sources in Finance", [
                "Market data (exchanges, Bloomberg, Reuters)",
                "Transactional data (banks, payment processors)",
                "Alternative data (social media, satellite, credit cards)",
                "Open data vs. Proprietary data"
            ]),
            ("Data Quality Issues", [
                "Missing values and imputation strategies",
                "Outliers and anomalies",
                "Data biases (survivorship bias, selection bias)",
                "Temporal aspects (time series, non-stationarity)"
            ]),
            ("GDPR and Privacy Regulations", [
                "Personal data protection requirements",
                "Right to explanation for automated decisions",
                "Data minimization and purpose limitation",
                "Anonymization vs. Pseudonymization",
                "Consent and data subject rights"
            ]),
            ("Data Preparation Best Practices", [
                "Exploratory Data Analysis (EDA)",
                "Feature engineering and selection",
                "Normalization and scaling",
                "Train/validation/test split strategies",
                "Handling imbalanced datasets"
            ])
        ],
        "charts": [
            "Data types pyramid (structured to unstructured)",
            "Financial data sources ecosystem",
            "Missing data visualization (heatmap)",
            "GDPR compliance workflow diagram",
            "Train/validation/test split illustration"
        ]
    },
    {
        "number": 27,
        "slug": "supervised_regression",
        "title": "Supervised Learning: Regression",
        "subtitle": "Predicting Continuous Outcomes in Finance",
        "sections": [
            ("Regression Fundamentals", [
                "Definition: Predicting continuous numerical values",
                "Features (X) and target variable (y)",
                "Training vs. Prediction phases",
                "Examples: Stock price prediction, property valuation"
            ]),
            ("Linear Regression", [
                "Model: y = β₀ + β₁x₁ + β₂x₂ + ... + ε",
                "Ordinary Least Squares (OLS) method",
                "Assumptions: Linearity, independence, normality",
                "Coefficients interpretation in finance"
            ]),
            ("Model Evaluation Metrics", [
                "R-squared (R²): Proportion of variance explained",
                "Mean Squared Error (MSE) and RMSE",
                "Mean Absolute Error (MAE)",
                "When to use which metric"
            ]),
            ("Financial Applications", [
                "Asset price forecasting",
                "Credit limit determination",
                "Portfolio return prediction",
                "Real estate valuation (hedonic pricing)",
                "Interest rate modeling"
            ]),
            ("Limitations and Extensions", [
                "Non-linear relationships (polynomial regression)",
                "Multicollinearity issues",
                "Ridge and Lasso regularization",
                "Time series specific considerations"
            ])
        ],
        "charts": [
            "Simple linear regression scatter plot with fitted line",
            "Multiple regression feature importance",
            "R-squared interpretation diagram",
            "Residual plot for diagnostics",
            "Ridge vs. Lasso regularization effect"
        ]
    },
    {
        "number": 28,
        "slug": "supervised_classification",
        "title": "Supervised Learning: Classification",
        "subtitle": "Predicting Categorical Outcomes in Finance",
        "sections": [
            ("Classification Fundamentals", [
                "Definition: Predicting categorical labels/classes",
                "Binary classification (2 classes) vs. Multi-class",
                "Examples: Default/No default, Buy/Hold/Sell",
                "Decision boundaries and class probabilities"
            ]),
            ("Logistic Regression", [
                "Despite the name, it's for classification",
                "Sigmoid function: σ(z) = 1/(1+e⁻ᶻ)",
                "Probability interpretation: P(y=1|x)",
                "Coefficients and odds ratios"
            ]),
            ("Confusion Matrix", [
                "True Positives (TP), True Negatives (TN)",
                "False Positives (FP), False Negatives (FN)",
                "Visual representation of prediction quality",
                "Cost-sensitive classification in finance"
            ]),
            ("Performance Metrics", [
                "Accuracy: (TP+TN) / Total",
                "Precision: TP / (TP+FP) - quality of positives",
                "Recall (Sensitivity): TP / (TP+FN) - coverage",
                "F1-Score: Harmonic mean of precision and recall",
                "ROC curve and AUC"
            ]),
            ("Financial Applications", [
                "Credit default prediction",
                "Fraud detection (transaction classification)",
                "Customer churn prediction",
                "Market regime classification",
                "Trading signal generation (buy/sell/hold)"
            ])
        ],
        "charts": [
            "Logistic regression sigmoid curve",
            "Confusion matrix heatmap",
            "Precision vs. Recall trade-off",
            "ROC curve with AUC score",
            "Classification decision boundary visualization"
        ]
    },
    {
        "number": 29,
        "slug": "algorithmic_trading",
        "title": "Algorithmic Trading Concepts",
        "subtitle": "Strategy Development, Backtesting, and Pitfalls",
        "sections": [
            ("What is Algorithmic Trading?", [
                "Automated execution of trading strategies",
                "Rule-based vs. ML-based strategies",
                "High-frequency trading (HFT) vs. Lower frequency",
                "Market making, arbitrage, trend following"
            ]),
            ("Strategy Components", [
                "Signal generation (entry/exit rules)",
                "Position sizing and risk management",
                "Order execution logic",
                "Performance monitoring and adjustment"
            ]),
            ("Backtesting Framework", [
                "Historical data simulation",
                "Transaction costs and slippage",
                "Rolling window validation",
                "Out-of-sample testing importance"
            ]),
            ("Common Pitfalls", [
                "Overfitting: Memorizing noise instead of patterns",
                "Look-ahead bias: Using future information",
                "Survivorship bias: Only using current assets",
                "Data snooping: Testing too many strategies",
                "Ignoring market impact and liquidity"
            ]),
            ("Performance Metrics", [
                "Sharpe ratio: Risk-adjusted returns",
                "Maximum drawdown: Largest peak-to-trough decline",
                "Win rate and profit factor",
                "Calmar ratio and Sortino ratio"
            ])
        ],
        "charts": [
            "Algorithmic trading workflow diagram",
            "Backtesting framework illustration",
            "Overfitting example (train vs. test performance)",
            "Equity curve with drawdown visualization",
            "Sharpe ratio comparison across strategies"
        ]
    },
    {
        "number": 30,
        "slug": "credit_scoring",
        "title": "Credit Scoring and Risk Models",
        "subtitle": "Traditional vs. ML Approaches, Fairness, Regulation",
        "sections": [
            ("Traditional Credit Scoring", [
                "FICO score and credit bureaus",
                "Linear scoring models (weighted sum)",
                "Key features: Payment history, utilization, length",
                "Limitations: Limited data, static rules"
            ]),
            ("ML-Based Credit Scoring", [
                "Logistic regression, decision trees, ensemble methods",
                "Alternative data sources (mobile, social, geolocation)",
                "Non-linear patterns and interactions",
                "Real-time updates and adaptive scoring"
            ]),
            ("Feature Importance", [
                "Which variables drive credit risk?",
                "Permutation importance and SHAP values",
                "Domain knowledge vs. Data-driven features",
                "Regulatory requirements for explanations"
            ]),
            ("Fairness and Bias", [
                "Protected attributes (race, gender, age)",
                "Disparate impact and statistical parity",
                "Fair lending laws (Equal Credit Opportunity Act)",
                "Balancing accuracy and fairness"
            ]),
            ("EBA Guidelines and Regulation", [
                "European Banking Authority ML guidelines",
                "Model validation and governance",
                "Stress testing and scenario analysis",
                "Documentation and auditability requirements"
            ])
        ],
        "charts": [
            "Traditional vs. ML credit scoring comparison",
            "Feature importance ranking chart",
            "Fairness metrics visualization (demographic parity)",
            "Credit score distribution by risk tier",
            "Model governance workflow diagram"
        ]
    },
    {
        "number": 31,
        "slug": "fraud_detection",
        "title": "Fraud Detection and AML",
        "subtitle": "Anomaly Detection, Imbalanced Data, Network Analysis",
        "sections": [
            ("Fraud Detection Challenges", [
                "Rare events: <1% of transactions are fraudulent",
                "Imbalanced data impact on ML models",
                "Evolving fraud patterns (adversarial behavior)",
                "Real-time detection requirements"
            ]),
            ("Anomaly Detection Methods", [
                "Supervised: Classification with labeled fraud cases",
                "Unsupervised: Isolation Forest, One-Class SVM",
                "Statistical outlier detection (z-score, IQR)",
                "Time series anomalies (sudden spikes)"
            ]),
            ("Handling Imbalanced Data", [
                "Resampling: Oversampling (SMOTE) and undersampling",
                "Cost-sensitive learning (higher penalty for fraud)",
                "Ensemble methods (boosting minority class)",
                "Evaluation metrics for imbalanced data (Precision-Recall)"
            ]),
            ("Network Analysis for AML", [
                "Anti-Money Laundering (AML) regulations",
                "Transaction graph networks",
                "Community detection for suspicious clusters",
                "Flow analysis and layering detection"
            ]),
            ("False Positives Trade-off", [
                "Cost of false alarms (manual review burden)",
                "Cost of missed fraud (financial loss)",
                "Precision vs. Recall optimization",
                "Human-in-the-loop systems"
            ])
        ],
        "charts": [
            "Imbalanced dataset visualization (class distribution)",
            "Anomaly detection scatter plot (outliers highlighted)",
            "Precision-Recall curve for fraud detection",
            "Transaction network graph (money laundering)",
            "False positive rate impact on operations"
        ]
    },
    {
        "number": 32,
        "slug": "nlp_finance",
        "title": "Natural Language Processing in Finance",
        "subtitle": "Sentiment Analysis, NER, Chatbots, Document Processing",
        "sections": [
            ("NLP Fundamentals", [
                "Text as unstructured data",
                "Tokenization, stemming, lemmatization",
                "Bag-of-words vs. Word embeddings",
                "Pre-trained models (BERT, GPT)"
            ]),
            ("Sentiment Analysis", [
                "Extracting sentiment from news, social media, reports",
                "Polarity: Positive, Negative, Neutral",
                "Financial sentiment dictionaries (Loughran-McDonald)",
                "Impact on stock prices and trading signals"
            ]),
            ("Named Entity Recognition (NER)", [
                "Identifying companies, people, locations, dates",
                "Extracting financial entities (ticker symbols, amounts)",
                "Relationship extraction (mergers, partnerships)",
                "Applications in news analysis and compliance"
            ]),
            ("Chatbots and Virtual Assistants", [
                "Customer service automation",
                "Intent classification and entity extraction",
                "Dialog management and conversational flow",
                "Integration with banking systems"
            ]),
            ("Document Processing", [
                "Automated contract analysis",
                "Financial report extraction (10-K, earnings calls)",
                "Regulatory document classification",
                "Optical Character Recognition (OCR) for scanned docs"
            ])
        ],
        "charts": [
            "NLP pipeline: Text → Tokenization → Embedding → Model",
            "Sentiment analysis word cloud (positive vs. negative)",
            "NER example annotation (tagged entities)",
            "Chatbot architecture diagram",
            "Document processing workflow"
        ]
    },
    {
        "number": 33,
        "slug": "robo_advisors",
        "title": "Robo-Advisors: ML Aspects",
        "subtitle": "Portfolio Optimization, Mean-Variance, Rebalancing",
        "sections": [
            ("What are Robo-Advisors?", [
                "Automated investment platforms",
                "Low-cost, algorithm-driven portfolio management",
                "Target audience: Retail investors, small portfolios",
                "Examples: Betterment, Wealthfront, Vanguard Digital Advisor"
            ]),
            ("Portfolio Optimization", [
                "Goal: Maximize return for given risk (or vice versa)",
                "Asset allocation based on investor profile",
                "Modern Portfolio Theory (Markowitz)",
                "Constraints: Minimum investment, asset limits"
            ]),
            ("Efficient Frontier", [
                "Risk-return trade-off curve",
                "Optimal portfolios along the frontier",
                "Selecting portfolio based on risk tolerance",
                "Capital Market Line and risk-free asset"
            ]),
            ("Mean-Variance Optimization", [
                "Expected return: E[Rₚ] = Σ wᵢE[Rᵢ]",
                "Portfolio variance: σₚ² = Σ Σ wᵢwⱼσᵢⱼ",
                "Optimization: Minimize risk for target return",
                "Limitations: Estimation errors, non-normal returns"
            ]),
            ("Rebalancing Strategies", [
                "Time-based rebalancing (monthly, quarterly)",
                "Threshold-based rebalancing (drift tolerance)",
                "Tax-loss harvesting optimization",
                "Transaction cost considerations"
            ])
        ],
        "charts": [
            "Robo-advisor workflow diagram",
            "Efficient frontier curve with optimal portfolios",
            "Mean-variance optimization scatter plot",
            "Asset allocation pie chart example",
            "Rebalancing drift illustration over time"
        ]
    },
    {
        "number": 34,
        "slug": "market_prediction",
        "title": "Market Prediction Limitations",
        "subtitle": "EMH, Signal-to-Noise, Overfitting, Realistic Expectations",
        "sections": [
            ("Efficient Market Hypothesis (EMH)", [
                "Weak form: Prices reflect past information",
                "Semi-strong: Prices reflect all public information",
                "Strong form: Prices reflect all information (public + private)",
                "Implications for predictability"
            ]),
            ("Signal-to-Noise Ratio", [
                "Financial markets are inherently noisy",
                "True predictive signal is weak",
                "Random walk hypothesis",
                "Why most predictions fail"
            ]),
            ("Overfitting in Market Prediction", [
                "Fitting noise instead of true patterns",
                "In-sample vs. Out-of-sample performance gap",
                "Parameter tuning on test data (data snooping)",
                "Model complexity and degrees of freedom"
            ]),
            ("Look-Ahead Bias", [
                "Using future information in historical analysis",
                "Common mistakes: Adjusted prices, survivorship",
                "Point-in-time data requirements",
                "Realistic backtesting practices"
            ]),
            ("Realistic Expectations", [
                "No model can consistently predict markets",
                "Best models provide small edge, not certainty",
                "Risk management more important than prediction",
                "Focus on process, not outcomes",
                "Behavioral factors and regime changes"
            ])
        ],
        "charts": [
            "EMH implications diagram (information levels)",
            "Signal-to-noise ratio visualization (true pattern vs. noise)",
            "Overfitting illustration (train vs. test error)",
            "Look-ahead bias example timeline",
            "Realistic prediction accuracy distribution"
        ]
    },
    {
        "number": 35,
        "slug": "explainability_bias",
        "title": "Explainability and Bias in ML",
        "subtitle": "Black Box Problem, SHAP, LIME, Fairness, Ethics",
        "sections": [
            ("The Black Box Problem", [
                "Complex models (neural networks, ensembles) are opaque",
                "Regulatory requirements for explainability",
                "Trust and adoption challenges",
                "Trade-off: Accuracy vs. Interpretability"
            ]),
            ("SHAP (SHapley Additive exPlanations)", [
                "Game theory approach to feature attribution",
                "Shapley values: Fair distribution of prediction",
                "Local explanations (per prediction)",
                "Global feature importance aggregation"
            ]),
            ("LIME (Local Interpretable Model-agnostic Explanations)", [
                "Approximating black box locally with simple model",
                "Perturbing inputs to understand sensitivity",
                "Instance-level explanations",
                "Model-agnostic (works for any ML model)"
            ]),
            ("Fairness Metrics", [
                "Demographic parity: Equal outcomes across groups",
                "Equalized odds: Equal error rates across groups",
                "Individual fairness: Similar individuals treated similarly",
                "Trade-offs between fairness criteria"
            ]),
            ("Ethical Considerations", [
                "Bias in training data perpetuates discrimination",
                "Feedback loops amplifying bias",
                "Transparency and accountability requirements",
                "Human oversight and contestability",
                "Social impact of AI in finance"
            ])
        ],
        "charts": [
            "Interpretability vs. Accuracy trade-off curve",
            "SHAP waterfall plot example",
            "LIME local explanation visualization",
            "Fairness metrics comparison table",
            "Bias feedback loop diagram"
        ]
    },
    {
        "number": 36,
        "slug": "ai_regulation",
        "title": "AI Regulation and Future Trends",
        "subtitle": "EU AI Act, High-Risk AI, LLMs, Generative AI",
        "sections": [
            ("EU AI Act Overview", [
                "Risk-based regulatory framework",
                "Unacceptable risk: Banned AI practices",
                "High-risk AI: Strict requirements (credit scoring, hiring)",
                "Limited risk: Transparency obligations",
                "Minimal risk: No specific regulation"
            ]),
            ("High-Risk AI in Finance", [
                "Credit scoring and loan approval systems",
                "Insurance underwriting and pricing",
                "Portfolio management and investment advice",
                "Requirements: Risk management, data quality, transparency",
                "Conformity assessments and CE marking"
            ]),
            ("Compliance Requirements", [
                "Technical documentation and record-keeping",
                "Human oversight and intervention capability",
                "Robustness, accuracy, and cybersecurity",
                "Post-market monitoring and incident reporting"
            ]),
            ("Large Language Models (LLMs)", [
                "Foundation models: GPT, Claude, LLaMA",
                "Applications in finance: Document analysis, chatbots",
                "Challenges: Hallucinations, bias, data privacy",
                "Regulatory considerations for general-purpose AI"
            ]),
            ("Generative AI in Finance", [
                "Synthetic data generation for training",
                "Report writing and summarization",
                "Code generation for quants",
                "Risks: Misinformation, IP concerns, copyright",
                "Future trends: Agentic AI, multi-modal models"
            ])
        ],
        "charts": [
            "EU AI Act risk pyramid (unacceptable to minimal)",
            "High-risk AI compliance workflow",
            "LLM architecture overview (simplified)",
            "Generative AI use cases in finance",
            "AI regulation timeline (global comparison)"
        ]
    }
]

# LaTeX preamble template
preamble = r"""\documentclass[8pt,aspectratio=169]{beamer}
\usetheme{Madrid}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{adjustbox}
\usepackage{multicol}
\usepackage{amsmath}
\usepackage{amssymb}

\definecolor{mlblue}{RGB}{0,102,204}
\definecolor{mlpurple}{RGB}{51,51,178}
\definecolor{mllavender}{RGB}{173,173,224}
\definecolor{mllavender2}{RGB}{193,193,232}
\definecolor{mllavender3}{RGB}{204,204,235}
\definecolor{mllavender4}{RGB}{214,214,239}
\definecolor{mlorange}{RGB}{255, 127, 14}
\definecolor{mlgreen}{RGB}{44, 160, 44}
\definecolor{mlred}{RGB}{214, 39, 40}

\setbeamercolor{palette primary}{bg=mllavender3,fg=mlpurple}
\setbeamercolor{palette secondary}{bg=mllavender2,fg=mlpurple}
\setbeamercolor{palette tertiary}{bg=mllavender,fg=white}
\setbeamercolor{structure}{fg=mlpurple}
\setbeamercolor{frametitle}{fg=mlpurple,bg=mllavender3}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{itemize items}[circle]
\setbeamersize{text margin left=5mm,text margin right=5mm}

"""

# Helper function to create chart placeholder
def chart_frame(title, description, size="5.5cm"):
    return f"""\\begin{{frame}}[t]{{{title}}}
\\begin{{center}}
\\framebox[0.9\\textwidth][c]{{
\\rule{{0pt}}{{{size}}}
\\textcolor{{gray}}{{[Chart: {description}]}}
}}
\\end{{center}}
\\end{{frame}}

"""

# Generate each lesson
for lesson in lessons:
    filename = f"{timestamp}_lesson_{lesson['number']:02d}_{lesson['slug']}.tex"
    filepath = os.path.join(base_dir, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        # Write preamble
        f.write(preamble)

        # Write title info
        f.write(f"\\title{{Lesson {lesson['number']}: {lesson['title']}}}\n")
        f.write(f"\\subtitle{{{lesson['subtitle']}}}\n")
        f.write("\\author{Digital Finance Course}\n")
        f.write("\\institute{FHGR}\n")
        f.write("\\date{\\today}\n\n")

        f.write("\\begin{document}\n\n")

        # Title slide
        f.write("% Title Slide\n")
        f.write("\\begin{frame}[plain]\n")
        f.write("\\titlepage\n")
        f.write("\\end{frame}\n\n")

        # Generate content sections
        for section_title, bullet_points in lesson['sections']:
            f.write(f"% Section: {section_title}\n")
            f.write(f"\\begin{{frame}}[t]{{{section_title}}}\n")

            # Two-column layout for better space utilization
            if len(bullet_points) > 4:
                mid = len(bullet_points) // 2
                f.write("\\begin{columns}[T]\n")
                f.write("\\column{0.48\\textwidth}\n")
                f.write("\\begin{itemize}\n")
                for bp in bullet_points[:mid]:
                    f.write(f"\\item {bp}\n")
                f.write("\\end{itemize}\n\n")
                f.write("\\column{0.48\\textwidth}\n")
                f.write("\\begin{itemize}\n")
                for bp in bullet_points[mid:]:
                    f.write(f"\\item {bp}\n")
                f.write("\\end{itemize}\n")
                f.write("\\end{columns}\n")
            else:
                f.write("\\begin{itemize}\n")
                for bp in bullet_points:
                    f.write(f"\\item {bp}\n")
                f.write("\\end{itemize}\n")

            f.write("\\end{frame}\n\n")

        # Add chart slides
        f.write("% Chart Slides\n")
        for chart_desc in lesson['charts']:
            chart_title = chart_desc.split('(')[0].strip()
            f.write(f"\\begin{{frame}}[t]{{{chart_title}}}\n")
            f.write("\\begin{center}\n")
            f.write("\\framebox[0.9\\textwidth][c]{\n")
            f.write("\\rule{0pt}{5.5cm}\n")
            f.write(f"\\textcolor{{gray}}{{[Chart: {chart_desc}]}}\n")
            f.write("}\n")
            f.write("\\end{center}\n")
            f.write("\\end{frame}\n\n")

        # Summary slide
        f.write("% Summary Slide\n")
        f.write(f"\\begin{{frame}}[t]{{Summary: {lesson['title']}}}\n")
        f.write("\\begin{itemize}\n")
        for section_title, _ in lesson['sections'][:3]:
            f.write(f"\\item {section_title}\n")
        f.write("\\end{itemize}\n\n")
        f.write("\\vspace{1em}\n")
        f.write("\\textbf{Key Takeaway:} ")

        # Generate key takeaway based on lesson
        takeaways = {
            25: "AI and ML are transforming finance, but understanding their scope and limitations is critical.",
            26: "Quality data is the foundation of successful ML - ensure compliance with privacy regulations.",
            27: "Regression models predict continuous outcomes - evaluate with appropriate metrics like R².",
            28: "Classification models predict categories - balance precision and recall based on business costs.",
            29: "Algorithmic trading requires rigorous backtesting - avoid overfitting and look-ahead bias.",
            30: "ML credit scoring offers advantages, but fairness and regulatory compliance are paramount.",
            31: "Fraud detection requires handling imbalanced data and optimizing the precision-recall trade-off.",
            32: "NLP enables analysis of unstructured text data for sentiment, entities, and automation.",
            33: "Robo-advisors use portfolio optimization to provide low-cost, automated investment management.",
            34: "Market prediction is limited by EMH and noise - maintain realistic expectations and focus on process.",
            35: "Explainability techniques like SHAP and LIME are essential for trust and regulatory compliance.",
            36: "AI regulation is evolving rapidly - stay informed about compliance requirements for high-risk applications."
        }
        f.write(takeaways[lesson['number']] + "\n")
        f.write("\\end{frame}\n\n")

        # Closing slide
        f.write("% Closing Slide\n")
        f.write("\\begin{frame}[plain]\n")
        f.write("\\vspace{3cm}\n")
        f.write("\\begin{center}\n")
        f.write("{\\Large Thank you}\\\\[2cm]\n")
        f.write("{\\normalsize Questions?}\n")
        f.write("\\end{center}\n")
        f.write("\\end{frame}\n\n")

        f.write("\\end{document}\n")

    print(f"Generated: {filename}")

print(f"\nAll 12 lesson slide decks generated in:\n{base_dir}")
