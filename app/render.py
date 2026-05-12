from __future__ import annotations

from pathlib import Path
from typing import Any


def page_shell(title: str, eyebrow: str, heading: str, body: str, content: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <style>
    :root {{
      --bg: #08131f;
      --panel: #102338;
      --panel-soft: #142b45;
      --line: #2c4867;
      --text: #edf2f8;
      --muted: #9ab2c9;
      --accent: #80c7ff;
      --warn: #ffc779;
      --danger: #ff8f88;
      --ok: #92d7a6;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background:
        radial-gradient(circle at top right, rgba(74, 126, 184, 0.18), transparent 28%),
        linear-gradient(180deg, #07111b 0%, #091726 100%);
      color: var(--text);
      font-family: "Segoe UI", Inter, sans-serif;
    }}
    .page {{ max-width: 1420px; margin: 0 auto; padding: 56px 56px 64px; }}
    .frame {{
      border: 1px solid rgba(128, 199, 255, 0.15);
      border-radius: 34px;
      background: rgba(6, 15, 26, 0.74);
      padding: 28px;
      box-shadow: 0 24px 80px rgba(0,0,0,0.34);
    }}
    .hero {{
      background: linear-gradient(160deg, rgba(16,35,56,0.98), rgba(10,24,39,0.96));
      border: 1px solid rgba(128, 199, 255, 0.16);
      border-radius: 28px;
      padding: 34px;
      margin-bottom: 24px;
    }}
    .eyebrow {{
      color: #93c6ff;
      letter-spacing: 0.26em;
      text-transform: uppercase;
      font-size: 13px;
      margin-bottom: 14px;
      font-weight: 600;
    }}
    h1 {{
      margin: 0 0 12px;
      font-size: 64px;
      line-height: 0.96;
      font-family: Georgia, "Times New Roman", serif;
      max-width: 980px;
    }}
    .body {{
      margin: 0;
      color: var(--muted);
      font-size: 25px;
      max-width: 980px;
      line-height: 1.4;
    }}
    .nav {{
      display: flex;
      gap: 12px;
      justify-content: flex-end;
      margin-bottom: 14px;
    }}
    .pill {{
      border-radius: 999px;
      padding: 10px 16px;
      border: 1px solid rgba(128, 199, 255, 0.18);
      background: rgba(20, 43, 69, 0.88);
      color: var(--text);
      font-size: 14px;
      font-weight: 600;
    }}
    .metrics {{
      display: grid;
      gap: 18px;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      margin-bottom: 24px;
    }}
    .metric, .card {{
      border-radius: 22px;
      background: rgba(17, 35, 56, 0.96);
      border: 1px solid rgba(128, 199, 255, 0.14);
      padding: 24px;
    }}
    .metric .label, .card .label {{
      color: #87bfff;
      text-transform: uppercase;
      letter-spacing: 0.18em;
      font-size: 12px;
      margin-bottom: 14px;
      font-weight: 700;
    }}
    .metric .value {{
      font-size: 46px;
      font-weight: 700;
      margin-bottom: 10px;
      font-family: Georgia, "Times New Roman", serif;
    }}
    .metric .sub {{
      color: var(--muted);
      font-size: 17px;
      line-height: 1.45;
    }}
    .grid {{
      display: grid;
      gap: 18px;
      grid-template-columns: repeat(12, minmax(0, 1fr));
    }}
    .span-4 {{ grid-column: span 4; }}
    .span-5 {{ grid-column: span 5; }}
    .span-6 {{ grid-column: span 6; }}
    .span-7 {{ grid-column: span 7; }}
    .span-8 {{ grid-column: span 8; }}
    .span-12 {{ grid-column: span 12; }}
    .row {{
      display: flex;
      justify-content: space-between;
      gap: 18px;
      padding: 16px 0;
      border-top: 1px solid rgba(128, 199, 255, 0.1);
    }}
    .row:first-of-type {{ border-top: 0; padding-top: 0; }}
    .title {{ font-size: 24px; font-weight: 700; margin-bottom: 8px; }}
    .copy, .small {{
      color: var(--muted);
      font-size: 17px;
      line-height: 1.5;
    }}
    .lane {{
      border-radius: 999px;
      padding: 8px 14px;
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      white-space: nowrap;
      height: fit-content;
    }}
    .lane.escalate {{ background: rgba(255, 143, 136, 0.14); color: var(--danger); }}
    .lane.watch {{ background: rgba(255, 199, 121, 0.14); color: var(--warn); }}
    .lane.clear {{ background: rgba(146, 215, 166, 0.14); color: var(--ok); }}
    pre {{
      margin: 0;
      white-space: pre-wrap;
      font-size: 15px;
      line-height: 1.55;
      color: #d6e8ff;
    }}
  </style>
</head>
<body>
  <div class="page">
    <div class="frame">
      <div class="nav">
        <div class="pill">Overview</div>
        <div class="pill">Queue</div>
        <div class="pill">Handoffs</div>
        <div class="pill">API summary</div>
      </div>
      <section class="hero">
        <div class="eyebrow">{eyebrow}</div>
        <h1>{heading}</h1>
        <p class="body">{body}</p>
      </section>
      {content}
    </div>
  </div>
</body>
</html>"""


def render_overview(summary: dict[str, Any], patients: list[dict[str, Any]]) -> str:
    metrics = f"""
    <section class="metrics">
      <div class="metric"><div class="label">patients</div><div class="value">{summary['patientCount']}</div><div class="sub">active pathways under coordination</div></div>
      <div class="metric"><div class="label">critical</div><div class="value">{summary['criticalCount']}</div><div class="sub">same-day escalation lanes</div></div>
      <div class="metric"><div class="label">stalled</div><div class="value">{summary['stalledCount']}</div><div class="sub">handoffs delayed 24h or more</div></div>
      <div class="metric"><div class="label">avg risk</div><div class="value">{summary['averageRiskScore']}</div><div class="sub">cross-pathway coordination pressure</div></div>
    </section>
    """
    queue = "".join(
        f"""
        <div class="row">
          <div>
            <div class="title">{patient['alias']} <span class="small">· {patient['program']}</span></div>
            <div class="copy">{patient['currentStage']}. {patient['nextAction']}</div>
          </div>
          <div class="lane {patient['lane']}">{patient['lane']}</div>
        </div>
        """
        for patient in patients
    )
    content = metrics + f"""
    <section class="grid">
      <div class="card span-8">
        <div class="label">coordination queue</div>
        {queue}
      </div>
      <div class="card span-4">
        <div class="label">operator recommendation</div>
        <div class="title">Shift coordinator capacity toward the highest-friction discharge and intake pathways.</div>
        <div class="copy">{summary['leadRecommendation']}</div>
      </div>
    </section>
    """
    return page_shell(
        "Care Pathway Command Center",
        "Care Pathway Command Center",
        "Every patient handoff should come with a clear next move.",
        "This command layer turns delay, outreach friction, and follow-up risk into a queue care teams can actually act on.",
        content,
    )


def render_queue(patients: list[dict[str, Any]]) -> str:
    rows = "".join(
        f"""
        <div class="row">
          <div>
            <div class="title">{patient['alias']} · {patient['ownerLane']}</div>
            <div class="copy">Risk {patient['riskScore']} · Delay {patient['delayHours']}h · Contactability {patient['contactability']} · {patient['referralStatus']}</div>
          </div>
          <div class="lane {patient['lane']}">{patient['lane']}</div>
        </div>
        """
        for patient in patients
    )
    return page_shell(
        "Care Queue",
        "Prioritized Queue",
        "The queue should explain urgency, not just sort it.",
        "Advisors and nurses need the why behind every escalation lane, plus the exact action that should happen next.",
        f'<section class="card span-12"><div class="label">active queue</div>{rows}</section>',
    )


def render_handoffs(handoffs: list[dict[str, Any]]) -> str:
    cards = "".join(
        f"""
        <div class="card span-4">
          <div class="label">{handoff['severity']} handoff</div>
          <div class="title">{handoff['patientAlias']}</div>
          <div class="copy">{handoff['fromLane']} to {handoff['toLane']}</div>
          <div class="copy">Delay {handoff['delayHours']}h · Cause: {handoff['cause']}</div>
          <div class="copy">Regulatory pressure: {handoff['regulatoryRisk']}</div>
        </div>
        """
        for handoff in handoffs
    )
    return page_shell(
        "Handoff Replay",
        "Handoff Replay",
        "Care quality breaks where teams stop seeing the same story.",
        "Each handoff carries its own delay signature, risk context, and recommendation so the pathway stays explainable under pressure.",
        f'<section class="grid">{cards}</section>',
    )


def render_api_summary(payload: dict[str, Any]) -> str:
    return page_shell(
        "API Summary",
        "API Summary",
        "The coordination layer can still speak cleanly to downstream systems.",
        "The same pathway command center can feed intervention queues, care dashboards, and audit views without losing the patient story.",
        f'<section class="card span-12"><div class="label">sample payload</div><pre>{payload}</pre></section>',
    )


def write_static_proof_pages(output_dir: Path, summary: dict[str, Any], patients: list[dict[str, Any]], handoffs: list[dict[str, Any]], payload: dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    pages = {
        "01-overview.html": render_overview(summary, patients),
        "02-queue.html": render_queue(patients),
        "03-handoffs.html": render_handoffs(handoffs),
        "04-api-summary.html": render_api_summary(payload),
    }
    for filename, html in pages.items():
        (output_dir / filename).write_text(html, encoding="utf-8")
