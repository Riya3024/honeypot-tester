from extractors.ioc_extractor import extract_iocs

class AnalyzerAgent:
    role = "IOC Analyzer Agent"

    def run(self, message: str) -> dict:
        return extract_iocs(message)
