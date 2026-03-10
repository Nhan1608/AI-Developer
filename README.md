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
