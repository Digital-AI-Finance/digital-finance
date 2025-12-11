"""
Generate missing chart PDFs for Module 01 lessons.
Creates placeholder charts for figures that don't exist yet.
"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

BASE = Path(r'D:\Joerg\Research\slides\DigitalFinance_3\module_01_fintech\figures')

# Charts that need to be generated with their topics
MISSING_CHARTS = {
    # Lesson 11: Regulatory Frameworks
    'eu_regulatory_timeline': 'EU FinTech Regulatory Timeline (2015-2025)',
    'psd2_structure': 'PSD2 Directive Structure',
    'psd2_provisions': 'Key PSD2 Provisions',
    'psd2_adoption_metrics': 'PSD2 Adoption Metrics by Country',
    'mica_framework': 'MiCA Regulatory Framework',
    'mica_asset_types': 'MiCA Crypto Asset Classifications',
    'mica_requirements': 'MiCA Compliance Requirements',
    'mica_implementation': 'MiCA Implementation Timeline',
    'dora_pillars': 'DORA Five Pillars',
    'dora_scope': 'DORA Scope and Coverage',
    'dora_compliance': 'DORA Compliance Requirements',
    'gdpr_principles': 'GDPR Core Principles',
    'global_regulatory_comparison': 'Global FinTech Regulation Comparison',
    'uk_regulatory_approach': 'UK FCA Regulatory Approach',
    'us_regulatory_landscape': 'US Financial Regulatory Landscape',
    'fintech_licensing_map': 'Global FinTech Licensing Requirements',
    'compliance_cost_structure': 'Compliance Cost Structure',
    'sandbox_global_map': 'Global Regulatory Sandboxes',
    'regulatory_harmonization': 'Regulatory Harmonization Efforts',

    # Lesson 12: Business Models
    'fintech_business_models': 'FinTech Business Model Types',
    'platform_model': 'Platform Business Model',
    'embedded_finance_examples': 'Embedded Finance Examples',
    'baas_architecture': 'Banking-as-a-Service Architecture',
    'baas_value_chain': 'BaaS Value Chain',
    'marqeta_model': 'Marqeta Business Model',
    'revenue_model_comparison': 'FinTech Revenue Models Comparison',
    'subscription_tiers': 'Subscription Tier Pricing',
    'freemium_funnel': 'Freemium Conversion Funnel',
    'data_monetization_model': 'Data Monetization Model',
    'fintech_unit_economics': 'FinTech Unit Economics',
    'ltv_calculation': 'Customer LTV Calculation',
    'ltv_cac_benchmarks': 'LTV/CAC Benchmarks by Sector',
    'network_effects_types': 'Network Effects Types',
    'marketplace_network_effects': 'Marketplace Network Effects',
    'superapp_model': 'Super-App Business Model',
    'defi_vs_traditional': 'DeFi vs Traditional Finance',
    'fintech_future_trends': 'FinTech Future Trends 2025-2030',
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 12,
    'figure.figsize': (10, 6),
    'figure.dpi': 150,
})


def create_timeline_chart(title, output_path):
    """Create a timeline/roadmap style chart."""
    fig, ax = plt.subplots(figsize=(10, 6))

    years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
    values = np.random.randint(20, 100, len(years))

    ax.bar(years, values, color='#4A90E2', alpha=0.7)
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_ylabel('Adoption / Implementation (%)')
    ax.set_ylim(0, 120)

    for i, v in enumerate(values):
        ax.text(i, v + 3, f'{v}%', ha='center', fontsize=9)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999',
             ha='right', style='italic')

    plt.tight_layout()
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()


def create_comparison_chart(title, output_path):
    """Create a comparison bar chart."""
    fig, ax = plt.subplots(figsize=(10, 6))

    categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
    values1 = np.random.randint(30, 90, len(categories))
    values2 = np.random.randint(20, 80, len(categories))

    x = np.arange(len(categories))
    width = 0.35

    ax.bar(x - width/2, values1, width, label='Traditional', color='#666666')
    ax.bar(x + width/2, values2, width, label='FinTech', color='#4A90E2')

    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=9)
    ax.legend()
    ax.set_ylabel('Value (%)')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999',
             ha='right', style='italic')

    plt.tight_layout()
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()


def create_pie_chart(title, output_path):
    """Create a pie/donut chart."""
    fig, ax = plt.subplots(figsize=(10, 6))

    labels = ['Segment A', 'Segment B', 'Segment C', 'Segment D', 'Other']
    sizes = [35, 25, 20, 12, 8]
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#D62728', '#999999']

    wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors,
                                       autopct='%1.0f%%', startangle=90)
    ax.set_title(title, fontsize=12, fontweight='bold')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999',
             ha='right', style='italic')

    plt.tight_layout()
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()


def create_flow_chart(title, output_path):
    """Create a simple flow/process chart."""
    fig, ax = plt.subplots(figsize=(10, 6))

    # Simple horizontal flow
    boxes = ['Input', 'Process A', 'Process B', 'Process C', 'Output']
    x_positions = np.linspace(0.1, 0.9, len(boxes))

    for i, (x, label) in enumerate(zip(x_positions, boxes)):
        # Draw box
        rect = plt.Rectangle((x - 0.08, 0.4), 0.16, 0.2,
                              facecolor='#4A90E2' if i % 2 == 0 else '#44A044',
                              edgecolor='black', alpha=0.7)
        ax.add_patch(rect)
        ax.text(x, 0.5, label, ha='center', va='center', fontsize=10, fontweight='bold')

        # Draw arrow
        if i < len(boxes) - 1:
            ax.annotate('', xy=(x_positions[i+1] - 0.08, 0.5),
                       xytext=(x + 0.08, 0.5),
                       arrowprops=dict(arrowstyle='->', color='black', lw=2))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title(title, fontsize=12, fontweight='bold', y=0.85)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999',
             ha='right', style='italic')

    plt.tight_layout()
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()


def create_metrics_chart(title, output_path):
    """Create a metrics/KPI style chart."""
    fig, ax = plt.subplots(figsize=(10, 6))

    metrics = ['Metric 1', 'Metric 2', 'Metric 3', 'Metric 4']
    values = np.random.randint(50, 150, len(metrics))

    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#D62728']
    bars = ax.barh(metrics, values, color=colors, alpha=0.7)

    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xlabel('Value')

    for bar, val in zip(bars, values):
        ax.text(val + 2, bar.get_y() + bar.get_height()/2,
                f'{val}', va='center', fontsize=10)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999',
             ha='right', style='italic')

    plt.tight_layout()
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()


def generate_chart(name, title):
    """Generate appropriate chart based on name."""
    folder = BASE / name
    folder.mkdir(exist_ok=True)
    output_path = folder / f'{name}.pdf'

    # Choose chart type based on keywords in name
    if any(kw in name for kw in ['timeline', 'adoption', 'implementation', 'growth']):
        create_timeline_chart(title, output_path)
    elif any(kw in name for kw in ['comparison', 'vs', 'benchmark']):
        create_comparison_chart(title, output_path)
    elif any(kw in name for kw in ['types', 'segments', 'breakdown', 'distribution']):
        create_pie_chart(title, output_path)
    elif any(kw in name for kw in ['flow', 'process', 'architecture', 'chain', 'model', 'funnel']):
        create_flow_chart(title, output_path)
    else:
        create_metrics_chart(title, output_path)

    return output_path


def main():
    print("=" * 70)
    print("GENERATING MISSING CHARTS")
    print("=" * 70)

    generated = 0

    for name, title in MISSING_CHARTS.items():
        output_path = generate_chart(name, title)
        print(f"  Generated: {name}.pdf")
        generated += 1

    print("\n" + "=" * 70)
    print(f"SUMMARY: Generated {generated} charts")
    print("=" * 70)


if __name__ == '__main__':
    main()
