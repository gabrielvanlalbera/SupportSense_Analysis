# Contributing

1. Use Python 3.10+ in a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run tests: `python -m unittest discover -s tests -v`.
4. Run the benchmark: `python run_experiment.py`.
5. Add tests for behaviour changes. Keep sample data synthetic and non-sensitive.
6. Never commit `.env`, API keys, generated outputs, or confidential company documents.
7. Document metric definitions and limitations; do not describe offline metrics as live business impact.
