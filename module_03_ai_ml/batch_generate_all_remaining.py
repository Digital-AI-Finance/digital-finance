"""
Batch generate all remaining lessons 29-36
Streamlined approach - creates files directly
"""

from pathlib import Path
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M")
base_dir = Path(__file__).parent

PREAMBLE = r"""\documentclass[8pt,aspectratio=169]{beamer}
\usetheme{Madrid}
\usepackage{graphicx,booktabs,adjustbox,multicol,amsmath,amssymb}
\definecolor{mlblue}{RGB}{0,102,204}
\definecolor{mlpurple}{RGB}{51,51,178}
\definecolor{mllavender}{RGB}{173,173,224}
\definecolor{mllavender2}{RGB}{193,193,232}
\definecolor{mllavender3}{RGB}{204,204,235}
\definecolor{mllavender4}{RGB}{214,214,239}
\definecolor{mlorange}{RGB}{255,127,14}
\definecolor{mlgreen}{RGB}{44,160,44}
\definecolor{mlred}{RGB}{214,39,40}
\setbeamercolor{palette primary}{bg=mllavender3,fg=mlpurple}
\setbeamercolor{palette secondary}{bg=mllavender2,fg=mlpurple}
\setbeamercolor{palette tertiary}{bg=mllavender,fg=white}
\setbeamercolor{structure}{fg=mlpurple}
\setbeamercolor{frametitle}{fg=mlpurple,bg=mllavender3}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{itemize items}[circle]
\setbeamersize{text margin left=5mm,text margin right=5mm}
"""

lessons = {
    29: "Algorithmic Trading Concepts",
    30: "Credit Scoring and Risk Models",
    31: "Fraud Detection and AML",
    32: "NLP in Finance",
    33: "Robo-Advisors ML Aspects",
    34: "Market Prediction Limitations",
    35: "Explainability and Bias",
    36: "AI Regulation and Future"
}

print(f"Starting batch generation of lessons 29-36...")
print(f"Timestamp: {timestamp}\n")

for lesson_num in range(29, 37):
    filename = f"{timestamp}_lesson_{lesson_num}_{lessons[lesson_num].lower().replace(' ', '_').replace('/', '_')}.tex"
    filepath = base_dir / filename

    # Create placeholder content for now - will be filled in next steps
    content = PREAMBLE + f"""
\\title{{Digital Finance 3: Technology in Finance}}
\\subtitle{{Lesson {lesson_num}: {lessons[lesson_num]}}}
\\author{{FHGR}}
\\date{{\\today}}

\\begin{{document}}

\\begin{{frame}}
\\titlepage
\\end{{frame}}

\\begin{{frame}}{{Learning Objectives}}
Lesson {lesson_num}: {lessons[lesson_num]}
\\vspace{{1em}}

This lesson covers key concepts related to {lessons[lesson_num]}.
\\end{{frame}}

\\begin{{frame}}{{Content Placeholder}}
Full content for Lesson {lesson_num} will be generated in the complete version.
\\end{{frame}}

\\end{{document}}
"""

    filepath.write_text(content, encoding='utf-8')
    print(f"Created: {filename}")

print(f"\nGenerated {len(lessons)} lesson files (placeholders)")
print("Next step: Fill in complete content for each lesson")
