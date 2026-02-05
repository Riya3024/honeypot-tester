from fastapi import APIRouter, Header, HTTPException
from datetime import datetime
import uuid

router = APIRouter()

VALID_API_KEY = "honeypot123"  # can be anything

@router.post("/honeypot")
def honeypot_endpoint(x_api_key: str = Header(None)):
    if x_api_key is None:
        raise HTTPException(
            status_code=401,
            detail="API key missing"
        )

    if x_api_key != VALID_API_KEY:
        raise HTTPException(
            status_code=403,
            detail="Invalid API key"
        )

    return {
        "status": "access_logged",
        "message": "This endpoint is monitored",
        "request_id": f"hp_{uuid.uuid4().hex[:8]}",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
