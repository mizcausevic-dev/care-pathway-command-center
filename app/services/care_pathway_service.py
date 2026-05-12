from __future__ import annotations

import json
from pathlib import Path
from statistics import mean
from typing import Any


class CarePathwayService:
    def __init__(self, data: dict[str, Any]) -> None:
        self.data = data

    @classmethod
    def load(cls, data_path: Path | None = None) -> "CarePathwayService":
        path = data_path or Path(__file__).resolve().parent.parent / "data" / "sample_pathways.json"
        return cls(json.loads(path.read_text(encoding="utf-8")))

    def patients(self) -> list[dict[str, Any]]:
        return [self._decorate_patient(patient) for patient in self.data["patients"]]

    def handoffs(self) -> list[dict[str, Any]]:
        patient_map = {patient["patientId"]: patient for patient in self.patients()}
        handoffs = []
        for handoff in self.data["handoffs"]:
            linked = patient_map[handoff["patientId"]]
            handoffs.append(
                {
                    **handoff,
                    "patientAlias": linked["alias"],
                    "program": linked["program"],
                    "lane": linked["lane"],
                }
            )
        return handoffs

    def summary(self) -> dict[str, Any]:
        patients = self.patients()
        handoffs = self.handoffs()
        critical = [patient for patient in patients if patient["lane"] == "escalate"]
        stalled = [patient for patient in patients if patient["delayHours"] >= 24]
        return {
            "patientCount": len(patients),
            "criticalCount": len(critical),
            "stalledCount": len(stalled),
            "handoffCount": len(handoffs),
            "averageRiskScore": round(mean(patient["riskScore"] for patient in patients), 1),
            "averageDelayHours": round(mean(patient["delayHours"] for patient in patients), 1),
            "leadRecommendation": (
                "Shift same-day coordination capacity toward cardiology discharge follow-up and behavioral intake completion."
            ),
        }

    def patient(self, patient_id: str) -> dict[str, Any]:
        for patient in self.patients():
            if patient["patientId"] == patient_id:
                return patient
        raise KeyError(patient_id)

    def sample_payload(self) -> dict[str, Any]:
        return {
            "dashboard": self.summary(),
            "patients": self.patients()[:3],
            "handoffs": self.handoffs(),
        }

    @staticmethod
    def _decorate_patient(patient: dict[str, Any]) -> dict[str, Any]:
        lane = "clear"
        if patient["riskScore"] >= 85 or patient["delayHours"] >= 36:
            lane = "escalate"
        elif patient["riskScore"] >= 55 or patient["delayHours"] >= 12:
            lane = "watch"

        return {
            **patient,
            "lane": lane,
            "barrierCount": len([signal for signal in patient["barrierSignals"] if signal != "none"]),
        }


def build_service() -> CarePathwayService:
    return CarePathwayService.load()
