from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.services.care_pathway_service import build_service


def main() -> None:
    service = build_service()
    summary = service.summary()
    print("care-pathway-command-center demo")
    print(f"patientCount: {summary['patientCount']}")
    print(f"criticalCount: {summary['criticalCount']}")
    print(f"stalledCount: {summary['stalledCount']}")
    print(f"averageRiskScore: {summary['averageRiskScore']}")
    print(f"averageDelayHours: {summary['averageDelayHours']}")
    for patient in service.patients()[:3]:
        print(f"{patient['patientId']}: {patient['lane']} / risk {patient['riskScore']}")


if __name__ == "__main__":
    main()
