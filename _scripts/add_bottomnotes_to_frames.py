"""
Add bottomnote calls to frames in Modules 02, 03, 04.
This script adds a bottomnote before each \\end{frame} based on frame title.

The bottomnotes are generated based on the frame title to provide
a key takeaway message for each slide.
"""

from pathlib import Path
import re

PROJECT_DIR = Path(__file__).parent.parent
MODULE_DIRS = [
    PROJECT_DIR / 'module_02_blockchain',
    PROJECT_DIR / 'module_03_ai_ml',
    PROJECT_DIR / 'module_04_traditional',
]

# Frames to skip (title page, summary, preview, terminology)
SKIP_PATTERNS = [
    r'\\titlepage',
    r'\\begin{frame}\s*$',  # Title frame without title
    r'Summary',
    r'Key Takeaways',
    r'Next Lesson',
    r'Learning Objectives',
    r'Terminology',
    r'Review',
    r'Questions',
]

def extract_frame_title(frame_content):
    """Extract frame title from frame content."""
    match = re.search(r'\\begin\{frame\}(?:\[[^\]]*\])?\{([^}]+)\}', frame_content)
    if match:
        return match.group(1)
    return None

def should_skip_frame(frame_content, title):
    """Check if this frame should be skipped."""
    if not title:
        return True
    for pattern in SKIP_PATTERNS:
        if re.search(pattern, frame_content, re.IGNORECASE) or re.search(pattern, title, re.IGNORECASE):
            return True
    return False

def has_bottomnote(frame_content):
    """Check if frame already has a bottomnote."""
    return '\\bottomnote{' in frame_content

def generate_bottomnote(title, content):
    """Generate a bottomnote based on frame title and content."""
    # Map of frame titles to bottomnotes (can be extended)
    title_lower = title.lower()

    # Generic bottomnote generation based on title keywords
    if 'trust' in title_lower:
        return "Digital transactions require trust mechanisms---blockchain removes the need for intermediaries."
    elif 'evolution' in title_lower or 'history' in title_lower:
        return "Understanding history helps predict future developments in the technology."
    elif 'satoshi' in title_lower or 'nakamoto' in title_lower:
        return "Bitcoin combined existing cryptographic primitives in a novel way to solve double-spending."
    elif 'definition' in title_lower or 'what is' in title_lower:
        return "Clear definitions are essential for understanding complex technical concepts."
    elif 'centralized' in title_lower and 'decentralized' in title_lower:
        return "Centralized systems trade trust for efficiency; decentralized systems trade efficiency for trustlessness."
    elif 'trilemma' in title_lower:
        return "The blockchain trilemma forces trade-offs between decentralization, security, and scalability."
    elif 'flow' in title_lower or 'process' in title_lower or 'how' in title_lower:
        return "Understanding the process flow is key to identifying optimization opportunities."
    elif 'public' in title_lower and 'private' in title_lower:
        return "Public and private blockchains serve different use cases with different trust models."
    elif 'use case' in title_lower or 'application' in title_lower:
        return "Real-world applications demonstrate the practical value of blockchain technology."
    elif 'example' in title_lower or 'case study' in title_lower:
        return "Case studies provide concrete evidence of technology impact and adoption patterns."
    elif 'limitation' in title_lower or 'challenge' in title_lower:
        return "Understanding limitations helps identify appropriate use cases and avoid over-engineering."
    elif 'vs' in title_lower or 'comparison' in title_lower:
        return "Comparative analysis helps identify the right tool for specific requirements."
    elif 'hype' in title_lower or 'cycle' in title_lower:
        return "Technology adoption follows predictable patterns---timing matters for investment decisions."
    elif 'statistic' in title_lower or 'metric' in title_lower or 'network' in title_lower:
        return "Network metrics provide objective measures of adoption and ecosystem health."
    elif 'bitcoin' in title_lower:
        return "Bitcoin remains the largest cryptocurrency by market cap and network security."
    elif 'ethereum' in title_lower:
        return "Ethereum pioneered smart contracts and remains the dominant platform for DeFi and NFTs."
    elif 'hash' in title_lower or 'crypto' in title_lower:
        return "Cryptographic primitives provide the security foundation for blockchain systems."
    elif 'consensus' in title_lower:
        return "Consensus mechanisms determine how distributed networks agree on shared state."
    elif 'proof' in title_lower and 'work' in title_lower:
        return "Proof-of-Work provides security through computational cost but has energy concerns."
    elif 'proof' in title_lower and 'stake' in title_lower:
        return "Proof-of-Stake offers energy efficiency while maintaining decentralization."
    elif 'smart contract' in title_lower:
        return "Smart contracts enable programmable, self-executing agreements without intermediaries."
    elif 'token' in title_lower:
        return "Tokens represent digital assets and enable new business models on blockchain."
    elif 'defi' in title_lower:
        return "DeFi recreates traditional financial services in a permissionless, programmable way."
    elif 'stablecoin' in title_lower:
        return "Stablecoins bridge traditional and crypto finance by maintaining price stability."
    elif 'security' in title_lower or 'attack' in title_lower:
        return "Security analysis identifies vulnerabilities and helps design robust systems."
    elif 'regulation' in title_lower:
        return "Regulatory frameworks shape adoption patterns and industry structure."
    elif 'future' in title_lower or 'trend' in title_lower:
        return "Future trends inform strategic planning and investment decisions."
    elif 'ai' in title_lower or 'machine learning' in title_lower or 'ml' in title_lower:
        return "AI and ML are transforming financial services through automation and prediction."
    elif 'data' in title_lower:
        return "Quality data is the foundation for effective machine learning models."
    elif 'regression' in title_lower:
        return "Regression models predict continuous outcomes based on input features."
    elif 'classification' in title_lower:
        return "Classification models assign discrete labels to observations."
    elif 'fraud' in title_lower:
        return "Fraud detection balances catching fraud with minimizing false positives."
    elif 'nlp' in title_lower or 'natural language' in title_lower:
        return "NLP extracts insights from unstructured text data at scale."
    elif 'robo' in title_lower or 'advisor' in title_lower:
        return "Robo-advisors democratize investment advice through automation."
    elif 'prediction' in title_lower or 'forecast' in title_lower:
        return "Market prediction is inherently difficult due to efficiency and noise."
    elif 'explainability' in title_lower or 'bias' in title_lower:
        return "Explainability and fairness are critical for responsible AI deployment."
    elif 'market' in title_lower and 'financial' in title_lower:
        return "Financial markets connect savers and borrowers, enabling capital allocation."
    elif 'bank' in title_lower:
        return "Banks play a central role in the financial system as intermediaries."
    elif 'payment' in title_lower:
        return "Payment systems are critical infrastructure for economic activity."
    elif 'trading' in title_lower:
        return "Electronic trading has transformed market structure and efficiency."
    elif 'risk' in title_lower:
        return "Risk management is essential for financial stability and profitability."
    elif 'derivative' in title_lower:
        return "Derivatives enable risk transfer and price discovery."
    elif 'cbdc' in title_lower:
        return "CBDCs represent the digitization of central bank money."
    else:
        # Generic fallback
        return f"Key concepts from this slide inform practical applications in finance."

def add_bottomnotes_to_file(filepath):
    """Add bottomnotes to all frames in a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into frames
    # Pattern to match frame blocks
    frame_pattern = r'(\\begin\{frame\}(?:\[[^\]]*\])?\{[^}]*\}.*?\\end\{frame\})'

    frames = re.findall(frame_pattern, content, re.DOTALL)

    modified = 0
    new_content = content

    for frame in frames:
        title = extract_frame_title(frame)

        # Skip certain frames
        if should_skip_frame(frame, title):
            continue

        # Skip if already has bottomnote
        if has_bottomnote(frame):
            continue

        # Generate bottomnote
        bottomnote_text = generate_bottomnote(title, frame)

        # Add bottomnote before \end{frame}
        new_frame = frame.replace(
            '\\end{frame}',
            f'\\bottomnote{{{bottomnote_text}}}\n\\end{{frame}}'
        )

        new_content = new_content.replace(frame, new_frame)
        modified += 1

    if modified > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return modified

def main():
    print("Adding bottomnotes to frames in Modules 02, 03, 04...")
    print("=" * 70)

    total_modified = 0

    for module_dir in MODULE_DIRS:
        if not module_dir.exists():
            print(f"Module directory not found: {module_dir}")
            continue

        print(f"\n{module_dir.name}:")
        print("-" * 50)

        tex_files = sorted(module_dir.glob('lesson_*.tex'))

        for tex_file in tex_files:
            modified = add_bottomnotes_to_file(tex_file)
            if modified > 0:
                print(f"  {tex_file.name}: {modified} bottomnotes added")
                total_modified += modified
            else:
                print(f"  {tex_file.name}: no changes needed")

    print("\n" + "=" * 70)
    print(f"Total bottomnotes added: {total_modified}")

if __name__ == '__main__':
    main()
