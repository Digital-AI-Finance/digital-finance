"""
Add bottomnotes and section dividers to Module 01 Lessons 09-12
"""
import re
from pathlib import Path

# Lesson configurations with section dividers and bottomnotes
LESSONS = {
    'lesson_09_insurtech.tex': {
        'sections': [
            (r'\\begin{frame}{Insurance Industry Challenges}', 'InsurTech Fundamentals'),
            (r'\\begin{frame}{Lemonade Case Study}', 'Lemonade Case Study'),
            (r'\\begin{frame}{Usage-Based Insurance \(UBI\)}', 'Usage-Based Insurance'),
            (r'\\begin{frame}{Parametric Insurance}', 'Parametric and Embedded'),
            (r'\\begin{frame}{InsurTech Market Segments}', 'Market and Distribution'),
            (r'\\begin{frame}{Regulatory Challenges}', 'Challenges and Future'),
        ],
        'bottomnotes': {
            'Insurance Industry Challenges': 'Insurance legacy systems struggle with 25-30\% operating costs---InsurTech disrupts every step.',
            'InsurTech Value Chain': 'InsurTech companies target specific pain points---from underwriting to claims to distribution.',
            'Lemonade Case Study': 'Lemonade offers 90-second policy purchase and 3-minute claims---AI-first from day one.',
            'Lemonade Business Model': 'Flat 25\% fee model with Giveback charity donation---reduces fraud incentive through alignment.',
            'Giveback Program': 'Behavioral economics: customers donate unclaimed premiums to charity---reducing fraudulent claims.',
            'AI Claims Processing': 'AI Jim approves 40\% of claims instantly---computer vision and anti-fraud detection automate the rest.',
            'Usage-Based Insurance (UBI)': 'Telematics-based pricing offers 30-50\% savings for safe drivers---IoT sensors track behavior.',
            'Telematics Data Points': 'Hard braking, acceleration, speed, and mileage data determine personalized premiums.',
            'Progressive Snapshot Program': 'Progressive enrolled 14M drivers---average 16\% discount through behavioral monitoring.',
            'Parametric Insurance': 'Index-based triggers eliminate claims adjusters---predefined events trigger instant payouts.',
            'Parametric Insurance Examples': 'Weather, earthquakes, flight delays, and crop yields all enable parametric products.',
            'Flight Delay Insurance': '2+ hour flight delay triggers automatic payout---no claim form, instant API-based processing.',
            'Embedded Insurance': 'Point-of-sale insurance captures the moment of need---integrated into e-commerce and travel.',
            'InsurTech Market Segments': 'Personal lines, commercial, life, and health each have specialized InsurTech disruptors.',
            'Distribution Innovation': 'Digital brokers and aggregators bypass traditional agents---API-first enables embedded distribution.',
            'Regulatory Challenges': 'State-by-state licensing and capital requirements slow InsurTech expansion---compliance is costly.',
            'Incumbent Response': 'Traditional insurers partner, acquire, and build innovation labs---digital transformation accelerates.',
            'Future: Predictive Prevention': 'IoT and wearables enable prevention over coverage---from reactive claims to proactive risk reduction.',
            'Key Takeaways': 'InsurTech transforms insurance from reactive claims processing to proactive risk prevention.',
        }
    },
    'lesson_10_regtech.tex': {
        'sections': [
            (r'\\begin{frame}{Regulatory Burden}', 'RegTech Fundamentals'),
            (r'\\begin{frame}{Compliance Cost Structure}', 'Compliance Economics'),
            (r'\\begin{frame}{KYC/AML Automation}', 'KYC and AML Solutions'),
            (r'\\begin{frame}{Transaction Monitoring}', 'Transaction Monitoring'),
            (r'\\begin{frame}{Regulatory Reporting}', 'Reporting and Risk'),
            (r'\\begin{frame}{Regulatory Sandboxes}', 'Future and Summary'),
        ],
        'bottomnotes': {
            'Regulatory Burden': 'Financial institutions spend \$270B annually on compliance---RegTech automates the burden.',
            'RegTech Value Proposition': 'RegTech reduces compliance costs 50-70\% through automation---speed and accuracy improve.',
            'RegTech Market Size': 'Global RegTech market reached \$12B (2023)---projected to reach \$45B by 2028.',
            'Compliance Cost Structure': 'Banks spend 4-10\% of revenue on compliance---staff, technology, and fines dominate costs.',
            'KYC/AML Automation': 'Automated KYC reduces onboarding time from days to minutes---AI flags suspicious patterns.',
            'KYC Process Flow': 'Document verification, biometric matching, and sanctions screening run in parallel---real-time decisions.',
            'AML Detection Systems': 'Machine learning detects suspicious patterns across millions of transactions---reducing false positives.',
            'False Positive Challenge': '95\% of AML alerts are false positives---ML models improve precision 5-10x over rules.',
            'Transaction Monitoring': 'Real-time monitoring across all channels---AI detects unusual patterns instantly.',
            'Suspicious Activity Detection': 'Graph analytics reveal hidden relationships---network analysis uncovers money laundering rings.',
            'Regulatory Reporting': 'Automated report generation reduces manual work 80\%---regulatory filings become push-button.',
            'Reporting Automation': 'APIs connect directly to regulators---real-time data submission replaces quarterly reports.',
            'Risk Management Tools': 'Integrated risk dashboards provide real-time exposure---stress testing runs continuously.',
            'Model Risk Management': 'AI models require validation and governance---explainability is mandatory for regulators.',
            'Regulatory Sandboxes': 'Sandboxes allow testing innovation under supervision---50+ countries have sandbox programs.',
            'Global Sandbox Adoption': 'UK FCA pioneered sandboxes in 2016---now standard for fostering responsible innovation.',
            'Incumbent vs RegTech': 'Banks partner with RegTech vendors---build vs buy favors specialized solutions.',
            'Future: Embedded Compliance': 'Compliance becomes invisible infrastructure---embedded at every transaction point.',
            'Key Takeaways': 'RegTech transforms compliance from cost center to competitive advantage---automation is essential.',
        }
    },
    'lesson_11_crowdfunding.tex': {
        'sections': [
            (r'\\begin{frame}{Crowdfunding Definition}', 'Crowdfunding Fundamentals'),
            (r'\\begin{frame}{Kickstarter Case Study}', 'Reward-Based Crowdfunding'),
            (r'\\begin{frame}{Equity Crowdfunding}', 'Equity Crowdfunding'),
            (r'\\begin{frame}{Real Estate Crowdfunding}', 'Specialized Platforms'),
            (r'\\begin{frame}{Platform Economics}', 'Economics and Regulation'),
            (r'\\begin{frame}{Future: Tokenization}', 'Future and Summary'),
        ],
        'bottomnotes': {
            'Crowdfunding Definition': 'Crowdfunding raises capital from many small investors---democratizing access to funding.',
            'Crowdfunding Models': 'Four models: donation, reward, lending, and equity---each serves different purposes.',
            'Global Market Size': 'Global crowdfunding reached \$17B (2023)---lending dominates, equity grows fastest.',
            'Kickstarter Case Study': 'Kickstarter funded 240,000+ projects totaling \$7B---all-or-nothing model reduces risk.',
            'Kickstarter Success Factors': '36\% success rate---strong video, clear rewards, and community engagement drive success.',
            'Reward Campaign Structure': 'Tiered rewards incentivize higher pledges---early-bird pricing creates urgency.',
            'Equity Crowdfunding': 'Retail investors buy startup equity---JOBS Act (2016) enabled US equity crowdfunding.',
            'Regulation Crowdfunding': 'Reg CF allows \$5M raises from retail investors---SEC registration exemption with limits.',
            'SeedInvest Case Study': 'SeedInvest funded 275+ startups---average investment \$1,000, minimum \$500.',
            'Investor Returns': 'Equity crowdfunding returns are highly variable---most investments fail, winners are rare.',
            'Real Estate Crowdfunding': 'Fundrise pioneered real estate crowdfunding---\$3B+ AUM with 8-12\% historical returns.',
            'Real Estate Platform Models': 'Debt vs equity: debt offers fixed returns (8-10\%), equity offers upside potential.',
            'Platform Economics': 'Platforms charge 5-10\% of raises---success fee model aligns incentives.',
            'Campaign Success Rates': 'Overall 30-40\% success---product categories outperform services and causes.',
            'Fraud and Failure Risk': 'Regulation reduces fraud but failures common---90\% of startups fail within 5 years.',
            'Regulatory Landscape': 'US, UK, and EU have distinct frameworks---cross-border crowdfunding expanding.',
            'Future: Tokenization': 'Security tokens enable 24/7 trading of crowdfunded equity---liquidity improves.',
            'Key Takeaways': 'Crowdfunding democratizes capital access---but high failure rates require portfolio diversification.',
        }
    },
    'lesson_12_fintech_ecosystem.tex': {
        'sections': [
            (r'\\begin{frame}{FinTech Ecosystem Overview}', 'Ecosystem Overview'),
            (r'\\begin{frame}{Embedded Finance}', 'Embedded Finance'),
            (r'\\begin{frame}{Banking-as-a-Service}', 'Banking-as-a-Service'),
            (r'\\begin{frame}{Super Apps}', 'Super Apps and Platforms'),
            (r'\\begin{frame}{Consolidation Trends}', 'Market Dynamics'),
            (r'\\begin{frame}{Future: AI-First Finance}', 'Future and Summary'),
        ],
        'bottomnotes': {
            'FinTech Ecosystem Overview': 'FinTech ecosystem spans payments to wealth to insurance---each segment has specialized disruptors.',
            'FinTech Investment Trends': 'Global FinTech investment peaked at \$238B (2021)---down to \$96B (2023) as valuations reset.',
            'Module Summary Map': 'Module 1 covered payments, banking, identity, lending, wealth, insurance, and regulation.',
            'Embedded Finance': 'Non-financial brands offer financial services---Buy Now Pay Later at checkout is embedded finance.',
            'Embedded Finance Market': 'Embedded finance projected to reach \$7T by 2030---every company becomes a fintech.',
            'Banking-as-a-Service': 'BaaS enables any company to offer banking---APIs connect to licensed bank infrastructure.',
            'BaaS Architecture': 'Three layers: licensed bank, BaaS platform, and brand---each earns revenue from the stack.',
            'BaaS Provider Landscape': 'Synapse, Unit, and Treasury Prime lead US BaaS---European players include Solarisbank.',
            'Super Apps': 'Super apps combine payments, commerce, and services---WeChat and Grab dominate Asia.',
            'WeChat Ecosystem': 'WeChat has 1.3B users---payments, messaging, mini-programs, and lifestyle in one app.',
            'Platform Strategy': 'Platforms capture value through network effects---winner-take-most dynamics emerge.',
            'Consolidation Trends': 'FinTech M&A accelerates---1,000+ deals annually as winners absorb competitors.',
            'Valuation Compression': '2022-2023 saw 60-80\% valuation declines---profitability now prioritized over growth.',
            'Regulatory Evolution': 'Regulators globally tighten FinTech oversight---same risk, same rules emerging principle.',
            'Future: AI-First Finance': 'AI transforms every financial function---from risk to service to operations.',
            'Key Takeaways': 'FinTech disrupted every financial sector---now consolidating with traditional finance.',
        }
    }
}

def add_bottomnote_command(content):
    """Add bottomnote command if not present"""
    if '\\newcommand{\\bottomnote}' in content:
        return content

    insert_pattern = r'(\\setbeamersize{text margin left=5mm,text margin right=5mm})'
    bottomnote_cmd = '''\\setbeamersize{text margin left=5mm,text margin right=5mm}

% Bottom note command for key takeaways
\\newcommand{\\bottomnote}[1]{%
\\vfill
\\begin{beamercolorbox}[wd=\\textwidth,ht=2.5ex,dp=1ex,leftskip=0.5em]{palette tertiary}
\\small\\textit{#1}
\\end{beamercolorbox}
}'''
    return re.sub(insert_pattern, bottomnote_cmd, content)

def add_sections(content, sections):
    """Add section dividers"""
    for pattern, section_name in sections:
        section_block = f'''% =============================================================================
\\section{{{section_name}}}
% =============================================================================

'''
        # Only add if section doesn't already exist
        if f'\\section{{{section_name}}}' not in content:
            content = re.sub(pattern, section_block + pattern.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)'), content)
    return content

def add_bottomnotes(content, bottomnotes):
    """Add bottomnotes to frames"""
    for frame_title, note in bottomnotes.items():
        # Pattern to find frame end
        # Match frame title and find the \end{frame}
        frame_pattern = rf'(\\begin{{frame}}(?:\[t\])?{{{re.escape(frame_title)}}}.*?)(\\end{{frame}})'

        def add_note(match):
            frame_content = match.group(1)
            end_frame = match.group(2)
            # Only add if bottomnote not already present in this frame
            if '\\bottomnote{' in frame_content:
                return match.group(0)
            return f'{frame_content}\\bottomnote{{{note}}}\n{end_frame}'

        content = re.sub(frame_pattern, add_note, content, flags=re.DOTALL)
    return content

def reduce_chart_widths(content):
    """Reduce chart widths to prevent overflow"""
    # Replace 0.75 and 0.72 with 0.65
    content = re.sub(r'\\includegraphics\[width=0\.7[25]\\textwidth\]',
                     r'\\includegraphics[width=0.65\\textwidth]', content)
    content = re.sub(r'\\includegraphics\[width=0\.70\\textwidth\]',
                     r'\\includegraphics[width=0.65\\textwidth]', content)
    return content

def process_lesson(filepath, config):
    """Process a single lesson file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add bottomnote command
    content = add_bottomnote_command(content)

    # Add section dividers
    content = add_sections(content, config['sections'])

    # Add bottomnotes to frames
    content = add_bottomnotes(content, config['bottomnotes'])

    # Reduce chart widths
    content = reduce_chart_widths(content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Processed: {filepath.name}")

def main():
    module_dir = Path(__file__).parent.parent / 'module_01_fintech'

    for filename, config in LESSONS.items():
        filepath = module_dir / filename
        if filepath.exists():
            process_lesson(filepath, config)
        else:
            print(f"File not found: {filepath}")

    print("\nAll lessons processed. Run pdflatex to compile.")

if __name__ == '__main__':
    main()
