[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![CI/CD](https://github.com/Nhan1608/AI-Developer/actions/workflows/main.yml/badge.svg)](https://github.com/Nhan1608/AI-Developer/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# AI Artifact Tracing Tool for Machine Learning Projects 
# Project Overview
The AI Artifact Tracing Tool is a static analysis utility designed to bring transparency and reproducibility to Machine Learning (ML) repositories. Developed at the Lassonde School of Engineering, this tool automates the extraction of critical metadata—such as model architectures, datasets, and hyperparameters—directly from source code.

In modern MLOps, tracking what was run is as important as the code itself. This tool bridges the gap by automatically structuring ML components into a digestible format.

# Key Features
Static Code Analysis: Utilizes Astroid to parse Python ASTs (Abstract Syntax Trees) and identify ML-related patterns without executing the code.

Metadata Extraction: Automatically detects:

Models: Architecture types (e.g., CNN, Transformer).

Datasets: Data loading sources and paths.

Hyperparameters: Learning rates, batch sizes, and optimizer configurations.

CI/CD Integration: A robust GitHub Actions pipeline handles automated unit and integration testing to ensure reliable parsing across different repository structures.

MLOps Ready: Supports reproducible workflows by creating a "blueprint" of the ML project's artifacts.

# Tech Stack
Language: Python 3.9+

Analysis Engine: Astroid (Advanced AST wrapping)

Automation: GitHub Actions (CI/CD)

Testing: Pytest

# Future Roadmap: LLM & RAG Integration

To transition this from a static analysis tool to a dynamic **AI Tutor** (aligned with IBM's internal tool goals), the following features are planned:

1. **LLM-Powered Summarization**:
   - Integrate **IBM watsonx.ai** or OpenAI APIs to transform raw metadata (JSON) into human-readable project summaries.
   - Example: Instead of just listing `RandomForest`, the tool will explain *why* that model was chosen based on the surrounding code comments.

2. **RAG (Retrieval-Augmented Generation) for Documentation**:
   - Implement a **RAG pipeline** where the extracted metadata is stored in a Vector Database (like Milvus or ChromaDB).
   - This would allow developers to "chat" with their repository: *"Show me all hyperparameters used in the last 3 experiments."*

3. **Automated Role-Play for Code Reviews**:
   - Use the extracted artifacts to generate AI-driven "mock" code reviews, helping junior developers grow their skills through interactive feedback.
