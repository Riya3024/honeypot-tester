def risk_score(iocs: dict) -> int:
    score = 0
    score += len(iocs["bank_accounts"]) * 35
    score += len(iocs["upi_ids"]) * 30
    score += len(iocs["phishing_urls"]) * 25
    score += len(iocs["ifsc_codes"]) * 20
    score += len(iocs["phone_numbers"]) * 15
    score += len(iocs["emails"]) * 10
    return min(score, 100)
