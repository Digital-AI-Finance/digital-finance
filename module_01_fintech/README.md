# Module 1: FinTech Fundamentals

## Overview
Complete Beamer slide deck for Module 1 (Lessons 1-12) of Digital Finance course.
Professional, chart-heavy presentations designed for university-level instruction.

---

## Contents

### Completed Lessons

#### Lesson 1: Introduction to FinTech
- **File**: `20251207_1915_lesson_01_intro_fintech.tex`
- **Topics**: FinTech definition, evolution, ecosystem, disruption patterns
- **Slides**: ~15

#### Lesson 2: Digital Payments Fundamentals
- **File**: `20251207_1915_lesson_02_payments_fundamentals.tex`
- **Topics**: Payment infrastructure, card networks, SWIFT, instant payments
- **Slides**: ~16

#### Lesson 3: Digital Payments II - Mobile Wallets
- **File**: `20251207_2009_lesson_03_mobile_wallets.tex`
- **Topics**: NFC, Apple Pay, M-Pesa, Alipay, super-apps
- **Slides**: 17
- **Charts**: 7 (generated)

#### Lesson 4: Neobanks and Challenger Banks
- **File**: `20251207_2009_lesson_04_neobanks.tex`
- **Topics**: Revolut, N26, business models, unit economics
- **Slides**: 17
- **Charts**: 5 (generated)

#### Lesson 5: Open Banking and APIs
- **File**: `20251207_2009_lesson_05_open_banking.tex`
- **Topics**: PSD2, SCA, AIS/PIS, use cases
- **Slides**: 18
- **Charts**: 7 (pending)

#### Lesson 6: Digital Identity and Authentication
- **File**: `20251207_2009_lesson_06_digital_identity.tex`
- **Topics**: KYC, eIDAS, biometrics, SSI
- **Slides**: 18
- **Charts**: 7 (pending)

#### Lesson 7: Peer-to-Peer Lending
- **File**: `20251207_2009_lesson_07_p2p_lending.tex`
- **Topics**: P2P model, LendingClub, alternative scoring
- **Slides**: 18
- **Charts**: 7 (pending)

#### Lesson 8: Robo-Advisors and Digital Wealth
- **File**: `20251207_2009_lesson_08_robo_advisors.tex`
- **Topics**: Betterment, portfolio construction, fees
- **Slides**: 18
- **Charts**: 7 (pending)

#### Lesson 9: InsurTech
- **File**: `20251207_2009_lesson_09_insurtech.tex`
- **Topics**: Lemonade, UBI, parametric insurance
- **Slides**: 18
- **Charts**: 7 (pending)

#### Lesson 10: RegTech
- **File**: `20251207_2009_lesson_10_regtech.tex`
- **Topics**: AML technology, transaction monitoring
- **Slides**: 18
- **Charts**: 7 (pending)

#### Lesson 11: Regulatory Frameworks
- **File**: `20251207_2009_lesson_11_regulatory_frameworks.tex`
- **Topics**: PSD2 deep dive, MiCA, DORA
- **Slides**: 18
- **Charts**: 7 (pending)

#### Lesson 12: Fintech Business Models
- **File**: `20251207_2009_lesson_12_business_models.tex`
- **Topics**: Embedded finance, BaaS, future trends
- **Slides**: 18
- **Charts**: 7 (pending)

---

## Statistics

| Metric | Value |
|--------|-------|
| Total Lessons | 12 |
| Total Slides | ~210 |
| Charts Generated | 12 |
| Charts Pending | ~158 |
| LaTeX Files | 12 |
| Total Size | ~80 KB (source) |

---

## Compilation

### Prerequisites
```bash
# LaTeX distribution with Beamer
# pdflatex compiler
# Python 3.8+ with matplotlib, seaborn, numpy, pandas
```

### Compile Individual Lesson
```bash
cd D:/Joerg/Research/slides/DigitalFinance_3/module_01_fintech
pdflatex 20251207_2009_lesson_03_mobile_wallets.tex
```

### Compile All Lessons
```bash
# Windows PowerShell
Get-ChildItem -Filter "*.tex" | ForEach-Object { pdflatex $_.Name }

# Linux/Mac bash
for f in *.tex; do pdflatex "$f"; done
```

### Generate Charts
```bash
python generate_all_charts.py
```

---

## Design Specifications

### Template
- **Document class**: Beamer, 8pt, 16:9 aspect ratio
- **Theme**: Madrid
- **Colors**: Lavender palette (mlpurple, mllavender series)
- **Margins**: 5mm left/right

### Color Palette
```latex
mlblue      RGB(0,102,204)
mlpurple    RGB(51,51,178)
mllavender  RGB(173,173,224)
mllavender2 RGB(193,193,232)
mllavender3 RGB(204,204,235)
mllavender4 RGB(214,214,239)
mlorange    RGB(255,127,14)
mlgreen     RGB(44,160,44)
mlred       RGB(214,39,40)
```

### Slide Structure
- Maximum 1 chart per slide
- Two-column layout preferred (0.48\textwidth each)
- Minimal bullet points (4-5 maximum)
- Chart-heavy design (60-70% chart-to-content ratio)

---

## Chart Categories

### Required Chart Types per Lesson

1. **Market Landscapes** (~35 charts total)
   - Growth trajectories
   - Market share distributions
   - Adoption curves
   - Regional comparisons

2. **Architecture Diagrams** (~30 charts)
   - Technical flows
   - System architectures
   - Integration patterns
   - Security layers

3. **Business Models** (~30 charts)
   - Revenue structures
   - Unit economics
   - Cost breakdowns
   - Value chains

4. **Process Flows** (~35 charts)
   - Transaction sequences
   - Workflow diagrams
   - User journeys
   - Regulatory processes

5. **Comparative Analyses** (~40 charts)
   - Traditional vs digital
   - Regional differences
   - Product comparisons
   - Performance benchmarks

---

## File Organization

```
module_01_fintech/
├── README.md                                    # This file
├── LESSONS_SUMMARY.md                           # Detailed lesson breakdown
├── generate_all_charts.py                       # Chart generation script
├── 20251207_1915_lesson_01_intro_fintech.tex
├── 20251207_1915_lesson_02_payments_fundamentals.tex
├── 20251207_2009_lesson_03_mobile_wallets.tex
├── 20251207_2009_lesson_04_neobanks.tex
├── 20251207_2009_lesson_05_open_banking.tex
├── 20251207_2009_lesson_06_digital_identity.tex
├── 20251207_2009_lesson_07_p2p_lending.tex
├── 20251207_2009_lesson_08_robo_advisors.tex
├── 20251207_2009_lesson_09_insurtech.tex
├── 20251207_2009_lesson_10_regtech.tex
├── 20251207_2009_lesson_11_regulatory_frameworks.tex
├── 20251207_2009_lesson_12_business_models.tex
└── figures/
    ├── mobile_wallet_adoption.pdf
    ├── nfc_technology_diagram.pdf
    ├── apple_pay_flow.pdf
    ├── mpesa_growth.pdf
    ├── china_wallet_comparison.pdf
    ├── qr_vs_nfc_comparison.pdf
    ├── global_wallet_share.pdf
    ├── neobank_vs_traditional.pdf
    ├── neobank_market_leaders.pdf
    ├── revolut_growth.pdf
    ├── neobank_unit_economics.pdf
    ├── cac_comparison.pdf
    └── [~158 more charts to be generated]
```

---

## Next Steps

### Immediate Tasks
1. **Complete chart generation** for lessons 5-12 (~158 charts)
2. **Test LaTeX compilation** for all lessons
3. **Verify figure references** match generated files
4. **Create placeholder charts** for any missing figures

### Chart Generation Priority
1. Lesson 5 (Open Banking) - regulatory framework critical
2. Lesson 11 (Regulatory Frameworks) - context for entire module
3. Lesson 12 (Business Models) - synthesis lesson
4. Lessons 6-10 - domain-specific visualizations

### Quality Assurance
- [ ] All charts generated and saved as PDF
- [ ] LaTeX compiles without errors for all lessons
- [ ] Figure references validated
- [ ] Consistent color scheme across all charts
- [ ] Professional typography and layout
- [ ] Grayscale-friendly design (print-compatible)

---

## Usage Notes

### For Instructors
- Each lesson designed for 50-75 minute lecture
- Charts support lecture narrative (not standalone)
- Minimal text on slides (instructor explains)
- Key takeaways slide at end of each lesson

### Customization
- Edit LaTeX files directly for content changes
- Regenerate charts using Python script
- Color scheme customizable in preamble
- Add/remove slides as needed

### Printing
- Optimized for 16:9 screen display
- Grayscale-friendly color palette
- High-resolution charts (300 dpi)
- Suitable for handout generation

---

## References

### Data Sources
- Market statistics: Company reports, Statista, CB Insights
- Regulatory information: EU official documents, FCA, SEC
- Technical specifications: Payment network documentation

### Academic Context
- Course: Digital Finance
- Level: Undergraduate/Graduate
- Prerequisites: Basic finance, microeconomics
- Learning outcomes: Understanding FinTech ecosystem, business models, regulation

---

## Version History

| Date | Version | Changes |
|------|---------|---------|
| 2025-12-07 | 1.0 | Initial creation of lessons 3-12 |
| 2025-12-07 | 1.1 | Generated first 12 charts (lessons 3-4) |

---

## Contact & Support

For questions or issues:
1. Check LESSONS_SUMMARY.md for detailed content breakdown
2. Review generate_all_charts.py for chart specifications
3. Verify LaTeX compilation with minimal example

---

**Generated**: 2025-12-07 20:20
**Format**: Beamer LaTeX, 8pt, Madrid theme, 16:9
**Location**: `D:/Joerg/Research/slides/DigitalFinance_3/module_01_fintech/`
