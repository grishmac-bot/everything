"""
5-pass agentic research loop for Sodexo APMEA strategic accounts growth strategy.
Each pass: research query -> Claude synthesis -> score -> identify gaps -> refine.
Final pass produces scored, validated strategy document.
"""

import anthropic
import json
import os
import sys
import time
from datetime import datetime
from scraper import scrape_all, load_rag_db, search_rag

PASSES_DIR = os.path.join(os.path.dirname(__file__), "passes")
RAG_DIR = os.path.join(os.path.dirname(__file__), "rag_db")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")

os.makedirs(PASSES_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

client = anthropic.Anthropic()
MODEL = "claude-opus-4-5"


def call_claude(prompt: str, system: str = "", max_tokens: int = 4096) -> str:
    messages = [{"role": "user", "content": prompt}]
    kwargs = {"model": MODEL, "max_tokens": max_tokens, "messages": messages}
    if system:
        kwargs["system"] = system
    resp = client.messages.create(**kwargs)
    return resp.content[0].text


def save_pass(pass_num: int, data: dict):
    path = os.path.join(PASSES_DIR, f"pass_{pass_num:02d}.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  Saved pass {pass_num} to {path}")


def load_pass(pass_num: int) -> dict:
    path = os.path.join(PASSES_DIR, f"pass_{pass_num:02d}.json")
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        return json.load(f)


def format_rag_context(entries: list[dict]) -> str:
    if not entries:
        return "No relevant research found."
    parts = []
    for e in entries:
        parts.append(f"SOURCE [{e['category'].upper()}] {e['url']}\n{e['content'][:800]}\n---")
    return "\n".join(parts)


# ─────────────────────────────────────────────────────────────────────────────
# PASS 1: Deep Research — Identify all workstreams, frameworks, benchmarks
# ─────────────────────────────────────────────────────────────────────────────

def pass_01_deep_research(rag_entries: list[dict]) -> dict:
    print("\n" + "="*60)
    print("PASS 1: Deep Research — Workstreams, Frameworks, Benchmarks")
    print("="*60)

    queries = [
        "strategic account management frameworks B2B growth",
        "account planning process enterprise clients",
        "share of wallet expansion facility management services",
        "Sodexo integrated facility management APMEA",
        "B2B revenue growth levers portfolio expansion",
        "strategic account management benchmarks growth rate",
        "facility management industry growth strategies",
        "multi-country account management framework",
    ]

    rag_context_parts = []
    for q in queries:
        results = search_rag(q, rag_entries, top_k=3)
        if results:
            rag_context_parts.append(f"QUERY: {q}\n" + format_rag_context(results))

    rag_context = "\n\n".join(rag_context_parts[:6])

    prompt = f"""You are a senior strategy consultant at McKinsey specializing in B2B FM (Facilities Management) and managed services growth strategy.

CONTEXT — Scraped research data:
{rag_context[:6000]}

TASK: Conduct an exhaustive deep dive into strategic account management for a company like Sodexo.

The situation: Karan is Managing Director, APMEA Strategic Accounts at Sodexo. He manages a €600M portfolio of large multinational clients (e.g., Google, Nokia) who have offices across APMEA and also take Sodexo services in other regions. His mandate: grow the portfolio 17% (to €702M) in 12 months.

DELIVERABLE: Produce a comprehensive list of ALL growth workstreams, frameworks, and mechanisms available. For each workstream:
1. Name and definition
2. The specific framework or methodology (cite real ones: LAMP, Strategic Selling, Challenger, SAMA, etc.)
3. How it applies to Sodexo's situation
4. Realistic revenue contribution potential (% of the 17% target)
5. Timeframe (quick wins <3mo, mid-term 3-6mo, long-term 6-12mo)
6. Key dependencies

Go beyond the obvious 3 steps mentioned. Identify at least 15-20 distinct workstreams. Be exhaustive. No hallucinations. Only cite frameworks that actually exist.

Format as structured JSON with this schema:
{{
  "workstreams": [
    {{
      "id": "WS01",
      "name": "...",
      "definition": "...",
      "framework": "...",
      "sodexo_application": "...",
      "revenue_contribution_pct": "...",
      "timeframe": "quick|mid|long",
      "dependencies": ["..."],
      "evidence_sources": ["..."]
    }}
  ],
  "industry_benchmarks": {{
    "avg_sam_growth_rate": "...",
    "wallet_share_expansion_typical": "...",
    "cross_sell_success_rate": "...",
    "new_geo_expansion_timeline": "..."
  }},
  "key_risks": ["..."]
}}"""

    print("  Calling Claude for deep research synthesis...")
    raw = call_claude(prompt, max_tokens=4096)

    # Extract JSON if wrapped in code block
    if "```json" in raw:
        raw = raw.split("```json")[1].split("```")[0].strip()
    elif "```" in raw:
        raw = raw.split("```")[1].split("```")[0].strip()

    try:
        data = json.loads(raw)
    except Exception:
        data = {"raw_response": raw, "parse_error": True}

    result = {
        "pass": 1,
        "timestamp": datetime.now().isoformat(),
        "rag_queries": queries,
        "rag_entries_used": len(rag_context_parts),
        "output": data,
    }
    save_pass(1, result)

    ws_count = len(data.get("workstreams", [])) if isinstance(data, dict) else 0
    print(f"  Identified {ws_count} workstreams")
    return result


# ─────────────────────────────────────────────────────────────────────────────
# PASS 2: Framework Validation + Gap Analysis
# ─────────────────────────────────────────────────────────────────────────────

def pass_02_validation(pass1_result: dict, rag_entries: list[dict]) -> dict:
    print("\n" + "="*60)
    print("PASS 2: Framework Validation + Gap Analysis")
    print("="*60)

    p1_output = json.dumps(pass1_result.get("output", {}), indent=2)[:4000]

    rag_results = search_rag("account management validation benchmarks Sodexo Compass Aramark", rag_entries, top_k=5)
    rag_context = format_rag_context(rag_results)

    prompt = f"""You are a devil's advocate strategy reviewer at BCG. You are reviewing a strategic framework for growing a €600M FM services portfolio by 17% in 12 months.

FRAMEWORK FROM PASS 1:
{p1_output}

ADDITIONAL RESEARCH:
{rag_context[:3000]}

YOUR TASK:
1. Validate each workstream — is it realistic? Does it have industry precedent? Score each 1-10.
2. Identify gaps — what critical workstreams are MISSING from the framework above?
3. Identify conflicts — which workstreams conflict with each other or are redundant?
4. Check the math — do the revenue contributions add up to 17%? What's missing to get there?
5. Add 5-8 workstreams that are missing but proven in industry.
6. Score the overall framework 1-100 on: completeness, specificity, actionability, financial rigor.

Be brutal. Real gaps only. No padding.

Return JSON:
{{
  "validation": [
    {{"ws_id": "WS01", "score": 8, "verdict": "valid|weak|remove", "reason": "..."}}
  ],
  "missing_workstreams": [
    {{
      "id": "WS_NEW_01",
      "name": "...",
      "definition": "...",
      "framework": "...",
      "revenue_contribution_pct": "...",
      "timeframe": "quick|mid|long"
    }}
  ],
  "math_check": {{
    "total_revenue_covered_pct": 0,
    "gap_to_17pct": 0,
    "recommendation": "..."
  }},
  "overall_score": {{
    "completeness": 0,
    "specificity": 0,
    "actionability": 0,
    "financial_rigor": 0,
    "total": 0,
    "max": 100
  }},
  "top_gaps": ["..."],
  "conflicts": ["..."]
}}"""

    print("  Calling Claude for validation...")
    raw = call_claude(prompt, max_tokens=4096)

    if "```json" in raw:
        raw = raw.split("```json")[1].split("```")[0].strip()
    elif "```" in raw:
        raw = raw.split("```")[1].split("```")[0].strip()

    try:
        data = json.loads(raw)
    except Exception:
        data = {"raw_response": raw, "parse_error": True}

    score = data.get("overall_score", {}).get("total", "N/A") if isinstance(data, dict) else "N/A"
    print(f"  Framework score after validation: {score}/100")

    result = {
        "pass": 2,
        "timestamp": datetime.now().isoformat(),
        "output": data,
    }
    save_pass(2, result)
    return result


# ─────────────────────────────────────────────────────────────────────────────
# PASS 3: Strategy Synthesis — Full Sequential Roadmap
# ─────────────────────────────────────────────────────────────────────────────

def pass_03_strategy_synthesis(pass1_result: dict, pass2_result: dict, rag_entries: list[dict]) -> dict:
    print("\n" + "="*60)
    print("PASS 3: Strategy Synthesis — Full Sequential Roadmap")
    print("="*60)

    p1_ws = pass1_result.get("output", {})
    p2_validation = pass2_result.get("output", {})

    # Merge workstreams: original + new ones from pass 2
    all_workstreams = []
    if isinstance(p1_ws, dict):
        all_workstreams.extend(p1_ws.get("workstreams", []))
    if isinstance(p2_validation, dict):
        all_workstreams.extend(p2_validation.get("missing_workstreams", []))

    ws_json = json.dumps(all_workstreams, indent=2)[:4000]

    rag_results = search_rag("B2B growth roadmap implementation timeline quarterly", rag_entries, top_k=4)
    rag_context = format_rag_context(rag_results)

    prompt = f"""You are the Chief Strategy Officer building Karan's 12-month APMEA Growth Playbook at Sodexo.

INPUTS:
- Validated workstreams: {ws_json}
- Research context: {rag_context[:2000]}

KARAN'S CONTEXT:
- Role: MD, Strategic Accounts APMEA, Sodexo
- Portfolio: €600M, target €702M (+17% in 12 months)
- Clients: Large multinationals (Google, Nokia type) — present in multiple APMEA countries + other regions globally
- Sodexo services: Food services, facility management, workplace experience, integrated FM
- Karan's lever: Relationship + deals. On-ground execution by country MDs.
- Growth vectors: (a) new geographies within existing clients, (b) deeper services at existing sites, (c) new clients in portfolio, (d) price/contract renegotiation

BUILD: A full sequential strategy roadmap. Organize into:
1. Foundation Phase (Month 1-2): Infrastructure and planning
2. Activation Phase (Month 3-5): Quick wins, relationship engagement
3. Expansion Phase (Month 6-9): Geographic and service expansion
4. Acceleration Phase (Month 10-12): Consolidation, late pipeline conversion

For each phase, list specific initiatives with:
- Initiative name
- Owner (Karan direct / country MD / joint)
- Framework used
- Revenue impact (€M)
- KPIs to track
- Concrete actions (3-5 bullet points, ultra-specific)

Then build a WATERFALL showing how €600M becomes €702M:
- Start: €600M
- Each workstream adds specific €M
- End: €702M+

Return JSON:
{{
  "phases": [
    {{
      "phase": "Foundation",
      "months": "1-2",
      "objective": "...",
      "initiatives": [
        {{
          "id": "F01",
          "name": "...",
          "owner": "...",
          "framework": "...",
          "revenue_impact_eur_m": 0,
          "kpis": ["..."],
          "actions": ["..."]
        }}
      ]
    }}
  ],
  "revenue_waterfall": [
    {{"item": "Baseline", "eur_m": 600, "cumulative": 600}},
    {{"item": "...", "eur_m": 0, "cumulative": 0}}
  ],
  "total_target": 702,
  "total_projected": 0
}}"""

    print("  Calling Claude for strategy synthesis...")
    raw = call_claude(prompt, max_tokens=4096)

    if "```json" in raw:
        raw = raw.split("```json")[1].split("```")[0].strip()
    elif "```" in raw:
        raw = raw.split("```")[1].split("```")[0].strip()

    try:
        data = json.loads(raw)
    except Exception:
        data = {"raw_response": raw, "parse_error": True}

    projected = data.get("total_projected", "N/A") if isinstance(data, dict) else "N/A"
    print(f"  Projected total: €{projected}M")

    result = {
        "pass": 3,
        "timestamp": datetime.now().isoformat(),
        "output": data,
    }
    save_pass(3, result)
    return result


# ─────────────────────────────────────────────────────────────────────────────
# PASS 4: Scenario Planning + Financial Model
# ─────────────────────────────────────────────────────────────────────────────

def pass_04_scenarios(pass3_result: dict, rag_entries: list[dict]) -> dict:
    print("\n" + "="*60)
    print("PASS 4: Scenario Planning + Financial Model")
    print("="*60)

    p3_output = json.dumps(pass3_result.get("output", {}), indent=2)[:3000]

    rag_results = search_rag("scenario planning conservative aggressive growth B2B services", rag_entries, top_k=3)
    rag_context = format_rag_context(rag_results)

    prompt = f"""You are a financial strategy modeler at Bain building scenario analysis for Sodexo APMEA.

STRATEGY FROM PASS 3:
{p3_output}

RESEARCH CONTEXT:
{rag_context[:2000]}

BUILD THREE SCENARIOS for growing from €600M to target:

CONSERVATIVE (12% growth = €672M):
- Assumptions: 2 of 4 major workstreams underperform, 1 key client churn, slower geographic expansion
- Which initiatives succeed vs stall
- Final revenue: €M

BASE CASE (17% growth = €702M):
- Assumptions: Plan executes as designed
- All initiatives track
- Final revenue: €M

AGGRESSIVE (22% growth = €732M):
- Assumptions: 2 major upsell wins, faster geo expansion, 1 new strategic logo won
- Which initiatives overperform
- Final revenue: €M

For each scenario:
- Quarterly revenue trajectory (Q1, Q2, Q3, Q4)
- Top 3 value drivers
- Top 3 risks
- Probability (must sum to 100%)
- Key leading indicators to watch monthly

Also include: a RISK REGISTER (top 10 risks, likelihood 1-5, impact 1-5, mitigation)

Return JSON:
{{
  "scenarios": [
    {{
      "name": "Conservative",
      "growth_pct": 12,
      "final_revenue_eur_m": 672,
      "probability_pct": 30,
      "quarterly_revenue": {{"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}},
      "value_drivers": ["..."],
      "risks": ["..."],
      "leading_indicators": ["..."]
    }}
  ],
  "risk_register": [
    {{
      "risk": "...",
      "likelihood": 3,
      "impact": 4,
      "mitigation": "..."
    }}
  ],
  "monthly_dashboard_kpis": ["..."]
}}"""

    print("  Calling Claude for scenario planning...")
    raw = call_claude(prompt, max_tokens=4096)

    if "```json" in raw:
        raw = raw.split("```json")[1].split("```")[0].strip()
    elif "```" in raw:
        raw = raw.split("```")[1].split("```")[0].strip()

    try:
        data = json.loads(raw)
    except Exception:
        data = {"raw_response": raw, "parse_error": True}

    scenarios = data.get("scenarios", []) if isinstance(data, dict) else []
    print(f"  Built {len(scenarios)} scenarios")

    result = {
        "pass": 4,
        "timestamp": datetime.now().isoformat(),
        "output": data,
    }
    save_pass(4, result)
    return result


# ─────────────────────────────────────────────────────────────────────────────
# PASS 5: Final QA, Scoring, Anti-Hallucination Check
# ─────────────────────────────────────────────────────────────────────────────

def pass_05_qa(pass1: dict, pass2: dict, pass3: dict, pass4: dict) -> dict:
    print("\n" + "="*60)
    print("PASS 5: Final QA, Anti-Hallucination Check, Scoring")
    print("="*60)

    summary = {
        "workstreams": pass1.get("output", {}).get("workstreams", [])[:5] if isinstance(pass1.get("output"), dict) else [],
        "validation_score": pass2.get("output", {}).get("overall_score", {}) if isinstance(pass2.get("output"), dict) else {},
        "phases": pass3.get("output", {}).get("phases", []) if isinstance(pass3.get("output"), dict) else [],
        "scenarios": pass4.get("output", {}).get("scenarios", []) if isinstance(pass4.get("output"), dict) else [],
    }

    prompt = f"""You are a senior QA reviewer at a top strategy firm. Your job: fact-check and score a B2B growth strategy document.

STRATEGY SUMMARY:
{json.dumps(summary, indent=2)[:4000]}

QA CHECKLIST — verify each item:

1. FRAMEWORK REALITY CHECK: Are all named frameworks (LAMP, Challenger, SAMA, Miller Heiman, etc.) real and correctly described?
2. MATH INTEGRITY: Does the waterfall add up to ~€702M? Flag any arithmetic errors.
3. SPECIFICITY: Are actions concrete enough to execute? (Bad: "reach out to clients." Good: "Schedule QBR with top 5 accounts by Week 3 using SAMA account planning template.")
4. HALLUCINATION SCAN: Flag any claims that cannot be verified (made-up statistics, non-existent programs, fake benchmarks).
5. COMPLETENESS: Rate coverage across all 4 growth vectors: (a) new geos, (b) deeper services, (c) new clients, (d) price.
6. KARAN-SPECIFICITY: Is this tailored to an APMEA MD managing €600M, or is it generic?
7. SCENARIO PROBABILITY: Do probabilities sum to 100%? Are scenarios meaningfully differentiated?

Produce:
- A QA finding for each check (pass/fail/warning + details)
- Final document score 1-100
- Top 3 critical fixes needed before this is presentable
- Certification: "READY FOR BOARD" or "NEEDS REVISION"

Return JSON:
{{
  "qa_findings": [
    {{"check": "...", "status": "pass|fail|warning", "details": "..."}}
  ],
  "final_score": 0,
  "critical_fixes": ["..."],
  "certification": "READY FOR BOARD|NEEDS REVISION",
  "confidence_level": "high|medium|low",
  "hallucinations_detected": ["..."],
  "strengths": ["..."],
  "weaknesses": ["..."]
}}"""

    print("  Calling Claude for QA and scoring...")
    raw = call_claude(prompt, max_tokens=3000)

    if "```json" in raw:
        raw = raw.split("```json")[1].split("```")[0].strip()
    elif "```" in raw:
        raw = raw.split("```")[1].split("```")[0].strip()

    try:
        data = json.loads(raw)
    except Exception:
        data = {"raw_response": raw, "parse_error": True}

    score = data.get("final_score", "N/A") if isinstance(data, dict) else "N/A"
    cert = data.get("certification", "N/A") if isinstance(data, dict) else "N/A"
    print(f"  Final QA score: {score}/100")
    print(f"  Certification: {cert}")

    result = {
        "pass": 5,
        "timestamp": datetime.now().isoformat(),
        "output": data,
    }
    save_pass(5, result)
    return result


# ─────────────────────────────────────────────────────────────────────────────
# MAIN LOOP
# ─────────────────────────────────────────────────────────────────────────────

def run_all_passes():
    print("\n" + "="*60)
    print("SODEXO APMEA STRATEGIC GROWTH AGENT — 5-PASS LOOP")
    print(f"Started: {datetime.now().isoformat()}")
    print("="*60)

    # Step 0: Scrape research data
    print("\nSTEP 0: Scraping research data...")
    import urllib3
    urllib3.disable_warnings()
    rag_entries = scrape_all(verbose=True)
    print(f"RAG DB ready: {len(rag_entries)} entries")

    # Run 5 passes
    p1 = pass_01_deep_research(rag_entries)
    p2 = pass_02_validation(p1, rag_entries)
    p3 = pass_03_strategy_synthesis(p1, p2, rag_entries)
    p4 = pass_04_scenarios(p3, rag_entries)
    p5 = pass_05_qa(p1, p2, p3, p4)

    print("\n" + "="*60)
    print("ALL PASSES COMPLETE")
    print(f"Finished: {datetime.now().isoformat()}")
    print("="*60)

    return {
        "pass1": p1,
        "pass2": p2,
        "pass3": p3,
        "pass4": p4,
        "pass5": p5,
    }


if __name__ == "__main__":
    all_results = run_all_passes()
    # Save master results
    master_path = os.path.join(PASSES_DIR, "master_results.json")
    with open(master_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nMaster results saved to: {master_path}")
    print("Next step: run generate_html.py to produce final HTML output")
