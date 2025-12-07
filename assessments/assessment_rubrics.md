# Assessment Rubrics
## BSc Digital Finance: Blockchain, Cryptocurrencies & DeFi

---

## Overview

This document provides detailed grading rubrics for all assessment components in the course. Each rubric breaks down evaluation criteria with specific descriptors for each performance level.

**Grading Scale:**
- **A (90-100%)**: Excellent - Exceeds expectations
- **B (80-89%)**: Good - Meets all expectations
- **C (70-79%)**: Satisfactory - Meets basic expectations
- **D (60-69%)**: Passing - Minimum acceptable
- **F (<60%)**: Failing - Does not meet expectations

---

## Milestone Rubrics

### Week 4: Topic Selection & Approval (5% of final grade)

| Criterion | Excellent (4.5-5) | Good (4.0-4.4) | Satisfactory (3.5-3.9) | Needs Work (<3.5) |
|-----------|-------------------|----------------|------------------------|-------------------|
| **Clarity** | Project scope is crystal clear, well-defined, and specific | Project scope is clear with minor ambiguities | Project scope is somewhat vague or too broad | Project scope is unclear or ill-defined |
| **Feasibility** | Project is ambitious yet achievable within timeframe, shows realistic planning | Project is achievable with reasonable effort | Project scope may be too large or too simple for 12 weeks | Project is unrealistic or trivial |
| **Relevance** | Directly addresses course learning outcomes with clear connections | Addresses most learning outcomes | Addresses some learning outcomes | Weak connection to course content |
| **Innovation** | Novel approach or unique perspective on problem | Some original elements | Standard approach | Derivative or overly simple |

**Total Points: 5**

---

### Week 8: Progress Checkpoint (10% of final grade)

| Criterion | Excellent (9-10) | Good (8.0-8.9) | Satisfactory (7.0-7.9) | Needs Work (<7.0) |
|-----------|------------------|----------------|------------------------|-------------------|
| **Completion** | 60%+ of project complete with all major components started | 50-60% complete with most components started | 40-50% complete, some key components missing | Less than 40% complete |
| **Quality** | Checkpoint deliverable is polished, well-organized, professional | Good quality with minor rough edges | Acceptable quality, needs refinement | Poor quality, significant issues |
| **Progress Plan** | Clear plan to completion with realistic timeline | Reasonable plan with some gaps | Vague plan or uncertain timeline | No clear plan forward |
| **Challenges Identified** | Proactively identified issues with concrete mitigation strategies | Identified some challenges with general solutions | Acknowledged challenges but no clear solutions | Unaware of major challenges |

**Total Points: 10**

---

### Week 11: Peer Review Session (5% of final grade)

#### Feedback Provided to Others (3%)

| Criterion | Excellent (2.7-3.0) | Good (2.4-2.6) | Satisfactory (2.1-2.3) | Needs Work (<2.1) |
|-----------|---------------------|----------------|------------------------|-------------------|
| **Constructiveness** | Specific, actionable feedback focusing on improvement | Generally helpful feedback with some specific suggestions | Generic feedback or mostly positive without substance | Unhelpful, vague, or overly critical |
| **Depth** | Demonstrates deep engagement with peer's work, technical understanding | Shows good understanding, addresses multiple aspects | Surface-level review, addresses only obvious points | Minimal effort, does not engage with content |
| **Professionalism** | Respectful, encouraging tone while being honest about weaknesses | Professional tone, balanced feedback | Acceptable but could be more tactful or balanced | Inappropriate tone or unprofessional |

#### Incorporation of Feedback (2%)

| Criterion | Excellent (1.8-2.0) | Good (1.6-1.7) | Satisfactory (1.4-1.5) | Needs Work (<1.4) |
|-----------|---------------------|----------------|------------------------|-------------------|
| **Responsiveness** | Thoughtfully incorporated all relevant feedback with explanation | Incorporated most feedback appropriately | Incorporated some feedback | Ignored most feedback without justification |
| **Documentation** | Clear documentation of what feedback was used and how | Documented major changes from feedback | Minimal documentation | No documentation of changes |

**Total Points: 5**

---

## Track A: Technical Implementation Rubrics

### Final Project Rubric - Track A (80% of final grade)

#### 1. Smart Contract Code (35% of 80% = 28 points total)

| Criterion | Weight | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Failing (<70%) |
|-----------|--------|---------------------|---------------|----------------------|----------------|
| **Functionality** | 40% | All features work flawlessly, handles edge cases gracefully | All core features work, minor bugs in edge cases | Core features work but with notable bugs | Many features broken or incomplete |
| **Code Quality** | 25% | Exceptionally clean, well-organized, follows Solidity best practices, excellent comments | Clean code, good structure, adequate comments | Code works but is messy, inconsistent style, minimal comments | Poor structure, hard to read, no comments |
| **Architecture** | 20% | Sophisticated design, excellent separation of concerns, modular | Good design, reasonable modularity | Basic but functional architecture | Poor design, tightly coupled |
| **Gas Optimization** | 15% | Highly optimized, uses advanced techniques, documented trade-offs | Good optimization, standard techniques applied | Basic optimization, room for improvement | No optimization, wasteful patterns |

**Calculation Example:**
- Functionality: 90% score x 40% weight = 36%
- Code Quality: 85% score x 25% weight = 21.25%
- Architecture: 88% score x 20% weight = 17.6%
- Gas Optimization: 80% score x 15% weight = 12%
- **Total:** 86.85% of 28 points = 24.3 points

**Common Deductions:**
- Missing error handling: -5%
- Inconsistent naming conventions: -3%
- Unused variables or functions: -2%
- No NatSpec documentation: -5%
- Inefficient loops or storage patterns: -3-5%

---

#### 2. Test Suite (20% of 80% = 16 points total)

| Criterion | Weight | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Failing (<70%) |
|-----------|--------|---------------------|---------------|----------------------|----------------|
| **Coverage** | 35% | 90%+ code coverage, all critical paths tested | 80-90% coverage, most paths tested | 70-80% coverage, basic paths tested | Less than 70% coverage |
| **Test Quality** | 30% | Tests are thorough, test both success and failure, edge cases covered | Good test coverage of main scenarios | Tests verify basic functionality only | Tests are superficial or poorly designed |
| **Organization** | 20% | Excellent test structure, clear naming, well-organized suites | Good organization, mostly clear | Basic organization, could be clearer | Disorganized, hard to understand |
| **Assertions** | 15% | Comprehensive assertions, checks events, state changes, return values | Good assertions for key behaviors | Basic assertions, checks main outcomes | Weak or missing assertions |

**Minimum Expectations:**
- At least 15 meaningful test cases
- Tests for access control
- Tests for invalid inputs
- Tests for state transitions
- Event emission tests

**Bonus Points (up to +2 points):**
- Fuzz testing: +1 point
- Formal verification: +1 point
- Gas benchmarking suite: +0.5 points

---

#### 3. Technical Documentation (20% of 80% = 16 points total)

| Criterion | Weight | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Failing (<70%) |
|-----------|--------|---------------------|---------------|----------------------|----------------|
| **Completeness** | 30% | All required sections, comprehensive coverage | All sections present, good detail | All sections but some lacking detail | Missing sections |
| **Technical Accuracy** | 25% | All technical details are correct, demonstrates deep understanding | Mostly accurate, minor errors | Some inaccuracies or misconceptions | Significant technical errors |
| **Clarity** | 20% | Exceptionally clear, accessible to both technical and non-technical readers | Clear writing, good explanations | Understandable but could be clearer | Confusing, hard to follow |
| **Diagrams/Visuals** | 15% | Excellent diagrams, architecture clearly visualized | Good diagrams, helpful visuals | Basic diagrams, minimally helpful | Poor or missing diagrams |
| **Security Analysis** | 10% | Thorough security analysis, all vulnerabilities addressed | Good security discussion | Basic security considerations | Security ignored or superficial |

**Required Sections Checklist:**
- [ ] Introduction with problem statement
- [ ] Architecture overview with diagram
- [ ] Contract specifications
- [ ] Security considerations
- [ ] Deployment guide
- [ ] User interaction guide
- [ ] Future improvements

---

#### 4. Video Demonstration (15% of 80% = 12 points total)

| Criterion | Weight | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Failing (<70%) |
|-----------|--------|---------------------|---------------|----------------------|----------------|
| **Demonstration** | 35% | Flawless demo, all features shown, smooth execution | Good demo, minor technical hiccups | Demo works but choppy or incomplete | Demo fails or shows limited functionality |
| **Explanation** | 30% | Clear, concise explanations of features and technical decisions | Good explanations, mostly clear | Adequate explanation, some unclear parts | Poor explanation, confusing |
| **Technical Depth** | 20% | Deep technical insights, explains trade-offs and design choices | Good technical detail | Basic technical coverage | Superficial, no technical depth |
| **Production Quality** | 15% | Professional video/audio, good editing, polished | Good quality, clear audio/video | Acceptable quality, some issues | Poor quality, hard to see/hear |

**Length Requirement:** 8-12 minutes (strict)
- Under 8 minutes: -5% per minute
- Over 12 minutes: -3% per minute

---

#### 5. GitHub Repository (10% of 80% = 8 points total)

| Criterion | Weight | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Failing (<70%) |
|-----------|--------|---------------------|---------------|----------------------|----------------|
| **Organization** | 30% | Excellent structure, clear separation of concerns | Good structure, logical organization | Basic structure, somewhat organized | Messy, disorganized |
| **README** | 25% | Comprehensive README with setup, usage, architecture | Good README, covers essentials | Basic README, minimal info | Poor or missing README |
| **Completeness** | 25% | All code, tests, scripts, documentation included | Most files included | Some files missing | Many missing files |
| **Best Practices** | 20% | .gitignore, environment templates, CI/CD, semantic commits | Good git practices, proper ignores | Basic practices | Poor version control practices |

**README Must Include:**
- Project description
- Setup instructions
- Dependencies and versions
- Deployment steps
- Testing commands
- Contract addresses (testnet)
- License

---

### Track A: Example Grading Calculation

**Student Project: NFT Marketplace**

| Component | Weight | Student Score | Points Earned |
|-----------|--------|---------------|---------------|
| Smart Contract Code | 28 pts | 88% | 24.64 |
| Test Suite | 16 pts | 85% | 13.60 |
| Technical Documentation | 16 pts | 92% | 14.72 |
| Video Demonstration | 12 pts | 90% | 10.80 |
| GitHub Repository | 8 pts | 87% | 6.96 |
| **Final Project Total** | **80 pts** | **87.65%** | **70.72** |

**Milestone Scores:**
- Topic Proposal: 5/5 = 5 pts
- Progress Checkpoint: 9/10 = 9 pts
- Peer Review: 4.5/5 = 4.5 pts

**Final Course Grade:**
- Milestones: 5 + 9 + 4.5 = 18.5/20
- Final Project: 70.72/80
- **Total: 89.22/100 = B+**

---

## Track B: Research Analysis Rubrics

### Final Project Rubric - Track B (80% of final grade)

#### 1. Written Report (40% of 80% = 32 points total)

| Criterion | Weight | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Failing (<70%) |
|-----------|--------|---------------------|---------------|----------------------|----------------|
| **Technical Understanding** | 30% | Demonstrates mastery of protocols/mechanisms, explains complex concepts clearly | Strong understanding, minor gaps | Basic understanding, some misconceptions | Weak understanding, major errors |
| **Research Quality** | 25% | Rigorous methodology, diverse credible sources (15+), proper citations | Good methodology, adequate sources (12-15) | Acceptable methodology, minimal sources (10-12) | Poor methodology, insufficient sources |
| **Analysis Depth** | 25% | Deep, nuanced analysis with original insights | Good analysis, some insights | Surface-level analysis | Superficial, no real analysis |
| **Writing Quality** | 15% | Excellent academic writing, clear structure, no errors | Good writing, minor errors | Adequate writing, some errors | Poor writing, many errors |
| **Critical Thinking** | 5% | Balanced assessment, considers multiple perspectives | Mostly balanced | Somewhat biased or one-sided | Uncritical or biased |

**Length Requirement:** 12-15 pages
- Under 12 pages: -10%
- Over 15 pages: -5% if not justified by content quality

**Required Elements Checklist:**
- [ ] Executive summary
- [ ] Clear research question
- [ ] Literature review (15+ sources)
- [ ] Methodology section
- [ ] Data analysis section
- [ ] Discussion section
- [ ] Conclusion with recommendations
- [ ] Proper citations (APA or IEEE)
- [ ] Professional formatting

---

#### 2. Data Analysis (30% of 80% = 24 points total)

| Criterion | Weight | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Failing (<70%) |
|-----------|--------|---------------------|---------------|----------------------|----------------|
| **Originality** | 30% | Novel analysis approach, unique insights not found elsewhere | Some original elements | Standard analysis | Derivative, no originality |
| **Rigor** | 25% | Statistically sound, appropriate methods, controlled variables | Mostly rigorous, minor issues | Basic rigor, some questionable methods | Lacks rigor, flawed methods |
| **Data Sources** | 20% | Multiple on-chain sources, well-documented, verifiable | Good sources, documented | Basic sources, minimal documentation | Poor or unreliable sources |
| **Visualizations** | 15% | Excellent charts (5+), clear, informative, professional | Good charts, mostly clear | Basic charts, adequate | Poor charts, unclear |
| **Interpretation** | 10% | Insightful interpretation, connects to broader context | Good interpretation | Basic interpretation | Weak or missing interpretation |

**Minimum Data Requirements:**
- At least 5 custom visualizations
- On-chain data from blockchain explorers or APIs
- Time series of at least 6 months
- Statistical analysis where appropriate

**Visualization Types Expected:**
- Time series plots (TVL, volume, users, etc.)
- Distribution charts (histogram, box plot)
- Comparative charts (protocol comparison)
- Network or flow diagrams
- Correlation or scatter plots

**Tools Accepted:**
- Dune Analytics (SQL queries)
- Python (pandas, matplotlib, seaborn)
- R (ggplot2)
- The Graph (GraphQL)
- Excel/Google Sheets (for simple analysis)

**Data Analysis Checklist:**
- [ ] Clear data collection methodology
- [ ] Data cleaning and preprocessing documented
- [ ] Appropriate statistical methods
- [ ] All visualizations have titles, labels, legends
- [ ] Results presented before interpretation
- [ ] Limitations acknowledged

---

#### 3. Presentation Slides (15% of 80% = 12 points total)

| Criterion | Weight | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Failing (<70%) |
|-----------|--------|---------------------|---------------|----------------------|----------------|
| **Content** | 40% | Covers all key findings, well-structured narrative | Good coverage, logical flow | Basic coverage, some gaps | Poor coverage, disjointed |
| **Visuals** | 30% | Excellent data visualizations, clear, professional | Good visuals, mostly clear | Basic visuals, adequate | Poor visuals, unclear |
| **Design** | 20% | Professional design, consistent branding, excellent readability | Good design, mostly consistent | Acceptable design, readable | Poor design, hard to read |
| **Conciseness** | 10% | Minimal text, effective use of bullet points and visuals | Good balance of text/visuals | Too much text | Walls of text |

**Slide Requirements:**
- 12-15 slides (title and references don't count)
- Title slide with name, date, topic
- Research question/motivation
- Methodology overview
- Key findings (3-5 slides with visualizations)
- Discussion/implications
- Conclusions and recommendations
- References slide

**Design Guidelines:**
- Consistent font (sans-serif recommended)
- High contrast for readability
- No more than 3-4 bullet points per slide
- Large enough font (minimum 18pt for body text)
- Professional color scheme
- All charts properly labeled

---

#### 4. Presentation Delivery (15% of 80% = 12 points total)

| Criterion | Weight | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Failing (<70%) |
|-----------|--------|---------------------|---------------|----------------------|----------------|
| **Clarity** | 30% | Exceptionally clear explanations, accessible to mixed audience | Clear, understandable | Mostly clear, some confusion | Unclear, confusing |
| **Technical Communication** | 25% | Explains complex concepts simply without losing accuracy | Good balance of technical and accessible | Too technical or too simple | Poor technical explanation |
| **Confidence** | 20% | Confident, well-prepared, maintains eye contact | Mostly confident, prepared | Somewhat nervous but adequate | Nervous, unprepared |
| **Q&A Handling** | 15% | Excellent responses, demonstrates deep knowledge | Good responses, handles most questions | Basic responses, struggles with some questions | Poor responses, can't answer questions |
| **Time Management** | 10% | Perfect timing (10-12 min + 3-5 min Q&A) | Within 1 minute of target | Within 2 minutes | Significantly over or under time |

**Presentation Format:**
- Live presentation (preferred) OR
- High-quality recorded video with clear audio/video

**Evaluation Approach:**
- 2 instructors independently score
- Average of scores (resolve discrepancies by discussion)
- Q&A questions assess understanding beyond memorization

**Length Requirement:** 10-12 minutes + 3-5 minutes Q&A (strict)
- Under 10 minutes: -5% per minute
- Over 12 minutes (excluding Q&A): -3% per minute

---

### Track B: Example Grading Calculation

**Student Project: Uniswap v3 vs Curve Efficiency Analysis**

| Component | Weight | Student Score | Points Earned |
|-----------|--------|---------------|---------------|
| Written Report | 32 pts | 91% | 29.12 |
| Data Analysis | 24 pts | 88% | 21.12 |
| Presentation Slides | 12 pts | 85% | 10.20 |
| Presentation Delivery | 12 pts | 89% | 10.68 |
| **Final Project Total** | **80 pts** | **88.9%** | **71.12** |

**Milestone Scores:**
- Topic Proposal: 4.8/5 = 4.8 pts
- Progress Checkpoint: 8.5/10 = 8.5 pts
- Peer Review: 4.7/5 = 4.7 pts

**Final Course Grade:**
- Milestones: 4.8 + 8.5 + 4.7 = 18/20
- Final Project: 71.12/80
- **Total: 89.12/100 = B+**

---

## Track C: Business Case Rubrics

### Final Project Rubric - Track C (80% of final grade)

#### 1. Business Plan Document (40% of 80% = 32 points total)

| Criterion | Weight | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Failing (<70%) |
|-----------|--------|---------------------|---------------|----------------------|----------------|
| **Problem-Solution Fit** | 25% | Compelling problem, innovative solution, clear why blockchain is necessary | Good problem, solid solution | Adequate problem, standard solution | Weak problem or poor solution fit |
| **Market Analysis** | 20% | Rigorous market sizing (TAM/SAM/SOM), detailed competitor analysis, clear positioning | Good market analysis, some depth | Basic market analysis | Superficial or flawed market analysis |
| **Business Model** | 20% | Viable, well-thought-out revenue model with sound unit economics | Good business model, mostly viable | Basic business model, some concerns | Unrealistic or unclear business model |
| **Regulatory Awareness** | 15% | Comprehensive regulatory analysis, compliance strategy, risk mitigation | Good regulatory coverage | Basic regulatory awareness | Regulatory issues ignored |
| **Writing Quality** | 10% | Excellent business writing, clear, persuasive, professional | Good writing, minor issues | Adequate writing, some errors | Poor writing quality |
| **Completeness** | 10% | All sections complete, comprehensive | All sections present, good detail | All sections, some lacking | Missing sections |

**Length Requirement:** 15-20 pages
- Under 15 pages: -10%
- Over 20 pages: Only acceptable if every page adds value, otherwise -5%

**Section Checklist:**
- [ ] Executive summary
- [ ] Problem statement (detailed)
- [ ] Solution and product description
- [ ] Market analysis (TAM/SAM/SOM)
- [ ] Competitive analysis
- [ ] Business model canvas or description
- [ ] Go-to-market strategy
- [ ] Regulatory considerations
- [ ] Team and operations plan
- [ ] Financial projections (3-year)
- [ ] Funding requirements

**Common Deductions:**
- Unrealistic market size claims: -5%
- Ignoring major competitors: -5%
- No regulatory analysis: -10%
- Missing customer personas: -3%
- Unclear revenue model: -5%
- No go-to-market plan: -5%

---

#### 2. Pitch Deck (30% of 80% = 24 points total)

| Criterion | Weight | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Failing (<70%) |
|-----------|--------|---------------------|---------------|----------------------|----------------|
| **Storytelling** | 25% | Compelling narrative, hooks attention, clear problem-solution arc | Good story, engaging | Basic story, adequate | Weak or no narrative |
| **Content** | 25% | All key elements covered, right balance of detail | Good coverage, minor gaps | Basic coverage | Missing key elements |
| **Design** | 20% | Professional, investor-ready design, consistent branding | Good design, mostly polished | Acceptable design | Amateurish design |
| **Visuals** | 20% | Excellent use of visuals, minimal text, clear charts | Good visuals, mostly clear | Basic visuals | Poor or missing visuals |
| **Persuasiveness** | 10% | Highly convincing, answers investor objections | Persuasive | Somewhat persuasive | Unconvincing |

**Slide Count:** 12-15 slides (not including title and backup slides)

**Required Slides:**
1. Title (company, tagline, logo)
2. Problem (specific pain point)
3. Solution (your product)
4. Why Now (market timing)
5. Market Size (TAM/SAM/SOM with sources)
6. Product (screenshots/mockups)
7. Business Model (revenue streams)
8. Traction or Go-to-Market
9. Competition (competitive matrix)
10. Competitive Advantage (moat)
11. Team (founders + key hires)
12. Financials (3-year summary)
13. Ask (funding amount, use of funds)
14. Vision (long-term impact)

**Design Evaluation:**
- Consistent fonts and colors: Yes/No
- Minimal text (no paragraphs): Yes/No
- Professional look: Yes/No
- All charts properly labeled: Yes/No
- High-resolution images: Yes/No

**Bonus Points (up to +2 points):**
- Working product demo: +1.5 points
- Letters of intent from potential customers: +1 point
- Advisory board commitments: +0.5 points

---

#### 3. Financial Model (15% of 80% = 12 points total)

| Criterion | Weight | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Failing (<70%) |
|-----------|--------|---------------------|---------------|----------------------|----------------|
| **Realism** | 30% | Conservative, well-justified assumptions | Reasonable assumptions, mostly realistic | Optimistic but plausible | Unrealistic assumptions |
| **Completeness** | 25% | All financial statements, detailed build-up | Key statements present, good detail | Basic statements | Missing key components |
| **Structure** | 20% | Excellent organization, clear tabs, easy to follow | Good organization | Basic organization | Disorganized, hard to follow |
| **Assumptions** | 15% | All assumptions clearly documented and justified | Most assumptions documented | Some documentation | Poor or missing documentation |
| **Sensitivity Analysis** | 10% | Multiple scenarios, key drivers identified | Basic sensitivity analysis | Minimal sensitivity | No sensitivity analysis |

**Required Tabs:**
- [ ] Assumptions (all key inputs documented)
- [ ] Revenue Model (bottom-up build)
- [ ] Cost Structure (fixed and variable)
- [ ] P&L Statement (monthly Year 1, quarterly Year 2-3)
- [ ] Cash Flow Statement
- [ ] Key Metrics Dashboard (CAC, LTV, churn, etc.)
- [ ] Sensitivity Analysis (best/base/worst case)

**Financial Statements Required:**
- Income statement (P&L)
- Cash flow statement
- Basic balance sheet (assets, liabilities, equity)

**Key Metrics to Include:**
- Customer Acquisition Cost (CAC)
- Lifetime Value (LTV)
- LTV/CAC ratio
- Monthly Recurring Revenue (MRR) if applicable
- Burn rate and runway
- Gross margin
- Break-even point

**Common Errors to Avoid:**
- Hockey stick growth with no justification: -10%
- Missing expense categories: -5%
- No cash flow analysis: -10%
- Unrealistic unit economics: -8%
- No sensitivity analysis: -5%
- Formulas broken or hardcoded numbers: -5%

---

#### 4. Pitch Presentation (15% of 80% = 12 points total)

| Criterion | Weight | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Failing (<70%) |
|-----------|--------|---------------------|---------------|----------------------|----------------|
| **Delivery** | 30% | Confident, polished, engaging, maintains eye contact | Good delivery, mostly smooth | Adequate delivery, some awkwardness | Poor delivery, reads slides |
| **Persuasiveness** | 25% | Highly convincing, passionate, inspiring | Persuasive, shows enthusiasm | Somewhat convincing | Unconvincing or flat |
| **Clarity** | 20% | Exceptionally clear, easy to understand | Clear communication | Mostly clear, some confusion | Unclear, confusing |
| **Q&A Handling** | 15% | Excellent responses, demonstrates deep knowledge, handles tough questions | Good responses, handles most questions well | Basic responses, struggles with some questions | Poor responses, defensive |
| **Time Management** | 10% | Perfect timing (10 min pitch + 5 min Q&A) | Within 1 minute of target | Within 2 minutes | Significantly over or under |

**Presentation Format:**
- Live pitch (preferred, simulates investor meeting)
- High-quality recorded video (if live not possible)

**Evaluation Panel:**
- Instructor (50% weight)
- Guest evaluator from industry (50% weight), if available
- Peer feedback (informational, not graded)

**Pitch Structure:**
1. Hook (30 seconds): Grab attention
2. Problem (1-2 minutes): Paint the pain
3. Solution (2-3 minutes): Your product
4. Market (1-2 minutes): Opportunity size
5. Business Model (1 minute): How you make money
6. Traction/Plan (1-2 minutes): Progress or go-to-market
7. Team (1 minute): Why you
8. Ask (30 seconds): What you need
9. Q&A (5 minutes): Investor questions

**Q&A Assessment:**
Questions will test:
- Understanding of market dynamics
- Technical feasibility
- Regulatory awareness
- Competitive positioning
- Financial projections justification
- Ability to think on feet

**Length Requirement:** 10 minutes pitch + 5 minutes Q&A (strict)
- Under 9 minutes: -10%
- 9-10 minutes: -5%
- Over 11 minutes: -5%
- Over 12 minutes: -10%

---

### Track C: Example Grading Calculation

**Student Project: DeFi Micro-Lending for Emerging Markets**

| Component | Weight | Student Score | Points Earned |
|-----------|--------|---------------|---------------|
| Business Plan Document | 32 pts | 90% | 28.80 |
| Pitch Deck | 24 pts | 87% | 20.88 |
| Financial Model | 12 pts | 85% | 10.20 |
| Pitch Presentation | 12 pts | 91% | 10.92 |
| **Final Project Total** | **80 pts** | **88.5%** | **70.80** |

**Milestone Scores:**
- Topic Proposal: 5/5 = 5 pts
- Progress Checkpoint: 8.8/10 = 8.8 pts
- Peer Review: 4.5/5 = 4.5 pts

**Final Course Grade:**
- Milestones: 5 + 8.8 + 4.5 = 18.3/20
- Final Project: 70.80/80
- **Total: 89.1/100 = B+**

---

## Cross-Track Comparison

### Grade Distribution Guidelines

To ensure fairness across tracks, instructors will aim for similar grade distributions:

| Grade | Expected % | Description |
|-------|------------|-------------|
| A (90-100%) | 20-30% | Exceptional work, publishable quality |
| B (80-89%) | 40-50% | Strong work, meets all expectations |
| C (70-79%) | 20-30% | Acceptable work, meets basic requirements |
| D (60-69%) | 5-10% | Minimal work, barely passing |
| F (<60%) | 0-5% | Insufficient work or major issues |

### Track Difficulty Adjustment

No curve or difficulty adjustment will be applied between tracks. Each track has been designed with equivalent rigor:

- **Track A**: Requires strong programming skills, technical depth
- **Track B**: Requires strong analytical skills, research rigor
- **Track C**: Requires business acumen, market understanding

Students should choose the track that aligns with their strengths and career goals, not based on perceived difficulty.

---

## Common Pitfalls Across All Tracks

### Content Issues
- **Scope Creep**: Starting with reasonable scope but adding features/sections, leading to incomplete work
- **Superficiality**: Covering many topics shallowly instead of fewer topics deeply
- **Lack of Critical Analysis**: Only presenting positives, ignoring risks or challenges
- **Poor Time Management**: Leaving everything to the last week

### Technical Issues (Track A)
- Deploying broken contracts
- No error handling
- Ignoring gas costs
- Insufficient testing
- Security vulnerabilities

### Research Issues (Track B)
- Cherry-picking data to support hypothesis
- Insufficient sample size
- No original analysis
- Poor visualization choices
- Ignoring contradictory evidence

### Business Issues (Track C)
- Unrealistic financial projections
- Ignoring competitors
- No regulatory consideration
- Vague go-to-market strategy
- Missing the "why blockchain?" justification

---

## Rubric Interpretation Guide

### Using These Rubrics

1. **Self-Assessment**: Use rubrics to self-evaluate before submission
2. **Feedback**: All grading will reference specific rubric criteria
3. **Improvement**: Use checkpoint feedback to improve final submission
4. **Transparency**: No surprises - if it's not in the rubric, it won't be graded

### Grading Process

1. **Initial Scoring**: Instructor scores each criterion independently
2. **Calibration**: Sample projects graded by multiple instructors to ensure consistency
3. **Feedback**: Detailed feedback provided for each major criterion
4. **Grade Calculation**: Weighted average based on rubric weights
5. **Final Review**: Borderline cases (X9.5%) reviewed by second instructor

### Appeals Process

If you believe your grade does not accurately reflect your work:

1. **Wait 24 Hours**: Review feedback objectively after initial disappointment
2. **Self-Evaluate**: Re-read rubrics and assess your work honestly
3. **Document Concerns**: Write specific rubric criteria you believe were misapplied
4. **Submit Appeal**: Email instructor with specific, evidence-based concerns
5. **Meeting**: Discuss in office hours if needed
6. **Resolution**: Instructor will re-evaluate with fresh perspective

**Note**: Appeals based on "I worked hard" or "I need a higher grade" will not be considered. Appeals must reference specific rubric criteria.

---

## Grading Timeline

| Submission | Feedback Timeline |
|------------|-------------------|
| Week 4: Topic Proposal | Within 3 days |
| Week 8: Progress Checkpoint | Within 5 days |
| Week 11: Peer Review | Immediate (peer feedback) |
| Week 12: Final Submission | Within 14 days (2 weeks) |

**Final grades will be submitted to the registrar within 14 days of the final submission deadline.**

---

## Sample Feedback Format

### Track A Example Feedback

**Student: John Doe**
**Project: NFT Marketplace**
**Overall Grade: 87.5% (B+)**

#### Smart Contract Code (88%)
**Strengths:**
- Excellent code organization and structure
- Comprehensive NatSpec documentation
- Good use of OpenZeppelin libraries
- Proper access control implementation

**Areas for Improvement:**
- Some gas inefficiencies in the `listItem` function (consider packing variables)
- Missing input validation for `price` parameter (should check for zero)
- Event emissions could be more detailed

**Specific Deductions:**
- Gas optimization: -3%
- Input validation: -2%

#### Test Suite (85%)
**Strengths:**
- Good coverage of main functionality
- Tests for both success and failure cases
- Clear test naming

**Areas for Improvement:**
- Missing edge case tests (empty arrays, max uint values)
- No fuzz testing for price manipulation
- Gas benchmarks would be valuable

**Specific Deductions:**
- Edge case coverage: -5%

[Additional sections...]

**Overall Comments:**
Solid implementation demonstrating good understanding of Solidity and smart contract development. The code is clean and well-documented. Primary areas for improvement are gas optimization and more comprehensive testing. Great work!

---

## Academic Integrity in Grading

### What Constitutes Academic Dishonesty

- **Plagiarism**: Copying code, text, or analysis without attribution
- **Collusion**: Submitting substantially similar work as another student
- **Contract Cheating**: Paying someone else to complete your project
- **AI Misuse**: Submitting AI-generated content without understanding

### Detection Methods

- Code similarity analysis tools
- Manual review of commits and development history
- Technical interviews for suspicious projects
- Comparison with publicly available projects

### Penalties

- **First Minor Offense**: Reduction in grade with opportunity to redo
- **Major Offense**: Zero on assignment or course failure
- **Repeat Offense**: Course failure + referral to academic integrity office

**When in doubt, cite your sources and ask your instructor.**

---

## Rubric Updates and Clarifications

These rubrics are living documents. If ambiguities arise during the course:

1. Instructor will issue clarifications via LMS announcement
2. No retroactive changes that disadvantage students
3. Clarifications apply to future submissions only
4. Students notified immediately of any updates

**Last Updated:** [Course Start Date]

**Questions?** Ask in office hours, on Discord, or via email for clarification on any rubric criterion.

---

**Success in this course is within your reach. Use these rubrics as a roadmap to excellence!**
