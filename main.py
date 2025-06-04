# main.py

from fastapi import FastAPI, Request
from fastapi.responses import Response
from datetime import datetime
import os
import json

app = FastAPI()
TRACK_FILE = "emails.json"

# Garante que o arquivo de log exista
if not os.path.exists(TRACK_FILE):
    with open(TRACK_FILE, "w") as f:
        json.dump({}, f)


def log_open(email_id: str, user_agent: str):
    with open(TRACK_FILE, "r+", encoding="utf-8") as f:
        data = json.load(f)
        entry = data.get(email_id, {"opens": []})
        entry["opens"].append({
            "timestamp": datetime.utcnow().isoformat(),
            "user_agent": user_agent
        })
        data[email_id] = entry
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()


@app.get("/track/{email_id}.png")
async def track(email_id: str, request: Request):
    user_agent = request.headers.get("User-Agent", "unknown")
    log_open(email_id, user_agent)

    # Retorna um PNG 1x1 invisível
    pixel = bytes([
        0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A,
        0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52,
        0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01,
        0x08, 0x06, 0x00, 0x00, 0x00, 0x1F, 0x15, 0xC4,
        0x89, 0x00, 0x00, 0x00, 0x0A, 0x49, 0x44, 0x41,
        0x54, 0x78, 0x9C, 0x63, 0xF8, 0xCF, 0x00, 0x00,
        0x02, 0x50, 0x01, 0xE2, 0x26, 0xDB, 0xF9, 0x00,
        0x00, 0x00, 0x00, 0x49, 0x45, 0x4E, 0x44, 0xAE,
        0x42, 0x60, 0x82
    ])
    return Response(content=pixel, media_type="image/png")
