from fastapi import FastAPI, File, UploadFile, Depends
from auth import verify_api_key

app = FastAPI(
    title="AI Voice Detection API",
    description="Upload an audio file to detect AI-generated voice",
    version="1.0"
)

@app.get("/")
def root():
    return {"message": "AI Voice Detection API is running"}

@app.post("/detect-voice")
async def detect_voice(
    audio_file: UploadFile = File(...),
    _: str = Depends(verify_api_key)
):
    # Dummy response (no ML yet)
    return {
        "status": "success",
        "prediction": "ai_generated",
        "confidence": 1,
        "details": {
            "model_version": "v1",
            "feature_length": 26
        }
    }
