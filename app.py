from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import fetch_usd

app = FastAPI()

# Middleware para permitir solicitudes desde cualquier origen (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Variable global para almacenar el valor y la fecha
usd_to_mxn = {"rate": None, "date": None}

@app.on_event("startup")
async def update_usd_rate():
    """Actualiza el valor del dólar al iniciar la aplicación."""
    result = fetch_usd.get_usd_to_mxn()
    if result:
        usd_to_mxn["rate"] = result["rate"]
        usd_to_mxn["date"] = result["date"]

@app.get("/api/usd-to-mxn", response_class=JSONResponse)
async def get_usd_rate():
    """Devuelve el valor del dólar y la fecha."""
    if usd_to_mxn["rate"] is None:
        return JSONResponse({"error": "Rate not available"}, status_code=503)
    return {"usd_to_mxn": usd_to_mxn["rate"], "date": usd_to_mxn["date"]}
