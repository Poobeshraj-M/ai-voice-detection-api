from fastapi import FastAPI, File, UploadFile, Header, HTTPException

app = FastAPI(
    title="AI Voice Detection API",
    description="Upload an audio file to detect AI-generated voice",
    version="1.0"
)

# Sample API Key (you can change anytime)
API_KEY = "my-secret-key-123"
@app.get("/")
def root():
    return {"message": "AI Voice Detection API is running"}


@app.post("/detect-voice")
async def detect_voice(
    audio_file: UploadFile = File(...),
    x_api_key: str = Header(None)
):
    # API key validation
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Dummy response (NO ML for now)
    return {
        "status": "success",
        "prediction": "ai_generated",
        "confidence": 1,
        "details": {
            "model_version": "v1",
            "feature_length": 26
        }
    }
