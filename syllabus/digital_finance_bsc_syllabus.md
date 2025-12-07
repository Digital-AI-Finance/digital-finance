# BSc Digital Finance - Course Syllabus

## Course Overview

**Course Title:** Digital Finance
**Level:** Bachelor of Science (BSc)
**Duration:** 48 lessons (4 modules x 12 lessons)
**Lesson Duration:** 45 minutes each
**Prerequisites:** None
**Programming Language:** Python
**Assessment:** Final project only (3 tracks: technical implementation, business case analysis, research paper)

## Course Description

This course provides a comprehensive introduction to digital finance, covering four major domains: Fintech innovations, blockchain technology, artificial intelligence and machine learning applications in finance, and traditional digital finance infrastructure. Students will gain practical skills in Python programming while exploring how technology is transforming financial services, from payment systems to algorithmic trading.

## Learning Outcomes

By the end of this course, students will be able to:
- Understand the technological foundations of modern financial services
- Implement basic financial algorithms using Python
- Evaluate fintech business models and their regulatory challenges
- Explain blockchain technology and its applications in finance
- Apply machine learning techniques to financial problems
- Analyze the infrastructure of traditional financial markets
- Critically assess the risks and opportunities of digital finance innovations

---

## MODULE 1: FINTECH (Lessons 1-12)

### Lesson 1: Introduction to Fintech

**Learning Objectives:**
- Define fintech and its historical evolution
- Identify major fintech sectors and their impact on traditional finance
- Understand the drivers of fintech innovation
- Recognize key stakeholders in the fintech ecosystem

**Topics Covered:**
- Definition and scope of fintech
- Historical timeline: from ATMs to mobile banking
- Major fintech sectors (payments, lending, wealth, insurance, infrastructure)
- Drivers of innovation: technology, regulation, customer expectations
- Traditional finance vs. fintech business models
- Global fintech landscape and regional differences
- The fintech ecosystem: startups, incumbents, regulators, investors

**Practical Activity:**
Map the fintech ecosystem by creating a visual diagram showing relationships between banks, fintech startups, regulators, and technology providers. Use Python to scrape and visualize data on fintech funding trends.

**Suggested Reading:**
- Arner, D.W., et al. (2015). "The Evolution of Fintech: A New Post-Crisis Paradigm?" Georgetown Journal of International Law
- CB Insights (latest). "State of Fintech Report"
- BIS (2018). "Sound Practices: Implications of fintech developments for banks and bank supervisors"

---

### Lesson 2: Digital Payments I - Fundamentals

**Learning Objectives:**
- Understand the payment value chain and key participants
- Explain how card networks operate (Visa, Mastercard)
- Identify the roles of acquirers, issuers, and payment processors
- Calculate payment fees and understand revenue models

**Topics Covered:**
- The four-party model: cardholder, issuer, acquirer, merchant
- Card network operations and interchange fees
- Payment processing flow and settlement
- Authorization, clearing, and settlement processes
- Merchant discount rates and revenue sharing
- Payment security basics (PCI-DSS, tokenization)
- Cross-border payments and currency conversion

**Practical Activity:**
Build a Python simulator that models a payment transaction flow through the four-party system, calculating fees at each step. Analyze how interchange rates affect merchant costs.

**Suggested Reading:**
- Chakravorti, S. (2010). "Externalities in Payment Card Networks"
- Mastercard/Visa public interchange fee schedules
- Payment Card Industry Data Security Standard (PCI-DSS) overview

---

### Lesson 3: Digital Payments II - Mobile Wallets

**Learning Objectives:**
- Compare different mobile payment technologies (NFC, QR codes, in-app)
- Analyze the business models of major mobile wallets
- Understand tokenization and secure element technology
- Evaluate mobile payment adoption factors across markets

**Topics Covered:**
- Mobile payment types: NFC (Apple Pay, Google Pay), QR code (Alipay, WeChat Pay)
- Tokenization and how it protects card data
- Secure element vs. host card emulation (HCE)
- Mobile wallet ecosystems and value propositions
- Adoption patterns in developed vs. developing markets
- Competition between tech giants and financial institutions
- Regulatory considerations for mobile payments

**Practical Activity:**
Create a Python-based comparison dashboard that analyzes mobile wallet market share across different regions. Implement a simple tokenization algorithm demonstrating how card data is protected.

**Suggested Reading:**
- Ozturk, A.B. (2016). "Customer acceptance of cashless payment systems in the hospitality industry"
- Statista reports on mobile payment adoption
- EMVCo tokenization specifications (overview)

---

### Lesson 4: Neobanks and Challenger Banks

**Learning Objectives:**
- Distinguish between neobanks, challenger banks, and traditional banks
- Analyze neobank business models and unit economics
- Identify regulatory challenges facing digital-only banks
- Evaluate the competitive advantages and risks of neobanks

**Topics Covered:**
- Definitions: neobanks vs. challenger banks vs. digital banks
- Key players: Revolut, N26, Chime, Monzo, Nubank
- Technology stack and core banking platforms
- Customer acquisition costs (CAC) and lifetime value (LTV)
- Revenue models: interchange, subscriptions, lending, premium features
- Banking licenses vs. partner bank models
- Regulatory arbitrage and compliance challenges

**Practical Activity:**
Build a Python model to calculate neobank unit economics, analyzing CAC, LTV, and path to profitability. Compare different revenue strategies using publicly available data.

**Suggested Reading:**
- Accenture (2021). "Neobanks: The New Frontier in Banking"
- Case studies: Revolut prospectus, N26 funding announcements
- European Banking Authority reports on digital-only banks

---

### Lesson 5: Open Banking and APIs

**Learning Objectives:**
- Explain the principles and regulations behind open banking
- Understand API architecture in financial services
- Identify use cases enabled by open banking
- Evaluate privacy and security considerations

**Topics Covered:**
- PSD2 (Europe), Open Banking (UK), and global equivalents
- API types: account information, payment initiation, confirmation of funds
- OAuth 2.0 and secure API authentication
- Third-party providers (TPPs) and aggregators
- Use cases: account aggregation, personal finance management, lending
- Data ownership and consent management
- Technical standards: OpenAPI, JSON, REST

**Practical Activity:**
Use Python to interact with an open banking sandbox API (e.g., Plaid, TrueLayer). Retrieve mock account data and create a simple transaction categorization tool.

**Suggested Reading:**
- European Commission (2015). "PSD2 Directive"
- Open Banking Implementation Entity (UK) standards documentation
- Zachariadis, M., & Ozcan, P. (2017). "The API Economy and Digital Transformation in Financial Services"

---

### Lesson 6: Digital Identity and Authentication

**Learning Objectives:**
- Understand multi-factor authentication (MFA) methods
- Explain biometric authentication technologies
- Analyze digital identity verification processes (KYC/AML)
- Evaluate privacy-preserving identity solutions

**Topics Covered:**
- Authentication factors: knowledge, possession, inherence
- Biometrics: fingerprint, face recognition, voice, behavioral
- Digital identity verification: eKYC, video verification, document authentication
- Know Your Customer (KYC) and Anti-Money Laundering (AML) requirements
- Federated identity and single sign-on (SSO)
- Self-sovereign identity and decentralized identifiers
- Privacy regulations (GDPR, CCPA) and identity data

**Practical Activity:**
Implement a Python-based MFA system demonstrating time-based one-time passwords (TOTP). Analyze the security trade-offs between different authentication methods.

**Suggested Reading:**
- NIST (2017). "Digital Identity Guidelines"
- FATF (2020). "Guidance on Digital Identity"
- Allen, C. (2016). "The Path to Self-Sovereign Identity"

---

### Lesson 7: Peer-to-Peer Lending

**Learning Objectives:**
- Explain how P2P lending platforms operate
- Understand credit risk assessment in P2P lending
- Analyze investor returns and borrower costs
- Identify regulatory challenges and failures (e.g., Lendy, FundingCircle)

**Topics Covered:**
- P2P lending business models: marketplace vs. balance sheet
- Credit scoring and risk-based pricing
- Loan origination, underwriting, and servicing
- Investor diversification and auto-invest algorithms
- Default rates, recovery rates, and investor protections
- Regulatory evolution: from unregulated to supervised
- Notable failures and lessons learned

**Practical Activity:**
Build a Python credit scoring model using synthetic borrower data. Simulate a P2P lending portfolio and calculate expected returns under different default scenarios.

**Suggested Reading:**
- Morse, A. (2015). "Peer-to-Peer Crowdfunding: Information and the Potential for Disruption"
- FCA (UK) reports on P2P lending regulation
- Case study: LendingClub prospectus and performance data

---

### Lesson 8: Robo-Advisors and Digital Wealth

**Learning Objectives:**
- Understand how robo-advisors automate investment management
- Explain modern portfolio theory (MPT) and its application
- Compare robo-advisor business models and fee structures
- Analyze the hybrid human-robo advisory model

**Topics Covered:**
- Robo-advisor definition and evolution
- Portfolio construction using MPT and ETFs
- Risk profiling questionnaires and asset allocation
- Rebalancing algorithms and tax-loss harvesting
- Fee structures: AUM-based, subscription, transaction
- Major players: Betterment, Wealthfront, Vanguard Personal Advisor
- Hybrid models combining human advisors with automation

**Practical Activity:**
Implement a basic robo-advisor algorithm in Python: risk profiling, asset allocation based on modern portfolio theory, and automatic rebalancing. Visualize efficient frontiers.

**Suggested Reading:**
- Markowitz, H. (1952). "Portfolio Selection" (foundational MPT paper)
- D'Acunto, F., et al. (2019). "Robo-Advising"
- Deloitte (2020). "The expansion of robo-advisory in wealth management"

---

### Lesson 9: InsurTech

**Learning Objectives:**
- Identify key insurtech innovation areas
- Understand usage-based insurance (UBI) and parametric insurance
- Explain how AI is transforming underwriting and claims
- Analyze embedded insurance models

**Topics Covered:**
- InsurTech landscape: distribution, underwriting, claims, new products
- Usage-based insurance (UBI): telematics, pay-as-you-drive
- Parametric insurance: weather, flight delay, earthquake
- AI in underwriting: automated risk assessment
- Claims automation: computer vision, fraud detection
- Embedded insurance: integrated into purchase flows
- Microinsurance and on-demand insurance models

**Practical Activity:**
Build a Python parametric insurance simulator for flight delay insurance. Model payout triggers based on actual flight delay data and calculate premium structures.

**Suggested Reading:**
- Swiss Re (2021). "InsurTech: Opportunities and Challenges"
- McKinsey (2020). "Insurance beyond digital: The rise of ecosystems and platforms"
- Case study: Lemonade IPO prospectus

---

### Lesson 10: RegTech

**Learning Objectives:**
- Define regulatory technology (RegTech) and its scope
- Understand how RegTech helps with compliance automation
- Identify key use cases: AML, KYC, transaction monitoring, reporting
- Analyze the intersection of RegTech and SupTech

**Topics Covered:**
- RegTech definition and drivers
- Compliance challenges: cost, complexity, regulatory change
- AML/KYC automation: identity verification, screening, monitoring
- Transaction monitoring and suspicious activity reporting (SAR)
- Regulatory reporting automation (e.g., MiFID II, EMIR)
- Natural language processing for regulatory interpretation
- SupTech: supervisor technology for regulators

**Practical Activity:**
Create a Python transaction monitoring system that flags suspicious patterns (e.g., structuring, rapid movement). Implement basic AML rules and visualize alert generation.

**Suggested Reading:**
- FSB (2017). "Artificial intelligence and machine learning in financial services"
- Institute of International Finance (2016). "RegTech in Financial Services: Technology Solutions for Compliance"
- Arner, D.W., et al. (2017). "FinTech, RegTech, and the Reconceptualization of Financial Regulation"

---

### Lesson 11: Regulatory Frameworks

**Learning Objectives:**
- Understand key financial regulations affecting fintech
- Explain regulatory sandboxes and innovation hubs
- Identify licensing requirements for different fintech activities
- Analyze regulatory arbitrage and cross-border challenges

**Topics Covered:**
- Banking regulations: Basel III, capital requirements, deposit insurance
- Payment regulations: PSD2, EMD (E-Money Directive), GDPR
- Securities regulations: MiFID II, crowdfunding rules
- Licensing regimes: banking license, e-money license, payment institution
- Regulatory sandboxes: FCA (UK), MAS (Singapore), FINMA (Switzerland)
- Cross-border regulatory challenges and passporting
- Consumer protection and investor protection rules

**Practical Activity:**
Map regulatory requirements for launching a neobank in three different jurisdictions (EU, US, Singapore). Create a Python-based compliance checklist generator.

**Suggested Reading:**
- FCA (2015). "Regulatory Sandbox" documentation
- European Commission PSD2 and EMD2 directives
- World Bank (2020). "Global Experiences from Regulatory Sandboxes"

---

### Lesson 12: Fintech Business Models

**Learning Objectives:**
- Analyze revenue models of major fintech sectors
- Understand network effects and platform economics
- Calculate unit economics and path to profitability
- Evaluate competitive moats and defensibility

**Topics Covered:**
- Revenue models: transaction fees, subscriptions, interchange, lending margins, data
- Network effects: two-sided markets, marketplace dynamics
- Unit economics: CAC, LTV, contribution margin, burn rate
- Venture capital funding and valuation metrics
- Path to profitability: case studies of successful and failed fintechs
- Competitive advantages: regulation, data, network effects, brand
- Exit strategies: IPO, acquisition, sustainable business

**Practical Activity:**
Build a Python financial model for a hypothetical fintech startup. Project revenue, costs, and cash flow over 5 years. Analyze sensitivity to key assumptions (growth rate, CAC, LTV).

**Suggested Reading:**
- Parker, G., et al. (2016). "Platform Revolution" (chapters on fintech)
- CB Insights fintech unicorn reports
- Public fintech financial statements: Square, PayPal, Robinhood

---

## MODULE 2: BLOCKCHAIN (Lessons 13-24)

### Lesson 13: What is Blockchain?

**Learning Objectives:**
- Define blockchain and distributed ledger technology
- Understand the difference between databases and blockchains
- Explain the core properties: immutability, transparency, decentralization
- Identify use cases beyond cryptocurrency

**Topics Covered:**
- Blockchain definition and history (from Bitcoin whitepaper 2008)
- Distributed ledger technology (DLT) vs. traditional databases
- Core properties: decentralization, immutability, transparency, consensus
- Public vs. private vs. consortium blockchains
- Blockchain trilemma: scalability, security, decentralization
- Use cases: cryptocurrency, supply chain, identity, voting, finance
- Common misconceptions about blockchain

**Practical Activity:**
Build a simple blockchain in Python from scratch: create blocks, link them with hashes, demonstrate immutability by attempting to alter historical blocks.

**Suggested Reading:**
- Nakamoto, S. (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System"
- Narayanan, A., et al. (2016). "Bitcoin and Cryptocurrency Technologies" (Chapter 1)
- World Economic Forum (2016). "The Future of Financial Infrastructure"

---

### Lesson 14: Blocks and Cryptographic Hashing

**Learning Objectives:**
- Explain the structure of a block
- Understand cryptographic hash functions (SHA-256)
- Demonstrate how blocks are linked via hashes
- Explain Merkle trees and their efficiency benefits

**Topics Covered:**
- Block structure: header (previous hash, timestamp, nonce) and body (transactions)
- Cryptographic hash functions: properties (deterministic, fixed-size, one-way, collision-resistant)
- SHA-256 algorithm and its use in Bitcoin
- Linking blocks: previous block hash creates the chain
- Merkle trees: efficient transaction verification
- Block size limits and scalability implications
- Genesis block and blockchain initialization

**Practical Activity:**
Implement SHA-256 hashing in Python. Build a Merkle tree from a set of transactions and demonstrate efficient verification of transaction inclusion.

**Suggested Reading:**
- Antonopoulos, A. (2017). "Mastering Bitcoin" (Chapter 7: The Blockchain)
- NIST documentation on SHA-256
- Merkle, R.C. (1988). "A Digital Signature Based on a Conventional Encryption Function"

---

### Lesson 15: Public Key Cryptography and Digital Signatures

**Learning Objectives:**
- Understand asymmetric cryptography fundamentals
- Explain how public/private key pairs work
- Demonstrate digital signature creation and verification
- Identify the role of addresses in blockchain systems

**Topics Covered:**
- Symmetric vs. asymmetric cryptography
- Public key cryptography: RSA, elliptic curve (ECDSA, secp256k1)
- Key pair generation: private key, public key, address
- Digital signatures: signing transactions with private keys
- Signature verification using public keys
- Address derivation from public keys (hashing and encoding)
- Key management and wallet security

**Practical Activity:**
Implement ECDSA signature creation and verification in Python using a cryptography library. Generate a key pair, sign a message, and verify the signature.

**Suggested Reading:**
- Diffie, W., & Hellman, M. (1976). "New Directions in Cryptography"
- Johnson, D., et al. (2001). "The Elliptic Curve Digital Signature Algorithm (ECDSA)"
- Antonopoulos, A. (2017). "Mastering Bitcoin" (Chapter 4: Keys, Addresses)

---

### Lesson 16: Proof of Work

**Learning Objectives:**
- Explain the proof-of-work consensus mechanism
- Understand mining: nonce search and difficulty adjustment
- Calculate mining economics and energy consumption
- Analyze the 51% attack and network security

**Topics Covered:**
- Consensus problem in distributed systems
- Proof of work (PoW): computational puzzle solving
- Mining process: finding nonce such that hash < target
- Difficulty adjustment to maintain block time (Bitcoin: ~10 min)
- Mining rewards: block subsidy + transaction fees
- Mining economics: hardware (ASICs), electricity, pools
- Energy consumption and environmental concerns
- 51% attacks and economic security model

**Practical Activity:**
Build a proof-of-work mining simulator in Python. Implement difficulty adjustment and calculate the probability of finding a valid block based on hash rate.

**Suggested Reading:**
- Nakamoto, S. (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System" (Section 4)
- Cambridge Bitcoin Electricity Consumption Index
- Budish, E. (2018). "The Economic Limits of Bitcoin and the Blockchain"

---

### Lesson 17: Proof of Stake

**Learning Objectives:**
- Explain the proof-of-stake consensus mechanism
- Compare PoW vs. PoS: energy, security, centralization
- Understand validator selection and slashing
- Analyze Ethereum's transition to PoS (The Merge)

**Topics Covered:**
- Proof of stake (PoS) fundamentals
- Validator selection: stake-weighted random selection
- Block proposal and attestation in PoS
- Slashing: penalties for malicious or negligent behavior
- Nothing-at-stake problem and solutions
- Energy efficiency: PoS vs. PoW comparison
- Ethereum 2.0 / The Merge (2022) case study
- Centralization concerns: stake concentration

**Practical Activity:**
Simulate a proof-of-stake validator selection process in Python. Model validator rewards and slashing penalties under different scenarios.

**Suggested Reading:**
- Buterin, V., & Griffith, V. (2017). "Casper the Friendly Finality Gadget"
- Ethereum Foundation (2022). "The Merge" documentation
- Saleh, F. (2021). "Blockchain without Waste: Proof-of-Stake"

---

### Lesson 18: Bitcoin Architecture

**Learning Objectives:**
- Understand Bitcoin's network architecture and protocol
- Explain UTXO (Unspent Transaction Output) model
- Trace a Bitcoin transaction from creation to confirmation
- Analyze Bitcoin's monetary policy and halving schedule

**Topics Covered:**
- Bitcoin network: peer-to-peer nodes, full nodes, SPV clients
- UTXO model vs. account model (Ethereum)
- Transaction structure: inputs, outputs, scripts
- Transaction lifecycle: broadcast, mempool, mining, confirmation
- Bitcoin monetary policy: 21 million cap, halving every 210,000 blocks
- Block reward history: 50 BTC (2009) to 3.125 BTC (2024+)
- Scalability challenges: block size, transaction throughput

**Practical Activity:**
Parse and analyze real Bitcoin transactions using Python and blockchain APIs. Visualize the UTXO graph and trace transaction chains.

**Suggested Reading:**
- Nakamoto, S. (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System"
- Antonopoulos, A. (2017). "Mastering Bitcoin" (Chapters 6, 8)
- Bitcoin Core documentation and BIPs (Bitcoin Improvement Proposals)

---

### Lesson 19: Ethereum and Smart Contracts

**Learning Objectives:**
- Explain Ethereum's purpose and differences from Bitcoin
- Understand smart contracts and the Ethereum Virtual Machine (EVM)
- Write and deploy a basic smart contract in Solidity
- Analyze gas fees and their economic role

**Topics Covered:**
- Ethereum vision: "world computer" and decentralized applications
- Account model vs. UTXO model
- Smart contracts: self-executing code on the blockchain
- Ethereum Virtual Machine (EVM) and bytecode execution
- Solidity programming language basics
- Gas: computation pricing and DoS prevention
- Transaction execution and state transitions
- Ethereum's roadmap: from PoW to PoS, sharding, rollups

**Practical Activity:**
Write a simple smart contract in Solidity (e.g., a basic token or voting contract). Deploy it to a testnet using Python and Web3.py. Interact with the contract.

**Suggested Reading:**
- Buterin, V. (2013). "Ethereum White Paper"
- Wood, G. (2014). "Ethereum Yellow Paper"
- Solidity documentation and OpenZeppelin tutorials

---

### Lesson 20: Tokens - ERC-20 and NFTs

**Learning Objectives:**
- Distinguish between coins and tokens
- Understand the ERC-20 token standard
- Explain non-fungible tokens (NFTs) and ERC-721
- Analyze token economics and use cases

**Topics Covered:**
- Coins (native assets) vs. tokens (smart contract assets)
- ERC-20: fungible token standard (balanceOf, transfer, approve)
- ERC-721: non-fungible token standard (unique digital assets)
- Token use cases: utility tokens, security tokens, governance tokens
- Initial Coin Offerings (ICOs) and token sales
- NFT applications: art, collectibles, gaming, real estate
- Token economics: supply, distribution, incentives
- Regulatory considerations: securities laws (Howey test)

**Practical Activity:**
Create an ERC-20 token smart contract in Solidity and deploy it using Python. Implement basic token transfers and query balances. Optionally, create a simple ERC-721 NFT.

**Suggested Reading:**
- ERC-20 and ERC-721 specifications (Ethereum Improvement Proposals)
- SEC (2017). "Report of Investigation Pursuant to Section 21(a): The DAO"
- Nadini, M., et al. (2021). "Mapping the NFT revolution"

---

### Lesson 21: DeFi Fundamentals

**Learning Objectives:**
- Define decentralized finance (DeFi) and its core principles
- Understand key DeFi primitives: DEXs, lending, stablecoins
- Explain liquidity pools and automated market makers (AMMs)
- Analyze risks: smart contract bugs, impermanent loss, oracle attacks

**Topics Covered:**
- DeFi definition: financial services without intermediaries
- Decentralized exchanges (DEXs): Uniswap, Sushiswap (AMM model)
- Liquidity pools and liquidity providers (LPs)
- Automated market makers (AMMs): constant product formula (x * y = k)
- Decentralized lending: Aave, Compound (overcollateralized loans)
- Yield farming and liquidity mining
- Risks: smart contract vulnerabilities, impermanent loss, liquidation
- Oracle problem: getting real-world data on-chain

**Practical Activity:**
Simulate a constant product AMM (Uniswap-style) in Python. Model liquidity provision, swaps, and calculate impermanent loss under different price scenarios.

**Suggested Reading:**
- Adams, H., et al. (2020). "Uniswap v2 Core" (whitepaper)
- Schär, F. (2021). "Decentralized Finance: On Blockchain- and Smart Contract-Based Financial Markets"
- DeFi Llama documentation and analytics

---

### Lesson 22: Stablecoins and the Terra/Luna Case

**Learning Objectives:**
- Explain different stablecoin mechanisms (fiat-backed, crypto-backed, algorithmic)
- Understand the risks of algorithmic stablecoins
- Analyze the Terra/Luna collapse (May 2022)
- Evaluate regulatory responses to stablecoins

**Topics Covered:**
- Stablecoin types: fiat-collateralized (USDC, USDT), crypto-collateralized (DAI), algorithmic (UST)
- Fiat-backed: reserves, audits, centralization risks
- Crypto-backed: overcollateralization, stability mechanisms (MakerDAO)
- Algorithmic stablecoins: supply expansion/contraction, death spirals
- Terra/Luna case study: UST de-peg, LUNA hyperinflation, $40B collapse
- Systemic risks and contagion effects
- Regulatory frameworks: MiCA (EU), stablecoin bills (US)

**Practical Activity:**
Build a Python simulation of an algorithmic stablecoin mechanism (Terra-style). Model the death spiral: stablecoin de-peg triggers token minting, causing hyperinflation.

**Suggested Reading:**
- Do Kwon (2019). "Terra Money: Stability and Adoption" (whitepaper)
- Briola, A., et al. (2023). "Anatomy of a Stablecoin's Failure: The Terra-Luna Case"
- FSB (2020). "Regulation, Supervision and Oversight of 'Global Stablecoin' Arrangements"

---

### Lesson 23: Security and Notable Hacks

**Learning Objectives:**
- Identify common blockchain security vulnerabilities
- Understand reentrancy attacks, oracle manipulation, and bridge exploits
- Analyze major hacks: The DAO, Poly Network, Ronin Bridge
- Explain best practices for smart contract security

**Topics Covered:**
- Smart contract vulnerabilities: reentrancy, integer overflow, access control
- The DAO hack (2016): $60M stolen via reentrancy, Ethereum hard fork
- Oracle manipulation attacks: flash loans and price manipulation
- Bridge hacks: Poly Network ($600M), Ronin Bridge ($625M), Wormhole ($325M)
- Private key compromises and custody risks
- 51% attacks on smaller blockchains
- Audit practices: formal verification, bug bounties, security tools
- Insurance protocols and loss recovery mechanisms

**Practical Activity:**
Implement a vulnerable smart contract in Solidity with a reentrancy bug. Write a Python script to exploit it on a local blockchain. Then fix the vulnerability.

**Suggested Reading:**
- Atzei, N., et al. (2017). "A Survey of Attacks on Ethereum Smart Contracts"
- Trail of Bits (ongoing). "Not So Smart Contracts" (GitHub repository)
- Post-mortem reports: The DAO, Poly Network, Ronin Bridge

---

### Lesson 24: Blockchain Regulation and Future

**Learning Objectives:**
- Understand the regulatory landscape for cryptocurrencies and blockchain
- Analyze different regulatory approaches (US, EU, Asia)
- Identify emerging trends: CBDCs, institutional adoption, ESG concerns
- Evaluate the future of blockchain in finance

**Topics Covered:**
- Regulatory approaches: US (SEC/CFTC), EU (MiCA), Asia (varied)
- Securities classification: Howey test, utility vs. security tokens
- AML/KYC requirements for exchanges and DeFi
- Tax treatment of crypto assets
- Central Bank Digital Currencies (CBDCs): design choices, pilots
- Institutional adoption: Bitcoin ETFs, corporate treasuries, custody solutions
- Environmental concerns: carbon footprint, proof-of-stake transition
- Future outlook: scalability (Layer 2, sharding), interoperability, real-world assets

**Practical Activity:**
Create a Python-based regulatory compliance checker for crypto transactions. Map out CBDC design choices and compare different central bank approaches.

**Suggested Reading:**
- BIS (2020). "Central Bank Digital Currencies: Foundational Principles and Core Features"
- European Commission (2020). "Markets in Crypto-Assets (MiCA) Regulation"
- Auer, R., & Böhme, R. (2020). "The Technology of Retail Central Bank Digital Currency"

---

## MODULE 3: AI/ML IN FINANCE (Lessons 25-36)

### Lesson 25: Introduction to AI/ML in Finance

**Learning Objectives:**
- Define artificial intelligence, machine learning, and deep learning
- Understand the AI/ML workflow: data, training, evaluation, deployment
- Identify financial applications of AI/ML across the industry
- Recognize limitations and ethical considerations

**Topics Covered:**
- AI vs. ML vs. deep learning: definitions and relationships
- Supervised, unsupervised, and reinforcement learning
- The ML workflow: problem framing, data collection, feature engineering, model training, evaluation, deployment
- Financial use cases: trading, risk management, fraud detection, customer service, credit scoring
- Data challenges in finance: quality, availability, privacy
- Black box problem and model interpretability
- Ethical considerations: bias, fairness, transparency

**Practical Activity:**
Set up a Python ML environment (pandas, numpy, scikit-learn). Load a financial dataset (e.g., stock prices, credit data) and perform exploratory data analysis (EDA).

**Suggested Reading:**
- Lopez de Prado, M. (2018). "Advances in Financial Machine Learning" (Introduction)
- FSB (2017). "Artificial Intelligence and Machine Learning in Financial Services"
- Goodfellow, I., et al. (2016). "Deep Learning" (Chapter 1)

---

### Lesson 26: Financial Data Types and Preparation

**Learning Objectives:**
- Identify different types of financial data (time series, cross-sectional, panel)
- Understand data preprocessing: cleaning, normalization, feature engineering
- Handle missing data and outliers in financial datasets
- Create features from raw financial data (technical indicators, fundamentals)

**Topics Covered:**
- Financial data types: time series (prices, returns), cross-sectional (fundamentals), panel (combined)
- Data sources: market data vendors (Bloomberg, Reuters), exchanges, alternative data
- Data quality issues: missing values, outliers, survivorship bias, look-ahead bias
- Preprocessing: normalization, standardization, log returns
- Feature engineering: technical indicators (moving averages, RSI, Bollinger Bands)
- Fundamental features: P/E ratios, EPS, revenue growth
- Alternative data: sentiment, satellite imagery, credit card transactions

**Practical Activity:**
Download historical stock data using Python (yfinance or similar). Clean the data, handle missing values, and engineer technical indicator features (SMA, RSI, MACD). Visualize the results.

**Suggested Reading:**
- Lopez de Prado, M. (2018). "Advances in Financial Machine Learning" (Chapter 2: Financial Data Structures)
- Damodaran, A. (2012). "Investment Valuation" (data quality chapters)
- Pandas documentation for time series data

---

### Lesson 27: Supervised Learning - Regression

**Learning Objectives:**
- Understand regression problems in finance (price prediction, risk forecasting)
- Implement linear regression and polynomial regression
- Evaluate regression models using appropriate metrics (RMSE, MAE, R-squared)
- Recognize overfitting and apply regularization (Ridge, Lasso)

**Topics Covered:**
- Regression fundamentals: predicting continuous outcomes
- Linear regression: ordinary least squares (OLS), assumptions
- Polynomial regression and feature expansion
- Evaluation metrics: RMSE, MAE, R-squared, adjusted R-squared
- Overfitting and bias-variance tradeoff
- Regularization: Ridge (L2), Lasso (L1), Elastic Net
- Financial applications: volatility forecasting, option pricing, yield curve fitting
- Walk-forward validation and out-of-sample testing

**Practical Activity:**
Build a linear regression model in Python to predict stock returns based on multiple features. Implement Ridge and Lasso regularization. Compare model performance using cross-validation.

**Suggested Reading:**
- James, G., et al. (2013). "An Introduction to Statistical Learning" (Chapter 3: Linear Regression)
- Campbell, J.Y., et al. (1997). "The Econometrics of Financial Markets" (Chapter 2)
- scikit-learn regression documentation

---

### Lesson 28: Supervised Learning - Classification

**Learning Objectives:**
- Understand classification problems in finance (default prediction, market regime detection)
- Implement logistic regression, decision trees, and random forests
- Evaluate classification models using confusion matrix, ROC, AUC
- Handle imbalanced datasets common in finance

**Topics Covered:**
- Classification fundamentals: predicting discrete outcomes
- Logistic regression: sigmoid function, log-odds, probability estimation
- Decision trees: splitting criteria, pruning, interpretation
- Random forests: ensemble learning, bagging, feature importance
- Evaluation metrics: accuracy, precision, recall, F1-score, ROC curve, AUC
- Confusion matrix: true/false positives/negatives
- Imbalanced datasets: class weights, SMOTE, undersampling
- Financial applications: credit default, fraud detection, trade signal generation

**Practical Activity:**
Build a classification model in Python to predict credit default using a public dataset (e.g., German Credit Data). Compare logistic regression, decision trees, and random forests. Handle class imbalance.

**Suggested Reading:**
- James, G., et al. (2013). "An Introduction to Statistical Learning" (Chapter 4: Classification)
- Breiman, L. (2001). "Random Forests"
- He, H., & Garcia, E.A. (2009). "Learning from Imbalanced Data"

---

### Lesson 29: Algorithmic Trading Concepts

**Learning Objectives:**
- Understand the components of algorithmic trading systems
- Explain different trading strategies (trend following, mean reversion, arbitrage)
- Implement a simple trading strategy and backtest it
- Recognize the challenges of overfitting and data snooping

**Topics Covered:**
- Algorithmic trading overview: execution algorithms vs. alpha-seeking strategies
- Strategy types: trend following, mean reversion, statistical arbitrage, market making
- Signal generation using ML: classification (buy/sell) or regression (price forecast)
- Backtesting: historical simulation, transaction costs, slippage
- Performance metrics: Sharpe ratio, maximum drawdown, win rate
- Overfitting dangers: multiple testing, data snooping, optimization bias
- Walk-forward analysis and out-of-sample testing
- Risk management: position sizing, stop-loss, portfolio constraints

**Practical Activity:**
Implement a simple mean reversion strategy in Python using moving averages. Backtest it on historical stock data, accounting for transaction costs. Calculate Sharpe ratio and maximum drawdown.

**Suggested Reading:**
- Chan, E. (2009). "Quantitative Trading: How to Build Your Own Algorithmic Trading Business"
- Lopez de Prado, M. (2018). "Advances in Financial Machine Learning" (Chapter 7: Cross-Validation in Finance)
- Bailey, D.H., et al. (2014). "The Probability of Backtest Overfitting"

---

### Lesson 30: Credit Scoring and Risk Models

**Learning Objectives:**
- Understand credit scoring models and their evolution
- Implement logistic regression for credit default prediction
- Explain model validation and regulatory requirements (Basel)
- Analyze the use of alternative data in credit assessment

**Topics Covered:**
- Traditional credit scoring: FICO score, credit bureaus, traditional features
- ML for credit scoring: logistic regression, gradient boosting, neural networks
- Features: payment history, credit utilization, income, employment, alternative data
- Model validation: IV, PSI, discrimination (AUC), calibration
- Regulatory requirements: Basel II/III, model risk management, stress testing
- Explainability requirements: ECOA, FCRA (US), GDPR (EU)
- Alternative data: mobile phone usage, social media, psychometrics
- Ethical concerns: bias, fairness, financial inclusion

**Practical Activity:**
Build a credit scoring model using Python and a public dataset (LendingClub, Kaggle). Implement logistic regression and gradient boosting. Evaluate using AUC and calibration plots. Analyze feature importance.

**Suggested Reading:**
- Thomas, L.C. (2009). "Consumer Credit Models: Pricing, Profit and Portfolios"
- Basel Committee (2005). "Studies on the Validation of Internal Rating Systems"
- Khandani, A.E., et al. (2010). "Consumer Credit-Risk Models via Machine-Learning Algorithms"

---

### Lesson 31: Fraud Detection and AML

**Learning Objectives:**
- Understand fraud patterns in financial transactions
- Implement anomaly detection techniques (isolation forest, autoencoders)
- Explain supervised vs. unsupervised approaches to fraud detection
- Analyze the challenges of extreme class imbalance

**Topics Covered:**
- Fraud types: card fraud, payment fraud, identity theft, account takeover
- AML patterns: structuring, layering, integration, suspicious activity
- Supervised methods: classification with labeled fraud examples
- Unsupervised methods: anomaly detection, clustering, autoencoders
- Hybrid approaches: semi-supervised learning, active learning
- Extreme class imbalance: fraud rate often < 0.1%
- Evaluation: precision-recall tradeoff, cost-sensitive learning
- Real-time detection and rule engines

**Practical Activity:**
Implement fraud detection using Python on a credit card transaction dataset (Kaggle). Try both supervised (random forest) and unsupervised (isolation forest, autoencoder) approaches. Handle extreme imbalance.

**Suggested Reading:**
- Ngai, E.W., et al. (2011). "The Application of Data Mining Techniques in Financial Fraud Detection"
- Liu, F.T., et al. (2008). "Isolation Forest"
- FATF (2021). "Opportunities and Challenges of New Technologies for AML/CFT"

---

### Lesson 32: Natural Language Processing in Finance

**Learning Objectives:**
- Understand NLP fundamentals and their financial applications
- Implement sentiment analysis on financial news and social media
- Extract information from financial documents (10-Ks, earnings calls)
- Analyze the predictive power of text data for market movements

**Topics Covered:**
- NLP basics: tokenization, stemming, lemmatization, stopwords
- Sentiment analysis: lexicon-based (FinBERT, Loughran-McDonald) vs. ML-based
- Document representation: bag-of-words, TF-IDF, word embeddings
- Financial text sources: news, earnings calls, 10-K filings, social media (Twitter/X)
- Named entity recognition (NER): extracting companies, people, amounts
- Topic modeling: LDA for discovering themes in financial documents
- Predictive modeling: using sentiment/text features for stock returns
- Limitations: causality, confounding factors, market efficiency

**Practical Activity:**
Implement sentiment analysis on financial news headlines using Python and a pre-trained model (FinBERT or VADER). Correlate sentiment scores with stock price movements. Visualize results.

**Suggested Reading:**
- Loughran, T., & McDonald, B. (2011). "When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks"
- Tetlock, P.C. (2007). "Giving Content to Investor Sentiment"
- Araci, D. (2019). "FinBERT: Financial Sentiment Analysis with Pre-trained Language Models"

---

### Lesson 33: Robo-Advisors - ML Perspectives

**Learning Objectives:**
- Understand how ML enhances robo-advisory services
- Implement portfolio optimization using ML techniques
- Explain reinforcement learning for dynamic asset allocation
- Analyze personalization and behavioral finance integration

**Topics Covered:**
- Traditional robo-advisors: rule-based MPT, risk profiling
- ML enhancements: better risk profiling via classification, return forecasting
- Portfolio optimization: mean-variance (Markowitz) vs. ML-based approaches
- Reinforcement learning: dynamic asset allocation, rebalancing policies
- Behavioral finance: incorporating investor biases, personalized recommendations
- Explainability: justifying recommendations to clients
- Regulatory considerations: suitability, fiduciary duty
- Hybrid models: combining human advisors with ML insights

**Practical Activity:**
Implement a portfolio optimization model in Python using historical returns. Compare traditional mean-variance optimization with ML-based expected return forecasts. Add reinforcement learning for dynamic rebalancing.

**Suggested Reading:**
- Fabozzi, F.J., et al. (2007). "Robust Portfolio Optimization and Management"
- Moody, J., & Saffell, M. (2001). "Learning to Trade via Direct Reinforcement"
- D'Acunto, F., et al. (2019). "Robo-Advising" (ML aspects)

---

### Lesson 34: Market Prediction Limitations

**Learning Objectives:**
- Understand the Efficient Market Hypothesis (EMH) and its implications
- Recognize the challenges of predicting financial markets
- Explain the difference between correlation and causation
- Identify common pitfalls: overfitting, look-ahead bias, data snooping

**Topics Covered:**
- Efficient Market Hypothesis: weak, semi-strong, strong forms
- Random walk theory and the unpredictability of returns
- Signal vs. noise: low signal-to-noise ratio in financial data
- Overfitting: fitting noise instead of signal, in-sample vs. out-of-sample
- Look-ahead bias: using future information in models
- Survivorship bias: only considering surviving assets
- Data snooping: multiple testing without correction
- Non-stationarity: financial relationships change over time
- Fundamental limits: markets adapt, strategies decay

**Practical Activity:**
Demonstrate overfitting in Python by training increasingly complex models on stock data. Show in-sample vs. out-of-sample performance divergence. Implement walk-forward validation.

**Suggested Reading:**
- Fama, E.F. (1970). "Efficient Capital Markets: A Review of Theory and Empirical Work"
- Lo, A.W. (2004). "The Adaptive Markets Hypothesis"
- Bailey, D.H., & Lopez de Prado, M. (2014). "The Deflated Sharpe Ratio"

---

### Lesson 35: Explainability and Bias in Finance AI

**Learning Objectives:**
- Understand the importance of model explainability in finance
- Implement SHAP and LIME for model interpretation
- Identify sources of bias in financial ML models
- Analyze regulatory requirements for explainable AI

**Topics Covered:**
- Black box problem: complex models (neural networks, ensembles) lack transparency
- Explainability techniques: feature importance, partial dependence plots, SHAP, LIME
- SHAP (SHapley Additive exPlanations): game-theoretic feature attribution
- LIME (Local Interpretable Model-agnostic Explanations): local linear approximations
- Bias sources: historical data bias, sampling bias, label bias, algorithm bias
- Fairness metrics: demographic parity, equalized odds, disparate impact
- Regulatory requirements: right to explanation (GDPR), fair lending laws (ECOA)
- Tradeoff: accuracy vs. interpretability

**Practical Activity:**
Train a black-box model (random forest or XGBoost) on credit data. Use SHAP and LIME in Python to explain individual predictions. Analyze the model for potential bias across demographic groups.

**Suggested Reading:**
- Lundberg, S.M., & Lee, S.I. (2017). "A Unified Approach to Interpreting Model Predictions" (SHAP)
- Ribeiro, M.T., et al. (2016). "Why Should I Trust You?: Explaining the Predictions of Any Classifier" (LIME)
- Barocas, S., & Selbst, A.D. (2016). "Big Data's Disparate Impact"

---

### Lesson 36: AI Regulation and the Future

**Learning Objectives:**
- Understand the regulatory landscape for AI in finance
- Analyze model risk management frameworks (SR 11-7)
- Identify emerging trends: foundation models, quantum ML, synthetic data
- Evaluate the future impact of AI on financial services

**Topics Covered:**
- Regulatory frameworks: SR 11-7 (Fed model risk management), EU AI Act, GDPR
- Model risk management: development, validation, governance
- Stress testing and scenario analysis for AI models
- AI-specific risks: adversarial attacks, data poisoning, concept drift
- Emerging trends: large language models (GPTs) in finance, multimodal models
- Quantum machine learning: potential future applications
- Synthetic data: privacy-preserving training, data augmentation
- Future outlook: AI-native banks, autonomous trading, hyper-personalization
- Workforce implications: augmentation vs. replacement

**Practical Activity:**
Create a Python-based model risk management framework template. Implement model monitoring for concept drift. Research and present on a cutting-edge AI application in finance (LLMs, quantum, etc.).

**Suggested Reading:**
- Federal Reserve (2011). "SR 11-7: Guidance on Model Risk Management"
- European Commission (2021). "Proposal for an AI Act"
- Cao, L. (2022). "AI in Finance: Challenges, Techniques, and Opportunities"

---

## MODULE 4: TRADITIONAL DIGITAL FINANCE (Lessons 37-48)

### Lesson 37: Financial Markets and Institutions Overview

**Learning Objectives:**
- Understand the structure of global financial markets
- Identify key financial institutions and their roles
- Explain market participants: buy-side, sell-side, market makers
- Recognize the technology stack supporting modern markets

**Topics Covered:**
- Market structure: equities, fixed income, derivatives, FX, commodities
- Financial institutions: commercial banks, investment banks, asset managers, insurance, pension funds
- Market participants: buy-side (asset managers, hedge funds), sell-side (brokers, dealers), market makers
- Exchanges vs. OTC markets
- Clearing and settlement: CCPs (central counterparties), CSDs (central securities depositories)
- Regulatory structure: SEC, CFTC, FINRA (US), FCA (UK), ESMA (EU)
- Technology evolution: from open outcry to electronic trading

**Practical Activity:**
Map the global financial system using Python to create an interactive visualization showing connections between institutions, markets, and regulators. Analyze market data from different asset classes.

**Suggested Reading:**
- Hull, J.C. (2018). "Options, Futures, and Other Derivatives" (Chapter 1: Introduction)
- BIS (2020). "Triennial Central Bank Survey of Foreign Exchange and OTC Derivatives Markets"
- Admati, A.R., & Hellwig, M. (2013). "The Bankers' New Clothes" (institutional overview)

---

### Lesson 38: Core Banking Systems

**Learning Objectives:**
- Understand the architecture of core banking systems
- Explain key functions: deposits, loans, payments, accounting
- Identify legacy challenges and modernization approaches
- Analyze cloud migration and API-first architectures

**Topics Covered:**
- Core banking definition: central system managing accounts, transactions, products
- Key modules: customer information, deposits, loans, general ledger, payments
- Legacy systems: mainframe-based (IBM z/OS, COBOL), monolithic architecture
- Challenges: technical debt, inflexibility, high maintenance costs
- Modernization approaches: wrap-and-replace, gradual migration, greenfield
- Cloud-native core banking: Thought Machine, Mambu, 10x Banking
- API-first architecture: microservices, containerization, event-driven
- Real-time processing vs. batch processing

**Practical Activity:**
Design a simplified core banking system architecture using Python to model accounts, transactions, and balances. Implement basic operations: deposit, withdrawal, transfer. Simulate batch vs. real-time processing.

**Suggested Reading:**
- Accenture (2020). "Core Banking Transformation"
- Gartner reports on core banking platforms
- Thought Machine (2019). "Vault Core Banking Engine" whitepaper

---

### Lesson 39: Payment Rails and SWIFT

**Learning Objectives:**
- Understand domestic payment rails (ACH, Faster Payments, SEPA)
- Explain SWIFT network and cross-border payments
- Identify correspondent banking and nostro/vostro accounts
- Analyze emerging alternatives: ISO 20022, blockchain, stablecoins

**Topics Covered:**
- Payment rails: infrastructure for moving money between banks
- Domestic systems: ACH (US), Faster Payments (UK), SEPA (EU), UPI (India)
- SWIFT: messaging network for cross-border payments (not actual money movement)
- Correspondent banking: intermediary banks, nostro/vostro accounts
- Cross-border challenges: delays (3-5 days), high fees, opacity
- ISO 20022: modern messaging standard with richer data
- Real-time gross settlement (RTGS) systems: Fedwire, TARGET2
- Alternatives: Ripple, stablecoins, CBDC networks

**Practical Activity:**
Simulate a cross-border payment flow in Python, modeling correspondent banking chain, FX conversion, and fees. Compare traditional SWIFT vs. blockchain-based settlement in terms of time and cost.

**Suggested Reading:**
- SWIFT (2021). "SWIFT Standards MT and ISO 20022"
- BIS (2018). "Cross-border retail payments"
- World Bank (2020). "Remittance Prices Worldwide" reports

---

### Lesson 40: Electronic Trading and Order Types

**Learning Objectives:**
- Understand electronic trading platforms and order routing
- Explain different order types: market, limit, stop, iceberg
- Analyze order book mechanics and price discovery
- Identify smart order routing (SOR) and execution algorithms

**Topics Covered:**
- Electronic trading evolution: from phone-based to algorithmic
- Order types: market, limit, stop, stop-limit, iceberg, fill-or-kill, good-till-canceled
- Order book: bid-ask spread, depth, liquidity
- Price discovery: matching engine, order priority (price-time, pro-rata)
- Trade execution: immediate-or-cancel vs. resting orders
- Smart order routing (SOR): finding best execution across venues
- Execution algorithms: VWAP, TWAP, implementation shortfall, POV
- Pre-trade and post-trade transparency (MiFID II)

**Practical Activity:**
Build a simple order book matching engine in Python. Simulate different order types and observe price formation. Implement a basic VWAP execution algorithm.

**Suggested Reading:**
- Harris, L. (2003). "Trading and Exchanges: Market Microstructure for Practitioners"
- Kissell, R. (2013). "The Science of Algorithmic Trading and Portfolio Management"
- Hasbrouck, J. (2007). "Empirical Market Microstructure"

---

### Lesson 41: Market Microstructure and HFT

**Learning Objectives:**
- Understand market microstructure: spread, depth, latency
- Explain high-frequency trading (HFT) strategies
- Analyze the role of market makers and liquidity provision
- Evaluate debates around HFT: benefits vs. risks

**Topics Covered:**
- Market microstructure: bid-ask spread, order book depth, tick size, latency
- High-frequency trading (HFT): definition, technology (co-location, FPGAs)
- HFT strategies: market making, arbitrage, momentum ignition, latency arbitrage
- Market maker role: providing liquidity, earning spread
- Speed advantage: microsecond-level latency, race to zero
- Market quality: liquidity, volatility, price efficiency
- Flash crashes: May 6, 2010, role of HFT
- Regulatory responses: circuit breakers, speed bumps, tick size pilot

**Practical Activity:**
Simulate a simplified HFT market-making strategy in Python. Model order book dynamics, latency, and adverse selection. Analyze profitability and risk.

**Suggested Reading:**
- Budish, E., et al. (2015). "The High-Frequency Trading Arms Race"
- SEC (2010). "Findings Regarding the Market Events of May 6, 2010" (Flash Crash report)
- Lewis, M. (2014). "Flash Boys" (popular account, take with critical perspective)

---

### Lesson 42: Risk Management Systems

**Learning Objectives:**
- Understand enterprise risk management frameworks
- Explain market, credit, and operational risk measurement
- Implement Value at Risk (VaR) and stress testing
- Analyze real-time risk monitoring systems

**Topics Covered:**
- Risk types: market risk, credit risk, operational risk, liquidity risk
- Market risk: Value at Risk (VaR), Expected Shortfall (ES), Greeks (delta, gamma, vega)
- Credit risk: probability of default (PD), loss given default (LGD), exposure at default (EAD)
- Operational risk: Basel III standardized approach, loss distribution
- Risk management systems: pre-trade, real-time, end-of-day
- VaR methodologies: historical simulation, variance-covariance, Monte Carlo
- Stress testing and scenario analysis
- Risk limits and breaches: automated alerts and escalation

**Practical Activity:**
Implement VaR calculation in Python using historical simulation and Monte Carlo methods. Build a simple risk dashboard that monitors portfolio exposure and triggers alerts.

**Suggested Reading:**
- Jorion, P. (2006). "Value at Risk: The New Benchmark for Managing Financial Risk"
- Basel Committee (2019). "Minimum Capital Requirements for Market Risk"
- Danielsson, J. (2011). "Financial Risk Forecasting"

---

### Lesson 43: RegTech and Compliance Systems

**Learning Objectives:**
- Understand regulatory compliance requirements in trading
- Explain transaction reporting (MiFID II, EMIR, Dodd-Frank)
- Implement trade surveillance and market abuse detection
- Analyze regulatory reporting automation

**Topics Covered:**
- Regulatory reporting: MiFID II (EU), EMIR (derivatives), Dodd-Frank (US)
- Transaction reporting: who, what, when, where, how much
- Best execution reporting and RTS 27/28 (MiFID II)
- Market abuse surveillance: spoofing, layering, wash trades, insider trading
- Trade surveillance systems: pattern detection, alerts, case management
- RegTech solutions: NLP for regulation interpretation, automated reporting
- Data quality and reconciliation challenges
- RegTech vendors: Nasdaq Surveillance, FIS, Comply Advantage

**Practical Activity:**
Build a simple trade surveillance system in Python that detects suspicious patterns (e.g., spoofing, wash trades). Generate regulatory reports in required formats (XML, JSON).

**Suggested Reading:**
- ESMA (2016). "MiFID II/MiFIR" regulatory technical standards
- FCA (2015). "Market Abuse Regulation" guidance
- CFTC (2013). "Dodd-Frank Act" implementation rules

---

### Lesson 44: Capital Markets Technology

**Learning Objectives:**
- Understand the technology stack for capital markets
- Explain front-office, middle-office, and back-office systems
- Identify key vendors: Bloomberg, Refinitiv, FactSet
- Analyze the role of FIX protocol in trading

**Topics Covered:**
- Front office: trading systems, order management (OMS), execution management (EMS)
- Middle office: risk management, P&L calculation, collateral management
- Back office: settlement, reconciliation, corporate actions, regulatory reporting
- Market data: Bloomberg Terminal, Refinitiv Eikon, FactSet
- FIX protocol: Financial Information eXchange, standardized messaging for trading
- Trading platforms: Bloomberg EMSX, Tradeweb, MarketAxess, EquiLend
- Cloud adoption: AWS, Azure, Google Cloud in capital markets
- Vendor landscape: consolidation and competition

**Practical Activity:**
Parse FIX protocol messages in Python to extract trade details. Build a simple order management system (OMS) that routes orders and tracks executions.

**Suggested Reading:**
- FIX Trading Community documentation
- Gartner Magic Quadrant for Trading Platforms
- Bloomberg and Refinitiv product documentation

---

### Lesson 45: Derivatives Technology

**Learning Objectives:**
- Understand derivatives processing lifecycle
- Explain pricing models and their implementation
- Analyze collateral management and margin systems
- Identify the impact of central clearing (Dodd-Frank, EMIR)

**Topics Covered:**
- Derivatives types: futures, options, swaps, structured products
- Trade lifecycle: execution, confirmation, valuation, collateral, settlement
- Pricing models: Black-Scholes, binomial trees, Monte Carlo, finite difference
- Greeks calculation: delta, gamma, vega, theta, rho
- Collateral management: initial margin, variation margin, margin calls
- Central clearing: CCPs (LCH, CME, Eurex), mandatory clearing post-2008
- Compression and portfolio optimization
- Derivatives systems: Calypso, Murex, Summit, TriOptima

**Practical Activity:**
Implement Black-Scholes option pricing in Python. Calculate Greeks numerically. Build a margin calculator that computes initial and variation margin for a derivatives portfolio.

**Suggested Reading:**
- Hull, J.C. (2018). "Options, Futures, and Other Derivatives"
- Gregory, J. (2014). "Central Counterparties: Mandatory Clearing and Bilateral Margin Requirements"
- ISDA documentation on derivatives lifecycle

---

### Lesson 46: Wealth Management Systems

**Learning Objectives:**
- Understand the technology supporting wealth management
- Explain portfolio management systems (PMS) and CRM integration
- Analyze rebalancing, tax optimization, and reporting
- Identify trends: robo-advisors, AI personalization, ESG integration

**Topics Covered:**
- Wealth management technology stack: CRM, PMS, trading, reporting
- Portfolio management systems: Charles River, BlackRock Aladdin, SimCorp
- Customer relationship management (CRM): Salesforce Financial Services Cloud
- Rebalancing engines: threshold-based, calendar-based, tax-aware
- Tax optimization: tax-loss harvesting, asset location, withdrawal strategies
- Client reporting: performance attribution, benchmarking, consolidated statements
- Integration with robo-advisors and digital channels
- ESG data integration and impact reporting

**Practical Activity:**
Build a portfolio rebalancing algorithm in Python with tax-loss harvesting. Generate client performance reports with attribution analysis. Integrate ESG scores.

**Suggested Reading:**
- Lusardi, A., & Mitchell, O.S. (2014). "The Economic Importance of Financial Literacy"
- BlackRock Aladdin platform documentation
- CFA Institute (2018). "From the Stockholder to the Stakeholder" (ESG integration)

---

### Lesson 47: Financial Data Vendors and Infrastructure

**Learning Objectives:**
- Understand the financial data ecosystem
- Identify major data vendors and their offerings
- Explain market data distribution: feeds, APIs, terminals
- Analyze alternative data and its growing importance

**Topics Covered:**
- Data vendor landscape: Bloomberg, Refinitiv (LSEG), FactSet, S&P Global, Morningstar
- Data types: market data (prices, quotes), reference data (identifiers, corporate actions), fundamental data
- Distribution methods: terminals, data feeds (real-time, delayed), APIs, bulk files
- Market data protocols: FIX, FAST, proprietary formats
- Data normalization and symbology: ISIN, SEDOL, CUSIP, Bloomberg ticker
- Alternative data: satellite imagery, credit card transactions, web scraping, social media
- Data quality challenges: accuracy, timeliness, coverage
- Cost management: data fees can be significant expense

**Practical Activity:**
Connect to a market data API (e.g., Alpha Vantage, IEX Cloud, Yahoo Finance) using Python. Retrieve and normalize data. Explore alternative data sources (e.g., Twitter sentiment, Google Trends).

**Suggested Reading:**
- Burton-Taylor (latest). "Global Market Data & Analysis Reports"
- Bloomberg and Refinitiv product catalogs
- Kolanovic, M., & Krishnamachari, R.T. (2017). "Big Data and AI Strategies" (JP Morgan, alternative data)

---

### Lesson 48: Central Bank Digital Currencies (CBDCs) and the Future

**Learning Objectives:**
- Understand CBDC design choices and motivations
- Analyze ongoing CBDC pilots (China, EU, Bahamas)
- Explain the potential impact on banking and payments
- Evaluate the future of digital finance: convergence of fintech, blockchain, AI

**Topics Covered:**
- CBDC definition: digital form of central bank money
- Design choices: retail vs. wholesale, account-based vs. token-based, centralized vs. distributed
- Motivations: financial inclusion, payment efficiency, monetary policy, counter private stablecoins
- Major pilots: e-CNY (China), digital euro (ECB), e-Krona (Sweden), Sand Dollar (Bahamas)
- Impact on banking: disintermediation risk, two-tier model
- Impact on payments: cross-border efficiency, programmable money
- Privacy vs. surveillance tradeoffs
- Future of digital finance: convergence of fintech, blockchain, AI, CBDCs
- Open questions: regulation, technology standards, international cooperation

**Practical Activity:**
Design a CBDC architecture in Python: choose design parameters (retail/wholesale, account/token). Simulate transactions and analyze privacy/efficiency tradeoffs. Compare with existing payment systems.

**Suggested Reading:**
- BIS (2020). "Central Bank Digital Currencies: Foundational Principles and Core Features"
- Auer, R., et al. (2020). "The Technology of Retail Central Bank Digital Currency"
- Atlantic Council CBDC Tracker (ongoing updates)
- IMF (2020). "Digital Money Across Borders: Macro-Financial Implications"

---

## Assessment

### Final Project (100% of grade)

Students choose ONE of three tracks:

**Track 1: Technical Implementation (Python-focused)**
- Build a complete fintech application, blockchain implementation, or ML financial model
- Requirements: well-documented code, data pipeline, testing, deployment considerations
- Examples: robo-advisor with backtesting, fraud detection system, P2P lending platform simulation, CBDC prototype

**Track 2: Business Case Analysis**
- Analyze a fintech company, blockchain project, or AI application in finance
- Requirements: business model, competitive analysis, regulatory landscape, financial projections
- Examples: neobank expansion strategy, DeFi protocol analysis, AI-driven trading firm assessment

**Track 3: Research Paper**
- Investigate a digital finance topic with empirical analysis or literature review
- Requirements: clear research question, methodology, data/sources, critical analysis, conclusions
- Examples: stablecoin stability analysis, HFT impact on market quality, bias in credit scoring models, CBDC adoption factors

**Evaluation Criteria:**
- Depth of understanding (30%)
- Quality of execution (30%)
- Critical thinking and analysis (20%)
- Clarity of presentation (10%)
- Code quality and documentation (10%, Track 1 only)

---

## Course Resources

### Required Software
- Python 3.8+ with Jupyter Notebook
- Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, scipy
- Additional as needed: web3.py (blockchain), transformers (NLP), plotly (visualization)

### Recommended Textbooks
- Arner, D.W., et al. (2020). "The Law and Regulation of Financial Technology"
- Narayanan, A., et al. (2016). "Bitcoin and Cryptocurrency Technologies"
- Lopez de Prado, M. (2018). "Advances in Financial Machine Learning"
- Hull, J.C. (2018). "Options, Futures, and Other Derivatives"

### Online Resources
- Course GitHub repository with code examples
- Financial datasets: Yahoo Finance, Quandl, Kaggle
- Blockchain explorers: Blockchain.com, Etherscan
- Regulatory websites: SEC, FCA, ESMA, BIS

### Office Hours
- Weekly sessions for technical questions and project guidance
- Discussion forum for asynchronous collaboration

---

## Schedule Notes

- Each lesson is 45 minutes
- Lessons include mini-lectures (20-25 min), live coding demonstrations (10-15 min), and discussion (5-10 min)
- Practical activities are to be completed independently and discussed in subsequent sessions
- Final project work begins after Lesson 36, with milestones and check-ins

---

**Version:** 1.0
**Last Updated:** December 2025
**Course Code:** BSc-DIGFIN-101
**Contact:** [Instructor contact information]
