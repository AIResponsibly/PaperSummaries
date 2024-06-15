import os
import glob
from datetime import datetime

def extract_info_from_md(md_file):
    with open(md_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        title = lines[0].strip().replace('# ', '')
        published = ''
        link = ''
        summary = ''
        for line in lines[1:]:
            if line.startswith('- **Published**:'):
                published = line.replace('- **Published**:', '').strip()
            elif line.startswith('- **Link**:'):
                link = line.replace('- **Link**:', '').strip()
            elif line.startswith('- **Summary**:'):
                summary = line.replace('- **Summary**:', '').strip()
        return title, published, link, summary

def generate_readme():
    readme_content = """# Responsible AI Paper Summaries

Subscribe to the [Responsible AI newsletter](https://airesponsibly.substack.com/) for weekly updates on new papers and more.

## Overview

Welcome to the Responsible AI Paper Summaries repository! Here, you'll find concise summaries of key papers in various areas of responsible AI.

This repository provides brief summaries of AI/ML papers in the following areas:
- **Explainability and Interpretability**
- **Fairness and Biases**
- **Privacy**
- **Security**
- **Safety**
- **Accountability**
- **Human Control and Interaction**
- **Legal and Ethical Guidelines**

## Recent Summaries
"""
    summaries_dir = 'summaries'

    topics = {
        'Explainability and Interpretability': 'explainability',
        'Fairness and Biases': 'fairness_bias',
        'Privacy': 'privacy',
        'Security': 'security',
        'Safety': 'safety',
        'Accountability': 'accountability',
        'Human Control and Interaction': 'human_control_interaction',
        'Legal and Ethical Guidelines': 'legal_governance'
    }

    all_summaries = []

    for topic, folder in topics.items():
        md_files = glob.glob(os.path.join(summaries_dir, folder, '*.md'))
        for md_file in md_files:
            try:
                title, published, link, summary = extract_info_from_md(md_file)
                if title and published and link and summary:
                    all_summaries.append((md_file, title, published, summary))
                else:
                    print(f"Warning: Missing information in file {md_file}")
            except Exception as e:
                print(f"Error processing file {md_file}: {e}")

    # Sort summaries by modification time and get the latest three
    all_summaries.sort(key=lambda x: os.path.getmtime(x[0]), reverse=True)
    latest_summaries = all_summaries[:3]

    for md_file, title, published, summary in latest_summaries:
        readme_content += f" - **[{title} - {published}]({md_file})**. {summary}\n\n"

    readme_content += "\n## Summaries by Topic\n"

    for topic, folder in topics.items():
        readme_content += f"\n<details open>\n  <summary>{topic}</summary>\n  <p>\n\n"
        md_files = glob.glob(os.path.join(summaries_dir, folder, '*.md'))
        for md_file in md_files:
            try:
                title, published, link, summary = extract_info_from_md(md_file)
                readme_content += f"  - [{title} - {published}]({md_file}). {summary}\n\n"
            except Exception as e:
                print(f"Error processing file {md_file}: {e}")
        readme_content += "  </p>\n</details>\n"

    readme_content += """
## How to Use

Each summary is stored in the relevant subfolder within the `summaries/` directory. You can browse through the summaries to quickly understand the main points of various papers.

## Contributing

We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for more details on how to contribute.
"""

    with open('README.md', 'w', encoding='utf-8') as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    generate_readme()
