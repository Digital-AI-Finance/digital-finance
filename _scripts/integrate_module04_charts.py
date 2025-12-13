"""
Integrate charts into Module 04 lessons
Adds chart slides after appropriate content sections
"""

from pathlib import Path
import re

# Chart mappings: lesson -> [(chart_folder, insertion_marker, bottomnote)]
CHART_MAPPINGS = {
    'lesson_40_electronic_trading.tex': [
        ('order_book', r'\\bottomnote\{Electronic trading has transformed market structure and efficiency\.\}',
         'Order book depth reveals supply and demand dynamics at each price level.'),
        ('hft_market_share', r'\\section\{High-Frequency Trading\}',
         'HFT now represents a significant portion of market activity in major venues.'),
        ('trading_latency', r'Round-trip execution: 200-1000 microseconds',
         'Latency optimization is critical for competitive advantage in electronic markets.'),
        ('market_makers', r'\\section\{Market Making\}',
         'Market makers provide continuous liquidity through bid-ask quotes.'),
        ('fx_volume', r'\\section\{FX Markets\}',
         'FX markets operate 24/5 with massive daily turnover across global centers.'),
    ],
    'lesson_41_market_microstructure.tex': [
        ('bid_ask_spread', r'\\section\{Bid-Ask Spread\}',
         'Bid-ask spread measures liquidity cost and information asymmetry.'),
        ('liquidity_metrics', r'\\section\{Liquidity\}',
         'Multiple dimensions capture different aspects of market liquidity.'),
        ('volatility_term_structure', r'\\section\{Volatility\}',
         'Volatility term structure reveals market expectations across time horizons.'),
        ('correlation_matrix', r'\\section\{Correlation\}',
         'Asset correlations drive portfolio diversification and risk management.'),
    ],
    'lesson_42_risk_management.tex': [
        ('var_histogram', r'\\section\{Value at Risk\}',
         'VaR quantifies potential losses at a given confidence level.'),
        ('risk_types', r'\\section\{Risk Types\}',
         'Financial institutions face multiple categories of risk requiring specialized management.'),
        ('stress_testing', r'\\section\{Stress Testing\}',
         'Stress tests evaluate resilience under extreme but plausible scenarios.'),
        ('basel_capital', r'\\section\{Basel\}',
         'Basel frameworks define minimum capital requirements for credit risk.'),
        ('credit_rating_distribution', r'\\section\{Credit Risk\}',
         'Credit ratings provide standardized assessment of default probability.'),
    ],
    'lesson_43_regtech_compliance.tex': [
        ('compliance_costs', r'\\section\{Compliance\}',
         'Compliance costs have grown substantially post-financial crisis.'),
        ('regulatory_fines', r'\\section\{Enforcement\}',
         'Regulatory fines for non-compliance can reach billions of dollars.'),
        ('aml_transaction_monitoring', r'\\section\{AML\}',
         'Transaction monitoring systems screen billions of transactions for suspicious patterns.'),
        ('kyc_process', r'\\section\{KYC\}',
         'KYC processes balance customer onboarding speed with risk management.'),
    ],
    'lesson_44_capital_markets_tech.tex': [
        ('capital_markets_workflow', r'\\section\{Capital Markets\}',
         'Capital markets involve complex workflows from origination to settlement.'),
        ('ipo_timeline', r'\\section\{IPO\}',
         'IPO process requires coordination across multiple parties over several months.'),
        ('bond_types', r'\\section\{Bond\}',
         'Bond markets offer diverse instruments across risk and maturity spectrum.'),
        ('underwriting_fees', r'\\section\{Underwriting\}',
         'Underwriting fees vary by deal size, complexity, and market conditions.'),
        ('clearing_process', r'\\section\{Clearing\}',
         'Clearing reduces counterparty risk through central counterparty novation.'),
    ],
    'lesson_45_derivatives_technology.tex': [
        ('derivatives_notional', r'\\section\{Derivatives Markets\}',
         'Derivatives markets measured in notional value dwarf underlying assets.'),
        ('option_payoff', r'\\section\{Options\}',
         'Option payoff profiles create asymmetric risk-return characteristics.'),
        ('option_greeks', r'Greeks measure option sensitivity',
         'Greeks quantify option price sensitivity to underlying factors.'),
        ('margin_requirements', r'\\section\{Margin\}',
         'Margin requirements ensure counterparty risk mitigation in derivatives trading.'),
    ],
    'lesson_46_wealth_management.tex': [
        ('wealth_aum', r'\\section\{Wealth Management\}',
         'Global wealth management AUM continues to grow driven by high-net-worth expansion.'),
        ('portfolio_allocation', r'\\section\{Portfolio\}',
         'Strategic asset allocation drives long-term portfolio returns.'),
        ('fee_comparison', r'\\section\{Fees\}',
         'Fee structures vary significantly across wealth management service models.'),
        ('etf_growth', r'\\section\{ETF\}',
         'ETF growth has transformed passive investing and fee compression.'),
    ],
    'lesson_47_data_vendors.tex': [
        ('data_vendor_market', r'\\section\{Data Vendors\}',
         'Bloomberg and Refinitiv dominate the financial data vendor market.'),
        ('alternative_data', r'\\section\{Alternative Data\}',
         'Alternative data sources provide unique insights beyond traditional datasets.'),
        ('fintech_traditional_comparison', r'\\section\{FinTech\}',
         'FinTech data providers challenge incumbents with modern APIs and pricing.'),
    ],
    'lesson_48_cbdc_future.tex': [
        ('cbdc_adoption', r'\\section\{CBDC\}',
         'Central bank digital currency projects span research, pilots, and live deployments.'),
        ('cbdc_design', r'design choices',
         'CBDC design involves fundamental choices about architecture and access models.'),
    ],
}

def create_chart_slide(chart_folder, bottomnote):
    """Generate LaTeX for a chart-only slide"""
    chart_name = chart_folder.replace('_', ' ').title()
    return f"""
\\begin{{frame}}[t]{{{chart_name}}}
\\begin{{center}}
\\includegraphics[width=0.60\\textwidth]{{figures/{chart_folder}/{chart_folder}.pdf}}
\\end{{center}}
\\bottomnote{{{bottomnote}}}
\\end{{frame}}
"""

def integrate_charts(lesson_file, chart_specs):
    """Add chart slides to lesson file"""
    file_path = Path('D:/Joerg/Research/slides/DigitalFinance_3/module_04_traditional') / lesson_file

    if not file_path.exists():
        print(f"SKIP: {lesson_file} not found")
        return False

    content = file_path.read_text(encoding='utf-8')
    original_content = content

    for chart_folder, marker, bottomnote in chart_specs:
        chart_slide = create_chart_slide(chart_folder, bottomnote)

        # Find the marker and insert after the frame
        if marker.startswith(r'\\section'):
            # Insert before section
            pattern = f'({re.escape(marker)})'
            replacement = f'{chart_slide.strip()}\\n\\n\\1'
        else:
            # Insert after frame ending (find next \end{frame})
            pattern = f'({re.escape(marker)}.*?\\\\end{{frame}})'
            replacement = f'\\1{chart_slide}'

        content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)

    if content != original_content:
        file_path.write_text(content, encoding='utf-8')
        print(f"✓ Updated {lesson_file} with {len(chart_specs)} charts")
        return True
    else:
        print(f"⚠ No changes made to {lesson_file}")
        return False

def main():
    print("Integrating charts into Module 04 lessons...\n")

    updated = 0
    for lesson_file, chart_specs in CHART_MAPPINGS.items():
        if integrate_charts(lesson_file, chart_specs):
            updated += 1

    print(f"\n✓ Updated {updated}/{len(CHART_MAPPINGS)} lessons")

if __name__ == '__main__':
    main()
