import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import streamlit as st
from rag_core import SupportKnowledgeBase, rag_answer

st.set_page_config(page_title="SupportSense", page_icon="🔎", layout="wide")
st.title("SupportSense")
st.caption("Northstar Cloud • Synthetic support-document assistant")
st.warning("Portfolio prototype with fictional documents. Do not enter confidential information.")
kb = SupportKnowledgeBase()
question = st.text_input("Ask a support question", placeholder="How long does a data export link last?")
if st.button("Search knowledge base", type="primary") and question.strip():
    retrieved = kb.retrieve(question, k=3)
    result = rag_answer({"question":question}, retrieved)
    st.subheader("Answer"); st.write(result["answer"])
    if result["citations"]:
        st.markdown("**Sources**")
        for doc_id in result["citations"]:
            doc = next((d for d in kb.docs if d["doc_id"] == doc_id), None)
            if doc:
                with st.expander(f'{doc["doc_id"]} — {doc["title"]}'): st.write(doc["text"])
    else: st.info("No source ID was returned. Check retrieved passages before relying on this answer.")
    with st.expander("Retrieved passages and similarity scores"):
        for d in retrieved:
            st.write(f'{d["doc_id"]} | score={d["score"]:.3f} | {d["title"]}')
            st.caption(d["text"])
