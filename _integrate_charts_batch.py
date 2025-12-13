"""
Batch integrate charts into Module 03 lessons
"""

import subprocess
from pathlib import Path

# Chart mappings
CHART_MAPPINGS = {
    28: {
        'file': 'lesson_28_classification.tex',
        'charts': {
            'decision_boundary': 'Decision boundaries visualization',
            'confusion_matrix': 'Confusion matrix structure',
            'confusion_matrix_finance': 'Confusion matrix in finance context',
            'roc_curve': 'ROC curve visualization',
            'roc_curve_example': 'ROC curve example'
        }
    },
    29: {
        'file': 'lesson_29_algorithmic_trading_concepts.tex',
        'charts': {
            'momentum_strategy': 'Momentum strategy performance',
            'trading_strategy_backtest': 'Backtest results',
            'order_types': 'Order types comparison',
            'market_making_spread': 'Market making spread analysis',
            'data_leakage': 'Data leakage example'
        }
    },
    30: {
        'file': 'lesson_30_credit_scoring_and_risk_models.tex',
        'charts': {
            'fico_score_ranges': 'FICO score ranges',
            'credit_score_distribution': 'Credit score distribution',
            'credit_model_comparison': 'Model comparison',
            'default_probability_curve': 'Default probability curve',
            'feature_importance_credit': 'Feature importance',
            'algorithm_comparison': 'Algorithm performance comparison'
        }
    },
    31: {
        'file': 'lesson_31_fraud_detection_and_aml.tex',
        'charts': {
            'fraud_types_distribution': 'Fraud types distribution',
            'fraud_detection_pipeline': 'Detection pipeline',
            'fraud_cost_benefit': 'Cost-benefit analysis',
            'anomaly_detection': 'Anomaly detection methods',
            'real_time_scoring': 'Real-time scoring architecture'
        }
    },
    32: {
        'file': 'lesson_32_nlp_in_finance.tex',
        'charts': {
            'nlp_pipeline_finance': 'NLP pipeline',
            'text_preprocessing': 'Text preprocessing steps',
            'sentiment_analysis': 'Sentiment analysis results',
            'word_embeddings': 'Word embeddings visualization',
            'news_sentiment_impact': 'News sentiment impact on markets'
        }
    },
    33: {
        'file': 'lesson_33_robo-advisors_ml_aspects.tex',
        'charts': {
            'robo_advisor_architecture': 'Architecture overview',
            'risk_profiling_questionnaire': 'Risk profiling approach',
            'portfolio_optimization_ml': 'ML-based optimization',
            'automated_rebalancing': 'Automated rebalancing',
            'robo_vs_human': 'Robo vs human comparison'
        }
    },
    34: {
        'file': 'lesson_34_market_prediction_limitations.tex',
        'charts': {
            'regime_change': 'Regime change detection',
            'model_decay': 'Model decay over time',
            'model_governance': 'Model governance framework',
            'ml_pipeline': 'Production ML pipeline'
        }
    },
    35: {
        'file': 'lesson_35_explainability_and_bias.tex',
        'charts': {
            'shap_values': 'SHAP values explanation',
            'lime_explanation': 'LIME explanation',
            'feature_attribution': 'Feature attribution methods',
            'pdp_ice_plots': 'PDP and ICE plots',
            'model_agnostic_methods': 'Model-agnostic methods',
            'algorithmic_bias': 'Algorithmic bias examples',
            'fairness_metrics': 'Fairness metrics comparison'
        }
    },
    36: {
        'file': 'lesson_36_ai_regulation_and_future.tex',
        'charts': {
            'ai_regulation_landscape': 'AI regulation landscape',
            'eu_ai_act_timeline': 'EU AI Act timeline'
        }
    }
}

def compile_lesson(lesson_num):
    """Compile a lesson and check for overflows"""
    module_dir = Path(r"D:\Joerg\Research\slides\DigitalFinance_3\module_03_ai_ml")
    lesson_file = CHART_MAPPINGS[lesson_num]['file']

    result = subprocess.run(
        ['pdflatex', '-interaction=nonstopmode', lesson_file],
        cwd=module_dir,
        capture_output=True,
        text=True
    )

    # Check for overflow warnings
    overflows = [line for line in result.stdout.split('\n') if 'Overfull' in line]

    return len(overflows) == 0, overflows

def print_status():
    """Print current integration status"""
    print("Chart Integration Status:")
    print("=" * 60)
    for lesson_num in sorted(CHART_MAPPINGS.keys()):
        info = CHART_MAPPINGS[lesson_num]
        print(f"\nLesson {lesson_num}: {info['file']}")
        print(f"  Charts to integrate: {len(info['charts'])}")
        for chart_name in info['charts'].keys():
            print(f"    - {chart_name}")

if __name__ == '__main__':
    print_status()
