"""
Generate all 12 lessons for Module 3: AI/ML in Finance
Creates complete LaTeX Beamer presentations with conceptual focus
"""

from pathlib import Path
from datetime import datetime

# Get timestamp for all files
timestamp = datetime.now().strftime("%Y%m%d_%H%M")

# Base directory
base_dir = Path(__file__).parent

# Ensure figures directory exists
(base_dir / "figures").mkdir(exist_ok=True)

# Common preamble for all lessons
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

# Lesson 25: Introduction to AI/ML
lesson_25 = PREAMBLE + r"""
\title{Digital Finance 3: Technology in Finance}
\subtitle{Lesson 25: Introduction to AI/ML in Finance}
\author{FHGR}
\date{\today}

\begin{document}

\begin{frame}
\titlepage
\end{frame}

\begin{frame}{Learning Objectives}
By the end of this lesson, you will be able to:
\begin{itemize}
\item Define artificial intelligence, machine learning, and deep learning
\item Understand the hierarchy and relationships between AI concepts
\item Identify key applications of AI/ML in finance
\item Distinguish between realistic capabilities and overhype
\item Recognize the evolution of AI in financial services
\end{itemize}
\end{frame}

\begin{frame}{What is Artificial Intelligence?}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Broad Definition:}
\begin{itemize}
\item Simulation of human intelligence by machines
\item Systems that can reason, learn, and act autonomously
\item Originated in 1956 at Dartmouth Conference
\item Multiple ``AI winters'' and resurgences
\end{itemize}

\column{0.48\textwidth}
\textbf{Key Characteristics:}
\begin{itemize}
\item Perception (vision, speech)
\item Reasoning (logic, planning)
\item Learning (from data, experience)
\item Natural language processing
\item Problem-solving
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{The AI Hierarchy: From Broad to Narrow}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Three Nested Concepts:}
\begin{enumerate}
\item \textcolor{mlpurple}{\textbf{Artificial Intelligence}} (broadest)\\
Any technique enabling computers to mimic human intelligence

\item \textcolor{mlblue}{\textbf{Machine Learning}} (subset)\\
Systems that learn from data without explicit programming

\item \textcolor{mlorange}{\textbf{Deep Learning}} (subset of ML)\\
Neural networks with multiple layers
\end{enumerate}

\column{0.48\textwidth}
\textbf{Analogy:}
\begin{itemize}
\item AI = Transportation
\item ML = Automobiles
\item Deep Learning = Electric cars
\end{itemize}

\vspace{1em}
\textbf{Modern Reality:}\\
Most ``AI in finance'' today is actually machine learning, specifically supervised learning algorithms.
\end{columns}
\end{frame}

\begin{frame}{Machine Learning: The Core Idea}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Traditional Programming:}
\begin{itemize}
\item Humans write explicit rules
\item Input + Rules = Output
\item Example: ``IF credit score < 600 THEN reject''
\item Hard to scale for complex patterns
\end{itemize}

\column{0.48\textwidth}
\textbf{Machine Learning:}
\begin{itemize}
\item Algorithm learns rules from data
\item Input + Output = Rules (learned)
\item Example: Discover credit patterns from 1M loan histories
\item Scales to high-dimensional problems
\end{itemize}
\end{columns}

\vspace{1em}
\textbf{Key Insight:}\\
ML excels when:
\begin{itemize}
\item Patterns are complex and non-obvious
\item Large amounts of data are available
\item Rules are difficult to articulate explicitly
\end{itemize}
\end{frame}

\begin{frame}{Three Types of Machine Learning}
\begin{columns}[T]
\column{0.31\textwidth}
\textbf{Supervised Learning}
\begin{itemize}
\item Labeled data (X, Y)
\item Learn mapping: X → Y
\item Examples:
  \begin{itemize}
  \item Credit scoring
  \item Fraud detection
  \item Stock prediction
  \end{itemize}
\item \textcolor{mlgreen}{Most common in finance}
\end{itemize}

\column{0.31\textwidth}
\textbf{Unsupervised Learning}
\begin{itemize}
\item Unlabeled data (X only)
\item Find hidden structure
\item Examples:
  \begin{itemize}
  \item Customer segmentation
  \item Anomaly detection
  \item Portfolio clustering
  \end{itemize}
\item Discovery-oriented
\end{itemize}

\column{0.31\textwidth}
\textbf{Reinforcement Learning}
\begin{itemize}
\item Agent learns via trial/error
\item Maximize cumulative reward
\item Examples:
  \begin{itemize}
  \item Algorithmic trading
  \item Dynamic hedging
  \item Game playing (chess, Go)
  \end{itemize}
\item Still research-heavy
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Deep Learning: Neural Networks at Scale}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{What Makes It ``Deep''?}
\begin{itemize}
\item Multiple hidden layers (10s to 100s)
\item Automatic feature learning
\item Inspired by brain neurons (loosely)
\item Requires massive data and compute
\end{itemize}

\vspace{0.5em}
\textbf{Breakthroughs (2012-present):}
\begin{itemize}
\item Image recognition (ImageNet 2012)
\item Speech recognition (Google, Apple)
\item Language models (GPT, BERT)
\item Game mastery (AlphaGo 2016)
\end{itemize}

\column{0.48\textwidth}
\textbf{Finance Applications:}
\begin{itemize}
\item Document processing (OCR, contracts)
\item Sentiment analysis (news, social media)
\item Time series forecasting (limited success)
\item Alternative data (satellite, text)
\end{itemize}

\vspace{0.5em}
\textbf{Reality Check:}\\
Deep learning excels with:
\begin{itemize}
\item Unstructured data (text, images)
\item Millions of training examples
\item Pattern recognition tasks
\end{itemize}
Not always superior for structured financial data (tabular).
\end{columns}
\end{frame}

\begin{frame}{AI/ML Applications in Finance: Overview}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Risk Management:}
\begin{itemize}
\item Credit scoring and underwriting
\item Fraud detection
\item Anti-money laundering (AML)
\item Market risk modeling
\item Stress testing
\end{itemize}

\vspace{0.5em}
\textbf{Trading and Investment:}
\begin{itemize}
\item Algorithmic trading strategies
\item Portfolio optimization
\item Market prediction (limited)
\item Robo-advisors
\item Alternative data analysis
\end{itemize}

\column{0.48\textwidth}
\textbf{Customer Service:}
\begin{itemize}
\item Chatbots and virtual assistants
\item Personalized recommendations
\item Customer segmentation
\item Churn prediction
\end{itemize}

\vspace{0.5em}
\textbf{Operations:}
\begin{itemize}
\item Document processing (OCR, NLP)
\item Regulatory compliance automation
\item Process optimization
\item Cybersecurity threat detection
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Common Thread:} Automation of pattern recognition tasks previously requiring human expertise.
\end{frame}

\begin{frame}{Case Study: Credit Scoring Evolution}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Traditional Approach (1960s-2000s):}
\begin{itemize}
\item FICO score (5 factors, fixed weights)
\item Linear scorecards
\item Based on credit bureau data only
\item Transparent, regulated
\item Limited predictive power
\end{itemize}

\vspace{0.5em}
\textbf{Limitations:}
\begin{itemize}
\item Misses non-linear relationships
\item Cannot handle alternative data
\item One-size-fits-all model
\end{itemize}

\column{0.48\textwidth}
\textbf{ML Approach (2010s-present):}
\begin{itemize}
\item Gradient boosting (XGBoost, LightGBM)
\item 100s to 1000s of features
\item Alternative data (mobile, social, payments)
\item Dynamic model updates
\item Higher accuracy (10-30\% improvement)
\end{itemize}

\vspace{0.5em}
\textbf{New Challenges:}
\begin{itemize}
\item Explainability (``black box'')
\item Fairness and bias
\item Regulatory acceptance
\item Data privacy
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Key Lesson:} Technology enables better predictions but introduces new risks and ethical questions.
\end{frame}

\begin{frame}{The Hype Cycle: Expectations vs Reality}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Gartner Hype Cycle Phases:}
\begin{enumerate}
\item Innovation Trigger
\item Peak of Inflated Expectations
\item Trough of Disillusionment
\item Slope of Enlightenment
\item Plateau of Productivity
\end{enumerate}

\vspace{0.5em}
\textbf{Where is AI/ML in Finance?}
\begin{itemize}
\item Overall: Slope of Enlightenment
\item Deep Learning: Still some hype
\item Traditional ML: Plateau (established)
\item Generative AI: Peak (2023-2024)
\end{itemize}

\column{0.48\textwidth}
\textbf{Common Misconceptions:}
\begin{itemize}
\item ``AI will replace all analysts'' (No)
\item ``ML always outperforms rules'' (No)
\item ``More data always helps'' (Diminishing returns)
\item ``Black boxes are always better'' (Transparency matters)
\end{itemize}

\vspace{0.5em}
\textbf{Realistic Expectations:}
\begin{itemize}
\item AI augments, not replaces, humans
\item ML excels at narrow, repetitive tasks
\item Domain expertise still critical
\item Hybrid approaches often best
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{What AI/ML Can and Cannot Do in Finance}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Can Do Well:}
\begin{itemize}
\item Pattern recognition (fraud, anomalies)
\item Classification (credit risk, default)
\item Prediction with stable patterns (short-term)
\item Data processing at scale (NLP, OCR)
\item Optimization (portfolio, pricing)
\item Personalization (recommendations)
\end{itemize}

\vspace{0.5em}
\textbf{Success Factors:}
\begin{itemize}
\item Large, high-quality datasets
\item Stable underlying patterns
\item Clear objective function
\item Ability to validate and test
\end{itemize}

\column{0.48\textwidth}
\textbf{Cannot Do (or Struggles):}
\begin{itemize}
\item Predict regime changes (crashes, crises)
\item Explain ``why'' without human input
\item Handle novel situations (out-of-sample)
\item Replace human judgment entirely
\item Guarantee fairness or ethics
\end{itemize}

\vspace{0.5em}
\textbf{Fundamental Limits:}
\begin{itemize}
\item No free lunch (NFL theorem)
\item Efficient Market Hypothesis constraints
\item Overfitting to historical noise
\item Adversarial dynamics (arms race)
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Bottom Line:} AI/ML is a powerful tool, not magic. Success requires proper problem framing, quality data, and realistic expectations.
\end{frame}

\begin{frame}{Historical Timeline: AI in Finance}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{1980s-1990s: Expert Systems}
\begin{itemize}
\item Rule-based systems (if-then)
\item Limited success, brittle
\item Example: MYCIN for medical diagnosis
\end{itemize}

\vspace{0.3em}
\textbf{2000s: First ML Wave}
\begin{itemize}
\item Support Vector Machines (SVM)
\item Random Forests
\item Credit scoring improvements
\end{itemize}

\vspace{0.3em}
\textbf{2010s: Deep Learning Era}
\begin{itemize}
\item Neural networks for NLP
\item Algorithmic trading explosion
\item Robo-advisors launched
\end{itemize}

\column{0.48\textwidth}
\textbf{2015-2020: Maturation}
\begin{itemize}
\item Gradient boosting dominance (XGBoost)
\item Regulatory frameworks emerge
\item Focus on explainability
\end{itemize}

\vspace{0.3em}
\textbf{2020-present: Generative AI}
\begin{itemize}
\item Large Language Models (GPT-3/4)
\item Financial document analysis
\item Code generation for analysts
\item New regulatory challenges
\end{itemize}

\vspace{0.3em}
\textbf{Future Trends:}
\begin{itemize}
\item Federated learning (privacy)
\item Causal inference integration
\item Hybrid human-AI systems
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Industry Adoption: Survey Data}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Adoption Rates (2023 surveys):}
\begin{itemize}
\item Large banks: 80-90\% have AI initiatives
\item Asset managers: 60-70\% use ML
\item Fintechs: 90\%+ (core to business)
\item Regional banks: 30-50\% (growing)
\end{itemize}

\vspace{0.5em}
\textbf{Top Use Cases:}
\begin{enumerate}
\item Fraud detection (85\%)
\item Customer service chatbots (70\%)
\item Credit risk modeling (65\%)
\item AML/KYC automation (60\%)
\item Algorithmic trading (50\%)
\end{enumerate}

\column{0.48\textwidth}
\textbf{Barriers to Adoption:}
\begin{itemize}
\item Data quality/availability (65\%)
\item Lack of skilled talent (60\%)
\item Regulatory uncertainty (55\%)
\item Integration with legacy systems (50\%)
\item Explainability requirements (45\%)
\end{itemize}

\vspace{0.5em}
\textbf{Investment Trends:}
\begin{itemize}
\item Global AI in finance market: \$10B (2023)
\item Projected: \$35B by 2030 (CAGR 20\%)
\item Focus shifting from experimentation to production scaling
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Key Players and Ecosystem}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Large Tech Companies:}
\begin{itemize}
\item Google Cloud (AI Platform, AutoML)
\item Amazon Web Services (SageMaker)
\item Microsoft Azure (ML Studio)
\item IBM (Watson Financial Services)
\end{itemize}

\vspace{0.5em}
\textbf{Specialized Fintechs:}
\begin{itemize}
\item Upstart (AI lending)
\item Kasisto (chatbots)
\item Kensho (analytics, acquired by S\&P)
\item Ayasdi (AML)
\end{itemize}

\column{0.48\textwidth}
\textbf{Traditional Finance + AI:}
\begin{itemize}
\item JPMorgan Chase (COiN, IndexGPT)
\item Goldman Sachs (Marcus, Marquee)
\item BlackRock (Aladdin platform)
\item Capital One (credit models)
\end{itemize}

\vspace{0.5em}
\textbf{Open Source Community:}
\begin{itemize}
\item scikit-learn (ML library)
\item TensorFlow, PyTorch (deep learning)
\item Hugging Face (NLP models)
\item Kaggle (competitions, datasets)
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Trend:} Increasing collaboration between big tech, fintechs, and traditional banks.
\end{frame}

\begin{frame}{Data: The Fuel for AI/ML}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Why Data Matters:}
\begin{itemize}
\item ML models are only as good as training data
\item More data often beats better algorithms
\item Quality > Quantity (garbage in, garbage out)
\end{itemize}

\vspace{0.5em}
\textbf{Types of Financial Data:}
\begin{itemize}
\item Structured: Prices, returns, accounting
\item Unstructured: News, reports, social media
\item Alternative: Satellite, mobile, web scraping
\item Real-time: Tick data, order books
\end{itemize}

\column{0.48\textwidth}
\textbf{Data Challenges:}
\begin{itemize}
\item Availability (proprietary, expensive)
\item Quality (errors, missing values)
\item Bias (survivorship, selection)
\item Privacy (GDPR, regulations)
\item Stationarity (patterns change over time)
\end{itemize}

\vspace{0.5em}
\textbf{Best Practices:}
\begin{itemize}
\item Rigorous data cleaning
\item Train/validation/test splits
\item Cross-validation
\item Out-of-sample testing
\item Monitor data drift
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Next Lesson:} Deep dive into financial data types and preparation.
\end{frame}

\begin{frame}{Ethical Considerations}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Fairness and Bias:}
\begin{itemize}
\item Models can perpetuate historical discrimination
\item Protected attributes (race, gender, age)
\item Proxy variables (zip code = race)
\item Disparate impact vs. disparate treatment
\end{itemize}

\vspace{0.5em}
\textbf{Transparency:}
\begin{itemize}
\item Right to explanation (GDPR Article 22)
\item Black box models vs. interpretability
\item Trade-off: accuracy vs. explainability
\end{itemize}

\column{0.48\textwidth}
\textbf{Accountability:}
\begin{itemize}
\item Who is responsible for AI decisions?
\item Human-in-the-loop vs. full automation
\item Audit trails and governance
\end{itemize}

\vspace{0.5em}
\textbf{Privacy:}
\begin{itemize}
\item Data minimization principle
\item Consent and purpose limitation
\item Anonymization challenges
\item Model inversion attacks
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Regulatory Response:} EU AI Act, algorithmic accountability laws, model risk management frameworks.
\end{frame}

\begin{frame}{Skills for AI/ML in Finance}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Technical Skills:}
\begin{itemize}
\item Programming (Python, R)
\item Statistics and probability
\item Linear algebra and calculus
\item ML algorithms and frameworks
\item Data manipulation (SQL, pandas)
\item Cloud platforms (AWS, Azure, GCP)
\end{itemize}

\vspace{0.5em}
\textbf{Finance Domain Knowledge:}
\begin{itemize}
\item Financial markets and instruments
\item Risk management principles
\item Regulatory environment
\item Business context
\end{itemize}

\column{0.48\textwidth}
\textbf{Soft Skills:}
\begin{itemize}
\item Problem framing
\item Critical thinking (avoiding overfitting)
\item Communication (explaining models)
\item Ethics and responsibility
\item Collaboration (cross-functional teams)
\end{itemize}

\vspace{0.5em}
\textbf{Career Paths:}
\begin{itemize}
\item Quantitative Analyst
\item Data Scientist (Finance)
\item ML Engineer
\item Risk Modeler
\item AI Product Manager
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Key Insight:} Success requires combination of technical skills, domain expertise, and ethical awareness.
\end{frame}

\begin{frame}{Summary and Key Takeaways}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Core Concepts:}
\begin{itemize}
\item AI > ML > Deep Learning (hierarchy)
\item ML learns patterns from data
\item Supervised learning dominates finance
\item Deep learning for unstructured data
\end{itemize}

\vspace{0.5em}
\textbf{Finance Applications:}
\begin{itemize}
\item Risk: Credit, fraud, AML
\item Trading: Algorithms, robo-advisors
\item Operations: NLP, automation
\item Customer: Chatbots, personalization
\end{itemize}

\column{0.48\textwidth}
\textbf{Reality Check:}
\begin{itemize}
\item AI augments, not replaces humans
\item Data quality is paramount
\item Hype vs. realistic capabilities
\item Ethical and regulatory challenges
\end{itemize}

\vspace{0.5em}
\textbf{Looking Ahead:}
\begin{itemize}
\item Next 11 lessons: Detailed exploration
\item Hands-on understanding (conceptual)
\item Critical evaluation skills
\item Practical applications
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Next Lesson Preview}
\textbf{Lesson 26: Financial Data for AI/ML}

\vspace{0.5em}
Topics to be covered:
\begin{itemize}
\item Structured vs. unstructured data
\item Data sources and vendors
\item Alternative data revolution
\item Data quality and preprocessing
\item GDPR and privacy considerations
\item Feature engineering basics
\end{itemize}

\vspace{1em}
\textbf{Preparation:}
\begin{itemize}
\item Review basic statistics (mean, variance, correlation)
\item Think about data quality issues in your own experience
\item Consider: What makes financial data unique?
\end{itemize}
\end{frame}

\end{document}
"""

# Lesson 26: Financial Data
lesson_26 = PREAMBLE + r"""
\title{Digital Finance 3: Technology in Finance}
\subtitle{Lesson 26: Financial Data for AI/ML}
\author{FHGR}
\date{\today}

\begin{document}

\begin{frame}
\titlepage
\end{frame}

\begin{frame}{Learning Objectives}
By the end of this lesson, you will be able to:
\begin{itemize}
\item Distinguish between structured and unstructured financial data
\item Identify major sources and vendors of financial data
\item Understand the alternative data revolution and its applications
\item Recognize data quality issues and preprocessing requirements
\item Explain GDPR and privacy implications for financial ML
\item Describe basic feature engineering concepts
\end{itemize}
\end{frame}

\begin{frame}{Structured vs. Unstructured Data}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Structured Data:}
\begin{itemize}
\item Organized in tables (rows, columns)
\item Predefined schema
\item Easy to query (SQL)
\item Numerical or categorical
\end{itemize}

\vspace{0.5em}
\textbf{Examples in Finance:}
\begin{itemize}
\item Stock prices (OHLCV)
\item Financial statements
\item Credit bureau data
\item Transaction records
\item Market microstructure (order book)
\end{itemize}

\column{0.48\textwidth}
\textbf{Unstructured Data:}
\begin{itemize}
\item No predefined format
\item Free-form text, images, audio
\item Requires NLP/computer vision
\item 80-90\% of enterprise data
\end{itemize}

\vspace{0.5em}
\textbf{Examples in Finance:}
\begin{itemize}
\item News articles, press releases
\item Earnings call transcripts
\item SEC filings (10-K, 8-K)
\item Social media (Twitter, Reddit)
\item Analyst reports
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Modern ML:} Combines both types (e.g., sentiment scores from text as features in tabular models).
\end{frame}

\begin{frame}{Traditional Financial Data Sources}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Market Data:}
\begin{itemize}
\item Stock prices (exchanges)
\item Bond yields (TRACE, Bloomberg)
\item Derivatives (CME, Eurex)
\item FX rates (interbank, EBS)
\item Crypto (Coinbase, Binance)
\end{itemize}

\vspace{0.5em}
\textbf{Fundamental Data:}
\begin{itemize}
\item Financial statements (EDGAR, SEDAR)
\item Company events (earnings, M\&A)
\item Economic indicators (BLS, Fed, ECB)
\item Industry metrics (PMI, CPI)
\end{itemize}

\column{0.48\textwidth}
\textbf{Credit/Risk Data:}
\begin{itemize}
\item Credit bureaus (Experian, Equifax, TransUnion)
\item Ratings (Moody's, S\&P, Fitch)
\item Loan performance data
\item Default histories
\end{itemize}

\vspace{0.5em}
\textbf{Major Vendors:}
\begin{itemize}
\item Bloomberg Terminal (\$20-25k/year)
\item Refinitiv (formerly Thomson Reuters)
\item FactSet
\item S\&P Capital IQ
\item Morningstar
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Trend:} Declining costs for basic data (Yahoo Finance free), but premium data remains expensive.
\end{frame}

\begin{frame}{The Alternative Data Revolution}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{What is Alternative Data?}
\begin{itemize}
\item Non-traditional data sources
\item Often unstructured or semi-structured
\item Provides early signals
\item Competitive edge (information advantage)
\end{itemize}

\vspace{0.5em}
\textbf{Categories:}
\begin{enumerate}
\item \textbf{Web-scraped:} Prices, reviews, job postings
\item \textbf{Sensor/IoT:} Satellite, credit cards, mobile location
\item \textbf{Social:} Twitter sentiment, Reddit mentions
\item \textbf{Business:} Email receipts, app usage
\end{enumerate}

\column{0.48\textwidth}
\textbf{Example Use Cases:}
\begin{itemize}
\item Satellite images: Count cars in parking lots (retail sales proxy)
\item Credit card data: Real-time consumer spending
\item Job postings: Company growth indicators
\item App downloads: User engagement trends
\item Shipping data: Supply chain analysis
\end{itemize}

\vspace{0.5em}
\textbf{Market Size:}
\begin{itemize}
\item \$1.7B in 2020
\item Projected \$17B by 2027
\item Hedge funds are largest buyers
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Challenges:} Quality control, legal/ethical concerns, data decay (alpha decay).
\end{frame}

\begin{frame}{Alternative Data: Examples in Detail}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Satellite Imagery:}
\begin{itemize}
\item Providers: Orbital Insight, RS Metrics
\item Use: Count oil tanks, construction activity
\item Example: China steel production estimates
\item Frequency: Daily to weekly
\item Cost: \$10k-100k+ per year
\end{itemize}

\vspace{0.5em}
\textbf{Credit Card Transactions:}
\begin{itemize}
\item Providers: Facteus, Second Measure
\item Use: Real-time revenue tracking
\item Example: Restaurant chain performance
\item Privacy: Aggregated, anonymized
\end{itemize}

\column{0.48\textwidth}
\textbf{Social Media Sentiment:}
\begin{itemize}
\item Providers: RavenPack, Bloomberg sentiment
\item Use: Market mood, event detection
\item Example: Tweet volume predicting volatility
\item Challenges: Noise, manipulation
\end{itemize}

\vspace{0.5em}
\textbf{Web Traffic:}
\begin{itemize}
\item Providers: SimilarWeb, Alexa (discontinued)
\item Use: Company engagement metrics
\item Example: E-commerce site visits
\item Limitation: Sample-based estimates
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Key Question:} Does alternative data provide genuine alpha or just noise?
Evidence: Mixed, diminishing returns as adoption increases (alpha decay).
\end{frame}

\begin{frame}{Data Quality: The GIGO Principle}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Garbage In, Garbage Out:}
\begin{itemize}
\item ML models amplify data quality issues
\item No algorithm fixes bad data
\item Quality > Quantity (usually)
\end{itemize}

\vspace{0.5em}
\textbf{Common Data Problems:}
\begin{itemize}
\item \textbf{Missing values:} Deletions, NaN, nulls
\item \textbf{Outliers:} Errors vs. true extremes
\item \textbf{Inconsistencies:} Units, formats, definitions
\item \textbf{Duplicates:} Same record multiple times
\item \textbf{Errors:} Typos, wrong values
\end{itemize}

\column{0.48\textwidth}
\textbf{Finance-Specific Issues:}
\begin{itemize}
\item \textbf{Survivorship bias:} Only successful firms remain
\item \textbf{Look-ahead bias:} Using future information
\item \textbf{Corporate actions:} Splits, dividends, mergers
\item \textbf{Restatements:} Accounting changes, revisions
\item \textbf{Stale data:} Delayed or infrequent updates
\end{itemize}

\vspace{0.5em}
\textbf{Impact on ML:}
\begin{itemize}
\item Biased predictions
\item Overfitting to noise
\item Poor generalization
\item Misleading performance metrics
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Best Practice:} Spend 50-80\% of project time on data cleaning and validation.
\end{frame}

\begin{frame}{Data Preprocessing Pipeline}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Step 1: Data Collection}
\begin{itemize}
\item Define requirements
\item Source identification
\item API integration or downloads
\item Compliance checks
\end{itemize}

\vspace{0.3em}
\textbf{Step 2: Cleaning}
\begin{itemize}
\item Handle missing values (drop, impute, flag)
\item Remove duplicates
\item Correct errors (domain knowledge)
\item Outlier treatment (winsorize, cap)
\end{itemize}

\vspace{0.3em}
\textbf{Step 3: Transformation}
\begin{itemize}
\item Normalization/standardization
\item Log transforms (skewed distributions)
\item Date/time parsing
\item Encoding categoricals
\end{itemize}

\column{0.48\textwidth}
\textbf{Step 4: Feature Engineering}
\begin{itemize}
\item Create derived features
\item Lag variables (time series)
\item Interactions (cross-products)
\item Domain-specific ratios
\end{itemize}

\vspace{0.3em}
\textbf{Step 5: Validation}
\begin{itemize}
\item Statistical checks (distributions)
\item Consistency tests
\item Cross-field validation
\item Expert review
\end{itemize}

\vspace{0.3em}
\textbf{Step 6: Versioning}
\begin{itemize}
\item Track data lineage
\item Version control for datasets
\item Reproducibility
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Automation:} Modern ML pipelines use tools like Apache Airflow, Prefect for orchestration.
\end{frame}

\begin{frame}{Handling Missing Data}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Why Data is Missing:}
\begin{enumerate}
\item \textbf{MCAR} (Missing Completely At Random): Pure chance, no pattern
\item \textbf{MAR} (Missing At Random): Related to observed data
\item \textbf{MNAR} (Missing Not At Random): Related to unobserved value itself
\end{enumerate}

\vspace{0.5em}
\textbf{Finance Example:}
\begin{itemize}
\item MCAR: Random system glitch
\item MAR: Small firms don't report segment data
\item MNAR: Firms hide bad performance
\end{itemize}

\column{0.48\textwidth}
\textbf{Strategies:}
\begin{itemize}
\item \textbf{Deletion:} Drop rows/columns (only if < 5\% missing, MCAR)
\item \textbf{Mean/Median imputation:} Replace with average (simple, biased)
\item \textbf{Forward/backward fill:} Time series (assumes persistence)
\item \textbf{Model-based:} Predict missing values (KNN, regression)
\item \textbf{Indicator variable:} Flag missingness as feature
\end{itemize}

\vspace{0.5em}
\textbf{Best Practice:}
\begin{itemize}
\item Understand WHY data is missing
\item Test sensitivity to imputation method
\item Document assumptions
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Feature Engineering Fundamentals}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{What is Feature Engineering?}
\begin{itemize}
\item Creating new variables from raw data
\item Domain knowledge + creativity
\item Often more important than algorithm choice
\item ``Applied feature engineering beats fancy algorithms''
\end{itemize}

\vspace{0.5em}
\textbf{Common Techniques:}
\begin{itemize}
\item \textbf{Ratios:} P/E, Debt/Equity, ROE
\item \textbf{Differences:} Price changes, growth rates
\item \textbf{Lags:} Yesterday's return, 30-day moving avg
\item \textbf{Aggregations:} Sum, mean, max over time window
\item \textbf{Interactions:} Sector × Size, Region × Industry
\end{itemize}

\column{0.48\textwidth}
\textbf{Finance-Specific Features:}
\begin{itemize}
\item Technical indicators (RSI, MACD, Bollinger Bands)
\item Volatility measures (realized, implied)
\item Momentum (12-month return)
\item Value factors (book-to-market)
\item Quality metrics (accruals, earnings quality)
\end{itemize}

\vspace{0.5em}
\textbf{Avoid:}
\begin{itemize}
\item Leakage (using future information)
\item High cardinality categoricals (too many levels)
\item Perfectly correlated features (redundant)
\item Features with no variance
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Art + Science:} Combines domain expertise with systematic experimentation.
\end{frame}

\begin{frame}{GDPR and Data Privacy Regulations}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{GDPR Key Principles (EU, 2018):}
\begin{itemize}
\item \textbf{Lawfulness:} Legal basis for processing
\item \textbf{Purpose limitation:} Specific, explicit purposes
\item \textbf{Data minimization:} Collect only necessary data
\item \textbf{Accuracy:} Keep data up-to-date
\item \textbf{Storage limitation:} Retain only as long as needed
\item \textbf{Integrity/confidentiality:} Secure processing
\end{itemize}

\vspace{0.5em}
\textbf{Individual Rights:}
\begin{itemize}
\item Right to access
\item Right to erasure (``right to be forgotten'')
\item Right to explanation (Article 22)
\end{itemize}

\column{0.48\textwidth}
\textbf{Implications for ML:}
\begin{itemize}
\item Consent requirements (explicit for sensitive data)
\item Anonymization challenges (re-identification risk)
\item Model explainability (if automated decision-making)
\item Data retention policies
\item Cross-border data transfers (adequacy decisions)
\end{itemize}

\vspace{0.5em}
\textbf{Other Regulations:}
\begin{itemize}
\item CCPA (California Consumer Privacy Act)
\item LGPD (Brazil)
\item POPIA (South Africa)
\end{itemize}

\vspace{0.5em}
\textbf{Penalties:} Up to 4\% of global revenue or 20M EUR (whichever is higher).
\end{columns}
\end{frame}

\begin{frame}{Anonymization vs. Pseudonymization}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Anonymization:}
\begin{itemize}
\item Irreversible removal of identifiers
\item No longer personal data under GDPR
\item Techniques:
  \begin{itemize}
  \item Aggregation
  \item Noise addition (differential privacy)
  \item Generalization (age → age range)
  \end{itemize}
\item Challenge: Re-identification risk (AOL search data, Netflix prize)
\end{itemize}

\vspace{0.5em}
\textbf{Re-identification Example:}
87\% of US population identifiable with just:
\begin{itemize}
\item ZIP code
\item Gender
\item Date of birth
\end{itemize}

\column{0.48\textwidth}
\textbf{Pseudonymization:}
\begin{itemize}
\item Replace identifiers with pseudonyms (tokens)
\item Reversible with key
\item Still personal data under GDPR
\item Techniques:
  \begin{itemize}
  \item Hashing
  \item Encryption
  \item Tokenization
  \end{itemize}
\item Reduces risk but doesn't eliminate it
\end{itemize}

\vspace{0.5em}
\textbf{Finance Use Cases:}
\begin{itemize}
\item Credit scoring: Pseudonymized customer IDs
\item Fraud detection: Anonymized transaction patterns
\item AML: Must balance privacy with compliance
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Best Practice:} Privacy by design (build privacy into system architecture from the start).
\end{frame}

\begin{frame}{Data Bias: Types and Examples}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Selection Bias:}
\begin{itemize}
\item Sample not representative of population
\item Example: Credit model trained only on approved loans (missing rejected applicants who would have repaid)
\end{itemize}

\vspace{0.3em}
\textbf{Survivorship Bias:}
\begin{itemize}
\item Only successful entities remain in dataset
\item Example: Mutual fund returns (failed funds disappear)
\item Impact: Overstates historical performance
\end{itemize}

\vspace{0.3em}
\textbf{Historical Bias:}
\begin{itemize}
\item Past discrimination baked into data
\item Example: Redlining in mortgage data
\item Model learns and perpetuates bias
\end{itemize}

\column{0.48\textwidth}
\textbf{Measurement Bias:}
\begin{itemize}
\item Systematic errors in data collection
\item Example: Self-reported income (underreporting)
\end{itemize}

\vspace{0.3em}
\textbf{Temporal Bias:}
\begin{itemize}
\item Data from one time period doesn't generalize
\item Example: Pre-2008 credit models failed post-crisis
\end{itemize}

\vspace{0.3em}
\textbf{Mitigation Strategies:}
\begin{itemize}
\item Diverse, representative datasets
\item Bias audits (fairness metrics)
\item Reweighting samples
\item Adversarial debiasing
\item Domain expert review
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Key Insight:} Bias in data leads to biased models, which lead to unfair outcomes. Proactive detection is essential.
\end{frame}

\begin{frame}{Time Series Data: Special Considerations}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Unique Challenges:}
\begin{itemize}
\item \textbf{Temporal dependence:} Observations not independent
\item \textbf{Non-stationarity:} Statistical properties change over time
\item \textbf{Seasonality:} Recurring patterns (quarterly earnings)
\item \textbf{Trends:} Long-term drift
\item \textbf{Structural breaks:} Regime changes (crises)
\end{itemize}

\vspace{0.5em}
\textbf{Cannot Use Standard ML:}
\begin{itemize}
\item Random train/test split violates temporal order
\item Cross-validation needs time-aware folds
\item Risk of look-ahead bias
\end{itemize}

\column{0.48\textwidth}
\textbf{Proper Approach:}
\begin{itemize}
\item \textbf{Walk-forward validation:} Train on past, test on future
\item \textbf{Expanding window:} Grow training set over time
\item \textbf{Rolling window:} Fixed-size window (adapts to recent data)
\end{itemize}

\vspace{0.5em}
\textbf{Feature Engineering:}
\begin{itemize}
\item Lags (t-1, t-2, ..., t-n)
\item Rolling statistics (moving averages, volatility)
\item Date/time features (day of week, month, quarter)
\item Event indicators (earnings announcement, FOMC)
\end{itemize}

\vspace{0.5em}
\textbf{Stationarity Tests:}
\begin{itemize}
\item Augmented Dickey-Fuller (ADF)
\item Differencing if non-stationary
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Data Storage and Infrastructure}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Storage Options:}
\begin{itemize}
\item \textbf{Relational databases:} PostgreSQL, MySQL (structured data, ACID transactions)
\item \textbf{NoSQL:} MongoDB, Cassandra (unstructured, scale)
\item \textbf{Data warehouses:} Snowflake, Redshift (analytics)
\item \textbf{Data lakes:} S3, Azure Data Lake (raw data, all formats)
\item \textbf{Time series DB:} InfluxDB, TimescaleDB (high-frequency data)
\end{itemize}

\vspace{0.5em}
\textbf{File Formats:}
\begin{itemize}
\item CSV (simple, inefficient)
\item Parquet (columnar, compressed, fast)
\item HDF5 (hierarchical, scientific)
\end{itemize}

\column{0.48\textwidth}
\textbf{Cloud vs. On-Premise:}
\begin{itemize}
\item Cloud: Scalability, cost-effective (pay-as-you-go)
\item On-prem: Control, security (for sensitive data)
\item Hybrid: Regulatory compliance + flexibility
\end{itemize}

\vspace{0.5em}
\textbf{Data Governance:}
\begin{itemize}
\item Data catalog (metadata management)
\item Access control (role-based)
\item Audit logs (who accessed what, when)
\item Data quality monitoring
\item Lineage tracking (source to destination)
\end{itemize}

\vspace{0.5em}
\textbf{Cost Considerations:}
\begin{itemize}
\item Storage: Cheap (S3 \$0.023/GB/month)
\item Compute: Expensive (processing, queries)
\item Data transfer: Can be costly (egress fees)
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Real-Time vs. Batch Data Processing}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Batch Processing:}
\begin{itemize}
\item Process large volumes periodically
\item Daily, weekly, monthly updates
\item Use cases:
  \begin{itemize}
  \item Monthly credit score updates
  \item Quarterly portfolio rebalancing
  \item Annual financial statement analysis
  \end{itemize}
\item Tools: Apache Spark, Hadoop, SQL
\item Pro: Efficient for large datasets
\item Con: Latency (hours to days)
\end{itemize}

\column{0.48\textwidth}
\textbf{Real-Time (Streaming):}
\begin{itemize}
\item Process data as it arrives
\item Milliseconds to seconds latency
\item Use cases:
  \begin{itemize}
  \item Fraud detection (transaction monitoring)
  \item Algorithmic trading (tick data)
  \item AML alerts (pattern matching)
  \end{itemize}
\item Tools: Apache Kafka, Flink, Kinesis
\item Pro: Immediate insights
\item Con: Complex infrastructure, costly
\end{itemize}
\end{columns}

\vspace{0.5em}
\textbf{Lambda Architecture:} Hybrid approach combining batch (accuracy) and streaming (speed) layers.
\end{frame}

\begin{frame}{Data Vendors: Comparison}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Bloomberg Terminal:}
\begin{itemize}
\item Cost: \$20-25k/user/year
\item Coverage: 99\% of financial instruments
\item Strengths: Real-time, analytics, news, messaging
\item Weaknesses: Expensive, proprietary
\end{itemize}

\vspace{0.3em}
\textbf{Refinitiv (LSEG):}
\begin{itemize}
\item Cost: \$15-30k/year
\item Strengths: Historical data, fundamentals
\item Eikon platform (Excel integration)
\end{itemize}

\vspace{0.3em}
\textbf{FactSet:}
\begin{itemize}
\item Cost: \$10-15k/year
\item Strengths: Quantitative analytics, screening
\item Popular among asset managers
\end{itemize}

\column{0.48\textwidth}
\textbf{Free/Low-Cost Alternatives:}
\begin{itemize}
\item Yahoo Finance: Free (15-20 min delay)
\item Alpha Vantage: API, free tier (500 calls/day)
\item Quandl: Free + premium datasets
\item FRED (Federal Reserve): Economic data
\end{itemize}

\vspace{0.3em}
\textbf{Alternative Data:}
\begin{itemize}
\item Thinknum (\$10k-50k/year)
\item YipitData (\$50k+/year)
\item Eagle Alpha (marketplace)
\end{itemize}

\vspace{0.3em}
\textbf{Selection Criteria:}
\begin{itemize}
\item Coverage and accuracy
\item Latency requirements
\item API availability
\item Cost vs. budget
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Data Quality Frameworks}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Six Dimensions of Quality:}
\begin{enumerate}
\item \textbf{Accuracy:} Values correct?
\item \textbf{Completeness:} All required data present?
\item \textbf{Consistency:} No contradictions across sources?
\item \textbf{Timeliness:} Data current and available when needed?
\item \textbf{Validity:} Conforms to format, range, type?
\item \textbf{Uniqueness:} No duplicates?
\end{enumerate}

\vspace{0.5em}
\textbf{Measurement:}
\begin{itemize}
\item Accuracy: \% records passing validation
\item Completeness: \% non-null values
\item Consistency: \% cross-checks passing
\end{itemize}

\column{0.48\textwidth}
\textbf{Quality Assurance Process:}
\begin{enumerate}
\item Define quality rules
\item Automated checks (scripts)
\item Exception handling
\item Root cause analysis
\item Continuous monitoring
\item Feedback loop to data sources
\end{enumerate}

\vspace{0.5em}
\textbf{Tools:}
\begin{itemize}
\item Great Expectations (Python library)
\item dbt (data build tool)
\item Custom SQL checks
\item Dashboards (Tableau, Power BI)
\end{itemize}

\vspace{0.5em}
\textbf{Best Practice:} Shift-left testing (validate early in pipeline, not at model training).
\end{columns}
\end{frame}

\begin{frame}{Summary and Key Takeaways}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Data Types:}
\begin{itemize}
\item Structured (tables) vs. unstructured (text, images)
\item Traditional (prices, financials) vs. alternative (satellite, social)
\item Real-time (streaming) vs. batch (periodic)
\end{itemize}

\vspace{0.5em}
\textbf{Quality is Critical:}
\begin{itemize}
\item GIGO principle applies
\item 50-80\% of effort on data work
\item Bias detection and mitigation
\item Time series requires special care
\end{itemize}

\column{0.48\textwidth}
\textbf{Regulations Matter:}
\begin{itemize}
\item GDPR and privacy laws
\item Anonymization challenges
\item Right to explanation
\item Compliance > model performance
\end{itemize}

\vspace{0.5em}
\textbf{Practical Considerations:}
\begin{itemize}
\item Cost-benefit of data vendors
\item Infrastructure (cloud, storage)
\item Feature engineering creativity
\item Continuous monitoring
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}{Next Lesson Preview}
\textbf{Lesson 27: Supervised Learning - Regression}

\vspace{0.5em}
Topics to be covered:
\begin{itemize}
\item Features, labels, and training data
\item Simple and multiple linear regression
\item Coefficients interpretation
\item R-squared and evaluation metrics
\item Overfitting and regularization (Ridge, Lasso)
\item Applications: Stock return prediction, pricing models
\end{itemize}

\vspace{1em}
\textbf{Preparation:}
\begin{itemize}
\item Review basic linear algebra (vectors, matrices)
\item Recall correlation and covariance concepts
\item Think: What financial problems involve predicting continuous values?
\end{itemize}
\end{frame}

\end{document}
"""

# Save all lessons to files
lessons = {
    "lesson_25_intro_ai_ml.tex": lesson_25,
    "lesson_26_financial_data.tex": lesson_26,
}

for filename, content in lessons.items():
    filepath = base_dir / f"{timestamp}_{filename}"
    filepath.write_text(content, encoding='utf-8')
    print(f"Created: {filepath}")

print(f"\nGenerated {len(lessons)} lessons so far.")
print(f"Timestamp: {timestamp}")
print("\nContinuing with remaining 10 lessons...")
