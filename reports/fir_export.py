from datetime import datetime

def generate_fir_report(iocs, risk):
    return {
        "complaint_type": "Suspected Online Financial Fraud",
        "timestamp": datetime.utcnow().isoformat(),
        "bank_accounts": iocs["bank_accounts"],
        "ifsc_codes": iocs["ifsc_codes"],
        "upi_ids": iocs["upi_ids"],
        "phishing_urls": iocs["phishing_urls"],
        "risk_level": "HIGH" if risk >= 70 else "MEDIUM",
        "legal_sections": ["IT Act 66D", "IPC 420"]
    }
