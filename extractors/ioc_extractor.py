import re

URL_REGEX = r"(https?://[^\s]+)"
UPI_REGEX = r"\b[\w.\-]{2,}@[a-zA-Z]{2,}\b"
PHONE_REGEX = r"\b[6-9]\d{9}\b"
EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

def extract_iocs(text: str) -> dict:
    return {
        "phishing_urls": re.findall(URL_REGEX, text),
        "upi_ids": re.findall(UPI_REGEX, text),
        "phone_numbers": re.findall(PHONE_REGEX, text),
        "emails": re.findall(EMAIL_REGEX, text)
    }
import re

URL_REGEX = r"(https?://[^\s]+)"
UPI_REGEX = r"\b[\w.\-]{2,}@[a-zA-Z]{2,}\b"
PHONE_REGEX = r"\b[6-9]\d{9}\b"
EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

ACCOUNT_REGEX = r"\b\d{9,18}\b"
IFSC_REGEX = r"\b[A-Z]{4}0[A-Z0-9]{6}\b"

def extract_iocs(text: str) -> dict:
    return {
        "phishing_urls": re.findall(URL_REGEX, text),
        "upi_ids": re.findall(UPI_REGEX, text),
        "phone_numbers": re.findall(PHONE_REGEX, text),
        "emails": re.findall(EMAIL_REGEX, text),
        "bank_accounts": re.findall(ACCOUNT_REGEX, text),
        "ifsc_codes": re.findall(IFSC_REGEX, text)
    }
