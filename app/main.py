from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="CRM FastAPI")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request) -> HTMLResponse:
    pipeline_stages = [
        {"name": "Nuevos", "count": 12, "amount": "$34,000"},
        {"name": "Calificados", "count": 8, "amount": "$22,500"},
        {"name": "Propuesta", "count": 5, "amount": "$17,200"},
        {"name": "Cierre", "count": 3, "amount": "$9,800"},
    ]

    activities = [
        {"client": "TechNova", "task": "Seguimiento de propuesta", "time": "Hoy · 11:30"},
        {"client": "GreenFoods", "task": "Demo agendada", "time": "Mañana · 09:00"},
        {"client": "UrbanData", "task": "Enviar contrato", "time": "Miércoles · 14:15"},
    ]

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "pipeline_stages": pipeline_stages,
            "activities": activities,
        },
    )
