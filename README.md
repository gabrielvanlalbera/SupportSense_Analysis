# SupportSense — Analyzing a RAG-Powered Customer Support Assistant

**SupportSense** is an AI/ML portfolio project that explores how a Retrieval-Augmented Generation (RAG)-style customer support assistant can help businesses retrieve relevant support documentation, handle uncertain questions, and make better operational decisions. The project combines exploratory data analysis, support-question segmentation, document retrieval evaluation, offline experiment analysis, and business-impact modeling into a single, reproducible workflow. Its goal is to demonstrate how AI solutions can be evaluated not only on technical performance but also on reliability, risk, and potential business value.

> **Project status:** This project uses synthetic and illustrative data for offline evaluation. It is not a deployed production assistant or a live customer A/B test.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Machine%20Learning-scikit--learn-orange?logo=scikitlearn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Analysis-Jupyter-F37626?logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/Interface-Streamlit-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Status-Portfolio%20Project-2ea44f" alt="Portfolio Project">
</p>

<p align="center">
  <a href="#-business-problem">Business Problem</a> •
  <a href="#-project-objectives">Objectives</a> •
  <a href="#-analytical-workflow">Workflow</a> •
  <a href="#-technology-stack">Technology</a> •
  <a href="#-run-locally">Run Locally</a> •
  <a href="#-future-improvements">Future Improvements</a>
</p>

---

## 💼 Business Problem

Customer support teams often deal with repetitive questions, scattered documentation, inconsistent answers, and requests that require human intervention.

A poorly designed AI assistant can introduce additional risks, including retrieving irrelevant information, producing unsupported answers, or failing to escalate questions it cannot confidently answer.

SupportSense investigates how a retrieval-based assistant can help address these challenges while providing a structured framework for evaluating its technical performance and potential business value.

| Business challenge | SupportSense approach |
|---|---|
| Support documentation is difficult to navigate | Inspect a structured knowledge base and retrieve relevant documents |
| Questions cover different topics | Segment benchmark questions into interpretable categories |
| Retrieval quality is uncertain | Evaluate document ranking using Hit@k and MRR |
| Unsupported answers create risk | Examine answer-grounding and abstention proxies |
| Proposed improvements need evidence | Compare alternative policies using an offline benchmark |
| Business benefits are uncertain | Model potential impact through explicit assumptions |

## 🎯 Project Objectives

- Explore knowledge-base quality, data structure, and evaluation-question coverage.
- Segment support questions into interpretable categories.
- Evaluate document retrieval using ranking metrics.
- Examine answer-grounding, citation, and abstention behavior.
- Compare a baseline policy with an alternative abstention-aware policy.
- Estimate potential business impact using transparent assumptions.
- Identify the evidence and safeguards required before real-world deployment.

## 🧠 Analytical Workflow

The project follows a five-stage workflow, moving from data understanding to technical evaluation and business recommendations.

```text
Knowledge Base + Evaluation Questions
                 |
                 v
       1. Exploratory Analysis
                 |
                 v
       2. Support Topic Segmentation
                 |
                 v
       3. Retrieval and RAG Modeling
                 |
                 v
       4. A/B Experiment Analysis
                 |
                 v
       5. Business Impact and Recommendations
```

## 📊 The Five Notebooks

### 1. Exploratory Analysis

**File:** `1. SupportSense - Exploratory Analysis.ipynb`

Establishes the foundation by examining the knowledge base and evaluation-question dataset.

**Key activities**
- Dataset structure and descriptive statistics
- Missing-value and duplicate checks
- Knowledge-base and question-set coverage
- Initial visualizations
- Identification of data-quality issues and evaluation gaps

**Business question:** Is the benchmark structured well enough to support meaningful retrieval evaluation?

### 2. Support Topic Segmentation

**File:** `2. SupportSense - Support Topic Segmentation.ipynb`

Groups benchmark questions into interpretable support categories using rule-based segmentation.

**Key activities**
- Question categorization
- Segment-level counts and distributions
- Inspection of topic coverage
- Identification of areas that may need additional evaluation examples

**Business question:** Which types of support questions are represented in the benchmark, and where are the coverage gaps?

*These are benchmark-question segments, not learned customer segments or real customer profiles.*

### 3. Retrieval and RAG Modeling

**File:** `3. SupportSense - Retrieval and RAG Modeling.ipynb`

Implements and evaluates a lightweight lexical retrieval baseline using TF-IDF.

**Key activities**
- Ranking candidate knowledge-base documents
- Evaluating retrieval using Hit@k and Mean Reciprocal Rank (MRR)
- Inspecting retrieval failures
- Exploring confidence thresholds and abstention behavior
- Examining whether retrieved evidence supports a response

**Business question:** Can the system retrieve useful knowledge, and when should it avoid answering?

**Technical note:** TF-IDF is a lexical retrieval method. It provides a reproducible retrieval baseline but is not, by itself, a complete generative RAG system or a production-ready language model.

### 4. A/B Experiment Analysis

**File:** `4. SupportSense - A-B Experiment Analysis.ipynb`

Compares a baseline policy with an alternative abstention-aware policy using an offline benchmark.

**Key activities**
- Paired evaluation of the two variants
- Retrieval and answer-grounding proxies
- Citation coverage and abstention metrics
- Unsupported-answer proxies
- Inspection of metric trade-offs
- Interpretation of latency and handling-time assumptions

**Business question:** Does the alternative policy show promising offline behavior without creating unacceptable trade-offs?

> This is an offline paired comparison, not a randomized live A/B test. Automated keyword-based metrics are proxies and require human validation. Illustrative latency and handling-time values are not production measurements.

### 5. Business Impact and Recommendations

**File:** `5. SupportSense - Business Impact and Recommendations.ipynb`

Connects technical evaluation to operational decision-making.

**Key activities**
- Low, base, and high impact scenarios
- Editable business assumptions
- Sensitivity analysis
- Potential operational benefits and risks
- Pilot design and measurement recommendations
- Guardrails for responsible deployment

**Business question:** Under what assumptions could a support assistant create value, and what evidence is needed before deployment?

*Scenario outputs are estimates based on assumptions, not observed savings, verified ROI, or measured customer outcomes.*

## ⭐ Key Capabilities

| Capability | Why it matters |
|---|---|
| Exploratory data analysis | Identifies data-quality and coverage issues early |
| Rule-based question segmentation | Makes benchmark composition easier to interpret |
| TF-IDF document retrieval | Provides a lightweight, reproducible baseline |
| Hit@k and MRR | Measures retrieval ranking quality |
| Abstention analysis | Examines behavior when evidence is insufficient |
| Paired offline comparison | Makes policy trade-offs easier to inspect |
| Sensitivity analysis | Shows how business conclusions change with assumptions |
| Pilot recommendations | Connects analysis to a practical evaluation plan |

## 🛠️ Technology Stack

- **Language:** Python
- **Data analysis:** pandas, NumPy
- **Machine learning and retrieval:** scikit-learn
- **Visualization:** Matplotlib, Seaborn
- **Interactive interface:** Streamlit
- **Analysis environment:** Jupyter Notebook
- **Version control:** Git and GitHub

The core notebook workflow is designed to run locally. Optional LLM functionality may require additional dependencies, configuration, and an API connection.

## 📁 Repository Structure

```text
SupportSense-RAG-AB-Test/
│
├── app/                       # Application interface and supporting code
├── data/
│   └── processed/              # Generated or processed analytical outputs
├── notebooks/
│   ├── 1. SupportSense - Exploratory Analysis.ipynb
│   ├── 2. SupportSense - Support Topic Segmentation.ipynb
│   ├── 3. SupportSense - Retrieval and RAG Modeling.ipynb
│   ├── 4. SupportSense - A-B Experiment Analysis.ipynb
│   └── 5. SupportSense - Business Impact and Recommendations.ipynb
├── tests/                      # Project tests
├── .github/                    # GitHub-related configuration
├── .env.example                # Example environment configuration
├── A_B_TEST_PLAN.md             # Experiment planning notes
├── CONTRIBUTING.md              # Contribution guidance
├── LICENSE
├── PROJECT_BRIEF.md             # Project scope and context
├── README.md
├── rag_core.py                  # Retrieval-related core logic
├── requirements.txt             # Core dependencies
├── requirements-llm.txt         # Optional LLM dependencies
└── run_experiment.py             # Experiment runner
```

*This tree summarizes the expected project layout. Individual files and generated outputs may vary as the project evolves.*

## 📏 Evaluation Metrics

SupportSense examines several dimensions of system behavior instead of relying on one headline score.

| Metric | Interpretation |
|---|---|
| Hit@k | Whether a relevant document appears within the top *k* retrieved results |
| Mean Reciprocal Rank (MRR) | How highly the first relevant result is ranked |
| Grounded-answer proxy | A heuristic indication of whether an answer matches expected evidence |
| Citation coverage | Whether responses include expected supporting references |
| Correct abstention | Whether the system abstains when the benchmark indicates it should |
| Unsupported-answer proxy | A heuristic indicator of potentially unsupported responses |
| Latency | Time required by an operation, where actually measured |

Metric definitions and implementations should be checked in the relevant notebooks. Proxy metrics must not be interpreted as verified factual correctness, customer satisfaction, or real-world business performance.

## 📈 Business Impact Framework

Potential business value is explored through explicit scenarios rather than presented as an established outcome.

Illustrative drivers may include:

- Number of eligible support requests
- Share of requests handled by the assistant
- Human review and escalation requirements
- Time saved per eligible request
- Implementation and operating costs

A credible business case would require observed ticket volumes, measured handling times, human-reviewed answer quality, actual operating costs, and an appropriately designed experiment.

## ⚠️ Limitations and Responsible Use

SupportSense is an analytical prototype, not a production-ready customer support deployment.

- The benchmark uses synthetic or illustrative data rather than a verified production customer dataset.
- Offline benchmark performance does not establish real-world answer quality.
- Automated evaluation metrics can misclassify answers and require human review.
- The offline policy comparison is not a live randomized A/B experiment.
- Business impact estimates depend on editable assumptions and are not verified savings.
- Production use would require privacy, security, access-control, monitoring, and escalation safeguards.

These limitations are important to the project: the objective is to demonstrate how an AI/ML system can be evaluated critically before deployment decisions are made.

## 🗺️ Future Improvements

SupportSense provides a foundation for further development. The following improvements would strengthen its technical evaluation and business relevance.

1. **Expand the evaluation dataset** — Use representative, permissioned support questions and a broader range of answerable and unanswerable cases.
2. **Introduce human-reviewed evaluation** — Validate retrieval relevance, answer grounding, citation quality, and abstention decisions using a documented review rubric.
3. **Compare retrieval approaches** — Benchmark TF-IDF against BM25 and dense-embedding retrieval to understand differences in ranking quality.
4. **Strengthen the RAG pipeline** — Integrate a generative model with retrieved evidence, source citations, and explicit safeguards against unsupported responses.
5. **Improve experiment design** — Define a primary metric, establish guardrails, conduct a power analysis, and report confidence intervals before running an authorized live A/B test.
6. **Measure operational performance** — Replace illustrative latency and handling-time assumptions with repeatable measurements and appropriately authorized operational data.
7. **Validate business impact** — Replace scenario assumptions with observed costs, ticket volumes, resolution times, escalation rates, and other relevant business metrics.
8. **Prepare for production use** — Add monitoring, access controls, privacy protections, error handling, and human escalation workflows.

*These are proposed improvements, not capabilities or outcomes already demonstrated by the current offline benchmark.*

## ⚙️ Run Locally

### Prerequisites

- Python 3.10 or newer
- Git
- VS Code with the Python and Jupyter extensions, or another Jupyter-compatible environment

### 1. Clone the repository

```bash
git clone https://github.com/gabrielvanlalbera/SupportSense_Analysis.git
cd SupportSense_Analysis
```

If you already have the repository locally, open that existing project folder instead.

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

If you need optional LLM functionality, inspect `requirements-llm.txt` and its configuration requirements before installing it.

### 4. Run the notebooks

Open the `notebooks/` folder and run the notebooks in numerical order, from **1 to 5**.

Execute the cells from top to bottom and save the notebooks to preserve their outputs.

### 5. Explore the application or experiment

Review `PROJECT_BRIEF.md`, `rag_core.py`, and `run_experiment.py` to understand the application and experiment entry points before running them.

For offline use, ensure the required packages and input data are already available locally. Any feature that calls an external LLM API will require network access and valid configuration.

## 👨‍💻 About This Project

SupportSense demonstrates an end-to-end analytical approach to an applied AI/ML business problem: from data inspection and retrieval evaluation to experiment design and business recommendations.

It is intended as a reproducible learning and portfolio project focused on **measuring AI system behavior, understanding trade-offs, and translating technical evidence into business decisions**.

---

**Repository:** [SupportSense — GitHub](https://github.com/gabrielvanlalbera/SupportSense_Analysis)

If you find this project useful, explore the notebooks, inspect the evaluation logic, and adapt the workflow to a properly sourced support dataset.
