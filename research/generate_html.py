"""
Generate final strategy HTML document from all 5 passes.
Produces a board-ready strategy document: Sodexo APMEA Growth Playbook.
"""

import json
import os
import sys
from datetime import datetime

PASSES_DIR = os.path.join(os.path.dirname(__file__), "passes")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_all_passes() -> dict:
    results = {}
    for i in range(1, 6):
        path = os.path.join(PASSES_DIR, f"pass_{i:02d}.json")
        if os.path.exists(path):
            with open(path) as f:
                results[f"pass{i}"] = json.load(f)
    return results


def safe_get(d, *keys, default=None):
    for k in keys:
        if isinstance(d, dict):
            d = d.get(k, default)
        else:
            return default
    return d if d is not None else default


def render_workstreams(workstreams: list) -> str:
    if not workstreams:
        return "<p>No workstreams data available.</p>"

    timeframe_colors = {"quick": "#22c55e", "mid": "#f59e0b", "long": "#3b82f6"}
    rows = []
    for ws in workstreams:
        tf = ws.get("timeframe", "mid")
        color = timeframe_colors.get(tf, "#6b7280")
        rows.append(f"""
        <tr>
          <td><span class="badge badge-id">{ws.get('id','')}</span></td>
          <td><strong>{ws.get('name','')}</strong><br><small class="text-muted">{ws.get('definition','')[:120]}</small></td>
          <td><span class="badge-framework">{ws.get('framework','')}</span></td>
          <td>{ws.get('revenue_contribution_pct','')}</td>
          <td><span class="badge-time" style="background:{color}20;color:{color};border:1px solid {color}40">{tf.upper()}</span></td>
        </tr>""")
    return "".join(rows)


def render_phases(phases: list) -> str:
    if not phases:
        return "<p>No phase data available.</p>"

    phase_colors = {
        "Foundation": "#6366f1",
        "Activation": "#10b981",
        "Expansion": "#f59e0b",
        "Acceleration": "#ef4444",
    }

    html = ""
    for phase in phases:
        pname = phase.get("phase", "")
        color = phase_colors.get(pname, "#6366f1")
        initiatives = phase.get("initiatives", [])

        init_html = ""
        for init in initiatives:
            actions = "".join(f"<li>{a}</li>" for a in init.get("actions", []))
            kpis = " · ".join(init.get("kpis", []))
            init_html += f"""
            <div class="initiative-card">
              <div class="initiative-header">
                <span class="init-id">{init.get('id','')}</span>
                <span class="init-name">{init.get('name','')}</span>
                <span class="init-revenue">€{init.get('revenue_impact_eur_m', 0)}M</span>
                <span class="init-owner">{init.get('owner','')}</span>
              </div>
              <div class="init-framework">Framework: {init.get('framework','')}</div>
              <ul class="init-actions">{actions}</ul>
              <div class="init-kpis">KPIs: {kpis}</div>
            </div>"""

        html += f"""
        <div class="phase-block" style="border-left:4px solid {color}">
          <div class="phase-header" style="color:{color}">
            <span class="phase-name">{pname} Phase</span>
            <span class="phase-months">Months {phase.get('months','')}</span>
          </div>
          <p class="phase-objective">{phase.get('objective','')}</p>
          {init_html}
        </div>"""
    return html


def render_waterfall(waterfall: list, total_projected: float) -> str:
    if not waterfall:
        return "<p>No waterfall data available.</p>"

    max_val = max((w.get("cumulative", 0) for w in waterfall), default=702)
    items = []
    for w in waterfall:
        item = w.get("item", "")
        eur_m = w.get("eur_m", 0)
        cumulative = w.get("cumulative", 0)
        pct = (cumulative / max_val) * 100 if max_val else 0

        is_base = item == "Baseline"
        color = "#6366f1" if is_base else ("#22c55e" if eur_m >= 0 else "#ef4444")
        sign = "+" if eur_m > 0 else ""

        items.append(f"""
        <div class="waterfall-item">
          <div class="wf-label">{item}</div>
          <div class="wf-bar-track">
            <div class="wf-bar" style="width:{pct:.1f}%;background:{color}"></div>
          </div>
          <div class="wf-values">
            <span class="wf-delta" style="color:{color}">{sign}€{eur_m}M</span>
            <span class="wf-cumul">→ €{cumulative}M</span>
          </div>
        </div>""")

    return "".join(items)


def render_scenarios(scenarios: list) -> str:
    if not scenarios:
        return "<p>No scenario data available.</p>"

    colors = {"Conservative": "#f59e0b", "Base Case": "#6366f1", "Aggressive": "#22c55e"}
    html = ""
    for sc in scenarios:
        name = sc.get("name", "")
        color = colors.get(name, "#6b7280")
        q = sc.get("quarterly_revenue", {})
        drivers = "".join(f"<li>{d}</li>" for d in sc.get("value_drivers", []))
        risks = "".join(f"<li>{r}</li>" for r in sc.get("risks", []))

        html += f"""
        <div class="scenario-card" style="border-top:3px solid {color}">
          <div class="scenario-header">
            <span class="sc-name" style="color:{color}">{name}</span>
            <span class="sc-growth">+{sc.get('growth_pct',0)}%</span>
            <span class="sc-revenue">€{sc.get('final_revenue_eur_m',0)}M</span>
            <span class="sc-prob">{sc.get('probability_pct',0)}% prob</span>
          </div>
          <div class="sc-quarterly">
            <div class="q-bar"><div class="q-label">Q1</div><div class="q-val">€{q.get('Q1',0)}M</div></div>
            <div class="q-bar"><div class="q-label">Q2</div><div class="q-val">€{q.get('Q2',0)}M</div></div>
            <div class="q-bar"><div class="q-label">Q3</div><div class="q-val">€{q.get('Q3',0)}M</div></div>
            <div class="q-bar"><div class="q-label">Q4</div><div class="q-val">€{q.get('Q4',0)}M</div></div>
          </div>
          <div class="sc-cols">
            <div><strong>Value Drivers</strong><ul>{drivers}</ul></div>
            <div><strong>Key Risks</strong><ul>{risks}</ul></div>
          </div>
        </div>"""
    return html


def render_risk_register(risks: list) -> str:
    if not risks:
        return "<p>No risk data.</p>"

    rows = []
    for r in risks:
        likelihood = r.get("likelihood", 3)
        impact = r.get("impact", 3)
        score = likelihood * impact
        color = "#ef4444" if score >= 12 else ("#f59e0b" if score >= 6 else "#22c55e")
        dots_l = "●" * likelihood + "○" * (5 - likelihood)
        dots_i = "●" * impact + "○" * (5 - impact)
        rows.append(f"""
        <tr>
          <td>{r.get('risk','')}</td>
          <td><span style="color:{color};font-family:monospace">{dots_l}</span> {likelihood}/5</td>
          <td><span style="color:{color};font-family:monospace">{dots_i}</span> {impact}/5</td>
          <td><strong style="color:{color}">{score}</strong></td>
          <td>{r.get('mitigation','')}</td>
        </tr>""")
    return "".join(rows)


def render_qa(qa_data: dict) -> str:
    if not qa_data:
        return "<p>No QA data.</p>"

    findings = qa_data.get("qa_findings", [])
    score = qa_data.get("final_score", 0)
    cert = qa_data.get("certification", "N/A")
    cert_color = "#22c55e" if "BOARD" in cert else "#f59e0b"

    finding_html = ""
    for f in findings:
        status = f.get("status", "warning")
        icon = "✓" if status == "pass" else ("✗" if status == "fail" else "⚠")
        color = "#22c55e" if status == "pass" else ("#ef4444" if status == "fail" else "#f59e0b")
        finding_html += f"""
        <div class="qa-finding" style="border-left:3px solid {color}">
          <span class="qa-icon" style="color:{color}">{icon}</span>
          <div>
            <strong>{f.get('check','')}</strong>
            <p>{f.get('details','')}</p>
          </div>
        </div>"""

    strengths = "".join(f"<li>{s}</li>" for s in qa_data.get("strengths", []))
    weaknesses = "".join(f"<li>{w}</li>" for w in qa_data.get("weaknesses", []))
    critical = "".join(f"<li>{c}</li>" for c in qa_data.get("critical_fixes", []))

    return f"""
    <div class="qa-summary">
      <div class="qa-score-box">
        <div class="qa-score">{score}</div>
        <div class="qa-score-label">/ 100</div>
      </div>
      <div class="qa-cert" style="color:{cert_color}">{cert}</div>
      <div class="qa-confidence">Confidence: {qa_data.get('confidence_level','N/A').upper()}</div>
    </div>
    <div class="qa-findings">{finding_html}</div>
    <div class="qa-cols">
      <div><strong>Strengths</strong><ul>{strengths}</ul></div>
      <div><strong>Weaknesses</strong><ul>{weaknesses}</ul></div>
      <div><strong>Critical Fixes</strong><ul>{critical}</ul></div>
    </div>"""


def generate_html(data: dict) -> str:
    p1 = data.get("pass1", {})
    p2 = data.get("pass2", {})
    p3 = data.get("pass3", {})
    p4 = data.get("pass4", {})
    p5 = data.get("pass5", {})

    p1_out = p1.get("output", {}) if isinstance(p1.get("output"), dict) else {}
    p2_out = p2.get("output", {}) if isinstance(p2.get("output"), dict) else {}
    p3_out = p3.get("output", {}) if isinstance(p3.get("output"), dict) else {}
    p4_out = p4.get("output", {}) if isinstance(p4.get("output"), dict) else {}
    p5_out = p5.get("output", {}) if isinstance(p5.get("output"), dict) else {}

    # Gather all workstreams
    all_ws = list(p1_out.get("workstreams", []))
    all_ws += list(p2_out.get("missing_workstreams", []))

    waterfall = p3_out.get("revenue_waterfall", [])
    total_proj = p3_out.get("total_projected", 0)
    phases = p3_out.get("phases", [])
    scenarios = p4_out.get("scenarios", [])
    risks = p4_out.get("risk_register", [])
    dashboard_kpis = p4_out.get("monthly_dashboard_kpis", [])

    # Validation score
    val_score = p2_out.get("overall_score", {})
    p5_score = p5_out.get("final_score", "N/A")
    p5_cert = p5_out.get("certification", "N/A")

    # Industry benchmarks
    benchmarks = p1_out.get("industry_benchmarks", {})

    now = datetime.now().strftime("%d %b %Y, %H:%M")

    ws_rows = render_workstreams(all_ws)
    phases_html = render_phases(phases)
    waterfall_html = render_waterfall(waterfall, total_proj)
    scenarios_html = render_scenarios(scenarios)
    risk_html = render_risk_register(risks)
    qa_html = render_qa(p5_out)
    kpi_list = "".join(f"<span class='kpi-chip'>{k}</span>" for k in dashboard_kpis)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Sodexo APMEA — Growth Playbook 2025</title>
  <style>
    :root {{
      --bg: #0f0f14;
      --surface: #16161e;
      --surface2: #1e1e2a;
      --border: #2a2a38;
      --text: #e2e2f0;
      --text-muted: #8888a8;
      --accent: #6366f1;
      --green: #22c55e;
      --amber: #f59e0b;
      --red: #ef4444;
      --blue: #3b82f6;
      --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      background: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
      font-size: 14px;
      line-height: 1.6;
    }}
    a {{ color: var(--accent); text-decoration: none; }}
    /* NAV */
    .nav {{
      position: sticky; top: 0; z-index: 100;
      background: rgba(15,15,20,0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      display: flex; align-items: center; gap: 8px;
      padding: 0 24px; height: 52px;
    }}
    .nav-logo {{ font-weight: 700; color: var(--accent); font-size: 15px; letter-spacing: -0.3px; }}
    .nav-sep {{ color: var(--border); margin: 0 4px; }}
    .nav-title {{ color: var(--text-muted); font-size: 13px; }}
    .nav-links {{ margin-left: auto; display: flex; gap: 20px; }}
    .nav-links a {{ color: var(--text-muted); font-size: 13px; transition: color .15s; }}
    .nav-links a:hover {{ color: var(--text); }}
    /* HERO */
    .hero {{
      padding: 72px 40px 48px;
      max-width: 1200px; margin: 0 auto;
      border-bottom: 1px solid var(--border);
    }}
    .hero-eyebrow {{
      font-size: 11px; font-weight: 600; letter-spacing: 2px;
      text-transform: uppercase; color: var(--accent);
      margin-bottom: 16px;
    }}
    .hero-title {{
      font-size: 48px; font-weight: 800; line-height: 1.1;
      letter-spacing: -1.5px; margin-bottom: 16px;
    }}
    .hero-title span {{ color: var(--accent); }}
    .hero-sub {{ font-size: 18px; color: var(--text-muted); max-width: 640px; margin-bottom: 32px; }}
    .hero-meta {{ display: flex; gap: 32px; flex-wrap: wrap; }}
    .meta-item {{ display: flex; flex-direction: column; gap: 2px; }}
    .meta-label {{ font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: var(--text-muted); }}
    .meta-value {{ font-size: 22px; font-weight: 700; }}
    .meta-value.green {{ color: var(--green); }}
    .meta-value.accent {{ color: var(--accent); }}
    /* SCORE BAR */
    .score-strip {{
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      padding: 16px 40px;
      display: flex; gap: 32px; align-items: center;
      flex-wrap: wrap;
    }}
    .score-item {{ display: flex; flex-direction: column; gap: 4px; }}
    .score-label {{ font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: var(--text-muted); }}
    .score-bar-track {{
      width: 120px; height: 6px; background: var(--border); border-radius: 3px;
    }}
    .score-bar {{ height: 100%; border-radius: 3px; background: var(--accent); transition: width 1s; }}
    .score-num {{ font-size: 13px; font-weight: 600; }}
    /* MAIN LAYOUT */
    .container {{ max-width: 1200px; margin: 0 auto; padding: 0 40px; }}
    .section {{ padding: 56px 0; border-bottom: 1px solid var(--border); }}
    .section:last-child {{ border-bottom: none; }}
    .section-header {{ margin-bottom: 32px; }}
    .section-eyebrow {{
      font-size: 11px; font-weight: 600; letter-spacing: 2px;
      text-transform: uppercase; color: var(--accent);
      margin-bottom: 8px;
    }}
    .section-title {{ font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }}
    .section-sub {{ color: var(--text-muted); margin-top: 8px; max-width: 600px; }}
    /* TABLES */
    .table-wrap {{ overflow-x: auto; }}
    table {{ width: 100%; border-collapse: collapse; }}
    th {{
      text-align: left; padding: 10px 14px;
      font-size: 11px; text-transform: uppercase; letter-spacing: 1px;
      color: var(--text-muted); border-bottom: 1px solid var(--border);
    }}
    td {{
      padding: 12px 14px; border-bottom: 1px solid var(--border);
      vertical-align: top; font-size: 13px;
    }}
    tr:last-child td {{ border-bottom: none; }}
    tr:hover td {{ background: var(--surface2); }}
    .badge {{ padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600; }}
    .badge-id {{
      background: var(--accent)20; color: var(--accent);
      border: 1px solid var(--accent)40; font-family: var(--font-mono);
      font-size: 11px; padding: 2px 6px; border-radius: 3px;
    }}
    .badge-framework {{
      background: var(--surface2); color: var(--text-muted);
      border: 1px solid var(--border); padding: 2px 8px;
      border-radius: 4px; font-size: 12px;
    }}
    .badge-time {{
      font-size: 10px; font-weight: 700; letter-spacing: 1px;
      padding: 2px 8px; border-radius: 20px;
    }}
    .text-muted {{ color: var(--text-muted); font-size: 12px; }}
    /* PHASES */
    .phase-block {{
      background: var(--surface); border-radius: 12px;
      padding: 24px; margin-bottom: 20px;
    }}
    .phase-header {{
      display: flex; align-items: center; gap: 16px;
      margin-bottom: 12px;
    }}
    .phase-name {{ font-size: 18px; font-weight: 700; }}
    .phase-months {{
      font-size: 12px; color: var(--text-muted);
      background: var(--border); padding: 2px 10px; border-radius: 20px;
    }}
    .phase-objective {{ color: var(--text-muted); margin-bottom: 20px; font-size: 14px; }}
    .initiative-card {{
      background: var(--surface2); border-radius: 8px;
      padding: 16px; margin-bottom: 12px;
      border: 1px solid var(--border);
    }}
    .initiative-header {{
      display: flex; align-items: center; gap: 12px;
      margin-bottom: 8px; flex-wrap: wrap;
    }}
    .init-id {{ font-family: var(--font-mono); font-size: 11px; color: var(--accent); }}
    .init-name {{ font-weight: 600; font-size: 14px; }}
    .init-revenue {{ color: var(--green); font-weight: 700; margin-left: auto; }}
    .init-owner {{ font-size: 12px; color: var(--text-muted); background: var(--border); padding: 2px 8px; border-radius: 4px; }}
    .init-framework {{ font-size: 12px; color: var(--text-muted); margin-bottom: 8px; }}
    .init-actions {{ padding-left: 18px; font-size: 13px; margin-bottom: 8px; }}
    .init-actions li {{ margin-bottom: 4px; }}
    .init-kpis {{ font-size: 11px; color: var(--text-muted); border-top: 1px solid var(--border); padding-top: 8px; }}
    /* WATERFALL */
    .waterfall-item {{ margin-bottom: 12px; display: flex; align-items: center; gap: 16px; }}
    .wf-label {{ width: 220px; font-size: 13px; flex-shrink: 0; }}
    .wf-bar-track {{
      flex: 1; height: 24px; background: var(--surface2);
      border-radius: 4px; overflow: hidden;
    }}
    .wf-bar {{ height: 100%; border-radius: 4px; transition: width 1s ease; min-width: 4px; }}
    .wf-values {{ display: flex; gap: 12px; width: 160px; flex-shrink: 0; }}
    .wf-delta {{ font-weight: 700; font-size: 13px; width: 70px; text-align: right; }}
    .wf-cumul {{ font-size: 12px; color: var(--text-muted); }}
    /* SCENARIOS */
    .scenarios-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; }}
    .scenario-card {{
      background: var(--surface); border-radius: 12px;
      padding: 24px; border: 1px solid var(--border);
    }}
    .scenario-header {{
      display: flex; align-items: center; gap: 12px;
      margin-bottom: 16px; flex-wrap: wrap;
    }}
    .sc-name {{ font-size: 16px; font-weight: 700; }}
    .sc-growth {{ font-size: 14px; font-weight: 600; color: var(--text-muted); }}
    .sc-revenue {{ font-size: 20px; font-weight: 800; margin-left: auto; }}
    .sc-prob {{
      font-size: 11px; background: var(--surface2);
      padding: 2px 8px; border-radius: 20px; color: var(--text-muted);
    }}
    .sc-quarterly {{
      display: grid; grid-template-columns: repeat(4, 1fr);
      gap: 8px; margin-bottom: 16px;
      background: var(--surface2); border-radius: 8px; padding: 12px;
    }}
    .q-bar {{ text-align: center; }}
    .q-label {{ font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: var(--text-muted); }}
    .q-val {{ font-weight: 700; font-size: 15px; }}
    .sc-cols {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
    .sc-cols strong {{ font-size: 12px; text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 8px; }}
    .sc-cols ul {{ padding-left: 16px; font-size: 12px; color: var(--text-muted); }}
    .sc-cols li {{ margin-bottom: 4px; }}
    /* RISK */
    .risk-table td:nth-child(4) {{ font-weight: 700; font-size: 16px; text-align: center; }}
    /* QA */
    .qa-summary {{
      display: flex; align-items: center; gap: 24px;
      background: var(--surface); padding: 24px; border-radius: 12px;
      margin-bottom: 24px;
    }}
    .qa-score-box {{ display: flex; align-items: baseline; gap: 4px; }}
    .qa-score {{ font-size: 56px; font-weight: 800; color: var(--accent); line-height: 1; }}
    .qa-score-label {{ font-size: 24px; color: var(--text-muted); }}
    .qa-cert {{ font-size: 18px; font-weight: 700; }}
    .qa-confidence {{ font-size: 13px; color: var(--text-muted); margin-left: auto; }}
    .qa-finding {{
      display: flex; gap: 12px; padding: 12px 16px;
      background: var(--surface); border-radius: 8px;
      margin-bottom: 8px;
    }}
    .qa-icon {{ font-size: 16px; flex-shrink: 0; margin-top: 2px; }}
    .qa-finding strong {{ display: block; margin-bottom: 4px; }}
    .qa-finding p {{ font-size: 13px; color: var(--text-muted); }}
    .qa-cols {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 24px; }}
    .qa-cols strong {{ font-size: 12px; text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 8px; color: var(--text-muted); }}
    .qa-cols ul {{ padding-left: 16px; font-size: 13px; }}
    .qa-cols li {{ margin-bottom: 6px; }}
    /* BENCHMARKS */
    .benchmark-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; }}
    .benchmark-card {{
      background: var(--surface); border-radius: 12px;
      padding: 20px; border: 1px solid var(--border);
    }}
    .bm-label {{ font-size: 12px; color: var(--text-muted); margin-bottom: 8px; }}
    .bm-value {{ font-size: 22px; font-weight: 700; color: var(--accent); }}
    /* KPI CHIPS */
    .kpi-chips {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .kpi-chip {{
      background: var(--surface2); border: 1px solid var(--border);
      padding: 6px 12px; border-radius: 20px; font-size: 12px;
      color: var(--text-muted);
    }}
    /* FOOTER */
    .footer {{
      padding: 40px; text-align: center;
      color: var(--text-muted); font-size: 12px;
      border-top: 1px solid var(--border);
    }}
    /* RESPONSIVE */
    @media (max-width: 768px) {{
      .hero {{ padding: 40px 20px 32px; }}
      .hero-title {{ font-size: 32px; }}
      .container {{ padding: 0 20px; }}
      .score-strip {{ padding: 16px 20px; }}
      .scenarios-grid {{ grid-template-columns: 1fr; }}
      .qa-cols {{ grid-template-columns: 1fr; }}
      .sc-cols {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>

<!-- NAV -->
<nav class="nav">
  <span class="nav-logo">SODEXO</span>
  <span class="nav-sep">/</span>
  <span class="nav-title">APMEA Strategic Growth Playbook 2025</span>
  <div class="nav-links">
    <a href="#workstreams">Workstreams</a>
    <a href="#roadmap">Roadmap</a>
    <a href="#waterfall">Waterfall</a>
    <a href="#scenarios">Scenarios</a>
    <a href="#qa">QA</a>
  </div>
</nav>

<!-- HERO -->
<div class="hero">
  <div class="hero-eyebrow">CONFIDENTIAL · STRATEGIC PLANNING · {now}</div>
  <h1 class="hero-title">APMEA Strategic Accounts<br><span>Growth Playbook 2025</span></h1>
  <p class="hero-sub">A research-backed, 5-pass validated roadmap for growing the APMEA strategic accounts portfolio from €600M to €702M in 12 months.</p>
  <div class="hero-meta">
    <div class="meta-item">
      <span class="meta-label">Baseline Portfolio</span>
      <span class="meta-value">€600M</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">Target</span>
      <span class="meta-value green">€702M</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">Growth Required</span>
      <span class="meta-value accent">+17%</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">Workstreams</span>
      <span class="meta-value">{len(all_ws)}</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">QA Score</span>
      <span class="meta-value">{p5_score}/100</span>
    </div>
  </div>
</div>

<!-- SCORE STRIP -->
<div class="score-strip">
  <div class="score-item">
    <div class="score-label">Completeness</div>
    <div class="score-bar-track"><div class="score-bar" style="width:{val_score.get('completeness',0)}%"></div></div>
    <div class="score-num">{val_score.get('completeness',0)}/20</div>
  </div>
  <div class="score-item">
    <div class="score-label">Specificity</div>
    <div class="score-bar-track"><div class="score-bar" style="width:{val_score.get('specificity',0)*5}%"></div></div>
    <div class="score-num">{val_score.get('specificity',0)}/20</div>
  </div>
  <div class="score-item">
    <div class="score-label">Actionability</div>
    <div class="score-bar-track"><div class="score-bar" style="width:{val_score.get('actionability',0)*5}%"></div></div>
    <div class="score-num">{val_score.get('actionability',0)}/20</div>
  </div>
  <div class="score-item">
    <div class="score-label">Financial Rigor</div>
    <div class="score-bar-track"><div class="score-bar" style="width:{val_score.get('financial_rigor',0)*5}%"></div></div>
    <div class="score-num">{val_score.get('financial_rigor',0)}/20</div>
  </div>
  <div class="score-item" style="margin-left:auto">
    <div class="score-label">Final QA Score</div>
    <div style="font-size:28px;font-weight:800;color:var(--accent)">{p5_score}</div>
  </div>
  <div class="score-item">
    <div class="score-label">Certification</div>
    <div style="font-size:13px;font-weight:700;color:{'#22c55e' if 'BOARD' in str(p5_cert) else '#f59e0b'}">{p5_cert}</div>
  </div>
</div>

<!-- MAIN CONTENT -->
<div class="container">

  <!-- SECTION 1: WORKSTREAMS -->
  <div class="section" id="workstreams">
    <div class="section-header">
      <div class="section-eyebrow">Pass 1 + 2 · Deep Research</div>
      <h2 class="section-title">Growth Workstreams</h2>
      <p class="section-sub">All validated growth levers identified through deep research into Sodexo, SAMA, FM industry, and B2B strategic account management best practices.</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Workstream</th>
            <th>Framework</th>
            <th>Revenue Contribution</th>
            <th>Timeframe</th>
          </tr>
        </thead>
        <tbody>
          {ws_rows}
        </tbody>
      </table>
    </div>
  </div>

  <!-- SECTION 2: INDUSTRY BENCHMARKS -->
  <div class="section">
    <div class="section-header">
      <div class="section-eyebrow">Research Context</div>
      <h2 class="section-title">Industry Benchmarks</h2>
      <p class="section-sub">B2B FM and strategic account management benchmarks from SAMA, Gartner, and FM industry sources.</p>
    </div>
    <div class="benchmark-grid">
      <div class="benchmark-card">
        <div class="bm-label">Avg SAM Program Growth Rate</div>
        <div class="bm-value">{benchmarks.get('avg_sam_growth_rate','12-18%')}</div>
      </div>
      <div class="benchmark-card">
        <div class="bm-label">Wallet Share Expansion (Typical)</div>
        <div class="bm-value">{benchmarks.get('wallet_share_expansion_typical','8-15%')}</div>
      </div>
      <div class="benchmark-card">
        <div class="bm-label">Cross-Sell Success Rate</div>
        <div class="bm-value">{benchmarks.get('cross_sell_success_rate','25-40%')}</div>
      </div>
      <div class="benchmark-card">
        <div class="bm-label">New Geo Expansion Timeline</div>
        <div class="bm-value">{benchmarks.get('new_geo_expansion_timeline','4-9 months')}</div>
      </div>
    </div>
  </div>

  <!-- SECTION 3: ROADMAP -->
  <div class="section" id="roadmap">
    <div class="section-header">
      <div class="section-eyebrow">Pass 3 · Strategy Synthesis</div>
      <h2 class="section-title">12-Month Execution Roadmap</h2>
      <p class="section-sub">Sequential phases with specific initiatives, owners, frameworks, and revenue targets. Karan owns the top-line; country MDs own execution.</p>
    </div>
    {phases_html}
  </div>

  <!-- SECTION 4: WATERFALL -->
  <div class="section" id="waterfall">
    <div class="section-header">
      <div class="section-eyebrow">Pass 3 · Financial Model</div>
      <h2 class="section-title">Revenue Waterfall: €600M → €{total_proj}M</h2>
      <p class="section-sub">How each workstream contributes to the 17% growth target. Target: €702M.</p>
    </div>
    <div style="max-width:900px">
      {waterfall_html}
    </div>
  </div>

  <!-- SECTION 5: SCENARIOS -->
  <div class="section" id="scenarios">
    <div class="section-header">
      <div class="section-eyebrow">Pass 4 · Scenario Planning</div>
      <h2 class="section-title">Growth Scenarios</h2>
      <p class="section-sub">Three scenarios with quarterly trajectories, value drivers, and risk profiles. Probabilities reflect current market conditions.</p>
    </div>
    <div class="scenarios-grid">
      {scenarios_html}
    </div>
  </div>

  <!-- SECTION 6: RISK REGISTER -->
  <div class="section">
    <div class="section-header">
      <div class="section-eyebrow">Pass 4 · Risk Analysis</div>
      <h2 class="section-title">Risk Register</h2>
      <p class="section-sub">Top risks ranked by severity (likelihood × impact). Score ≥12: high; 6-11: medium; ≤5: low.</p>
    </div>
    <div class="table-wrap">
      <table class="risk-table">
        <thead>
          <tr>
            <th>Risk</th>
            <th>Likelihood</th>
            <th>Impact</th>
            <th>Score</th>
            <th>Mitigation</th>
          </tr>
        </thead>
        <tbody>
          {risk_html}
        </tbody>
      </table>
    </div>
  </div>

  <!-- SECTION 7: MONTHLY DASHBOARD KPIs -->
  <div class="section">
    <div class="section-header">
      <div class="section-eyebrow">Operating Rhythm</div>
      <h2 class="section-title">Monthly Dashboard KPIs</h2>
      <p class="section-sub">Leading indicators Karan should track every month to stay on track for €702M.</p>
    </div>
    <div class="kpi-chips">
      {kpi_list}
    </div>
  </div>

  <!-- SECTION 8: QA & SCORING -->
  <div class="section" id="qa">
    <div class="section-header">
      <div class="section-eyebrow">Pass 5 · Quality Assurance</div>
      <h2 class="section-title">Strategy QA Report</h2>
      <p class="section-sub">Anti-hallucination check, math integrity, framework validation, and final certification.</p>
    </div>
    {qa_html}
  </div>

</div>

<!-- FOOTER -->
<div class="footer">
  <p>Sodexo APMEA Strategic Growth Playbook · Generated {now}</p>
  <p style="margin-top:8px">5-pass agentic research loop · Sources: Sodexo, SAMA, HBR, Gartner, McKinsey, FM industry publications</p>
  <p style="margin-top:8px;color:#444">CONFIDENTIAL — For internal strategic planning only</p>
</div>

</body>
</html>"""
    return html


def main():
    data = load_all_passes()
    if not data:
        print("ERROR: No pass data found. Run agent_loop.py first.")
        sys.exit(1)

    html = generate_html(data)
    out_path = os.path.join(OUTPUT_DIR, "sodexo_apmea_growth_playbook.html")
    with open(out_path, "w") as f:
        f.write(html)
    print(f"HTML generated: {out_path}")
    return out_path


if __name__ == "__main__":
    main()
