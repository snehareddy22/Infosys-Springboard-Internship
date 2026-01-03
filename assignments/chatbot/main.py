from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from chatbot import router as chatbot_router

app = FastAPI()

# CORS (safe for demo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve frontend HTML
@app.get("/", response_class=HTMLResponse)
def serve_ui():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()

# Chatbot API
app.include_router(chatbot_router)

