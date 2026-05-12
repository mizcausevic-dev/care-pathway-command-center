from __future__ import annotations

import unittest

from app.services.care_pathway_service import build_service


class CarePathwayServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.service = build_service()

    def test_summary_counts(self) -> None:
        summary = self.service.summary()
        self.assertEqual(summary["patientCount"], 4)
        self.assertEqual(summary["criticalCount"], 1)

    def test_critical_patient_exists(self) -> None:
        patient = self.service.patient("pt-1042")
        self.assertEqual(patient["lane"], "escalate")

    def test_handoffs_include_patient_alias(self) -> None:
        handoff = self.service.handoffs()[0]
        self.assertIn("patientAlias", handoff)


if __name__ == "__main__":
    unittest.main()
