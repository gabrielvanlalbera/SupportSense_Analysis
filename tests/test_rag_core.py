import unittest
from rag_core import SupportKnowledgeBase, baseline_answer, rag_answer

class TestSupportRAG(unittest.TestCase):
    def setUp(self): self.kb = SupportKnowledgeBase()
    def test_password_retrieves_password_doc(self):
        docs = self.kb.retrieve("How do I reset my password?", k=3)
        self.assertTrue(docs); self.assertIn("KB-001", [d["doc_id"] for d in docs])
    def test_baseline_cites_top_passage(self):
        docs = self.kb.retrieve("How long does a data export link last?", k=3)
        result = baseline_answer("How long does a data export link last?", docs)
        self.assertTrue(result["citations"])
        self.assertIn(result["citations"][0], [d["doc_id"] for d in docs])
    def test_rag_abstains_without_evidence(self):
        result = rag_answer({"question":"unrelated"}, [], use_llm=False)
        self.assertTrue(result["abstained"]); self.assertFalse(result["citations"])
    def test_fallback_does_not_use_answer_key(self):
        q = {"question":"How long does an export link last?", "answer":"do not use this answer key"}
        docs = self.kb.retrieve(q["question"], k=3)
        result = rag_answer(q, docs, use_llm=False)
        self.assertNotEqual(result["answer"], q["answer"])
        self.assertTrue(result["citations"])

if __name__ == "__main__": unittest.main()
