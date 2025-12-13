"""
Customize generic bottomnotes in Module 03 based on slide content
Replaces placeholder text with context-specific insights
"""

from pathlib import Path
import re

BASE_DIR = Path(r"D:\Joerg\Research\slides\DigitalFinance_3")
MODULE_03 = BASE_DIR / "module_03_ai_ml"

# Mapping of slide titles/keywords to appropriate bottomnotes
BOTTOMNOTE_TEMPLATES = {
    # Lesson 25 - Intro AI/ML
    'AI Hierarchy': 'AI encompasses ML which includes deep learning - understanding this hierarchy clarifies terminology.',
    'Machine Learning Types': 'Supervised, unsupervised, and reinforcement learning serve different problem types in finance.',
    'AI Finance Applications': 'AI applications span trading, risk, fraud detection, and customer service across finance.',
    'ML in Finance Timeline': 'ML adoption in finance accelerated after 2010 with big data and computing advances.',
    'Bias-Variance': 'The bias-variance tradeoff is fundamental - models must balance underfitting and overfitting.',

    # Lesson 26 - Financial Data
    'Data Types': 'Financial data includes structured (prices), semi-structured (news), and unstructured (social media).',
    'Data Preprocessing': 'Data preprocessing typically consumes 80% of ML project time in finance.',
    'Feature Engineering': 'Domain expertise in feature engineering often matters more than model complexity.',
    'Survivorship Bias': 'Survivorship bias inflates backtest returns by excluding failed companies from historical data.',

    # Lesson 27 - Regression
    'Linear Regression': 'Linear regression provides interpretable baselines before trying complex models.',
    'Regression Metrics': 'MSE penalizes large errors more than MAE - choose based on business cost of errors.',
    'Residual Analysis': 'Residual patterns reveal model assumptions violations and improvement opportunities.',
    'Overfitting': 'Overfitting produces excellent in-sample fit but poor out-of-sample predictions.',

    # Lesson 28 - Classification
    'Decision Boundary': 'Decision boundaries show how classifiers separate classes in feature space.',
    'Confusion Matrix': 'Confusion matrices reveal error types - critical when false positives/negatives have different costs.',
    'ROC Curve': 'ROC curves show classifier performance across all threshold choices.',
    'Precision-Recall': 'Precision-recall curves are preferred for imbalanced datasets common in finance.',

    # Lesson 29 - Algorithmic Trading
    'Momentum Strategy': 'Momentum strategies exploit price persistence but require careful transaction cost modeling.',
    'Backtest': 'Backtests must account for look-ahead bias, survivorship bias, and market impact.',
    'Order Types': 'Order type selection affects execution quality and information leakage.',
    'Market Making': 'Market makers profit from bid-ask spread while managing inventory risk.',
    'Data Leakage': 'Data leakage invalidates backtests by using future information in predictions.',

    # Lesson 30 - Credit Scoring
    'FICO Score': 'FICO scores range 300-850 with most lenders requiring 620+ for prime rates.',
    'Credit Score Distribution': 'Credit score distributions vary significantly across demographic groups.',
    'Credit Model': 'Credit models must balance predictive power with regulatory fairness requirements.',
    'Default Probability': 'Default probability curves show non-linear relationships with key risk factors.',
    'Feature Importance': 'Feature importance in credit models must be explainable to regulators.',

    # Lesson 31 - Fraud Detection
    'Fraud Types': 'Fraud evolves constantly - models require continuous monitoring and retraining.',
    'Fraud Detection Pipeline': 'Multi-stage fraud pipelines balance speed with accuracy for real-time decisions.',
    'Cost-Benefit': 'Fraud threshold selection depends on false positive costs vs fraud losses.',
    'Anomaly Detection': 'Anomaly detection identifies novel fraud patterns without labeled examples.',
    'Real-Time Scoring': 'Real-time fraud scoring must complete within milliseconds for card transactions.',

    # Lesson 32 - NLP in Finance
    'NLP Pipeline': 'NLP pipelines transform unstructured text into structured features for analysis.',
    'Text Preprocessing': 'Text preprocessing includes tokenization, stemming, and stop word removal.',
    'Sentiment Analysis': 'Sentiment analysis quantifies market mood from news and social media.',
    'Word Embeddings': 'Word embeddings capture semantic relationships for financial text analysis.',
    'News Sentiment': 'News sentiment can predict short-term price movements but signals decay quickly.',

    # Lesson 33 - Robo-Advisors ML
    'Robo Architecture': 'Robo-advisors automate portfolio construction, rebalancing, and tax optimization.',
    'Risk Profiling': 'Risk profiling questionnaires map investor preferences to portfolio allocations.',
    'Portfolio Optimization': 'ML-enhanced optimization can incorporate regime detection and factor timing.',
    'Rebalancing': 'Automated rebalancing maintains target allocations while minimizing transactions.',
    'Robo vs Human': 'Robo-advisors offer lower fees but humans excel at complex planning scenarios.',

    # Lesson 34 - Prediction Limitations
    'Regime Change': 'Regime changes invalidate models trained on different market conditions.',
    'Model Decay': 'Model performance degrades over time as markets adapt to predictive signals.',
    'Model Governance': 'Model governance ensures ongoing monitoring, validation, and documentation.',
    'ML Pipeline': 'Production ML pipelines require versioning, monitoring, and rollback capabilities.',

    # Lesson 35 - Explainability
    'SHAP Values': 'SHAP values decompose predictions into individual feature contributions.',
    'LIME': 'LIME provides local explanations by approximating complex models with simple ones.',
    'Feature Attribution': 'Feature attribution methods help debug models and build stakeholder trust.',
    'PDP ICE': 'Partial dependence plots show average feature effects on predictions.',
    'Algorithmic Bias': 'Algorithmic bias can perpetuate or amplify historical discrimination.',
    'Fairness Metrics': 'Multiple fairness metrics exist - no single definition satisfies all criteria.',

    # Lesson 36 - AI Regulation
    'AI Regulation Landscape': 'AI regulation varies globally with EU taking the most prescriptive approach.',
    'EU AI Act': 'EU AI Act classifies AI systems by risk level with strictest rules for high-risk uses.',
    'AI Investment': 'AI investment in financial services continues growing despite regulatory uncertainty.',
}

def get_appropriate_bottomnote(frame_content, frame_title):
    """Generate appropriate bottomnote based on frame content and title"""

    # Try to match by title keywords
    title_lower = frame_title.lower() if frame_title else ""
    content_lower = frame_content.lower()

    for keyword, note in BOTTOMNOTE_TEMPLATES.items():
        if keyword.lower() in title_lower or keyword.lower() in content_lower:
            return note

    # Fallback: generate based on content analysis
    if 'chart' in content_lower or 'figure' in content_lower or 'includegraphics' in content_lower:
        return 'This visualization illustrates key patterns discussed in the lecture.'
    elif 'itemize' in content_lower or 'enumerate' in content_lower:
        return 'These concepts form the foundation for practical applications in finance.'
    else:
        return 'Understanding these principles enables better decision-making in financial ML.'


def customize_bottomnotes(tex_path):
    """Replace generic bottomnotes with context-specific ones"""
    content = tex_path.read_text(encoding='utf-8', errors='ignore')
    original_content = content

    # Find frames with generic bottomnotes
    generic_patterns = [
        r'\\bottomnote\{Key insight from this visualization\.\}',
        r'\\bottomnote\{Summary of key concepts presented above\.\}'
    ]

    changes = 0

    # Process each frame
    frame_pattern = r'(\\begin\{frame\}(?:\[[^\]]*\])?\{([^}]+)\}.*?)(\\bottomnote\{(?:Key insight from this visualization|Summary of key concepts presented above)\.\})(.*?\\end\{frame\})'

    def replace_bottomnote(match):
        nonlocal changes
        frame_start = match.group(1)
        frame_title = match.group(2)
        old_bottomnote = match.group(3)
        frame_end = match.group(4)

        # Get appropriate bottomnote
        new_note = get_appropriate_bottomnote(frame_start + frame_end, frame_title)
        new_bottomnote = f'\\bottomnote{{{new_note}}}'

        if new_bottomnote != old_bottomnote:
            changes += 1

        return frame_start + new_bottomnote + frame_end

    content = re.sub(frame_pattern, replace_bottomnote, content, flags=re.DOTALL)

    if content != original_content:
        tex_path.write_text(content, encoding='utf-8')
        return changes
    return 0


def main():
    print("=" * 70)
    print("CUSTOMIZING MODULE 03 BOTTOMNOTES")
    print("=" * 70)

    total_changes = 0

    tex_files = sorted(MODULE_03.glob("lesson_*.tex"))

    for tex_file in tex_files:
        changes = customize_bottomnotes(tex_file)
        if changes > 0:
            print(f"  {tex_file.name}: {changes} bottomnotes customized")
            total_changes += changes
        else:
            print(f"  {tex_file.name}: no changes needed")

    print()
    print(f"Total bottomnotes customized: {total_changes}")


if __name__ == "__main__":
    main()
