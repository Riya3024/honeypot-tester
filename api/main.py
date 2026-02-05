from fastapi import FastAPI
from graphs.agent_graph import ScamLangGraph
from graphs.scam_network import ScamNetwork
from api.honeypot import router as honeypot_router
from fastapi import FastAPI, Header, HTTPException, Request
from datetime import datetime
import uuid


app = FastAPI(title="Agentic Scam Honeypot V3.1")
app.include_router(honeypot_router)

graph = ScamLangGraph()
network = ScamNetwork()



app = FastAPI(title="AI Honeypot API")

API_KEY = "honeypot123"

@app.post("/honeypot")
async def honeypot(request: Request, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return {
        "status": "honeypot_triggered",
        "message": "Interaction logged",
        "request_id": f"hp_{uuid.uuid4().hex[:8]}",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/")
def root():
    return {
        "status": "running",
        "service": "Agentic Scam Honeypot API",
        "docs": "/docs"
    }

@app.post("/message")
def process_message(message: str):
    result = graph.run(message)
    network.add_iocs(result["iocs"])

    return {
        "agent_reply": result["reply"],
        "risk": result["risk"],
        "blockchain_hash": result["block"]["hash"],
        "network_stats": {
            "nodes": network.graph.number_of_nodes(),
            "edges": network.graph.number_of_edges()
        },
        "fir": result["fir"]
    }
