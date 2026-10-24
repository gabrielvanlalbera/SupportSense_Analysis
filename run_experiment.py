"""Run a paired offline comparison of baseline and RAG-style answers."""
import json, time
import pandas as pd
from rag_core import ROOT, SupportKnowledgeBase, baseline_answer, rag_answer, evaluate_answer, load_json

def main():
    questions = load_json(ROOT / "data" / "evaluation_questions.json")
    kb = SupportKnowledgeBase()
    rows = []
    for q in questions:
        retrieved = kb.retrieve(q["question"], k=3)
        for variant in ("A_baseline", "B_rag"):
            start = time.perf_counter()
            result = baseline_answer(q["question"], retrieved) if variant == "A_baseline" else rag_answer(q, retrieved)
            rows.append(evaluate_answer(q, result, retrieved, (time.perf_counter()-start)*1000, variant))
    out = ROOT / "outputs"; out.mkdir(exist_ok=True)
    df = pd.DataFrame(rows); df.to_csv(out/"ab_results.csv", index=False)
    metrics = ["retrieval_hit","grounded_answer_proxy","citation_coverage","correct_abstention",
               "unsupported_answer_proxy","unnecessary_abstention","latency_ms","estimated_handle_seconds"]
    summary = df.groupby("variant")[metrics].mean().round(3).to_dict(orient="index")
    (out/"ab_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    lines = ["# SupportSense Offline A/B Benchmark", "",
      "> Synthetic paired benchmark; not a live randomized A/B test. Keyword metrics are proxies and need human validation.", "",
      "| Metric | A: Baseline | B: RAG-style |","|---|---:|---:|"]
    for m in metrics: lines.append(f"| {m} | {summary.get('A_baseline',{}).get(m,0)} | {summary.get('B_rag',{}).get(m,0)} |")
    lines += ["","## Interpretation","- Higher retrieval hit, grounded-answer proxy, citation coverage, and correct abstention are generally desirable.",
      "- Lower unsupported-answer proxy, unnecessary abstention, latency, and estimated handling time are desirable.",
      "- Estimated handling time is illustrative, not observed agent time. Optional LLM mode may change results.",
      "","## Next step","Randomize eligible support sessions only in a properly authorized live experiment, pre-register metrics, run a power analysis, and report confidence intervals."]
    (out/"experiment_report.md").write_text("\n".join(lines), encoding="utf-8")
    print("Wrote outputs/ab_results.csv, outputs/ab_summary.json, outputs/experiment_report.md")
    print(json.dumps(summary, indent=2))
if __name__ == "__main__": main()
