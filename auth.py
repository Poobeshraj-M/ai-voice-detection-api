import os
from fastapi import Header, HTTPException

def verify_api_key(x_api_key: str = Header(None)):
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="API_KEY not configured on server"
        )

    if x_api_key != api_key:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
