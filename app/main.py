from __future__ import annotations

import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.render import render_api_summary, render_handoffs, render_overview, render_queue
from app.services.care_pathway_service import build_service

service = build_service()
app = FastAPI(
    title="Care Pathway Command Center",
    description="Operational command layer for patient handoffs, coordination queues, and follow-up escalation.",
    version="1.0.0",
)


@app.get("/", response_class=HTMLResponse)
def overview() -> str:
    return render_overview(service.summary(), service.patients())


@app.get("/queue", response_class=HTMLResponse)
def queue() -> str:
    return render_queue(service.patients())


@app.get("/handoffs", response_class=HTMLResponse)
def handoffs() -> str:
    return render_handoffs(service.handoffs())


@app.get("/api-summary", response_class=HTMLResponse)
def api_summary() -> str:
    return render_api_summary(service.sample_payload())


@app.get("/api/dashboard/summary")
def dashboard_summary() -> dict:
    return service.summary()


@app.get("/api/patients")
def patients() -> list[dict]:
    return service.patients()


@app.get("/api/patients/{patient_id}")
def patient(patient_id: str) -> dict:
    return service.patient(patient_id)


@app.get("/api/handoffs")
def handoffs_api() -> list[dict]:
    return service.handoffs()


@app.get("/api/sample")
def sample() -> dict:
    return service.sample_payload()


def main() -> None:
    import uvicorn

    port = int(os.getenv("PORT", "4887"))
    uvicorn.run("app.main:app", host="127.0.0.1", port=port, reload=False)


if __name__ == "__main__":
    main()
