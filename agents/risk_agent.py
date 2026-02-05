from risk.risk_engine import risk_score

class RiskAgent:
    role = "Threat Scoring Agent"

    def run(self, iocs: dict) -> int:
        return risk_score(iocs)
