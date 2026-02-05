import hashlib
import json
import time

class EvidenceChain:
    def __init__(self):
        self.prev_hash = "GENESIS"
        self.chain = []

    def add_block(self, iocs, risk):
        block = {
            "timestamp": time.time(),
            "iocs": iocs,
            "risk": risk,
            "prev_hash": self.prev_hash
        }

        block_hash = hashlib.sha256(
            json.dumps(block, sort_keys=True).encode()
        ).hexdigest()

        block["hash"] = block_hash
        self.chain.append(block)
        self.prev_hash = block_hash
        return block
