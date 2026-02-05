from blockchain.evidence_chain import EvidenceChain
from reports.fir_export import generate_fir_report

class EvidenceAgent:
    role = "Evidence & FIR Agent"

    def __init__(self):
        self.chain = EvidenceChain()

    def run(self, iocs: dict, risk: int):
        block = self.chain.add_block(iocs, risk)
        fir = generate_fir_report(iocs, risk)
        return block, fir
