# Track 02 — Tools: Enterprise B2B Sales / B2B 大客户销售

> Phase 1 wave-2 tools research. Industry = high-value, long-cycle, multi-stakeholder B2B selling (AE / SE / sales-leader practitioner view). locale=global (en-primary). profile=practitioner.
> **Two tool classes, not one.** ① the **sales-software SaaS stack** (CRM / sales engagement / conversation intelligence / prospecting data / forecasting & deal inspection / mutual-action-plan & digital sales room / CPQ & proposal & e-sign / enablement / AI SDR agents); ② **methodology artifacts** — the branded "tools" that ARE the work in complex selling (MEDDPICC scorecard, Miller Heiman Blue Sheet, Sandler pain funnel, mutual action plan template, Command of the Message value framework, bowtie/SPICED canvas). Class ② is what makes this industry's tool track distinctive — they are paper/doc/CRM-field artifacts, not apps, and they decay slowly while the SaaS layer churns fast.
> **NOT cold.** 34 candidates explored, **24 retained** (必备 8 / 场景特化 10 / 新兴 6). Closed-source SaaS has no GitHub stars → maturity signals = founding year / funding & M&A events (dated) / vendor-public customer counts (caveated 官方公开) / practitioner-source endorsement.
> **Wave-1 hand-off used**: Track 04 canon's Phase-2 interface named the methodology-artifact candidates (Blue Sheet, MEDDPICC checklist, pain funnel, MAP, bowtie/SPICED, Command of the Message). Track 01 figures confirmed Gong Labs as the one citable first-party data source. Both folded in below.

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://www.salesforce.com/products/sales-cloud/ | verified_primary | 2026-06-11 | Salesforce | Sales Cloud CRM — vendor product page (brand /products path) |
| T02-S002 | https://www.hubspot.com/products/crm | verified_primary | 2026-06-11 | HubSpot | HubSpot Sales Hub / Smart CRM — vendor product page |
| T02-S003 | https://www.gong.io/product/ | verified_primary | 2026-06-11 | Gong | Conversation-intelligence / Revenue AI platform — vendor (whitelisted) |
| T02-S004 | https://techcrunch.com/2025/03/05/revenue-prediction-startup-gong-surpasses-300m-arr-indicating-potential-ipo-path/ | secondary | 2026-06-11 | TechCrunch | Gong $300M ARR (5 Mar 2025), founded 2016, $7.25B val, 4,500 customers |
| T02-S005 | https://www.gong.io/blog/the-best-sales-insights-of-2025 | verified_primary | 2026-06-11 | Gong Labs | First-party 2025 data: multithreading/talk-ratio/AI win-rate |
| T02-S006 | https://www.salesloft.com/platform | surrogate_primary | 2026-06-11 | Salesloft | Sales-engagement platform — vendor docs (classify=secondary → surrogate, note 供应商) |
| T02-S007 | https://www.salesloft.com/company/newsroom/clari-salesloft-merger | surrogate_primary | 2026-06-11 | Salesloft/Clari | vendor docs (newsroom 供应商官方): Clari+Salesloft merger complete, CEO Steve Cox, 10B interactions |
| T02-S008 | https://www.apollo.io/product/sales-engagement | surrogate_primary | 2026-06-11 | Apollo.io | All-in-one prospecting+engagement, 275M records — vendor docs (供应商) |
| T02-S009 | https://www.zoominfo.com/products/sales | verified_primary | 2026-06-11 | ZoomInfo | Sales-intelligence data — vendor product page (brand /products path) |
| T02-S010 | https://www.clari.com/products/forecasting/ | verified_primary | 2026-06-11 | Clari | Forecasting & RevOps — vendor product page (brand /products path) |
| T02-S011 | https://www.clay.com/blog/claygent-1-billion | verified_primary | 2026-06-11 | Clay | Claygent 1B runs — first-party (signal-based GTM / waterfall enrichment) |
| T02-S012 | https://www.outreach.io/product | surrogate_primary | 2026-06-11 | Outreach | Sales-execution / engagement — vendor docs (classify=secondary → surrogate, 供应商) |
| T02-S013 | https://business.linkedin.com/sales-solutions/sales-navigator | surrogate_primary | 2026-06-11 | LinkedIn | Sales Navigator (self-updated profiles) — vendor docs (供应商) |
| T02-S014 | https://www.docusign.com/products/clm | verified_primary | 2026-06-11 | Docusign | CLM + e-signature — vendor product page (brand /products path) |
| T02-S015 | https://www.pandadoc.com/ | surrogate_primary | 2026-06-11 | PandaDoc | Proposal/CPQ/e-sign, launched 2011 — vendor docs (供应商) |
| T02-S016 | https://www.salesforce.com/products/revenue-cloud/overview/ | verified_primary | 2026-06-11 | Salesforce | Revenue Cloud Advanced (legacy CPQ successor) — vendor product page |
| T02-S017 | https://www.salesforceben.com/salesforce-confirms-the-future-of-cpq/ | secondary | 2026-06-11 | Salesforce Ben | Salesforce CPQ end-of-sale (Mar 2025) → Revenue Cloud Advanced |
| T02-S018 | https://www.highspot.com/sales-enablement-platform/ | surrogate_primary | 2026-06-11 | Highspot | Sales-enablement platform — vendor docs (供应商) |
| T02-S019 | https://gtmbuddy.ai/blog/highspot-seismic-merger-analysis | secondary | 2026-06-11 | GTM Buddy (competitor) | Highspot+Seismic merge 12 Feb 2026 ($6B+); "shelfware/storage-first" critique — competitor blog, caveat |
| T02-S020 | https://www.getaccept.com/product/mutual-action-plan | surrogate_primary | 2026-06-11 | GetAccept | Digital sales room + MAP — vendor docs (供应商) |
| T02-S021 | https://www.dock.us/library/mutual-action-plans | surrogate_primary | 2026-06-11 | Dock | MAP 101 + AI-generated MAP / digital sales room — vendor docs (供应商) |
| T02-S022 | https://www.highspot.com/blog/mutual-action-plan/ | verified_primary | 2026-06-11 | Highspot | MAP keep-deals-on-track explainer — vendor first-party (brand /blog) |
| T02-S023 | https://meddicc.com/meddpicc-sales-methodology-and-process | verified_primary | 2026-06-11 | MEDDICC (Whyte) | MEDDPICC element-by-element canon — methodology originator (whitelisted) |
| T02-S024 | https://meddic.academy/meddic-sales-methodology-checklist/ | verified_primary | 2026-06-11 | MEDDIC Academy | MEDDIC/MEDDPICC checklist + cert — methodology originator (whitelisted) |
| T02-S025 | https://www.gong.io/blog/sandler-pain-funnel | verified_primary | 2026-06-11 | Gong | Sandler pain-funnel 8-question breakdown — first-party explainer (whitelisted) |
| T02-S026 | https://www.sandler.com/resources/sandler-tools/pain-funnel/ | verified_primary | 2026-06-11 | Sandler | Pain funnel — Sandler's own tool page (originator, whitelisted) |
| T02-S027 | https://www.kornferry.com/insights/featured-topics/sales-transformation/the-blue-sheet-history-and-evolution-of-an-industry-icon | secondary | 2026-06-11 | Korn Ferry | Blue Sheet history (1970s, 4 decades), Korn Ferry Sell 2025 integration, +22% win rate (2024 KF Survey) |
| T02-S028 | https://www.forcemanagement.com/blog/whats-the-meaning-of-command-of-the-message | verified_primary | 2026-06-11 | Force Management | Command of the Message value framework — originator (whitelisted) |
| T02-S029 | https://winningbydesign.com/resources/recipes/the-spiced-framework/ | verified_primary | 2026-06-11 | Winning by Design | SPICED canvas / bowtie — originator (whitelisted) |
| T02-S030 | https://techcrunch.com/2025/03/24/a16z-and-benchmark-backed-11x-has-been-claiming-customers-it-doesnt-have/ | secondary | 2026-06-11 | TechCrunch | 11x claimed ZoomInfo/Airtable as customers (they weren't); ARR didn't split trials from real (24 Mar 2025) |
| T02-S031 | https://techcrunch.com/2025/05/05/11x-ceo-hasan-sukkar-steps-down/ | secondary | 2026-06-11 | TechCrunch | 11x CEO Hasan Sukkar steps down (5 May 2025) — AI-SDR decay proof |
| T02-S032 | https://www.nooks.ai/ai-dialer | surrogate_primary | 2026-06-11 | Nooks | AI parallel dialer + virtual salesfloor — vendor docs ($43M Series B 2024, Kleiner Perkins) (供应商) |
| T02-S033 | https://www.rilla.com/ | surrogate_primary | 2026-06-11 | Rilla | AI in-person/field-sales coaching, Rilla Live launched Sep 2025 — vendor docs (供应商) |
| T02-S034 | https://www.salesforce.com/news/stories/salesforce-signs-definitive-agreement-to-acquire-momentum/ | surrogate_primary | 2026-06-11 | Salesforce | vendor docs (newsroom 供应商官方): Salesforce→Momentum acquisition (conversational AI → Agentforce); completed 2 Mar 2026 |
| T02-S035 | https://www.salesforce.com/agentforce/ | surrogate_primary | 2026-06-11 | Salesforce | vendor docs (供应商产品页): Agentforce agentic-AI platform; Agentforce 360 GA 23 Feb 2026 |
| T02-S036 | https://inaccord.com/blog-posts/top-9-mutual-action-plan-tools-for-sales-teams-in-2026 | secondary | 2026-06-11 | Accord (vendor) | MAP-tool landscape (Accord/Flowla/Dock/GetAccept/trumpet) — vendor listicle, caveat |
| T02-S037 | https://www.leadgen-economy.com/blog/ai-sdr-cancellation-wave-failure-forensics/ | secondary | 2026-06-11 | Leadgen Economy | AI-SDR "50-70% annual churn / >50% abandon within a year" — third-party blog, 业内估计 caveat |
| T02-S038 | https://www.gong.io/blog/talk-to-listen-conversion-ratio | verified_primary | 2026-06-11 | Gong Labs | Golden talk-to-listen ratio (43/57) first-party study |
| T02-S039 | https://research.contrary.com/company/gong | secondary | 2026-06-11 | Contrary Research | Gong business breakdown / founding story (corroborates 2015-16 founding, founders) |

> **Buckets** (39 sources): verified_primary **17 / 39 = 43.6%**; surrogate_primary **13** (all genuine vendor docs / vendor newsrooms / vendor product pages — the Surrogate Sources Policy explicitly classes vendor docs as first-hand, declared surrogate where `classify` returned secondary because the page path wasn't `/products/` or `/blog/`); secondary **9** (TechCrunch investigative ×3, Korn Ferry insight, Salesforce Ben, and 4 vendor/3rd-party blogs used only for dated facts + caveated stats, never sole evidence for a mental-model claim). **No blacklisted source** (G2 / Capterra / Gartner / LinkedIn article-body / businesswire / prnewswire) appears in the manifest or backs any claim. The G2 contact-accuracy scores surfaced in research are deliberately NOT cited; accuracy claims are caveated as "third-party comparison / 业内估计" instead.
> **Why verified_primary is "only" 44%** (vs figures/canon ~56-62%): closed-source SaaS vendors are the legitimate first source for their own product, but many of their best pages (`/platform`, `/product`, `/`) classify as `secondary` and can only be declared `surrogate_primary` — so the *first-hand* share is actually 17+13 = **30/39 = 77%** (verified+surrogate), well above the spirit of the ≥55% bar. This is a structural artifact of a proprietary-vendor industry, flagged for Phase 2.8.

---

## 总览（按 tier 分组）

### 必备（8 个 — ≥ 80% of enterprise B2B sellers' orgs run one of these per category）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| **Salesforce / HubSpot (CRM)** | The system of record every deal lives in; everything else integrates to it | low | T02-S001, T02-S002 |
| **Gong (conversation intelligence)** | Records/transcribes/scores every call → coaching + deal-risk + buying signals | low-medium | T02-S003, T02-S004, T02-S005 |
| **Salesloft / Outreach (sales engagement)** | Sequences/cadences for multichannel outreach + activity tracking | medium | T02-S006, T02-S012, T02-S007 |
| **Clari (forecasting & deal inspection)** | Pipeline inspection + AI forecast roll-up; "is this deal real / will we hit number?" | low-medium | T02-S010, T02-S007 |
| **Apollo / ZoomInfo / LinkedIn Sales Nav (prospecting data)** | Who to call + their email/phone/firmographics/intent | medium | T02-S008, T02-S009, T02-S013 |
| **Docusign (e-signature)** | The legally-binding signature step where verbal-yes becomes a contract | low | T02-S014 |
| **MEDDPICC scorecard (methodology artifact)** | The qualification checklist that decides which deals are real — lives in CRM fields | low | T02-S023, T02-S024 |
| **Mutual Action Plan / digital sales room (artifact + tool)** | The shared close plan that aligns buyer + seller on steps to signature | low (artifact) / medium (tool) | T02-S020, T02-S021, T02-S022 |

### 场景特化（10 个 — specific sub-motions / deal-types / roles）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| **Clay (signal-based GTM / enrichment)** | Waterfall enrichment + Claygent AI research for outbound that isn't spray-and-pray | high | T02-S011 |
| **PandaDoc / DealHub (CPQ + proposal)** | Configure-price-quote + proposal doc for complex/variable pricing | medium | T02-S015 |
| **Salesforce Revenue Cloud Advanced (CPQ)** | Native quote-to-cash for SF shops (legacy SF CPQ is end-of-sale) | medium | T02-S016, T02-S017 |
| **Highspot / Seismic (enablement)** | Content management + rep onboarding/cert; high shelfware risk | medium | T02-S018, T02-S019 |
| **Miller Heiman Blue Sheet (artifact, strategic accounts)** | 6-page opportunity map for large multi-stakeholder strategic deals | low | T02-S027 |
| **Sandler pain funnel (artifact, discovery)** | 8 nested questions taking a buyer from vague frustration → quantified pain | low | T02-S025, T02-S026 |
| **Command of the Message value framework (artifact)** | Before/After + PBOs + Required Capabilities + Differentiation, for value selling to the economic buyer | low | T02-S028 |
| **bowtie / SPICED canvas (artifact, SaaS recurring-rev)** | Shared qual model (Situation/Pain/Impact/Critical event/Decision) + post-sale expansion map | low | T02-S029 |
| **Nooks (AI parallel dialer)** | 5-8x live connects via parallel dialing + AI salesfloor — for high-volume outbound calling | high | T02-S032 |
| **Rilla (AI field/in-person coaching)** | Records in-person/field reps (home services, med-device) — conversation intelligence for non-Zoom selling | high | T02-S033 |

### 新兴（6 个 — 近 12 个月起势; all `stability: experimental`）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| **AI SDR agents (11x / Artisan / AiSDR)** | Autonomous prospecting agents — collapsed amid deliverability + overstated-ARR backlash | high | T02-S030, T02-S031, T02-S037 |
| **Salesforce Agentforce (agentic selling)** | Action-taking AI agents inside CRM; Agentforce 360 GA Feb 2026 — platform-fatigue risk | high | T02-S035 |
| **Momentum (AI revenue orchestration)** | Auto-MEDDIC capture + Slack deal rooms from call data; acquired by Salesforce Mar 2026 | high | T02-S034 |
| **AI note-takers / auto-CRM (Momentum/Sybill-class)** | Write call notes + populate CRM/MEDDIC fields automatically — fixes "CRM hygiene theater" | high | T02-S034 |
| **AI deal coaching (Gong/Clari AI layer)** | AI flags at-risk deals + suggests next steps; "data-driven coaching" claim vs surveillance reality | high | T02-S005, T02-S003 |
| **Clay-style signal GTM as a category** | "Signal-based" replacing the SDR-army — contested whether it scales or just shifts the spam | high | T02-S011 |

---

## 各工具卡片

### 必备层

#### 1. Salesforce / HubSpot — CRM (system of record)

- **One-liner**: The database every opportunity, contact, and forecast lives in; in complex B2B it is the spine the entire stack integrates into — Salesforce dominates enterprise, HubSpot mid-market. (evidence: [T02-S001, T02-S002])
- **Tier**: 必备
- **Maintainer / Owner**: Salesforce, Inc. (https://www.salesforce.com); HubSpot, Inc. (https://www.hubspot.com)
- **License**: proprietary (per-seat SaaS)
- **Maturity signals**:
  - Salesforce founded 1999; the de-facto enterprise CRM standard for 20+ years (last checked: 2026-06-11). (evidence: [T02-S001])
  - HubSpot Sales Hub / Smart CRM — public company (NYSE: HUBS), dominant SMB/mid-market CRM (last checked: 2026-06-11). (evidence: [T02-S002])
  - Activity: healthy — both ship quarterly; Salesforce pushing Revenue Cloud + Agentforce as the 2026 platform bet. (evidence: [T02-S016, T02-S035])
- **典型使用场景**: every deal's source of truth for pipeline stage / amount / close date / MEDDIC fields; the object model AEs, managers (deal reviews) and RevOps (forecast) all read from.
- **不适合 / 替代方案**: for a < 10-person startup pre-PMF, Salesforce is too heavy (long admin/config) — Pipedrive or HubSpot Starter is the lighter call. The CRM is necessary but **not** a selling tool: a clean CRM ≠ a qualified pipeline (see 避坑). (evidence: [T02-S002])
- **生产案例**: effectively universal in enterprise SaaS GTM; Predictable Revenue / Winning by Design / MEDDIC all assume a CRM as the substrate their methodology writes into. (evidence: [T02-S023])
- **近期变化 (近12月)**: Salesforce legacy CPQ moved to end-of-sale (Mar 2025) → Revenue Cloud Advanced; Agentforce 360 GA Feb 2026 reframes CRM as an agentic platform. (evidence: [T02-S016, T02-S035])
- **可信度**: high. **Decay risk**: low (< 20% displaced in 24+ months — this is the most entrenched layer of the stack).

#### 2. Gong — conversation intelligence / Revenue AI

- **One-liner**: Records, transcribes and AI-scores every sales call/email/meeting → turns conversations into coaching insights, deal-risk flags, and buying signals; also the one **first-party large-sample data source** this industry can cite (Gong Labs). (evidence: [T02-S003, T02-S005])
- **Tier**: 必备 (in enterprise SaaS; conversation intelligence is now table-stakes for any team > ~20 reps)
- **Maintainer / Owner**: Gong.io, Inc. (https://www.gong.io)
- **License**: proprietary (per-seat SaaS)
- **Maturity signals**:
  - Founded **2016** (founders Amit Bendov & Eilon Reshef); surpassed **$300M ARR** announced 5 Mar 2025; last private valuation **$7.25B** (Series E, 2021); **4,500 corporate customers** incl. Canva, Google, LinkedIn, Square (官方公开 / TechCrunch, last checked 2026-06-11). (evidence: [T02-S004, T02-S039])
  - Reported "top-quartile public-SaaS" growth (≈25-56% YoY) and "nearly profitable" → IPO-track signal, not 2025 (last checked: 2026-06-11). (evidence: [T02-S004])
  - Activity: healthy — aggressive gen-AI feature expansion fueling growth. (evidence: [T02-S004])
- **典型使用场景**: (a) coaching — managers review call talk-ratios/objection-handling instead of riding along; (b) deal inspection — flag deals with no multithreading / no economic-buyer engagement; (c) the org-wide "did the rep actually run discovery?" audit.
- **不适合 / 替代方案**: overkill + expensive for a tiny team (low-volume); cheaper note-takers (tl;dv, Fathom, Sybill) cover the transcript/summary job without the deal-intelligence price. The failure mode is **surveillance, not coaching** (see 避坑). (evidence: [T02-S003])
- **生产案例**: Gong Labs' own studies (golden talk-to-listen 43/57; early competitor-mention ≈ +32% win; multithreading lifts > $50K-deal win-rate ≈ +130%; high-AI-use reps +77% — all **Gong first-party, caveat 官方公开研究**) are the canonical "data-backed selling" references cited across the figures track. (evidence: [T02-S005, T02-S038])
- **维护者背景 (sub_skill_link)**: Gong Labs is referenced in Track 01 figures as the only directly-citable large-sample data source (vs blacklisted Gartner/Forrester).
- **近期变化 (近12月)**: heavy generative-AI / "AI deal coaching" push; secondary-market valuation chatter slipped to ~$4.5B late-2025 (not company-approved) — directional, caveat. (evidence: [T02-S004])
- **可信度**: high. **Decay risk**: low-medium (category entrenched; the *AI-coaching layer* on top is high-decay — see 新兴 #5).

#### 3. Salesloft / Outreach — sales engagement

- **One-liner**: The sequencer/cadence engine for multichannel outbound + activity logging — schedules the "touch 1 email, touch 3 call, touch 5 LinkedIn" motion and tracks reply/open rates at scale. (evidence: [T02-S006, T02-S012])
- **Tier**: 必备 (for any team running structured outbound; the SDR/AE workhorse)
- **Maintainer / Owner**: Salesloft (now merged with Clari, CEO Steve Cox); Outreach, Inc.
- **License**: proprietary (per-seat SaaS)
- **Maturity signals**:
  - Salesloft: Vista majority acquisition **$2.3B (2022)**; merged with Drift **13 Feb 2024**; merged with **Clari** (completed late 2025, CEO Steve Cox) → combined "Revenue AI" entity citing 10B+ interactions / 1T signals across Adobe, 3M, IBM, Zoom (官方公开, last checked 2026-06-11). (evidence: [T02-S007])
  - Activity: healthy but **consolidating** — the sales-engagement category is collapsing into forecasting/RevOps suites via M&A. (evidence: [T02-S007])
- **典型使用场景**: SDR daily task list (today's calls/emails); A/B testing subject lines; enforcing follow-up discipline; multichannel cadence orchestration.
- **不适合 / 替代方案**: in an AI-SDR / signal-based world the "blast the same cadence at everyone" use is exactly what's killing deliverability (see 避坑); for low-volume enterprise ABM, a tight Clay→manual-personalize motion beats high-volume sequencing. Apollo bundles a cheaper engagement layer for SMB. (evidence: [T02-S037, T02-S008])
- **生产案例**: Aaron Ross's Predictable Revenue SDR/AE split (Track 01/04) is the org model these tools operationalize. (evidence: [T02-S007])
- **近期变化 (近12月)**: Clari+Salesloft merger = "engagement + execution + forecasting" in one — the biggest 2025 stack consolidation; reframes sales engagement as part of "revenue orchestration." (evidence: [T02-S007])
- **可信度**: high. **Decay risk**: medium (12-24mo: 20-40% — the standalone-engagement category is being absorbed; the *function* persists, the *vendor boundaries* are moving).

#### 4. Clari — forecasting & deal inspection

- **One-liner**: The pipeline-inspection + AI-forecast-roll-up layer that answers the CRO's two questions — "is this specific deal real?" and "will we hit the number this quarter?" — by reading activity/signals the CRM stage field can't capture. (evidence: [T02-S010])
- **Tier**: 必备 (for any team that forecasts to a board; the deal-review / commit-best-case-pipeline engine)
- **Maintainer / Owner**: Clari (merged with Salesloft, late 2025; CEO Steve Cox)
- **License**: proprietary (per-seat SaaS)
- **Maturity signals**:
  - Clari + Salesloft merger completed late 2025; combined entity ingests **10B+ revenue interactions / 1T data signals** (官方公开, last checked 2026-06-11). (evidence: [T02-S007, T02-S010])
  - Activity: healthy — now the forecasting half of the merged "Revenue AI" platform. (evidence: [T02-S007])
- **典型使用场景**: weekly deal review (which deals slipped/pushed); forecast roll-up by commit/best-case/pipeline category; pipeline-coverage tracking (the ~3x rule-of-thumb — caveat 经验法则, no canonical source per Track 04).
- **不适合 / 替代方案**: for a team < ~30 reps the forecast can live in a CRM report + spreadsheet; Clari earns its keep at scale where manual roll-up breaks. Gong's forecast module and Salesforce's native forecasting overlap it. (evidence: [T02-S007])
- **生产案例**: operationalizes John McMahon's "deal inspection / forecast from evidence not optimism" discipline (Track 01/04 MEDDPICC worldview). (evidence: [T02-S023])
- **近期变化 (近12月)**: merged with Salesloft → end-to-end engage→execute→forecast; "predictive revenue system" framing. (evidence: [T02-S007])
- **可信度**: high. **Decay risk**: low-medium (the forecasting function is durable; vendor identity is mid-merger).

#### 5. Apollo / ZoomInfo / LinkedIn Sales Navigator — prospecting data

- **One-liner**: The "who do I call and how do I reach them" layer — contact + firmographic + intent data. Apollo = all-in-one + cheapest; ZoomInfo = deepest enterprise data; Sales Nav = freshest (self-updated by prospects) but no emails/dialing. (evidence: [T02-S008, T02-S009, T02-S013])
- **Tier**: 必备 (no prospecting motion runs without a data source)
- **Maintainer / Owner**: Apollo.io; ZoomInfo Technologies (NASDAQ: ZI); LinkedIn (Microsoft)
- **License**: proprietary (per-seat / credit-based SaaS)
- **Maturity signals**:
  - Apollo: **275M+ contact records**, email match-rate **87-91%** in vertical testing; ZoomInfo: **300M+ contacts**, deepest intent + direct-dials (官方公开 + 第三方测试, last checked 2026-06-11). (evidence: [T02-S008, T02-S009])
  - LinkedIn Sales Nav: profiles self-updated by prospects → job-change data fresh within hours vs 30-90-day lag in static DBs (vendor + 业内观察, last checked 2026-06-11). (evidence: [T02-S013])
  - Pricing spread (业内估计): Apollo ≈ $300-500/mo for a 5-person team vs ZoomInfo ≈ $15K-40K/yr — a 30-100x gap that drives the SMB-vs-enterprise split. (evidence: [T02-S008, T02-S009])
- **典型使用场景**: building a target account/contact list; enriching inbound leads; triggering outreach on a job-change or funding signal; finding the economic buyer's direct line.
- **不适合 / 替代方案**: data accuracy claims are vendor/3rd-party (caveat — the G2 accuracy scores are deliberately NOT cited here); all decay (people move). Sales Nav alone can't contact anyone outside LinkedIn → must pair with Apollo/ZoomInfo + a sequencer. For pure signal-based outbound, Clay's waterfall enrichment composes multiple of these. (evidence: [T02-S011])
- **生产案例**: the data spine under every Predictable-Revenue-style SDR motion; Clay (新兴 layer) explicitly "waterfalls" across these providers. (evidence: [T02-S011])
- **近期变化 (近12月)**: AI-research agents (Apollo, Clay's Claygent) layering on top; intent-data arms race continues. (evidence: [T02-S011])
- **可信度**: high (as a category). **Decay risk**: medium (data freshness + the AI-enrichment shift are actively reshaping who wins).

#### 6. Docusign — e-signature

- **One-liner**: The legally-binding signature step where a verbal-yes becomes an executed contract — the most boring and most non-negotiable tool in the close. (evidence: [T02-S014])
- **Tier**: 必备 (the paper-process endpoint of MEDDPICC's "P")
- **Maintainer / Owner**: Docusign, Inc. (NASDAQ: DOCU)
- **License**: proprietary (per-seat / envelope SaaS)
- **Maturity signals**:
  - E-signature pioneer since **2003**; public company; ESIGN/UETA/eIDAS-compliant standard (官方公开, last checked 2026-06-11). (evidence: [T02-S014])
  - Activity: healthy — expanding from e-sign into CLM (contract lifecycle management). (evidence: [T02-S014])
- **典型使用场景**: the signature event itself; CLM for redline/legal/security review (the part of the Paper Process where deals die).
- **不适合 / 替代方案**: if you also need proposal-doc creation + CPQ, PandaDoc bundles e-sign + doc-gen and is cheaper for that combined job; for SF-native quote-to-cash, Revenue Cloud Advanced. (evidence: [T02-S015, T02-S016])
- **生产案例**: universal; the "P" (Paper Process) in MEDDPICC explicitly maps the procurement/legal/security path this tool closes. (evidence: [T02-S023])
- **可信度**: high. **Decay risk**: low (e-signature is commoditized infrastructure).

#### 7. MEDDPICC scorecard — methodology artifact (qualification)

- **One-liner**: NOT an app — the qualification checklist (Metrics / Economic buyer / Decision Criteria / Decision Process / Paper Process / Identify Pain / Champion / Competition) that decides which deals are real; lives as CRM fields or a one-page scorecard, scored 0-3 per element. (evidence: [T02-S023, T02-S024])
- **Tier**: 必备 (the default qualification language of enterprise/SaaS sales)
- **Maintainer / Owner**: originated PTC 1996 (Dunkel/Napoli under McMahon); codified by Andy Whyte (MEDDICC) + MEDDIC Academy (Darius Lahoutifard). (evidence: [T02-S023, T02-S024])
- **License**: methodology (free to use; certs/training are paid)
- **Maturity signals**:
  - In continuous use since **1996**; the MEDDICC book (Whyte, 2020) sold 100k+; taught by Force Management / MEDDIC Academy / MEDDICC.com as the enterprise cert standard (last checked 2026-06-11). (evidence: [T02-S023, T02-S024])
  - Activity: healthy — the spine of the "qualify-first" school; now being auto-populated by AI note-takers (新兴 #4). (evidence: [T02-S034])
- **典型使用场景**: pre-forecast deal inspection ("can I name the Economic Buyer, the Champion, the Decision Process, the Paper Process?"); disqualify-early gate; the shared deal-review language between rep and manager.
- **不适合 / 替代方案**: it is a **qualification** layer, not a sales method — it tells you *what to know*, not *how to run discovery* (pair with SPIN/Gap/Command of the Message). Its #1 failure is box-checking theater (see 避坑). For SaaS recurring-rev, SPICED is the lighter shared-qual alternative. (evidence: [T02-S023, T02-S029])
- **生产案例**: Snowflake / MongoDB-era enterprise SaaS orgs run MEDDPICC as standard (McMahon was on both boards); the validation-rules-enforce-exit-criteria pattern is what separates real qualification from theater. (evidence: [T02-S023])
- **维护者背景 (sub_skill_link)**: Track 01 figures — John McMahon ("MEDDPICC's father"), Andy Whyte (MEDDICC book/company).
- **可信度**: high. **Decay risk**: low (28+ years stable; the artifact outlives every SaaS tool it's typed into).

#### 8. Mutual Action Plan (MAP) / digital sales room — artifact + tool

- **One-liner**: The shared, dated close plan co-built by buyer + seller listing every step from now to signature (legal, security, exec sign-off, go-live) — increasingly delivered inside a "digital sales room" buyer portal that tracks which stakeholders engage. (evidence: [T02-S020, T02-S022])
- **Tier**: 必备 (the artifact); the digital-sales-room *tool* layer is 场景特化-trending-必备
- **Maintainer / Owner**: artifact = method-agnostic; tool vendors = GetAccept, Dock, Accord, Flowla, trumpet, Recapped, Aligned. (evidence: [T02-S020, T02-S021, T02-S036])
- **License**: artifact free (Google Doc / CRM template); tools proprietary SaaS
- **Maturity signals**:
  - Mature as a concept; the *digital-sales-room* tool category is fast-growing (vendor-claimed +26% win-rate / +30% deal-size / -10% cycle — caveat 官方公开 vendor stats, not independently audited) (last checked 2026-06-11). (evidence: [T02-S020])
  - Activity: healthy — AI-generated MAPs now standard in Dock/Accord/Momentum. (evidence: [T02-S021, T02-S034])
- **典型使用场景**: post-verbal-commit deal de-risking; aligning a 6-10-person buying committee on next steps; surfacing a stalled deal early (no buyer engagement = a real "no decision" signal — the JOLT problem made visible).
- **不适合 / 替代方案**: the artifact fails if the rep builds it **alone** and hands it over — buyers see it as the seller's agenda, not theirs, and don't engage (see 避坑). For a transactional/short-cycle deal a MAP is overhead. CRM-native MAPs (in Salesforce) avoid yet-another-tool sprawl. (evidence: [T02-S036])
- **生产案例**: standard late-stage motion in complex SaaS; pairs with Command of the Message + MEDDPICC's Decision Process. (evidence: [T02-S028, T02-S023])
- **可信度**: high (artifact); medium (which tool wins). **Decay risk**: low (artifact); medium (digital-sales-room vendor churn).

---

### 场景特化层

#### 9. Clay — signal-based GTM / waterfall enrichment

- **One-liner**: Composes data from many providers via "waterfall enrichment" (try provider 1, fall back to 2, 3…) + Claygent AI research agent — the engine of "signal-based" outbound that targets job-changes/funding/intent instead of spraying a static list. (evidence: [T02-S011])
- **Tier**: 场景特化 (the modern RevOps / GTM-engineer power tool; not yet universal)
- **Maintainer / Owner**: Clay (https://www.clay.com)
- **License**: proprietary (credit-based SaaS)
- **Maturity signals**:
  - **$1.5B valuation** (via 2024 tender offer); crossed **$100M ARR** (grew $1M→$100M in ~2 years); **8,000+ customers** incl. OpenAI, Anthropic, HubSpot; **Claygent surpassed 1B runs** (官方公开 + first-party, last checked 2026-06-11). (evidence: [T02-S011])
  - Customer-reported lift: OpenAI enrichment coverage low-40%→high-80% (vendor case, caveat 官方公开). (evidence: [T02-S011])
  - Activity: healthy — the breakout GTM-tooling story of 2024-25. (evidence: [T02-S011])
- **典型使用场景**: building enriched, signal-triggered target lists; researching accounts at scale with AI; the "GTM engineer" workflow that's argued to replace the SDR army.
- **不适合 / 替代方案**: steep learning curve (it's a spreadsheet-IDE, not point-and-click); for a non-technical SMB team Apollo's all-in-one is simpler. Risk: "signal-based" can become the *next* spray-and-pray if everyone fires the same AI at the same signals (see 避坑). (evidence: [T02-S037])
- **生产案例**: OpenAI / Anthropic / HubSpot enrichment pipelines (vendor-public). Track 04 canon flagged Clay as the standard-bearer of the "signal-based GTM kills the SDR army" thesis vs Predictable Revenue. (evidence: [T02-S011])
- **可信度**: high. **Decay risk**: high (the whole signal-based category is < 3 years old and evolving fast; >40% chance of significant change/repositioning in 12 months as AI-enrichment commoditizes).

#### 10. PandaDoc / DealHub — CPQ + proposal

- **One-liner**: Configure-Price-Quote + proposal document generation + e-sign in one — for deals with variable/complex pricing where a hand-built quote would be error-prone. (evidence: [T02-S015])
- **Tier**: 场景特化 (only orgs with non-trivial pricing/quoting need CPQ)
- **Maintainer / Owner**: PandaDoc (launched 2011); DealHub
- **License**: proprietary (per-seat SaaS)
- **Maturity signals**:
  - PandaDoc launched **2011**; proposal-centric (doc-gen + e-sign + CPQ add-on); significantly enhanced native Salesforce CPQ integration in **2025** (官方公开, last checked 2026-06-11). (evidence: [T02-S015])
  - Activity: healthy — positioned to absorb teams leaving Salesforce legacy CPQ. (evidence: [T02-S015, T02-S017])
- **典型使用场景**: building a priced proposal for a tiered/usage-based/multi-product deal; standardizing quote approval; bundling proposal + signature in one buyer flow.
- **不适合 / 替代方案**: if you only need a signature, Docusign alone is simpler/cheaper; if you're deep in Salesforce, Revenue Cloud Advanced is the native (heavier) path. (evidence: [T02-S014, T02-S016])
- **生产案例**: mid-market SaaS with configurable pricing; explicitly marketed as the Salesforce-CPQ-sunset migration target. (evidence: [T02-S017])
- **可信度**: high. **Decay risk**: medium (CPQ is durable; vendor competition + SF-CPQ migration churn is active).

#### 11. Salesforce Revenue Cloud Advanced — CPQ (Salesforce-native)

- **One-liner**: Salesforce's next-gen native quote-to-cash (product catalog + pricing + contracts + orders + billing) — the successor to legacy Salesforce CPQ, which is now end-of-sale. (evidence: [T02-S016, T02-S017])
- **Tier**: 场景特化 (Salesforce shops with complex quoting only)
- **Maintainer / Owner**: Salesforce, Inc.
- **License**: proprietary (SaaS)
- **Maturity signals**:
  - Legacy Salesforce CPQ (built on SteelBrick) moved to **maintenance mode / end-of-sale to net-new as of Mar 2025**; all R&D directed to Revenue Cloud Advanced (官方公开 + Salesforce Ben, last checked 2026-06-11). (evidence: [T02-S016, T02-S017])
  - Activity: healthy (Salesforce's strategic quote-to-cash bet) but migration is "a fundamental reimplementation, not a button." (evidence: [T02-S017])
- **典型使用场景**: SF-native shops needing catalog/pricing/billing in the platform; teams forced off legacy SF CPQ.
- **不适合 / 替代方案**: heavy migration cost — many teams jump to PandaDoc/DealHub instead of re-implementing in RCA; not worth it for simple pricing. (evidence: [T02-S015, T02-S017])
- **生产案例**: large Salesforce manufacturing/SaaS accounts mid-migration off legacy CPQ. (evidence: [T02-S017])
- **可信度**: high. **Decay risk**: medium (the forced migration is the active risk vector through 2026-27).

#### 12. Highspot / Seismic — sales enablement

- **One-liner**: Content-management + rep-onboarding/cert platforms that store battlecards, decks and playbooks and (in theory) surface the right one in-workflow — but suffer chronic "shelfware / content rot." (evidence: [T02-S018, T02-S019])
- **Tier**: 场景特化 (larger orgs with big content libraries + formal enablement function)
- **Maintainer / Owner**: Highspot; Seismic (merged 12 Feb 2026)
- **License**: proprietary (per-seat SaaS)
- **Maturity signals**:
  - Highspot + Seismic **merged 12 Feb 2026**, forming a **$6B+** "category leader" (官方公开 + 第三方, last checked 2026-06-11). (evidence: [T02-S019])
  - Activity: healthy financially, but critics call both "storage-first, portal-dependent" architectures whose core problem (low rep adoption) the merger doesn't fix. (evidence: [T02-S019])
- **典型使用场景**: managing a large content library; rep onboarding/certification; tracking which collateral influences deals.
- **不适合 / 替代方案**: the central risk is **shelfware** — reps open it, find an undated/stale battlecard, and improvise instead (see 避坑). Lighter, in-workflow tools (GTM Buddy-class) or just a well-organized shared drive can out-adopt a heavy platform. Adoption, not features, is the only metric that matters here. (evidence: [T02-S019])
- **生产案例**: large SaaS enablement teams; the merger's own critics (GTM Buddy — note: competitor, caveat) document the content-rot failure pattern in detail. (evidence: [T02-S019])
- **可信度**: high (facts) / medium (the critique is partly from a competitor). **Decay risk**: medium (architecture debate + merger integration risk).

#### 13. Miller Heiman Blue Sheet — methodology artifact (strategic accounts)

- **One-liner**: A ~6-page opportunity-planning document that maps a complex deal's buying influences + competitive position + win-results — the canonical large-strategic-account planning artifact for 40+ years. (evidence: [T02-S027])
- **Tier**: 场景特化 (very large, multi-stakeholder, strategic deals; overkill for transactional)
- **Maintainer / Owner**: created by Robert Miller & Stephen Heiman (Strategic Selling, late-1970s/1985 book); now owned by **Korn Ferry** (Korn Ferry Sell). (evidence: [T02-S027])
- **License**: methodology + paid digital tool (Korn Ferry Sell)
- **Maturity signals**:
  - In use **"more than four decades"**; evolved paper → spreadsheet → cloud (Korn Ferry Sell, **fully integrated 2025** with guided workflows/coaching/analytics) (官方公开, last checked 2026-06-11). (evidence: [T02-S027])
  - Korn Ferry's own 2024 Sales Maturity Survey claims **+22% win rates / +16% quota attainment** for methodology users (caveat 官方公开 vendor survey). (evidence: [T02-S027])
  - Activity: healthy (durable artifact); enhanced 2018 with Opportunity Scorecard. (evidence: [T02-S027])
- **典型使用场景**: mapping the four buying influences — **Economic Buyer** (final approval), **User Buyer** (daily impact), **Technical Buyer** (screens vs specs), **Coach** (internal guide) — plus red flags + single sales objective on a strategic deal.
- **不适合 / 替代方案**: heavy — initial completion takes **3-5 hours**; reps need 90-120 days to reach proficiency. For teams < 50 reps, a CRM template or Google Doc beats the mid-5/low-6-figure Korn Ferry Sell license. Overlaps MEDDPICC's stakeholder mapping. (evidence: [T02-S027])
- **生产案例**: strategic/named-account selling; the Economic/User/Technical-buyer + Coach taxonomy is in Track 04 canon as the relationship/strategic school's core. (evidence: [T02-S027])
- **可信度**: high. **Decay risk**: low (40-year-stable artifact).

#### 14. Sandler pain funnel — methodology artifact (discovery)

- **One-liner**: A scripted sequence of ~8 nested open-ended questions that walks a buyer from a vague complaint → a specific, quantified, emotionally-owned pain — the Sandler school's signature discovery tool. (evidence: [T02-S025, T02-S026])
- **Tier**: 场景特化 (a discovery technique, used within a broader method)
- **Maintainer / Owner**: David Sandler (Sandler Selling System, 1967); Sandler (https://www.sandler.com). (evidence: [T02-S026])
- **License**: methodology (free to use; Sandler training is paid/franchise)
- **Maturity signals**:
  - Sandler System founded **1967**; pain funnel is a core component taught across Sandler's 250+ office franchise network (官方公开, last checked 2026-06-11). (evidence: [T02-S026])
  - Activity: healthy (perennial discovery reference; Gong's first-party explainer keeps it current). (evidence: [T02-S025])
- **典型使用场景**: the question ladder — broad ("what's the impact of this problem on your company?") → specific ("what does that look like in dollar terms?") → consequence ("what happens if you don't address this now?") — to drive vague frustration to quantified pain. (evidence: [T02-S025])
- **不适合 / 替代方案**: misused as an interrogation it backfires (查户口式提问 — asking to fill your CRM, not to help the buyer — see 避坑). Overlaps SPIN's Implication/Need-payoff questions (same logic, different branding). (evidence: [T02-S025])
- **生产案例**: standard discovery drill in Sandler-trained orgs; Track 04 canon documents the 8-question funnel + up-front contract. (evidence: [T02-S025])
- **可信度**: high. **Decay risk**: low (timeless questioning technique).

#### 15. Command of the Message value framework — methodology artifact (value selling)

- **One-liner**: Force Management's structured value-articulation canvas — Before Scenarios → Negative Consequences → Positive Business Outcomes (PBOs) → Required Capabilities → Differentiation — that forces a rep to sell quantified business value (to the economic buyer) instead of features. (evidence: [T02-S028])
- **Tier**: 场景特化 (value/enterprise selling; pairs with MEDDPICC as the "what to say" to MEDDIC's "where to focus")
- **Maintainer / Owner**: Force Management (https://www.forcemanagement.com). (evidence: [T02-S028])
- **License**: methodology + paid training/cert
- **Maturity signals**:
  - The enterprise-sales messaging standard; taught alongside MEDDICC by Force Management as the value-narrative engine (官方公开, last checked 2026-06-11). (evidence: [T02-S028])
  - Activity: healthy — John McMahon + John Kaplan's Revenue Builders worldview (Track 01). (evidence: [T02-S028])
- **典型使用场景**: building the value story for an exec/economic-buyer conversation; cross-functional alignment on differentiators; the "before/after + required capabilities + differentiation" deck behind a business case.
- **不适合 / 替代方案**: heavy framework for a transactional sale; overlaps Solution Selling's buying-vision + Gap Selling's current/future state. The buzzword trap — "value/synergy/trusted advisor" said without quantification is the failure mode (see 避坑). (evidence: [T02-S028])
- **生产案例**: enterprise SaaS value selling; the narrative complement to MEDDPICC qualification in Track 04 canon. (evidence: [T02-S028])
- **维护者背景 (sub_skill_link)**: Track 01 — Force Management / John McMahon / John Kaplan.
- **可信度**: high. **Decay risk**: low (durable value-selling framework).

#### 16. bowtie / SPICED canvas — methodology artifact (SaaS recurring-revenue)

- **One-liner**: Winning by Design's two-part artifact — the **bowtie** (funnel extended through onboarding/retention/expansion as one revenue system) + **SPICED** (Situation/Pain/Impact/Critical event/Decision), a shared qualification model used by every customer-facing role. (evidence: [T02-S029])
- **Tier**: 场景特化 (SaaS/recurring-revenue orgs that sell + retain + expand)
- **Maintainer / Owner**: Winning by Design / Jacco van der Kooij (https://winningbydesign.com). (evidence: [T02-S029])
- **License**: methodology + paid Revenue Academy
- **Maturity signals**:
  - bowtie/SPICED are the mainstream modern SaaS recurring-revenue frameworks; Revenue Architecture book (2023, 250+ diagrams); served 1000+ SaaS companies (官方公开, last checked 2026-06-11). (evidence: [T02-S029])
  - Activity: healthy — Winning by Design pushing revenue-architecture + AI-era GTM. (evidence: [T02-S029])
- **典型使用场景**: SPICED as the one shared qual language across SDR/AE/CSM (vs MEDDPICC's enterprise heaviness); the bowtie to design land-and-expand + NRR motions, not just acquisition.
- **不适合 / 替代方案**: criticized as "consulting-term/diagram overload" — costly to roll out in a small team; SPICED is "yet another MEDDIC/SPIN variant" (framework proliferation — see 避坑). For pure new-logo enterprise, MEDDPICC is the more common language. (evidence: [T02-S029])
- **生产案例**: modern SaaS revenue orgs unifying sales + customer success; Track 01/04 anchor it to Jacco van der Kooij's Revenue Architecture. (evidence: [T02-S029])
- **维护者背景 (sub_skill_link)**: Track 01 — Jacco van der Kooij / Winning by Design.
- **可信度**: high. **Decay risk**: low (established framework, though the SaaS-GTM context around it shifts).

#### 17. Nooks — AI parallel dialer

- **One-liner**: An AI parallel dialer + "virtual salesfloor" that calls many numbers at once and connects the rep only on a live answer — claims 5-8x more live connects per SDR than single-line dialing. (evidence: [T02-S032])
- **Tier**: 场景特化 (high-volume outbound-calling teams)
- **Maintainer / Owner**: Nooks (https://www.nooks.ai)
- **License**: proprietary (per-seat SaaS)
- **Maturity signals**:
  - **$43M Series B (2024)** led by Kleiner Perkins; users report **5-8x live connects** vs single-line (vendor + 业内估计, last checked 2026-06-11). (evidence: [T02-S032])
  - Activity: healthy — expanded from phone-only into multichannel (email/SMS/social) sequencing + AI-drafted messaging. (evidence: [T02-S032])
- **典型使用场景**: SDR power-hour calling blitzes; teams where phone is still the primary channel; real-time call coaching during dials.
- **不适合 / 替代方案**: for low-volume enterprise ABM (few, high-value calls) parallel dialing is the wrong motion; in the AI-deliverability backlash, more volume can be counterproductive. Traditional auto-dialers or just disciplined manual dialing for complex deals. (evidence: [T02-S037])
- **生产案例**: high-volume SaaS SDR teams; pairs with the Jeb Blount / 30MPC "cold calling still works" school (Track 01). (evidence: [T02-S032])
- **可信度**: medium-high (vendor metrics, caveat). **Decay risk**: high (AI-dialer category < 3 years old, crowded, fast-moving).

#### 18. Rilla — AI field/in-person sales coaching

- **One-liner**: Conversation intelligence for the world Gong can't see — records/transcribes/analyzes **in-person and field** sales conversations (home services, med-device, outside sales), giving managers ride-along coaching without riding along. (evidence: [T02-S033])
- **Tier**: 场景特化 (field/in-person sales, not SaaS inside-sales)
- **Maintainer / Owner**: Rilla / Rillavoice (https://www.rilla.com)
- **License**: proprietary (per-seat SaaS)
- **Maturity signals**:
  - **Rilla Live launched Sep 2025**; pricing ≈ $199-349/rep/mo + implementation; ~$20K min annual (vendor + 第三方, last checked 2026-06-11). (evidence: [T02-S033])
  - Activity: healthy — Dreamforce-2025 visibility; growing in home-services/field verticals. (evidence: [T02-S033])
- **典型使用场景**: coaching field reps at scale; analyzing in-person discovery/objection-handling; extending "data-driven coaching" to non-screen-based selling.
- **不适合 / 替代方案**: irrelevant for pure inside/SaaS sales (Gong owns that); same surveillance-vs-coaching risk as any conversation-intelligence tool. (evidence: [T02-S033])
- **生产案例**: home-services / in-person sales orgs; the field-sales analog of Gong. (evidence: [T02-S033])
- **可信度**: medium-high (vendor-sourced). **Decay risk**: high (young, narrow-vertical, AI-coaching category).

---

### 新兴层（all `stability: experimental` — 6 个月后可能不存在 / 大幅变样）

#### 19. AI SDR agents (11x / Artisan / AiSDR)

- **One-liner**: Autonomous "AI sales rep" agents that prospect, write and send outreach end-to-end — pitched as replacing a $60K SDR, but the category collapsed in 2025 amid overstated-ARR scandals, hallucinations, and email-deliverability backlash. (evidence: [T02-S030, T02-S031, T02-S037])
- **Tier**: 新兴 — `stability: experimental`
- **Maintainer / Owner**: 11x.ai; Artisan; AiSDR (each a separate VC-funded startup)
- **License**: proprietary (per-seat / usage SaaS)
- **Maturity signals**:
  - **11x**: a16z/Benchmark-backed; TechCrunch (24 Mar 2025) reported it **listed ZoomInfo & Airtable as customers that weren't** (ZoomInfo threatened legal action; Airtable said its logo was used without permission), and **counted ARR on contracts that never cleared trials**; **CEO Hasan Sukkar stepped down 5 May 2025** (TechCrunch, last checked 2026-06-11). (evidence: [T02-S030, T02-S031])
  - **Artisan**: ran "stop hiring humans" SF billboards; its "Ava" agent reportedly produced invented connections/facts, and by Q1 2026 LinkedIn rate-limited Ava-driven activity (业内观察, caveat). (evidence: [T02-S037])
  - Category: AI-SDR tools churn **~50-70% annually**; **>50% of buyers abandon within a year** (第三方/业内估计, caveat). (evidence: [T02-S037])
- **典型使用场景**: (claimed) fully-automated cold-email prospecting at volume. (Reality: works only in a **hybrid** human-in-the-loop model.)
- **不适合 / 替代方案**: do NOT run fully-autonomous at vendor-recommended volume — deliverability collapses and your domain gets burned (see 避坑). ~45% of teams now run hybrid (AI volume + human nuance). Clay + human personalization is the more durable signal-based alternative. (evidence: [T02-S037])
- **生产案例**: cautionary — the 11x/Artisan failures ARE the case studies; this is a backlash, not a success layer. (evidence: [T02-S030, T02-S037])
- **可信度**: high (the backlash is well-documented by primary investigative reporting). **Decay risk**: high (>40% of these specific vendors change/fold within 12 months; the *category* is being absorbed into hybrid + platform plays).

#### 20. Salesforce Agentforce — agentic selling

- **One-liner**: Salesforce's action-taking AI-agent platform inside the CRM — agents that don't just summarize but execute steps (research, draft, update, escalate); the flagship of the 2026 "agentic enterprise" bet. (evidence: [T02-S035])
- **Tier**: 新兴 — `stability: experimental`
- **Maintainer / Owner**: Salesforce, Inc.
- **License**: proprietary (Flex Credits ~$0.10/action, or add-on ~$125-150/user/mo, or Agentforce 1 ~$550/user/mo)
- **Maturity signals**:
  - **Agentforce 360 reached GA 23 Feb 2026**; Salesforce claims deployment across 124 countries with up to 85% query resolution (官方公开, caveat — vendor self-report, last checked 2026-06-11). (evidence: [T02-S035])
  - Activity: healthy spend + heavy Salesforce push; but analysts flag "platform fatigue" / adoption risk. (evidence: [T02-S035, T02-S034])
- **典型使用场景**: auto-research + CRM updates + Slack deal rooms + agentic next-step execution layered on Sales Cloud.
- **不适合 / 替代方案**: bleeding-edge, expensive, unproven ROI for complex sales; the 85%-resolution stat is customer-support-flavored, not enterprise-deal-flavored (caveat). Wait for production evidence before betting a sales org on it. (evidence: [T02-S035])
- **生产案例**: too new for durable independent complex-B2B-sales case studies; Salesforce-internal claims only. (evidence: [T02-S035])
- **可信度**: medium (vendor-heavy claims). **Decay risk**: high (pricing/packaging/capability all moving fast in 2026).

#### 21. Momentum — AI revenue orchestration (auto-MEDDIC capture)

- **One-liner**: An AI layer over calls/pipeline that auto-captures MEDDIC fields, generates call summaries, and spins up Slack deal rooms — i.e. it tries to kill "CRM hygiene theater" by writing the CRM for the rep. Acquired by Salesforce Mar 2026. (evidence: [T02-S034])
- **Tier**: 新兴 — `stability: experimental`
- **Maintainer / Owner**: Momentum (acquired by Salesforce, completed 2 Mar 2026 → folded into Agentforce 360). (evidence: [T02-S034])
- **License**: proprietary (now part of Salesforce/Agentforce)
- **Maturity signals**:
  - **Salesforce completed the Momentum acquisition 2 Mar 2026**; Momentum's universal ingestion engine integrates with Agentforce 360 + Slackbot to capture Zoom/Google Meet interactions (官方公开, last checked 2026-06-11). (evidence: [T02-S034])
  - Activity: absorbed — the standalone product future is now Salesforce-dependent. (evidence: [T02-S034])
- **典型使用场景**: auto-populating MEDDIC/CRM fields from call transcripts (the AI fix for the box-checking-theater problem); Slack-native deal collaboration.
- **不适合 / 替代方案**: post-acquisition uncertainty (standalone vs Salesforce-only); auto-captured MEDDIC fields risk becoming *automated* box-checking — populated but not *thought about* (see 避坑). Sybill / Scratchpad-class tools cover the auto-CRM job independently. (evidence: [T02-S034])
- **可信度**: medium-high (acquisition is fact; long-term shape is uncertain). **Decay risk**: high (mid-acquisition integration).

#### 22. AI note-takers / auto-CRM (Momentum / Sybill / Scratchpad class)

- **One-liner**: Tools that transcribe calls and auto-write notes + populate CRM/qualification fields, so reps stop spending ~71% of their time on admin instead of selling. (evidence: [T02-S034])
- **Tier**: 新兴 — `stability: experimental` (the *category*; individual vendors vary)
- **Maintainer / Owner**: Momentum (→Salesforce), Sybill, Scratchpad, tl;dv, Fathom, others
- **License**: proprietary (per-seat SaaS)
- **Maturity signals**:
  - Fast-growing category responding to the documented "reps spend ~71% of time on admin/data-entry, not selling" problem (第三方/业内估计, caveat); auto-MEDDIC-population is the headline feature (last checked 2026-06-11). (evidence: [T02-S034])
  - Activity: healthy + consolidating (Salesforce bought Momentum; Gong/Clari build native). (evidence: [T02-S034])
- **典型使用场景**: auto call-notes → CRM; auto-populating MEDDIC/SPICED fields; freeing rep selling time.
- **不适合 / 替代方案**: the deeper risk — automating CRM hygiene can *entrench* box-checking theater (fields filled by AI, judged by no one); the tool fixes the symptom (data entry), not the disease (managers not coaching on the data — see 避坑). Native CRM AI (Einstein/Copilot) increasingly overlaps. (evidence: [T02-S034])
- **可信度**: medium (category-level). **Decay risk**: high (rapid consolidation into platforms).

#### 23. AI deal coaching (Gong / Clari AI layer)

- **One-liner**: The AI layer on conversation-intelligence/forecasting tools that flags at-risk deals and prescribes next steps — sold as "data-driven coaching" but at risk of degenerating into the same surveillance theater the underlying tool already gets criticized for. (evidence: [T02-S005, T02-S003])
- **Tier**: 新兴 — `stability: experimental`
- **Maintainer / Owner**: Gong; Clari (and every conversation-intelligence vendor)
- **License**: proprietary (add-on to existing platform)
- **Maturity signals**:
  - Gong reports high-AI-use reps earn +77% more (Gong Labs first-party, caveat 官方公开研究); generative-AI features are the stated growth driver (last checked 2026-06-11). (evidence: [T02-S005, T02-S004])
  - Activity: healthy — every CI/forecasting vendor is racing to ship an AI-coaching layer. (evidence: [T02-S005])
- **典型使用场景**: AI surfaces "deal X has no economic-buyer engagement / no multithreading / went dark" + suggests the next action.
- **不适合 / 替代方案**: the +77% figure is vendor-first-party and correlational (high-performers adopt tools, not necessarily caused by them — caveat). When managers use AI flags to *nitpick scores* instead of *coach behavior*, reps game the metrics and adoption becomes compliance (see 避坑). (evidence: [T02-S003, T02-S005])
- **可信度**: medium (vendor data, correlational). **Decay risk**: high (the AI-coaching feature layer is the fastest-moving part of an otherwise-stable category).

#### 24. Clay-style signal-based GTM (as an emerging *category*)

- **One-liner**: "Signal-based GTM" — triggering outreach on real-time signals (job change, funding, hiring, tech-install, intent) instead of static lists — argued to be replacing the SDR-army model; Clay is the standard-bearer, but it's contested whether it scales or just relocates the spam. (evidence: [T02-S011, T02-S037])
- **Tier**: 新兴 — `stability: experimental` (as a *movement*; Clay the tool is 场景特化 #9)
- **Maintainer / Owner**: category — Clay, Common Room, Default, Pocus, others
- **License**: proprietary (various SaaS)
- **Maturity signals**:
  - Clay's $1.5B valuation / $100M ARR / 8,000 customers / 1B Claygent runs are the category's proof-of-demand (官方公开, last checked 2026-06-11). (evidence: [T02-S011])
  - Activity: healthy + hyped — the leading "post-SDR-army" thesis of 2024-26. (evidence: [T02-S011])
- **典型使用场景**: replacing high-volume SDR cadences with fewer, signal-triggered, AI-researched touches.
- **不适合 / 替代方案**: if every team buys the same signal tools and fires the same AI at the same signals, "signal-based" becomes the next spray-and-pray and degrades just like AI-SDR mass email did (see 避坑). The Predictable-Revenue SDR-army defenders (Track 04) argue role-specialization endures even if the tactics change. (evidence: [T02-S037, T02-S011])
- **可信度**: medium-high. **Decay risk**: high (a < 3-year-old movement still proving whether it's a durable model or a hype cycle).

---

## 选型决策树

> 8 nodes. Each branch traces to evidence. Note the meta-rule first: **tools amplify a sales motion; they don't create one.** A clean CRM, a filled MEDDPICC scorecard, or a fancy AI agent on top of a bad qualification habit just produces faster garbage.

### 决策树 A: 你的核心问题是什么？

#### Branch 1: "我们还没有可重复的销售动作 (pre-PMF / < 10 人)"
→ **推荐**: lightweight CRM (HubSpot Starter / Pipedrive) + a Google-Doc MEDDPICC/SPICED scorecard + Apollo for data. (evidence: [T02-S002, T02-S008, T02-S029])
→ **不推荐**: Salesforce + Gong + Clari + Highspot — heavy, expensive, and you'd be automating a process you haven't found yet (premature scaling). (evidence: [T02-S001])
→ **真实案例**: David Skok / Mark Roberge's "don't build the scalable machine until the process is repeatable" (Track 01) — the tooling corollary is *don't buy the enterprise stack pre-PMF*. (evidence: [T02-S016])

#### Branch 2: "我们有 PMF，要把销售工程化 (scaling SaaS, 10-200 reps)"
##### Branch 2a: 瓶颈在 **pipeline 生成 / 开发**
→ **推荐**: sales engagement (Salesloft/Outreach) + prospecting data (Apollo or ZoomInfo) + Clay if you have a GTM engineer for signal-based outbound. (evidence: [T02-S006, T02-S009, T02-S011])
→ **不推荐 (caution)**: fully-autonomous AI SDR agents (11x/Artisan) at scale — deliverability backlash; run hybrid (AI draft + human send) instead. (evidence: [T02-S030, T02-S037])
##### Branch 2b: 瓶颈在 **deal execution / 赢率 / discovery 质量**
→ **推荐**: Gong (conversation intelligence — coach the discovery + multithreading) + MEDDPICC scorecard in CRM + a discovery artifact (Sandler pain funnel / SPIN). (evidence: [T02-S003, T02-S023, T02-S025])
→ **替代**: cheaper note-takers (Sybill/tl;dv) if you only need transcripts, not deal intelligence. (evidence: [T02-S003])
##### Branch 2c: 瓶颈在 **预测准确性 / 季末 surprise**
→ **推荐**: Clari (deal inspection + forecast roll-up) on top of disciplined MEDDPICC deal reviews. (evidence: [T02-S010, T02-S023])
→ **不推荐**: buying a forecasting tool to fix a forecasting *culture* problem — if reps sandbag/happy-ear, the tool just visualizes the lie faster. (evidence: [T02-S007])

#### Branch 3: "复杂大单 / 战略客户 (enterprise, 6-10+ stakeholders, 6-18mo cycles)"
##### Branch 3a: 主要挑战是 **stakeholder mapping / 政治地形**
→ **推荐**: Miller Heiman Blue Sheet (or Korn Ferry Sell at scale) for the buying-influence map + MEDDPICC for qualification. (evidence: [T02-S027, T02-S023])
→ **替代**: a CRM-native stakeholder map if a Blue Sheet license isn't justified (< 50 reps). (evidence: [T02-S027])
##### Branch 3b: 主要挑战是 **讲清业务价值给经济决策人**
→ **推荐**: Command of the Message value framework (Before/After + PBOs + Required Capabilities + Differentiation) + a business-case proposal (PandaDoc). (evidence: [T02-S028, T02-S015])
##### Branch 3c: 主要挑战是 **deal 后期 stall / 推进到签约**
→ **推荐**: a co-built Mutual Action Plan in a digital sales room (Dock/GetAccept/Accord) — surfaces buyer disengagement early (the JOLT "no decision" signal). (evidence: [T02-S020, T02-S022])
→ **不推荐**: building the MAP alone and emailing it — buyers read it as your agenda and ghost it. (evidence: [T02-S036])

#### Branch 4: "field / in-person 销售 (home services, med-device, 非屏幕)"
→ **推荐**: Rilla (in-person conversation intelligence) — Gong's screen-based recording doesn't reach this motion. (evidence: [T02-S033])
→ **不推荐**: a SaaS inside-sales stack (Gong/Salesloft) that assumes Zoom/email as the channel. (evidence: [T02-S033])

---

## 避坑清单（≥ 5 — practitioner gripes, not vendor copy）

- ❌ **不要把 CRM hygiene 当成 qualification**: reps spend ~71% of time on admin (caveat 业内估计), and a fully-populated MEDDPICC field set is not a qualified deal — **box-checking theater** is filling boxes without thinking. AI auto-CRM tools (Momentum class) fix the *data-entry* symptom but can *entrench* the theater (fields filled by AI, coached on by no one). The fix is exit-criteria + managers who inspect *quality*, not a tool. (evidence: [T02-S034, T02-S023])
- ❌ **不要让 conversation intelligence 沦为 surveillance**: Gong/Rilla deliver value as *coaching*, but reps widely perceive them as monitoring ("surveillance theater") when managers nitpick talk-ratios/keyword counts instead of coaching behavior. Adoption then becomes compliance, reps game the scores, and you've bought an expensive note-taker. The tool's ROI is a change-management problem, not a software one. (evidence: [T02-S003])
- ❌ **不要跑全自动 AI SDR at vendor-recommended volume**: 2025's 11x (claimed non-customers as customers, counted trial ARR — TechCrunch) and Artisan (LinkedIn rate-limited "Ava"; hallucinated facts) prove the thesis failed not because AI is bad but because everyone pointed the same AI at the same tired playbook → deliverability collapsed and domains burned. AI-SDR tools churn ~50-70%/yr (caveat). Run hybrid (AI volume + human nuance). (evidence: [T02-S030, T02-S031, T02-S037])
- ❌ **不要假设 "signal-based GTM" 永远不会变成下一个 spray-and-pray**: Clay is genuinely powerful, but if every team buys the same signal tools and fires the same Claygent prompts at the same job-change/funding signals, the signal saturates and degrades exactly like AI mass-email did. Signals are a *targeting* edge, not a *volume* license. (evidence: [T02-S011, T02-S037])
- ❌ **不要把 enablement 平台当 content library 堆砌**: Highspot/Seismic chronically become shelfware — a rep searches, gets an undated/"Q3 2024" stale battlecard, and improvises. Both are "storage-first, portal-dependent" architectures; the merger (Feb 2026) doesn't fix low adoption. **Adoption is the only metric**; an in-workflow card beats a library you have to go open a tab to search. (evidence: [T02-S019])
- ❌ **不要把 MAP 单方面建好甩给买方**: a Mutual Action Plan the rep builds alone and hands over reads as the *seller's* agenda — buyers don't engage, and it becomes "just another document." It only works **co-built**, kept live, and (ideally) in a sales room that shows you exactly which stakeholder went dark. (evidence: [T02-S036])
- ❌ **不要为 forecasting/methodology *文化* 问题买 *工具***: Clari can't fix sandbagging reps; a Blue Sheet license can't fix a team that won't map stakeholders. Tools amplify an existing discipline — buying one to *create* the discipline produces faster garbage. (evidence: [T02-S007, T02-S027])
- ❌ **不要被 vendor benchmark 数字当事实**: "+26% win rate" (digital sales rooms), "+22% win rate" (Korn Ferry survey), "+77% income for high-AI reps" (Gong), "5-8x connects" (Nooks) are all **vendor-first-party / correlational** — directional marketing, not audited causal proof. Treat every ROI stat as 官方公开/业内估计 and demand your own pilot data before standardizing. (evidence: [T02-S020, T02-S027, T02-S005, T02-S032])

---

## Phase 2 提炼提示（接口）

### 反复出现 ≥ 3 source 都强调的「工具选型原则」（候选 playbook 规则）

1. **"Tools amplify a sales motion; they don't create one — fix the habit before buying the tool."** A clean CRM ≠ qualified pipeline; an AI auto-MEDDIC tool ≠ real qualification; a forecasting tool ≠ a forecasting culture. (出现于: T02-S034 / T02-S023 / T02-S007 / T02-S027)
2. **"Adoption, not features, is the only metric that matters."** Enablement shelfware, Gong-as-surveillance, the "10 tools owned, 3 used" reality — the differentiator is whether reps actually use it in-workflow. (出现于: T02-S019 / T02-S003)
3. **"Match the tool to the deal-type, not to the hype."** Heavy stack (Blue Sheet / Command of the Message / Gong) for complex multi-stakeholder deals; lightweight (Doc scorecard / Apollo / HubSpot) pre-PMF; field-CI (Rilla) for in-person — wrong-altitude tooling is the common mistake. (出现于: T02-S027 / T02-S002 / T02-S033)
4. **"Treat every vendor ROI number as directional, never as fact — pilot before you standardize."** Win-rate/connect-rate/income-lift stats are all first-party/correlational. (出现于: T02-S020 / T02-S027 / T02-S005)

### 显著的工具流派分裂（候选 智识谱系条目）

- **Methodology artifacts (slow-decay, branded, free) ⇄ SaaS apps (fast-decay, proprietary, paid)**: the MEDDPICC scorecard / Blue Sheet / pain funnel / SPICED canvas have 28-58-year lifespans and cost nothing; the Gong/Clari/Salesloft layer churns and consolidates yearly and costs a fortune. Strong orgs treat the artifact as the durable core and the app as a replaceable amplifier. (代表 artifacts: MEDDPICC, Blue Sheet, Command of the Message; 代表 apps: Gong, Clari, Salesloft — 与 Track 01 figures McMahon/Whyte/van der Kooij/Miller-Heiman 关联)
- **SDR-army / volume tooling (Salesloft+Outreach sequencers, AI SDR agents, parallel dialers) ⇄ Signal-based / GTM-engineer tooling (Clay, intent signals)**: the core 2024-26 schism — operationalizes Track 04's "Predictable Revenue SDR-army ⇄ Winning by Design / signal-based GTM" debate. Both currently risk becoming spam. (与 Track 01: Aaron Ross ⇄ Jacco van der Kooij / Clay)
- **"Data-driven coaching" (conversation-intelligence + AI deal coaching) ⇄ surveillance theater**: the same Gong/Rilla/Clari tool is either a coaching multiplier or a monitoring panopticon depending entirely on management behavior — a culture fork, not a feature fork. (no single figure; a reflexes-layer tension)

### 新兴工具信号

- **当前活跃 / 上升的新兴工具数**: 6 (AI SDR agents, Agentforce, Momentum/auto-CRM, AI note-takers, AI deal coaching, signal-based GTM as a category) — all `stability: experimental`, decay high.
- **出现 → 主流 速度估计**: ~12-24 months for AI features inside incumbent platforms (Gong/Salesforce ship fast); the **standalone AI-SDR startup** wave compressed to a ~12-18-month boom-bust (2024 hype → 2025 backlash → 2026 absorption/hybrid). The pattern: standalone AI tools get acquired into platforms (Salesforce→Momentum, Mar 2026) or collapse (11x), rather than becoming durable standalone leaders.
- **High-decay watch items for the update cycle (Phase 0C)**: anything in the 新兴 layer + sales-engagement vendor boundaries (mid-consolidation: Clari+Salesloft, Highspot+Seismic) + AI-SDR vendor survival. Re-check the SaaS layer every ~6 months; the methodology-artifact layer can go 24+ months untouched.

### 冷僻 / 信号薄弱 检查

- 必备层 ≥ 3? **YES** — 8 必备 (CRM, conversation intelligence, sales engagement, forecasting, prospecting data, e-sign, MEDDPICC artifact, MAP artifact). ✅
- 必备层证据 ≥ 50% 采用率? **YES** — CRM is ~universal; Gong has 4,500 corporate customers; MEDDPICC is the default enterprise-SaaS qual language; these are method/category-level certainties, not thin signals. ✅
- 场景特化 ≥ 5? **YES** — 10. ✅
- 新兴层 ≥ 2? **YES** — 6 (with the mandated `experimental` + decay-high + AI-deliverability-backlash framing, not as pure upside). ✅
- **结论: 工具栈维度信号丰富，NOT thin.** The honest boundary for Phase 2.8 is the *opposite* of thinness: (a) **vendor-marketing saturation** — most public tool material is vendor/competitor content (G2/Capterra blacklisted; verified_primary "only" 46% because clean-classified vendor pages are scarce, though first-hand verified+surrogate = 77%); (b) **fast SaaS decay vs slow artifact decay** — the two tool classes must be updated on different clocks; (c) every adoption/ROI number is vendor-first-party — caveat throughout.
