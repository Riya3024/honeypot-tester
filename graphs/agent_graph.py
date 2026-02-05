from agents.decoy_agent import DecoyAgent
from agents.analyzer_agent import AnalyzerAgent
from agents.risk_agent import RiskAgent
from agents.evidence_agent import EvidenceAgent

class ScamLangGraph:
    def __init__(self):
        self.decoy = DecoyAgent()
        self.analyzer = AnalyzerAgent()
        self.risk = RiskAgent()
        self.evidence = EvidenceAgent()

    def run(self, message: str):
        reply = self.decoy.run(message)
        iocs = self.analyzer.run(message)
        risk = self.risk.run(iocs)
        block, fir = self.evidence.run(iocs, risk)

        return {
            "reply": reply,
            "iocs": iocs,
            "risk": risk,
            "block": block,
            "fir": fir
        }
