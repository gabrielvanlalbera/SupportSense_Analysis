# A/B Validation Plan — SupportSense

## Hypothesis
Compared with returning the top retrieved passage, grounded answer synthesis improves support-answer usefulness without increasing unsupported answers or unacceptable latency.

## Offline paired evaluation (included)
Run both variants on the same synthetic question set. Track expected-document retrieval, keyword-based answer proxy, citation coverage, correct abstention, unsupported-answer proxy, latency, and illustrative handling time. Review individual failures.

## Human review (recommended)
Blind reviewers to variant identity. Score factual correctness, evidence support, completeness, citation correctness, and appropriate abstention from 1–5. Resolve disagreements using a written rubric.

## Future live test (not implemented)
- Population: eligible support sessions with approved docs.
- Randomization: user or session, chosen in advance to avoid contamination.
- A: current search/snippet workflow. B: assistant with citations and escalation.
- Primary metric: verified resolution without correction/escalation.
- Guardrails: critical factual errors, unsupported-answer rate, satisfaction, handling time, latency, and cost per resolved session.
- Calculate sample size from baseline rate and minimum detectable effect before launch.
- Pre-register duration, stopping rules, and analysis; report effect size and confidence intervals.
- Require privacy/security review, access controls, audit logs, human escalation, and rollback.

Ship only if the primary metric improves meaningfully and no pre-defined guardrail crosses its harm threshold.
