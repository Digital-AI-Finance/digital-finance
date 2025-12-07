# Final Project Guidelines
## BSc Digital Finance: Blockchain, Cryptocurrencies & DeFi

---

## Overview

The final project is the sole assessment component for this course, accounting for 100% of your grade. This project-based assessment allows you to demonstrate comprehensive understanding of blockchain technology, cryptocurrencies, and decentralized finance through a format that aligns with your strengths and interests.

You will choose ONE of three project tracks:
- **Track A: Technical Implementation** - Build a working prototype
- **Track B: Research Analysis** - Conduct data-driven analysis
- **Track C: Business Case** - Develop a startup proposal

---

## Learning Outcomes Assessed

This project assesses your ability to:

| # | Learning Outcome |
|---|------------------|
| LO1 | Explain core blockchain concepts using appropriate technical terminology |
| LO4 | Develop basic smart contracts using Solidity (Track A) |
| LO5 | Identify smart contract vulnerabilities and apply security best practices |
| LO6 | Evaluate blockchain projects using fundamental analysis criteria |
| LO7 | Analyze case studies of blockchain successes and failures |
| LO8 | Compare consensus mechanisms and Layer 2 solutions |
| LO9 | Navigate regulatory frameworks and jurisdictional differences |
| LO10 | Communicate blockchain concepts to stakeholders |

---

## General Requirements (All Tracks)

### Timeline and Milestones

| Week | Milestone | Deliverable | Weight |
|------|-----------|-------------|--------|
| Week 4 | Topic Selection & Approval | 1-page proposal | 5% |
| Week 8 | Progress Checkpoint | Draft/prototype + peer feedback | 10% |
| Week 11 | Peer Review Session | Review 2 peer projects, receive feedback | 5% |
| Week 12 | Final Submission | Complete project deliverables | 80% |

### Collaboration Policy

- **Individual or Team**: You may work individually or in teams of 2-3 members
- **Team Work**: All team members must contribute equally and will receive the same grade
- **Team Contract**: Teams must submit a collaboration agreement in Week 4 outlining roles and responsibilities
- **Individual Contributions**: For team projects, include a 1-page statement detailing each member's contributions

### Academic Integrity

- All code, data, and content must be original or properly cited
- Using existing libraries (OpenZeppelin, ethers.js, web3.py) is encouraged and should be documented
- AI-assisted code is permitted but must be understood and documented
- Plagiarism will result in automatic failure

---

## Track A: Technical Implementation

### Description

Build a functional blockchain-based application demonstrating technical proficiency in smart contract development, testing, and deployment. Your project should solve a real-world problem or demonstrate an innovative use case.

### Target Audience

Students with programming experience interested in blockchain development, DeFi protocols, NFT platforms, or Web3 applications.

### Project Scope Examples

**DeFi Applications:**
- Decentralized lending platform with collateralization
- Automated market maker (AMM) with custom bonding curve
- Yield aggregator or farming optimizer
- Stablecoin mechanism (algorithmic or collateralized)

**NFT Platforms:**
- NFT marketplace with royalty mechanisms
- Dynamic NFTs that change based on on-chain data
- NFT-gated content or membership system
- Fractional NFT ownership platform

**Governance & DAOs:**
- Voting system with delegation and quadratic voting
- Treasury management contract with multi-sig
- Reputation-based governance system
- Grant distribution mechanism

**Trading & Finance:**
- Trading bot with on-chain execution
- Options or derivatives protocol
- Prediction market platform
- Portfolio rebalancing system

**Other Applications:**
- Decentralized identity system
- Supply chain tracking with verification
- Decentralized insurance protocol
- Cross-chain bridge (testnet only)

### Required Deliverables

#### 1. Smart Contract Code (35%)

**Requirements:**
- At least one primary smart contract (200+ lines of Solidity)
- Proper code structure with clear comments
- Use of established patterns (checks-effects-interactions, access control)
- Integration with external contracts/oracles where appropriate
- Deployed to Ethereum testnet (Sepolia or Goerli)

**Documentation:**
- Contract architecture diagram
- Function-by-function documentation
- State variables and their purposes
- Events and their usage
- Gas optimization decisions

#### 2. Test Suite (20%)

**Requirements:**
- Minimum 15 test cases covering critical functionality
- Use of testing framework (Hardhat, Foundry, or Truffle)
- Tests for both success and failure scenarios
- Edge case coverage
- At least 80% code coverage

**Test Categories:**
- Unit tests for individual functions
- Integration tests for multi-contract interactions
- Security tests for vulnerabilities
- Gas usage benchmarks
- Event emission verification

#### 3. Technical Documentation (20%)

**Length:** 5-7 pages

**Required Sections:**
1. **Introduction**: Problem statement and solution overview
2. **Architecture**: System design and contract structure
3. **Technical Specifications**:
   - Smart contract interfaces
   - Data structures
   - Key algorithms
4. **Security Analysis**:
   - Potential vulnerabilities considered
   - Security measures implemented
   - Known limitations
5. **Deployment Guide**:
   - Setup instructions
   - Deployment steps
   - Configuration parameters
6. **User Guide**: How to interact with the contracts
7. **Future Improvements**: Planned enhancements

#### 4. Video Demonstration (15%)

**Length:** 8-12 minutes

**Content:**
- Live demo of deployed contracts on testnet
- Walkthrough of key features
- Explanation of technical decisions
- Discussion of challenges and solutions
- Screen recording with voiceover or live presentation

#### 5. GitHub Repository (10%)

**Requirements:**
- Clean, organized repository structure
- Comprehensive README with setup instructions
- All source code and tests
- Deployment scripts
- CI/CD configuration (optional bonus)

**Repository Structure:**
```
project-name/
├── contracts/          # Solidity contracts
├── scripts/           # Deployment scripts
├── test/             # Test files
├── docs/             # Documentation
├── README.md         # Project overview
├── package.json      # Dependencies
└── .env.example      # Environment template
```

### Evaluation Criteria

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Functionality** | 30 | Does the project work as intended? All features functional? |
| **Code Quality** | 20 | Clean, well-structured, commented, follows best practices? |
| **Security** | 20 | No obvious vulnerabilities? Security best practices applied? |
| **Testing** | 15 | Comprehensive test coverage? Edge cases considered? |
| **Documentation** | 10 | Clear technical documentation and user guide? |
| **Innovation** | 5 | Original idea or novel implementation approach? |

### Common Pitfalls to Avoid

- Overly ambitious scope leading to incomplete implementation
- Insufficient testing, especially of edge cases
- Ignoring gas optimization (contracts too expensive to use)
- Poor access control allowing unauthorized actions
- Incomplete or unclear documentation
- Not handling transaction failures gracefully
- Missing security considerations (reentrancy, overflow, etc.)

---

## Track B: Research Analysis

### Description

Conduct an in-depth analytical study of a blockchain protocol, DeFi ecosystem, or emerging technology using on-chain data, market analysis, and technical evaluation. Your research should provide original insights backed by data.

### Target Audience

Students interested in blockchain analytics, investment research, protocol analysis, or data science applications in crypto.

### Project Scope Examples

**Protocol Deep Dives:**
- Comparative analysis of DEX models (Uniswap v3 vs. Curve vs. Balancer)
- Layer 2 scaling solutions: performance and adoption analysis
- Liquid staking protocols: risks and centralization concerns
- Lending protocol comparison: efficiency and risk metrics

**Market Analysis:**
- NFT market trends: volume, pricing, and collector behavior
- Stablecoin ecosystem analysis: stability mechanisms and risks
- Token distribution and concentration analysis
- Correlation analysis between DeFi tokens and broader markets

**Emerging Technologies:**
- Account abstraction adoption and use cases
- Zero-knowledge proof applications in privacy and scaling
- Real-world asset tokenization: current state and potential
- Cross-chain interoperability: bridge usage and security

**Sector Studies:**
- Decentralized identity solutions comparison
- GameFi economics and sustainability analysis
- NFT marketplace competitive landscape
- DAO governance effectiveness study

**Historical Analysis:**
- DeFi summer 2020: catalyst analysis and lessons
- Bear market impact on protocol revenues (2022-2023)
- Evolution of MEV and its impact on users
- Regulatory responses to major crypto events

### Required Deliverables

#### 1. Written Report (40%)

**Length:** 12-15 pages (excluding references and appendices)

**Required Sections:**

1. **Executive Summary** (1 page)
   - Key findings summary
   - Methodology overview
   - Main conclusions

2. **Introduction** (1-2 pages)
   - Research question and motivation
   - Background and context
   - Scope and limitations
   - Structure of report

3. **Literature Review** (2-3 pages)
   - Existing research on the topic
   - Relevant whitepapers and technical documentation
   - Industry reports and analysis
   - Identification of research gap

4. **Methodology** (1-2 pages)
   - Data sources (on-chain, market, qualitative)
   - Analysis techniques
   - Tools used (Dune Analytics, The Graph, Python libraries)
   - Assumptions and limitations

5. **Analysis** (4-6 pages)
   - Presentation of findings
   - Data visualizations and tables
   - Technical explanations
   - Comparative analysis where relevant

6. **Discussion** (2-3 pages)
   - Interpretation of results
   - Implications for stakeholders
   - Risk assessment
   - Future outlook

7. **Conclusion** (1 page)
   - Summary of key findings
   - Recommendations
   - Areas for future research

8. **References**
   - Minimum 15 credible sources
   - Proper citation format (APA or IEEE)

#### 2. Data Analysis (30%)

**Requirements:**
- Original on-chain data analysis using tools like:
  - Dune Analytics (SQL queries)
  - The Graph (GraphQL queries)
  - Python with web3.py or ethers.js
  - Blockchain explorers (Etherscan, etc.)
- Minimum 5 custom visualizations (charts/graphs)
- Statistical analysis where appropriate
- Clear methodology for data collection and processing

**Visualization Types:**
- Time series analysis (TVL, volume, users)
- Distribution analysis (wallet holdings, transaction sizes)
- Network analysis (token flows, user relationships)
- Comparative charts (protocol comparison, metrics over time)
- Heatmaps, scatter plots, or other advanced visualizations

#### 3. Presentation Slides (15%)

**Length:** 12-15 slides

**Required Content:**
- Title and author information
- Research question and motivation
- Methodology overview
- Key findings with visualizations
- Discussion and implications
- Conclusions and recommendations
- Q&A preparation

**Design:**
- Professional appearance
- Consistent formatting
- Clear, readable charts
- Not text-heavy (bullet points, not paragraphs)

#### 4. Presentation Delivery (15%)

**Length:** 10-12 minutes + 3-5 minutes Q&A

**Format:** Live presentation or high-quality recorded video

**Evaluated on:**
- Clarity of explanation
- Ability to explain technical concepts to mixed audience
- Confidence and preparation
- Response to questions
- Time management
- Visual aid effectiveness

### Evaluation Criteria

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Technical Understanding** | 25 | Deep comprehension of protocols/mechanisms analyzed? |
| **Data Analysis** | 25 | Rigorous on-chain analysis with original insights? |
| **Critical Evaluation** | 20 | Balanced assessment of risks and opportunities? |
| **Research Quality** | 15 | Proper methodology, citations, academic rigor? |
| **Presentation** | 10 | Clear communication to both technical and non-technical audiences? |
| **Originality** | 5 | Novel approach or unique insights beyond existing research? |

### Common Pitfalls to Avoid

- Relying only on secondary sources without original data analysis
- Cherry-picking data to support predetermined conclusions
- Insufficient sample size or time period for analysis
- Failing to acknowledge limitations and assumptions
- Overly technical presentation inaccessible to general audience
- Lack of critical evaluation (only presenting positive aspects)
- Poor data visualization (unclear charts, missing labels)
- Not connecting findings to real-world implications

---

## Track C: Business Case

### Description

Develop a comprehensive business proposal for a blockchain-based startup or product. This track requires understanding the intersection of technology, business models, regulation, and market dynamics.

### Target Audience

Students interested in entrepreneurship, business development, product management, or strategy roles in the blockchain industry.

### Project Scope Examples

**Financial Services:**
- Neobank with blockchain settlement layer
- Micro-lending platform using DeFi protocols
- Remittance service using stablecoins
- Invoice factoring on blockchain
- Decentralized credit scoring system

**Infrastructure & Tooling:**
- Institutional custody solution
- Developer tools for smart contract deployment
- Blockchain analytics platform
- Compliance and KYC/AML service
- Gas optimization service for dApps

**Consumer Applications:**
- NFT loyalty program for retail brands
- Tokenized real estate investment platform
- Blockchain-based music royalties distribution
- Decentralized social media platform
- Web3 gaming marketplace

**Enterprise Solutions:**
- Supply chain transparency platform
- Trade finance blockchain
- Carbon credit marketplace
- Intellectual property rights management
- Decentralized cloud storage service

**Emerging Markets:**
- Financial inclusion product for unbanked populations
- Agricultural supply chain financing
- Educational credential verification
- Healthcare data sharing platform
- Energy trading peer-to-peer network

### Required Deliverables

#### 1. Business Plan Document (40%)

**Length:** 15-20 pages

**Required Sections:**

1. **Executive Summary** (1-2 pages)
   - Business concept overview
   - Problem and solution
   - Market opportunity
   - Competitive advantage
   - Financial highlights
   - Funding requirements

2. **Problem Statement** (2 pages)
   - Detailed description of the problem
   - Current solutions and their limitations
   - Market pain points
   - Opportunity size

3. **Solution & Product Description** (3-4 pages)
   - Product/service overview
   - How blockchain technology solves the problem
   - Key features and benefits
   - Technical architecture (high-level)
   - Product roadmap (MVP, V1, V2)
   - Why blockchain is necessary (not just trendy)

4. **Market Analysis** (3-4 pages)
   - Target market definition and segmentation
   - Market size (TAM, SAM, SOM)
   - Market trends and growth projections
   - Customer personas (3-5 detailed profiles)
   - Customer acquisition strategy

5. **Competitive Analysis** (2-3 pages)
   - Direct competitors
   - Indirect competitors
   - Competitive positioning matrix
   - Differentiation strategy
   - Barriers to entry and moat

6. **Business Model** (2-3 pages)
   - Revenue streams
   - Pricing strategy
   - Cost structure
   - Unit economics
   - Business model canvas
   - Path to profitability

7. **Go-to-Market Strategy** (2 pages)
   - Launch strategy
   - Marketing channels
   - Partnership strategy
   - Community building approach
   - Customer retention plan

8. **Regulatory Considerations** (2 pages)
   - Relevant regulations (MiCA, SEC, local laws)
   - Compliance requirements
   - Licensing needs
   - Token classification (if applicable)
   - Risk mitigation strategy

9. **Team & Operations** (1-2 pages)
   - Organizational structure
   - Key roles and required expertise
   - Advisory board
   - Operational plan
   - Technology stack

10. **Financial Projections** (2-3 pages)
    - 3-year financial forecast
    - Revenue projections
    - Cost breakdown
    - Cash flow analysis
    - Key assumptions
    - Break-even analysis
    - Funding requirements and use of funds

#### 2. Pitch Deck (30%)

**Length:** 12-15 slides

**Required Slides:**
1. Cover (company name, tagline, logo)
2. Problem (the pain point you're solving)
3. Solution (your product/service)
4. Why Now? (market timing)
5. Market Size (TAM, SAM, SOM with sources)
6. Product Demo/Screenshots (visual representation)
7. Business Model (how you make money)
8. Traction (if applicable, or go-to-market plan)
9. Competition (competitive landscape)
10. Competitive Advantage (your moat)
11. Team (founders and key members)
12. Financial Projections (3-year summary)
13. Funding Ask (amount, use of funds, milestones)
14. Vision (long-term impact)
15. Contact Information

**Design Requirements:**
- Professional, investor-ready design
- Consistent branding (colors, fonts, logo)
- Minimal text (visuals over words)
- Clear data visualization
- No more than 3-4 bullet points per slide

#### 3. Financial Model (15%)

**Format:** Excel or Google Sheets spreadsheet

**Requirements:**
- Monthly projections for Year 1
- Quarterly projections for Years 2-3
- Revenue build-up with clear assumptions
- Expense categories (fixed and variable)
- Headcount plan
- Cash flow statement
- Key metrics dashboard (CAC, LTV, churn, etc.)
- Sensitivity analysis for key assumptions
- Clear documentation of all assumptions

**Tabs to Include:**
- Assumptions
- Revenue Model
- Cost Structure
- P&L Statement
- Cash Flow
- Balance Sheet (basic)
- Key Metrics
- Sensitivity Analysis

#### 4. Pitch Presentation (15%)

**Length:** 10 minutes pitch + 5 minutes Q&A

**Format:** Live presentation or high-quality recorded video

**Evaluation Criteria:**
- Clarity and persuasiveness
- Storytelling ability
- Handling of questions
- Confidence and passion
- Professionalism
- Time management

**Tips:**
- Practice extensively
- Anticipate tough questions
- Show passion for the problem and solution
- Be realistic about challenges
- Demonstrate deep market knowledge
- Show why your team can execute

### Evaluation Criteria

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Problem-Solution Fit** | 25 | Is the problem real and significant? Is the solution compelling? |
| **Market Opportunity** | 20 | Is the market large enough? Is the analysis rigorous? |
| **Business Model** | 20 | Is the monetization strategy viable? Are unit economics sound? |
| **Competitive Positioning** | 15 | Is differentiation clear? Are barriers to entry identified? |
| **Regulatory Awareness** | 10 | Are compliance requirements understood? Risks addressed? |
| **Financial Viability** | 10 | Are projections realistic? Assumptions justified? |

### Common Pitfalls to Avoid

- Solution looking for a problem (blockchain for blockchain's sake)
- Unrealistic market size claims or financial projections
- Ignoring regulatory complexity and compliance costs
- Underestimating competition (claiming "no competitors")
- Weak differentiation or unclear competitive advantage
- Vague go-to-market strategy without specific tactics
- Overly technical pitch inaccessible to non-technical evaluators
- No clear path to revenue or profitability
- Ignoring customer acquisition costs
- Missing the "why blockchain?" justification

---

## Submission Guidelines (All Tracks)

### Week 4: Topic Selection & Approval (5%)

**Deliverable:** 1-page proposal

**Content:**
- Project title
- Selected track (A, B, or C)
- Brief description (200-300 words)
- Preliminary objectives
- Expected challenges
- Team members (if applicable)

**Submission:** Via LMS by end of Week 4
**Feedback:** Instructor approval or revision request within 3 days

### Week 8: Progress Checkpoint (10%)

**Track A:** Working prototype with at least 50% of core features implemented
**Track B:** Complete data analysis and first draft of report (at least 8 pages)
**Track C:** Complete business plan draft and preliminary financial model

**Submission:** Via LMS by end of Week 8
**Peer Feedback:** Review 2 classmates' checkpoints and provide constructive feedback (1 page per review)

### Week 11: Peer Review Session (5%)

**Format:** In-class or virtual session

**Activities:**
- Present 5-minute project overview
- Receive feedback from 2-3 peers
- Provide feedback to 2-3 peers

**Grading:**
- Quality of feedback provided to others (3%)
- Incorporation of received feedback into final project (2%)

### Week 12: Final Submission (80%)

**Deadline:** Last day of Week 12, 11:59 PM

**Submission Package:**
All deliverables specified for your chosen track, packaged as:
- One PDF document containing all written materials
- One presentation file (PPT or PDF)
- Video file (or link to unlisted YouTube/Vimeo)
- GitHub repository link (Track A)
- Excel/Sheets link (Track C)
- Peer review incorporation document (1 page explaining how peer feedback was addressed)

**Late Policy:**
- Up to 24 hours late: 10% penalty
- 24-48 hours late: 20% penalty
- 48-72 hours late: 30% penalty
- More than 72 hours late: Not accepted without prior arrangement

---

## Grading Summary

### Milestone Weights

| Milestone | Weight | Description |
|-----------|--------|-------------|
| Topic Proposal | 5% | Clear, feasible project scope |
| Progress Checkpoint | 10% | Substantial progress demonstrated |
| Peer Review | 5% | Quality feedback given and received |
| Final Deliverables | 80% | Complete project meeting track requirements |

### Final Project Component Weights (80% of Total)

**Track A: Technical Implementation**
- Smart Contract Code: 35%
- Test Suite: 20%
- Technical Documentation: 20%
- Video Demonstration: 15%
- GitHub Repository: 10%

**Track B: Research Analysis**
- Written Report: 40%
- Data Analysis: 30%
- Presentation Slides: 15%
- Presentation Delivery: 15%

**Track C: Business Case**
- Business Plan Document: 40%
- Pitch Deck: 30%
- Financial Model: 15%
- Pitch Presentation: 15%

---

## Resources and Support

### Technical Resources (Track A)
- OpenZeppelin Contracts documentation
- Hardhat/Foundry tutorials
- Remix IDE
- Sepolia testnet faucets
- Web3 development guides

### Research Resources (Track B)
- Dune Analytics
- The Graph
- DeFi Llama
- Token Terminal
- Messari Research
- CoinGecko
- Academic databases (Google Scholar, SSRN)

### Business Resources (Track C)
- Y Combinator Startup School
- a16z Crypto Startup School
- Crunchbase (for market data)
- PitchBook (competitor analysis)
- Regulatory guidance (SEC, ESMA, MiCA documentation)
- Business model canvas templates

### Support Channels
- Office hours: Weekly, schedule via LMS
- Discord server: Peer collaboration and Q&A
- Project feedback sessions: Weeks 4, 8, 11
- Technical troubleshooting: TA support hours
- Writing center: For report/business plan review

---

## Frequently Asked Questions

**Q: Can I change tracks after Week 4 approval?**
A: Yes, but only with instructor permission and if you can demonstrate equivalent progress in the new track.

**Q: Can I work on a project I started before this course?**
A: Yes, if you substantially extend it and clearly document what is new work for this course.

**Q: For Track A, do I need to deploy to mainnet?**
A: No, testnet deployment is required. Mainnet is optional and offers no bonus points.

**Q: For Track B, do I need to create my own dataset?**
A: You must perform original analysis, but can use existing data sources (on-chain data, public APIs). The analysis and insights must be original.

**Q: For Track C, do I need a functional prototype?**
A: No, but high-fidelity mockups or wireframes are expected. A working prototype is a bonus.

**Q: Can I use AI tools like ChatGPT or Copilot?**
A: Yes, but you must understand all code/content and document AI usage. You're responsible for accuracy and security.

**Q: What if my team member doesn't contribute equally?**
A: Use the team contract from Week 4. If issues arise, notify instructor immediately. Individual grades can be adjusted based on documented contribution.

**Q: Can I interview industry experts for my project?**
A: Absolutely encouraged, especially for Tracks B and C. Document all interviews and include as appendices.

**Q: Is there a page limit maximum?**
A: Stay within the specified ranges. Quality over quantity. Concise, well-structured writing is valued.

---

## Evaluation Transparency

All projects will be evaluated using the detailed rubrics in the accompanying `assessment_rubrics.md` document. Grading will consider:

1. **Technical correctness and rigor**
2. **Depth of understanding** demonstrated
3. **Quality of execution** (code, writing, design)
4. **Originality and creativity**
5. **Professional presentation**
6. **Practical applicability**

Grades will be returned within 2 weeks of final submission with detailed feedback on each rubric criterion.

---

**Good luck with your projects! This is your opportunity to demonstrate comprehensive mastery of blockchain technology and create portfolio-worthy work.**
