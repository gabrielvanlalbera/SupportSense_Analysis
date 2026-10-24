# SupportSense — RAG Document Assistant + A/B Evaluation

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green)

SupportSense is a portfolio project for **Northstar Cloud**, a fictional B2B SaaS company. It helps support agents answer product, billing, security, and troubleshooting questions from approved documentation. It includes document retrieval, source IDs, abstention, an optional LLM answer generator, a Streamlit demo, and an offline paired A/B evaluation harness.

> **Transparency:** the company and documents are fictional. The default version works without an API key and uses extractive answers. This is not a live customer experiment and does not establish real-world business impact.

## Business problem
Support agents spend time finding answers across help articles. A grounded assistant could reduce search effort, but it must improve answer usefulness without increasing unsupported claims.

## Features
- TF-IDF retrieval over synthetic support documents.
- Source citations using document IDs and titles.
- Abstention when evidence is insufficient.
- Optional OpenAI answer synthesis (requires API key and optional dependencies).
- Streamlit interactive demo.
- Paired offline comparison: **A: top-passage baseline** vs **B: grounded answer synthesis**.
- CSV/JSON/Markdown outputs, unit tests, and GitHub Actions CI.

## Architecture
```text
Synthetic knowledge base + benchmark questions
                    |
              TF-IDF retrieval
                    |
          +---------+---------+
          |                   |
    A: top passage       B: RAG-style
          |              synthesis
          +---------+---------+
                    |
       Offline metrics + experiment report
```
Default mode is deterministic and API-free. Optional LLM mode uses retrieved passages only and instructs the model to ignore instructions embedded in documents. This does not guarantee factual correctness; review answers and citations.

## Quick start
Python 3.10+ recommended.
```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python run_experiment.py
python -m unittest discover -s tests -v
```
Outputs are generated under `outputs/`: `ab_results.csv`, `ab_summary.json`, and `experiment_report.md`.

Run the UI:
```bash
streamlit run app/streamlit_app.py
```

### Optional LLM generation
1. Copy `.env.example` to `.env` and set `OPENAI_API_KEY`.
2. Install `pip install -r requirements-llm.txt`.
3. Set `SUPPORTSENSE_USE_LLM=true` in your environment or `.env`.
4. Run the app or experiment. `OPENAI_MODEL` defaults to `gpt-4.1-mini`.
Never commit `.env`. API use may incur charges; do not send confidential documents to a hosted model without authorization.

## A/B evaluation
The included benchmark runs both variants against the same small set of synthetic questions. Metrics include expected-document retrieval, a keyword-based answer proxy, citation coverage, abstention, latency, and an illustrative handling-time estimate.

**Limitations:** automated keyword checks are not human quality judgments; estimated handling time is not observed agent time; the corpus is small and synthetic; and this is not a live randomized A/B test. See [`A_B_TEST_PLAN.md`](A_B_TEST_PLAN.md) for human evaluation and live experiment recommendations.

## Repository structure
```text
SupportSense-RAG-AB-Test/
├── app/streamlit_app.py
├── data/company_docs.json
├── data/evaluation_questions.json
├── tests/test_rag_core.py
├── .github/workflows/tests.yml
├── .env.example
├── .gitignore
├── A_B_TEST_PLAN.md
├── CONTRIBUTING.md
├── LICENSE
├── PROJECT_BRIEF.md
├── README.md
├── requirements.txt
├── requirements-llm.txt
├── rag_core.py
└── run_experiment.py
```

## Resume bullet (after you run and review it)
> Built SupportSense, a document-grounded support assistant for a simulated SaaS business; implemented retrieval, citations, safe abstention, and a paired offline A/B evaluation harness.

Only add measured numbers after validating results. Do not claim production deployment or a live experiment unless true.

## License
MIT. See [`LICENSE`](LICENSE).
