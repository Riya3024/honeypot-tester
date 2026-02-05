import streamlit as st
from graphs.agent_graph import ScamLangGraph
from graphs.scam_network import ScamNetwork
import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)


st.set_page_config(layout="wide")
st.title("🕵️ Agentic Scam Honeypot Dashboard")

graph = ScamLangGraph()
network = ScamNetwork()

msg = st.text_area("Incoming Scam Message")

if st.button("Analyze"):
    result = graph.run(msg)
    network.add_iocs(result["iocs"])

    st.subheader("🤖 AI Reply")
    st.write(result["reply"])

    st.subheader("⚠️ Risk Score")
    st.metric("Threat Level", result["risk"])

    st.subheader("🔐 Blockchain Hash")
    st.code(result["block"]["hash"])

    st.subheader("🌐 Network Stats")
    st.json({
        "nodes": network.graph.number_of_nodes(),
        "edges": network.graph.number_of_edges()
    })
