# Food & Beverage × Sales Playbook

## Overview

Sales organizations within Food & Beverage (F&B) companies operate in one of the most complex, relationship-driven commercial environments in any industry. Whether the company is a CPG manufacturer selling through distributors and brokers, a foodservice supplier managing direct-to-operator accounts, or a beverage brand navigating on-premise and off-premise channels, the sales team must juggle multi-tier distribution networks, seasonal demand cycles, trade promotion budgets, and razor-thin margins. A mid-market F&B company might have 50–200 sales reps organized by channel (retail, foodservice, e-commerce, convenience), geography, and key account tier — all coordinated through a patchwork of CRM, trade management, and ERP systems.

The regulatory and competitive landscape adds further complexity. F&B sales teams must track product certifications (organic, non-GMO, kosher, halal), navigate retailer compliance requirements (EDI, vendor scorecards, OTIF penalties), and respond to rapidly shifting consumer trends (plant-based, functional beverages, clean label). Promotions are the lifeblood of F&B sales — trade spend often represents 15–25% of gross revenue — yet most organizations lack visibility into promotion ROI, deduction management, and post-promotion analytics. Sales leaders are under pressure to grow volume while protecting margin, all while their reps spend too much time on manual order entry, broker coordination, and retailer portal management instead of selling.

The SE opportunity here is enormous. F&B companies are drowning in spreadsheets for trade promotion planning, broker scorecards, and pipeline tracking. Most have outgrown their CRM (or never adopted one properly) and are looking for a platform that can unify account management, promotion execution, and sales analytics — especially one that can incorporate AI to automate the tedious administrative burden that keeps reps out of the field.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | F&B sales teams rely heavily on broker networks and sales coordinators for order management, deduction tracking, and promotion execution — AI agents can absorb much of this work |
| 2 | Scale Impact Without Overhead | High | Growing into new channels (DTC, e-commerce, foodservice) without proportionally scaling the sales team is a top-of-mind challenge for F&B leaders |
| 3 | Consolidate Tech Stack with AI | Medium-High | F&B sales orgs typically run 4-7 disconnected tools (CRM, trade promo management, order management, broker portals, retailer scorecards) that can collapse into monday.com |

## Prioritized Use Cases

---

### Use Case 1: Trade Promotion Planning & ROI Tracking

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Trade spend is the second-largest line item on most F&B P&Ls (after COGS), yet 60-70% of trade promotions fail to break even. Sales teams plan promotions in disconnected spreadsheets, submit them through clunky TPM systems, and rarely close the loop on actual vs. planned lift. Deductions pile up unreconciled, and finance constantly battles sales over accruals. The average F&B company loses 2-5% of gross revenue to unresolved deductions and poorly targeted promotions.

#### The Solution
monday.com Work Management becomes the central trade promotion planning hub. Each promotion is an item with structured columns: retailer/distributor (dropdown), promotion type (BOGO, TPR, display, ad feature — dropdown), planned spend (numbers), expected lift % (numbers), start/end dates, status (Submitted → Approved → Executing → Reconciled), and assigned broker/rep (people). Timeline view shows the full promotional calendar across all accounts. Dashboards aggregate planned vs. actual spend by retailer, brand, and promotion type. monday.com CRM links each promotion to the account record for full relationship context.

#### The Outcome
30-40% reduction in time spent on promotion planning cycles. Full visibility into trade spend allocation across channels. Post-promotion ROI analysis available within days instead of quarters. 15-20% improvement in promotion effectiveness through data-driven planning.

#### Discovery Questions
- "How do your sales teams currently plan and track trade promotions — is it centralized or does each region/broker manage their own?"
- "What's your current process for reconciling trade deductions against planned promotions?"
- "Do you have visibility into promotion ROI by retailer, brand, or promotion type — and how long does it take to get that data?"
- "How much of your trade spend budget is managed through brokers vs. direct sales?"
- "When a promotion underperforms, how quickly can your team identify it and adjust?"

#### Industry Context
Trade Promotion Management (TPM) is a $7B+ software category, but most mid-market F&B companies can't afford or don't need enterprise TPM systems like Exceedra or AFS. They end up in spreadsheet hell. Key terminology: TPR (Temporary Price Reduction), BOGO (Buy One Get One), scan-back, bill-back, off-invoice, MCB (Manufacturer Chargeback), OTIF (On Time In Full). Promotions are typically planned quarterly with monthly adjustments. Brokers often manage execution but report inconsistently.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Trade Promotion Management workspace in monday.com. Create a board called 'Trade Promotion Calendar' with these columns: Promotion Name (text), Retailer/Distributor (dropdown: Kroger, Walmart, Costco, Sysco, US Foods, UNFI, KeHE, Custom), Channel (dropdown: Retail, Foodservice, E-commerce, Convenience, Club), Promotion Type (dropdown: TPR, BOGO, Display, Ad Feature, Scan-Back, Bill-Back, Shipper Display), Brand (dropdown: Brand A, Brand B, Brand C), SKU Group (text), Planned Spend (numbers, USD), Actual Spend (numbers, USD), Expected Lift % (numbers), Actual Lift % (numbers), Start Date (date), End Date (date), Status (status: Planning, Submitted, Approved, Executing, Reconciled, Closed), Assigned Rep (people), Broker (dropdown), ROI (formula: Actual Lift divided by Actual Spend). Groups: Q1 2026, Q2 2026, Q3 2026, Q4 2026. Add a Timeline view called 'Promo Calendar' showing promotions by date range. Add a Dashboard with: total planned vs. actual spend (numbers widget), promotions by status (chart), ROI by retailer (chart), spend by channel (chart), upcoming promotions this month (table). Add an automation: when Status changes to 'Executing', notify the assigned rep and broker. Add another automation: when End Date arrives, change Status to 'Reconciled' and notify finance team."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** PromoGuard
**Agent Purpose:** Automatically monitors trade promotion performance and flags underperforming promotions for mid-flight adjustment.

**Triggers:**
- When a promotion status changes to "Executing"
- Daily scan of all active promotions against expected lift benchmarks
- When actual spend exceeds planned spend by more than 15%
- When a deduction is logged without a matching promotion
- Weekly summary every Monday at 8 AM

**Actions:**
- Compare actual scan data/lift against expected lift and flag promotions below 70% of target
- Generate mid-promotion adjustment recommendations (extend, cut, reallocate budget)
- Auto-create deduction reconciliation items linking deductions to specific promotions
- Notify sales rep and broker when a promotion is underperforming with suggested actions
- Generate weekly promotion performance digest with ROI rankings by retailer
- Escalate unreconciled deductions older than 30 days to finance

**Data Required:**
- Trade promotion board data (planned vs. actual spend and lift)
- POS/scan data integration (via retailer portals or syndicated data feeds)
- Deduction feeds from ERP/accounts receivable
- Historical promotion performance for benchmarking

**Autonomy Level:** Human-in-the-Loop
PromoGuard analyzes and recommends but never cancels or modifies a live promotion without rep approval. Deduction matching is auto-suggested but requires finance sign-off for write-offs over $5,000.

**Example Interaction:**
> PromoGuard detects that the Kroger BOGO promotion on Brand A 12-packs, now in week 2 of a 4-week run, is tracking at only 45% of expected lift. It cross-references historical data and identifies that a competing brand launched a deeper TPR in the same category during week 1. PromoGuard creates an alert item on the Trade Promotion Calendar, notifies the Kroger account rep and the broker team, and recommends either adding a shipper display or shifting $8,000 of remaining budget to a scan-back to incentivize incremental volume. The rep reviews the recommendation, approves the shipper display option, and PromoGuard updates the promotion plan, adjusts the expected ROI forecast, and notifies the supply chain team of potential incremental volume.

---

### Use Case 2: Distributor & Broker Scorecard Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
F&B companies that sell through broker networks and distributor partners have limited visibility into partner performance. Brokers represent multiple manufacturers and prioritize whoever pays the most attention (or commission). Distributor fill rates, void reports, and new store authorizations are tracked in scattered emails and quarterly business reviews. Sales managers spend 10+ hours per month manually compiling broker scorecards from disparate data sources, and underperforming partners go unaddressed for quarters.

#### The Solution
monday.com CRM serves as the partner relationship hub. Each broker and distributor is a CRM account with linked performance boards. A "Broker Scorecard" board tracks KPIs per broker per quarter: new authorizations won (numbers), void fill rate % (numbers), promotion execution compliance % (numbers), communication responsiveness (rating), market share growth (numbers), and overall score (formula). A "Distributor Performance" board tracks: OTIF % (numbers), fill rate % (numbers), damage/return rate (numbers), inventory turns (numbers), and new item pickup velocity (numbers). Dashboards provide stack-ranked views of all partners with traffic-light indicators.

#### The Outcome
50% reduction in time spent compiling partner scorecards. Immediate visibility into underperforming brokers/distributors. Data-driven quarterly business reviews replace anecdotal feedback. 10-15% improvement in broker engagement through accountability transparency.

#### Discovery Questions
- "How many broker partners do you work with, and how do you currently evaluate their performance?"
- "What does your quarterly business review process look like with your distributors?"
- "Do you have real-time visibility into distributor fill rates, void reports, and new store authorizations?"
- "How do you decide when to replace an underperforming broker in a region?"
- "What percentage of your sales team's time goes into compiling data for partner reviews?"

#### Industry Context
The broker model is unique to F&B. Manufacturers pay brokers (typically 3-5% commission) to represent their brands to retailers. Major broker firms include Acosta, Advantage Solutions, and Crossmark. Distributors (Sysco, US Foods, UNFI, KeHE) are the logistics backbone. "Void" = authorized SKU not on shelf. "Authorization" = retailer agreement to carry a SKU. OTIF penalties from major retailers (Walmart charges $3/case for late shipments) make distributor performance critical.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Broker & Distributor Scorecard system in monday.com. Create a board called 'Broker Scorecards' with columns: Broker Name (text), Region (dropdown: Northeast, Southeast, Midwest, Southwest, West, National), Quarter (dropdown: Q1, Q2, Q3, Q4), Year (dropdown: 2025, 2026), New Authorizations Won (numbers), Void Fill Rate % (numbers), Promo Execution Compliance % (numbers), Communication Score (rating 1-5), Market Share Growth % (numbers), Commission Paid (numbers, USD), Overall Score (formula: weighted average of KPIs), Status (status: Exceeding, Meeting, Below Expectations, Under Review). Groups by region. Create a second board called 'Distributor Performance' with columns: Distributor Name (text), Channel (dropdown: Retail, Foodservice, Natural/Specialty), OTIF % (numbers), Fill Rate % (numbers), Damage Rate % (numbers), New Item Pickup Days (numbers), Inventory Turns (numbers), OTIF Penalty Exposure (numbers, USD), Performance Rating (status: Green, Yellow, Red), Account Manager (people). Add a Dashboard with: broker overall scores ranked (chart), distributor OTIF trends (chart), total OTIF penalty exposure (numbers widget), brokers below expectations (table), top performing distributors (table). Add automation: when Overall Score drops below 70, change Status to 'Under Review' and notify VP of Sales."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** PartnerPulse
**Agent Purpose:** Continuously monitors broker and distributor KPIs and proactively identifies performance trends before they become problems.

**Triggers:**
- Weekly data sync from distributor portals and broker reports
- When any KPI drops below threshold (e.g., OTIF < 95%, void fill < 80%)
- When a broker's rolling 3-month trend is declining
- Monthly on the 1st for comprehensive partner health report
- When a new product launch is within 30 days (to assess partner readiness)

**Actions:**
- Auto-populate scorecard boards with latest data from distributor/broker feeds
- Generate trend analysis comparing current quarter vs. previous quarter for each partner
- Flag brokers with declining authorization wins and recommend intervention (increased market visits, added incentives, or partner replacement)
- Create QBR preparation packets summarizing partner performance, discussion points, and recommended actions
- Alert account managers when OTIF penalties are trending above budget threshold
- Recommend optimal broker assignments for new product launches based on historical performance

**Data Required:**
- Distributor portal data (Sysco, UNFI, KeHE reporting dashboards)
- Broker activity reports (store visits, authorization requests, promotion compliance)
- POS/syndicated data (IRI/Circana, Nielsen) for market share tracking
- Commission payment records from accounting

**Autonomy Level:** Escalation-Based
PartnerPulse auto-updates scorecards and generates reports autonomously. Performance alerts go directly to account managers. Partner replacement recommendations require VP Sales approval. QBR prep packets are auto-generated but reviewed by the account manager before sharing.

**Example Interaction:**
> PartnerPulse detects that Acosta's Southeast region has seen a 15% decline in new authorizations over the last two quarters, while their commission payouts have remained flat. It cross-references this with market data showing competitors gaining shelf space in the region. PartnerPulse generates a detailed brief for the Southeast account manager: authorization trends by retailer, competitive activity summary, and three recommended actions (increase co-marketing fund by $15K, schedule joint ride-alongs in top 10 underperforming accounts, or initiate RFP for regional broker replacement). The account manager uses this as the basis for a candid conversation with the Acosta team lead.

---

### Use Case 3: Sales Pipeline & Forecast Management

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
F&B sales pipelines are uniquely complex. A single "deal" might involve getting authorized at a retailer chain (3-12 month cycle), negotiating slotting fees, coordinating a distributor to carry the product, planning an introductory promotion, and managing the first 90 days of sell-through. Many F&B companies track this in spreadsheets or basic CRM that doesn't understand the multi-stage, multi-stakeholder nature of F&B sales cycles. Forecasting is particularly painful: sales leaders cobble together rep-level estimates, broker commitments, and retailer signals into quarterly forecasts that are routinely off by 20-30%.

#### The Solution
monday.com CRM with a customized F&B sales pipeline. Stages reflect the actual F&B sales cycle: Prospecting → Buyer Meeting → Category Review → Authorization → Slotting Negotiation → Distribution Setup → First Order → Shelf Reset → Ongoing. Each deal has columns for: retailer/chain (dropdown), buyer name (text), category (dropdown), # of SKUs (numbers), # of stores (numbers), estimated annual revenue (numbers), slotting fees (numbers), required promotion commitment (numbers), distributor (connected board), broker (connected board), expected authorization date (date), and confidence % (numbers). monday.com AI Sidekick helps reps update pipeline items via natural language and generates weekly forecast summaries.

#### The Outcome
Single source of truth for the entire F&B sales pipeline. 25-35% improvement in forecast accuracy through structured stage tracking. 20% faster time-to-authorization through better visibility and follow-up discipline. Clear view of pipeline by channel, retailer, and brand.

#### Discovery Questions
- "Walk me through what happens from the moment your sales team identifies a new retail opportunity to the first order shipping — how many steps and systems are involved?"
- "How accurate are your quarterly sales forecasts, and what's the biggest driver of forecast misses?"
- "Do you track slotting fees and introductory promotion commitments as part of the deal record, or is that managed separately?"
- "How do your sales reps currently report on pipeline — is it real-time or do you rely on weekly/monthly snapshots?"
- "When a new authorization is won, what's the handoff process to get the product distributed and on-shelf?"

#### Industry Context
F&B sales cycles are driven by retailer category reviews (annual or semi-annual), which creates a "window" dynamic unlike SaaS sales. Slotting fees ($5K-$50K+ per SKU per chain) are upfront costs that affect deal economics. "Shelf reset" is when the retailer physically reorganizes the category shelf — new products appear during resets. "Velocity" = units sold per store per week, the key metric retailers use to evaluate if a product stays on shelf. "Cut" = losing shelf space to a competitor.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an F&B Sales Pipeline in monday.com CRM. Create a board called 'Retail Pipeline' with columns: Account/Retailer (text), Buyer Contact (text), Channel (dropdown: Grocery, Mass, Club, Convenience, Natural, Foodservice, E-commerce), Category (dropdown: Snacks, Beverages, Frozen, Dairy, Bakery, Produce, Deli, Custom), Brand (dropdown: Brand A, Brand B, Brand C), # SKUs (numbers), # Stores (numbers), Estimated Annual Revenue (numbers, USD), Slotting Fees (numbers, USD), Intro Promo Commitment (numbers, USD), Net Deal Value (formula: Revenue minus Slotting minus Promo), Distributor (text), Broker (text), Expected Auth Date (date), Confidence % (numbers), Stage (status: Prospecting, Buyer Meeting, Category Review, Authorization, Slotting Negotiation, Distribution Setup, First Order, Shelf Reset, Ongoing), Sales Rep (people), Priority (status: Hot, Warm, Cool). Groups: Active Pipeline, Won This Quarter, Lost/Stalled. Add a Timeline view showing expected authorization dates. Add a Dashboard with: total pipeline value (numbers widget), pipeline by stage (funnel chart), pipeline by channel (chart), weighted forecast (formula-based numbers widget), deals closing this quarter (table), slotting fee exposure (numbers widget). Add automation: when Stage changes to 'Authorization', send notification to supply chain and distribution teams. Add automation: when Expected Auth Date is 7 days away and Stage is before 'Authorization', notify sales manager."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** PipelinePredictor
**Agent Purpose:** Analyzes the F&B sales pipeline to generate accurate forecasts, identify at-risk deals, and recommend next best actions for each opportunity.

**Triggers:**
- Daily scan of all active pipeline items
- When a deal hasn't been updated in 14+ days
- When a category review date is approaching (30/15/7 days out)
- When confidence % is updated by a rep
- Friday at 4 PM for weekly forecast generation

**Actions:**
- Generate weighted pipeline forecast by channel, brand, and quarter
- Flag stale deals and prompt reps for updates with specific questions
- Identify category review windows at target retailers and alert reps to prepare
- Compare rep-submitted confidence % against historical win rates for similar deals and flag over-optimistic or conservative estimates
- Auto-generate weekly pipeline summary for sales leadership with trend analysis
- Recommend re-engagement tactics for stalled deals based on similar won opportunities

**Data Required:**
- Pipeline board data (all deal attributes and stage history)
- Historical win/loss data for pattern matching
- Retailer category review calendar
- Rep activity data (meeting notes, email touchpoints)

**Autonomy Level:** Human-in-the-Loop
PipelinePredictor generates forecasts and recommendations autonomously. Deal stage changes always require rep confirmation. Forecast adjustments are suggested to sales leadership, not auto-published to finance.

**Example Interaction:**
> It's Friday afternoon, and PipelinePredictor generates the weekly pipeline summary. It flags that the Whole Foods authorization for Brand B's new organic snack line has been in "Category Review" for 8 weeks — 3 weeks longer than the average for natural channel deals. It cross-references with market intelligence showing Whole Foods recently increased their local/regional brand allocation and recommends the rep request a follow-up meeting emphasizing the brand's regional sourcing story. It also adjusts the weighted forecast down from $420K to $310K for the deal, noting the extended timeline, and shows the impact on the Q2 forecast, which is now 12% below target. The VP of Sales uses this to prioritize a joint call with the rep and the broker.

---

### Use Case 4: New Product Launch Coordination

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Launching a new product in F&B requires flawless coordination across sales, marketing, supply chain, regulatory, and broker/distributor partners. A typical launch involves 50-100+ tasks across 8-12 weeks: retailer presentations, packaging finalization, UPC registration, distributor onboarding, promotional planning, sales samples, shelf tags, and first shipment coordination. Most F&B companies manage launches through a chaotic mix of email chains, project trackers, and hope. When launches stumble (late shipments, missing shelf tags, unexecuted promotions), the company risks losing the authorization entirely — and the $25-50K+ in slotting fees already paid.

#### The Solution
monday.com Work Management provides a templatized new product launch framework. A "Product Launch" board template includes all standard workstreams as groups: Retailer Authorization, Regulatory & Compliance, Packaging & Creative, Supply Chain & Production, Distributor Onboarding, Marketing & Promotion, Sales Enablement, and Post-Launch Monitoring. Each group contains pre-built task items with dependencies, owners, and target dates. A cross-functional Dashboard shows launch readiness across all active launches. Automations trigger handoffs between teams (e.g., when regulatory approval is received, packaging finalization is unblocked).

#### The Outcome
40% reduction in launch timeline through parallel workstream execution. Near-zero missed launch tasks through automated checklists and notifications. Better first-90-day sell-through rates due to coordinated promotional support. Reusable templates reduce launch planning time from weeks to days.

#### Discovery Questions
- "How many new products or line extensions do you launch per year, and what's your success rate in the first 90 days?"
- "When a launch goes wrong — late shipment, missing promotional support, distributor not ready — what's the typical root cause?"
- "Is there a single owner or team that coordinates cross-functional launch activities, or does it fall to the sales rep?"
- "How do you track whether brokers and distributors are executing their part of the launch plan?"
- "What's the financial impact when a launch misses its retail shelf reset window?"

#### Industry Context
In F&B, timing is everything for launches. Retailers have fixed "shelf reset" windows (typically quarterly). Missing a reset means waiting 3-6 months for the next one — during which competitors may claim the space. Slotting fees are typically non-refundable. "Speed to shelf" = time from authorization to product appearing on shelf. First 90-day velocity determines whether the product survives or gets "cut" (discontinued by the retailer).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a New Product Launch Tracker in monday.com. Create a board called 'Product Launch Central' with groups: Retailer Authorization (tasks: Submit category review packet, Buyer presentation, Negotiate slotting terms, Receive authorization confirmation), Regulatory & Compliance (tasks: UPC/GTIN registration, Nutrition facts panel finalization, Allergen label review, State-specific compliance check), Packaging & Creative (tasks: Final packaging design approval, Print production, Sales sample production, Shelf tag/POS material), Supply Chain (tasks: Production run scheduling, Safety stock build, Distributor warehouse allocation, First shipment coordination), Distributor Onboarding (tasks: New item setup in distributor system, Pricing confirmation, Minimum order quantities agreed, Distributor sales team briefing), Marketing & Promotion (tasks: Introductory promotion plan finalized, Digital marketing assets, In-store demo scheduling, Social media launch campaign), Post-Launch (tasks: Week 1 velocity check, 30-day fill rate review, 60-day promotion compliance audit, 90-day keep/cut assessment). Each task has columns: Owner (people), Due Date (date), Status (status: Not Started, In Progress, Blocked, Complete), Dependencies (dependency), Notes (text), Priority (status: Critical Path, Standard). Add a Timeline view showing all tasks with dependencies. Add a Dashboard with: launch readiness % (progress widget), tasks by status (chart), overdue tasks (table), upcoming milestones this week (table). Add automation: when all tasks in 'Regulatory & Compliance' group are Complete, notify packaging team to begin print production. Add automation: 3 days before any Due Date, notify task Owner."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** LaunchCommander
**Agent Purpose:** Orchestrates new product launches by tracking cross-functional progress, identifying risks, and ensuring no critical path item slips.

**Triggers:**
- Daily at 9 AM: scan all active launches for overdue or at-risk tasks
- When any task status changes to "Blocked"
- When a critical path task is due within 3 days and not yet "In Progress"
- When a retailer shelf reset date is within 30 days
- When all tasks in a group are marked "Complete" (triggers next phase)

**Actions:**
- Generate daily launch status summary for the launch owner with traffic-light readiness by workstream
- Auto-escalate blocked tasks with context to the relevant department head
- Calculate and display critical path impact: "If this task slips 5 days, the launch date moves from March 15 to March 20, risking the Kroger shelf reset window"
- Coordinate distributor readiness check: auto-send status inquiry to distributor contacts 14 days before first shipment
- Generate post-launch velocity reports at 30/60/90 days with keep/cut risk assessment
- Create retrospective template after launch completion with lessons learned prompts

**Data Required:**
- Launch board task data and dependencies
- Retailer shelf reset calendar
- Distributor onboarding timelines
- POS velocity data (post-launch)
- Historical launch performance benchmarks

**Autonomy Level:** Escalation-Based
LaunchCommander auto-generates reports and status updates. Escalations go to department heads. It suggests timeline adjustments but doesn't move dates without the launch owner's approval. Post-launch velocity reports are auto-generated and shared with the sales team.

**Example Interaction:**
> LaunchCommander detects that the packaging print production for the new sparkling water line is still in "In Progress" with only 12 days until the first shipment date to UNFI's warehouse. It calculates that at the current pace, the print run will complete 3 days after the warehouse receiving window closes, which means missing the Target shelf reset by one full cycle (13 weeks). LaunchCommander escalates to the VP of Marketing with a clear impact statement, suggests two alternatives (expedited print run at $8K premium, or a simplified label for initial shipment with full branding in the second production run), and updates the risk assessment on the launch dashboard from Green to Red for the Packaging workstream.

---

### Use Case 5: Key Account Planning & Execution

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Key account managers in F&B juggle massive retailer relationships — a single Walmart or Kroger relationship might involve hundreds of SKUs, dozens of promotions per year, multiple buyer contacts across categories, and complex joint business planning (JBP) agreements. The typical key account manager spends 40-50% of their time on administrative tasks: pulling reports, updating trackers, preparing for buyer meetings, reconciling deductions, and chasing internal teams for information. The actual strategic selling time — analyzing data, building customer-specific plans, and negotiating growth opportunities — gets squeezed.

#### The Solution
monday.com CRM anchors each key account with a connected ecosystem of boards: Account Overview (contacts, annual plan, volume targets), Promotion Calendar (linked to trade promo board), JBP Tracker (annual initiatives and milestones), Meeting Prep (auto-populated agendas), and Issue Log (deductions, out-of-stocks, compliance issues). Sidekick AI enables reps to query their account data conversationally: "What's our fill rate at Kroger this quarter?" or "Show me all unresolved deductions over $5K." Automated meeting prep pulls latest performance data, open issues, and upcoming promotions into a single brief before every buyer meeting.

#### The Outcome
60% reduction in meeting preparation time for key account managers. Complete account history and context accessible in one place. Faster identification and resolution of account issues. Key account managers can manage 20-30% more accounts without sacrificing relationship quality.

#### Discovery Questions
- "How many key accounts does each account manager handle, and how much of their time goes to administrative work vs. strategic selling?"
- "Do you do Joint Business Plans with your top retailers, and how do you track progress against those commitments?"
- "Before a buyer meeting, how does your rep prepare — and how long does that preparation take?"
- "When a key account has an issue — deductions, out-of-stocks, promotion non-compliance — how quickly does the account manager learn about it?"
- "If a key account manager leaves, how much institutional knowledge walks out the door?"

#### Industry Context
Joint Business Planning (JBP) is a structured annual process where manufacturer and retailer agree on mutual growth targets, promotional plans, and investment levels. Top retailers expect their key suppliers to come to JBP meetings with data-driven proposals. "Category Captain" = the manufacturer that advises the retailer on category strategy (coveted position). "Fill rate" = % of ordered quantity actually shipped. "Out-of-stock" = product not available on shelf (costs F&B companies an estimated 4% of annual sales).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Key Account Management hub in monday.com. Create a board called 'Key Account Plans' with columns: Account Name (text), Retailer Tier (dropdown: Tier 1 - Top 5, Tier 2 - Top 20, Tier 3 - Regional), Channel (dropdown: Grocery, Mass, Club, Natural, Convenience), Annual Revenue Target (numbers, USD), YTD Revenue (numbers, USD), % to Target (formula), # Active SKUs (numbers), # Stores (numbers), JBP Status (status: Not Started, In Development, Submitted, Agreed, In Execution), Key Buyer (text), Account Manager (people), Last Meeting Date (date), Next Meeting Date (date), Open Issues (numbers), Health Score (status: Green, Yellow, Red). Groups: Tier 1 Accounts, Tier 2 Accounts, Tier 3 Accounts. Create a connected board called 'Account Issues Log' with columns: Account (connect to Key Account Plans), Issue Type (dropdown: Deduction, Out-of-Stock, OTIF Miss, Promo Non-Compliance, Pricing Error, Quality), Amount at Risk (numbers, USD), Status (status: Open, Investigating, Resolved, Escalated), Owner (people), Days Open (formula). Add a Dashboard with: total revenue vs target across all key accounts (chart), accounts by health score (chart), open issues by type (chart), top 10 issues by amount at risk (table), upcoming buyer meetings this week (table). Add automation: when Next Meeting Date is 3 days away, create a 'Meeting Prep' item in a subitems group with checklist: Pull latest sales data, Review open issues, Check promotion compliance, Update JBP progress."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** AccountBrief
**Agent Purpose:** Automatically generates comprehensive buyer meeting preparation briefs by aggregating data from multiple boards and external sources.

**Triggers:**
- 48 hours before any scheduled buyer meeting
- When an account manager manually requests a brief
- When a critical issue (deduction > $10K, OTIF < 90%) is logged against a key account with a meeting in the next 7 days
- Monthly on the 1st for JBP progress summaries

**Actions:**
- Pull latest sales performance data (YTD revenue, velocity trends, growth vs. category) and format into a buyer-ready summary
- Compile all open issues for the account with resolution status and recommended talking points
- List upcoming and recently completed promotions with performance metrics
- Identify 2-3 growth opportunities based on category gaps, competitive activity, or new product availability
- Generate a suggested meeting agenda tailored to the account's current health and JBP status
- After the meeting, prompt the account manager for notes and auto-update the account record

**Data Required:**
- Key Account Plans board
- Account Issues Log
- Trade Promotion Calendar
- Pipeline board (new SKU opportunities)
- POS/syndicated data for category performance context

**Autonomy Level:** Fully Autonomous
AccountBrief generates and delivers briefs without any manual trigger. Account managers receive them automatically and can request updates. Meeting note prompts are sent automatically post-meeting.

**Example Interaction:**
> Two days before the quarterly business review with Costco, AccountBrief generates a 2-page brief for the account manager. It shows that YTD revenue is tracking 8% above JBP target, driven by strong performance of the new organic trail mix. However, it flags that OTIF has dipped to 93% over the last 30 days (below Costco's 97% requirement), with two late shipments traced to a production bottleneck. It suggests leading the meeting with the positive growth story, then proactively addressing the OTIF issue with a corrective action plan (already drafted: additional safety stock build and backup freight carrier). It also identifies an opportunity to propose a new seasonal SKU for the upcoming holiday reset, noting that the trail mix category at Costco grew 12% YoY. The account manager walks into the meeting fully prepared in 5 minutes instead of the usual 3 hours of report-pulling.

---

### Use Case 6: Sales Team Performance & Activity Tracking

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
F&B sales managers struggle to understand what their reps are actually doing in the field. Unlike inside sales where CRM captures every call and email, F&B field reps visit stores, meet with buyers, attend food shows, and coordinate with brokers — activities that rarely make it into any system. Managers rely on weekly ride-alongs, anecdotal reporting, and lagging revenue indicators to assess rep performance. By the time an underperforming rep is identified, a full quarter of territory development may be lost.

#### The Solution
monday.com Work Management provides a lightweight field activity tracker. Reps log activities (store visits, buyer meetings, food show attendance, new item presentations, competitive shelf surveys) via a mobile-friendly form that takes 30 seconds per entry. Each activity links to the relevant account in CRM. Dashboards show activity volume and mix by rep, correlating activity levels with pipeline progression and revenue outcomes. AI Sidekick lets managers ask "Show me Sarah's activity last week in the Southeast territory" or "Which reps have the highest meeting-to-authorization conversion?"

#### The Outcome
Real-time visibility into field sales activity across the entire team. Data-driven coaching conversations replace gut-feel assessments. 15-20% improvement in rep productivity through activity pattern optimization. Early warning system for disengaged or struggling reps.

#### Discovery Questions
- "How do you currently track what your field sales reps are doing day-to-day?"
- "Can you correlate sales activity — store visits, buyer meetings — with actual results like new authorizations?"
- "How quickly can you identify when a rep is underperforming, and what data informs that judgment?"
- "Do your reps resist CRM data entry? What's the adoption challenge been?"
- "What does a 'great week' look like for one of your field reps — how many visits, meetings, presentations?"

#### Industry Context
F&B field sales is relationship-heavy and geographically dispersed. Reps cover territories that might span multiple states. A typical rep might have 50-200 accounts, visiting 8-15 per week. "Ride-alongs" are when the manager travels with the rep for a day to observe. "Food shows" (NACS, Fancy Food, IDDBA) are major industry events where buyers source new products. "Shelf surveys" involve reps auditing competitive products and planogram compliance in stores.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Field Sales Activity Tracker in monday.com. Create a board called 'Field Activity Log' with columns: Rep Name (people), Activity Date (date), Account (text), Activity Type (dropdown: Store Visit, Buyer Meeting, Food Show, New Item Presentation, Competitive Shelf Survey, Broker Ride-Along, Training, Internal Meeting), Channel (dropdown: Grocery, Mass, Club, Convenience, Natural, Foodservice), Outcome (dropdown: Authorization Progress, Promotion Discussed, Issue Identified, Relationship Building, Competitive Intel, No Action Needed), Notes (long text), Follow-Up Required (checkbox), Follow-Up Date (date). Create a form for easy mobile entry with all fields above. Add a Dashboard with: activities per rep this week (chart), activity type distribution (pie chart), activities by channel (chart), follow-ups due this week (table), activity trend over 12 weeks by rep (chart), meetings-to-authorizations ratio by rep (chart). Add automation: when Follow-Up Required is checked, create a follow-up reminder 1 day before Follow-Up Date and notify the rep."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** FieldCoach
**Agent Purpose:** Analyzes field sales activity patterns to provide personalized coaching recommendations and territory optimization insights.

**Triggers:**
- Weekly on Friday at 3 PM for individual rep activity summaries
- Monthly on the last day for territory performance correlation analysis
- When a rep's activity volume drops below their 4-week rolling average by 30%+
- When a territory's pipeline shows no new opportunities for 21+ days
- Before quarterly performance reviews

**Actions:**
- Generate weekly activity digest for each rep: total activities, mix, outcomes, and comparison to team average
- Correlate activity patterns with results: identify which activity types drive the most authorizations per rep
- Flag reps whose activity mix is suboptimal (e.g., too many relationship visits, not enough new item presentations)
- Generate territory heat maps showing account coverage gaps
- Create pre-review performance packets for managers with data-driven coaching recommendations
- Identify "winning patterns" from top performers and recommend adoption by lower-performing reps

**Data Required:**
- Field Activity Log board
- Pipeline board (authorization outcomes)
- Revenue data by rep/territory
- Historical activity and performance data for trend analysis

**Autonomy Level:** Human-in-the-Loop
FieldCoach generates all analysis autonomously but delivers coaching recommendations to the sales manager, not directly to reps. The manager decides how and when to share insights. Performance review packets are auto-generated but only accessible to the manager.

**Example Interaction:**
> FieldCoach's monthly analysis reveals that the top 3 performing reps in the Midwest region average 4.2 new item presentations per week and attend 2+ food shows per quarter, while the bottom 3 average only 1.8 presentations and 0.5 food shows. It generates a coaching brief for the regional manager showing this correlation, along with a recommendation to increase food show attendance for underperforming reps (with specific upcoming shows: IDDBA in June, Sweets & Snacks in May). It also flags that one rep, despite high overall activity volume, has zero competitive shelf surveys logged — suggesting they may be missing competitive threats in their territory. The regional manager uses these insights in next week's team meeting.

---

### Use Case 7: Deduction & Dispute Management

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Deductions are the bane of F&B finance and sales teams. Retailers and distributors routinely deduct amounts from payments for trade promotions, freight claims, damaged goods, pricing discrepancies, and compliance penalties. A mid-market F&B company might process 200-1,000+ deductions per month, totaling 3-8% of gross revenue. Many go uncontested simply because the team can't research and dispute them fast enough — the dispute window is typically 30-90 days. The result: hundreds of thousands (or millions) in annual write-offs that could have been recovered.

#### The Solution
monday.com Work Management serves as the deduction management hub. Each deduction is an item with: retailer/distributor (dropdown), deduction type (dropdown: trade promo, freight, damage, pricing, compliance, unknown), amount (numbers), invoice reference (text), date received (date), dispute deadline (date), linked promotion (connected board), status (New → Researching → Disputed → Approved → Written Off → Recovered), assigned to (people), and resolution notes (long text). Automations prioritize high-value deductions, flag approaching deadlines, and route deductions to the appropriate team (trade → sales, freight → logistics, pricing → finance).

#### The Outcome
25-40% improvement in deduction recovery rate through faster research and dispute filing. Zero missed dispute deadlines through automated alerts. Clear visibility into deduction trends by retailer, type, and root cause. 50%+ reduction in deduction research time through automated matching.

#### Discovery Questions
- "How many deductions does your company process per month, and what percentage are currently being disputed vs. written off?"
- "What's your current process for researching and matching deductions to their root cause — is it manual?"
- "Do you have visibility into deduction trends by retailer or type, or does each one feel like a one-off?"
- "How many FTEs are dedicated to deduction management, and how much of their time is spent on research vs. dispute filing?"
- "What's the typical dollar amount of annual write-offs from uncontested deductions?"

#### Industry Context
F&B deductions are categorized as "valid" (legitimate claims for authorized promotions or genuine issues) and "invalid" (errors, duplicate deductions, unauthorized deductions). The research process involves matching deduction backup documentation to promotion plans, proof of delivery, and pricing agreements. Major retailers use portals (Walmart Retail Link, Kroger 84.51°) where manufacturers must file disputes. "Backup" = documentation the retailer provides to justify the deduction. Common codes: "Trade Allowance," "Damaged Merchandise," "Freight Claim," "Short Ship."

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Deduction Management System in monday.com. Create a board called 'Deduction Tracker' with columns: Deduction ID (text, auto-generated), Retailer/Distributor (dropdown: Walmart, Kroger, Costco, Sysco, US Foods, UNFI, Target, Custom), Deduction Type (dropdown: Trade Promotion, Freight Claim, Damaged Goods, Pricing Discrepancy, OTIF Penalty, Compliance, Unknown), Amount (numbers, USD), Invoice Reference (text), Date Received (date), Dispute Deadline (date), Days Until Deadline (formula: Dispute Deadline minus today), Linked Promotion (connect board), Status (status: New, Researching, Disputed, Awaiting Response, Approved Valid, Recovered, Written Off), Assigned To (people), Root Cause (dropdown: Valid - Authorized Promo, Valid - Legitimate Claim, Invalid - Duplicate, Invalid - Unauthorized, Invalid - Calculation Error, Pending Research), Recovery Amount (numbers, USD), Resolution Notes (long text). Groups: Active (New/Researching/Disputed), Awaiting Response, Resolved This Month. Add a Dashboard with: total open deduction exposure (numbers widget), deductions by type (pie chart), recovery rate % (numbers widget), deductions approaching deadline (< 7 days) (table), monthly trend — new vs. resolved (chart), top 5 retailers by deduction volume (chart). Add automation: when Status is 'New' and Amount > $5000, change Priority to urgent and notify deduction manager. Add automation: when Days Until Deadline < 7 and Status is not 'Disputed', notify Assigned To with urgent flag."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** DeductionDetective
**Agent Purpose:** Automatically researches deductions, matches them to their root cause, and prepares dispute packages for invalid deductions.

**Triggers:**
- When a new deduction item is created (within 1 hour)
- Daily scan for deductions approaching dispute deadline (< 14 days)
- When deduction backup documentation is uploaded
- Weekly summary every Monday for deduction portfolio review
- When a pattern is detected (3+ similar deductions from same retailer in 30 days)

**Actions:**
- Auto-match incoming deductions to trade promotions by retailer, date range, and amount within tolerance
- Classify deductions as likely valid or likely invalid based on matching results
- For likely invalid deductions: auto-generate dispute letter with supporting documentation (promotion agreement, proof of delivery, pricing confirmation)
- Flag duplicate deductions by cross-referencing deduction ID patterns, amounts, and dates
- Detect deduction patterns (e.g., systematic overcharges from a specific retailer) and generate trend alerts
- Generate weekly deduction portfolio report: new, resolved, recovered, written off, at-risk

**Data Required:**
- Deduction Tracker board
- Trade Promotion Calendar board (for matching)
- Proof of delivery/shipment data from logistics
- Pricing agreements and contracts
- Historical deduction data for pattern recognition

**Autonomy Level:** Human-in-the-Loop
DeductionDetective auto-researches and classifies all deductions. Dispute letters are auto-drafted but require analyst approval before submission. Valid deductions under $1,000 are auto-approved. Write-offs over $10,000 require manager sign-off.

**Example Interaction:**
> DeductionDetective processes 47 new deductions received overnight from Walmart. Within 30 minutes, it has matched 31 to authorized trade promotions (classified as valid), identified 8 as likely duplicates of previously resolved deductions (flagged for dispute), found 4 with pricing discrepancies that don't match any authorized promotion (classified as unauthorized — dispute letters drafted), and marked 4 as requiring manual research (unusual codes). For the 8 duplicates, it has already generated dispute letters with the original deduction resolution documentation attached. The deduction analyst reviews the package, approves all 8 disputes with one click, and the team has recovered $34,000 before lunch. The analyst's morning just went from 4 hours of research to 20 minutes of review.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| TPR | Temporary Price Reduction — a promotional mechanism where the retailer temporarily lowers the shelf price, funded by the manufacturer |
| BOGO | Buy One Get One — common F&B promotion type |
| Slotting Fee | Upfront payment to a retailer for shelf space allocation for a new product ($5K-$50K+ per SKU per chain) |
| Velocity | Units sold per store per week — the primary metric retailers use to evaluate product performance |
| OTIF | On Time In Full — delivery compliance metric; major retailers penalize manufacturers for failures |
| Void | An authorized SKU that is not present on the shelf (out-of-stock at store level) |
| Shelf Reset | Periodic reorganization of store shelves by category — the window when new products gain or lose shelf space |
| Category Captain | A leading manufacturer that advises the retailer on overall category strategy and planogram |
| JBP | Joint Business Plan — annual collaborative plan between manufacturer and retailer with mutual growth targets |
| Planogram | Visual diagram showing optimal product placement on retail shelves |
| Scan-Back | Promotion funded per unit scanned at register, vs. off-invoice discount |
| Bill-Back | Promotional payment claimed by retailer after the promotion period based on scan data |
| Broker | Third-party sales representative firm (Acosta, Advantage) that represents manufacturers to retailers for commission |
| DSD | Direct Store Delivery — manufacturer delivers directly to store vs. through distributor warehouse |
| MCB | Manufacturer Chargeback — deduction taken by distributor for price differences |
| ACV | All Commodity Volume — measure of retail distribution (% of total market sales represented by stores carrying the product) |
| Cut | When a retailer discontinues a product from its shelves, typically due to low velocity |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| VP of Sales | Sets revenue targets, manages channel strategy, owns broker/distributor relationships | Decision-maker |
| Director of Trade Marketing | Manages trade promotion budget, plans promotions, analyzes ROI | Decision-maker for trade spend tools |
| National Account Manager | Manages relationships with top 5-10 retailers, owns JBP process | Influencer, key user |
| Regional Sales Manager | Oversees field reps in a geography, responsible for regional revenue targets | Influencer |
| Field Sales Representative | Visits stores, presents new items, manages local broker relationships | End user |
| Sales Operations Manager | Manages CRM, reporting, forecasting processes, sales compensation | Technical decision-maker |
| Director of Revenue Management | Owns pricing strategy, deduction management, trade accruals | Influencer, budget holder |
| Broker Manager | Internal role managing the relationship with external broker firms | Key user |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Supply Chain / Logistics | Order fulfillment, inventory planning, OTIF compliance | Connected boards for demand signals from pipeline, launch coordination |
| Marketing | Trade promotions, brand activations, new product launches | Shared promotion calendar, campaign-to-sales attribution |
| Finance | Deductions, trade accruals, revenue recognition | Deduction management integration, trade spend reconciliation |
| Product & R&D | New product development, line extensions | Stage-gate NPD board connected to launch tracker |
| Operations | Production scheduling, capacity planning | Demand forecast from pipeline feeds production planning |
| Customer Success | Post-sale support, ongoing account health | Shared account health view for retention signals |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Salesforce | Enterprise CRM, not tailored to F&B sales cycles | monday CRM offers faster setup, F&B-specific pipeline stages, and better visual planning tools without $150K+ implementation |
| Blacksmith Applications / AFS | Dedicated TPM systems for trade promotion | monday.com replaces mid-market TPM needs at a fraction of the cost with flexible board structures |
| SAP Trade Management | Enterprise trade management within SAP ecosystem | Too expensive and rigid for mid-market; monday.com provides 80% of functionality with 10x faster deployment |
| Excel / Google Sheets | Universal fallback for everything | No automation, no real-time visibility, no collaboration — monday.com is the natural upgrade path |
| Repsly / Pitcher | Field sales execution tools | monday.com provides broader platform (pipeline + field activity + promotions) vs. point solutions |
| HubSpot CRM | SMB/mid-market CRM | Lacks F&B-specific pipeline stages, trade promo integration, and operational workflow capabilities |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have a CRM (Salesforce)" | "How well does it handle your F&B-specific needs — trade promotions, broker scorecards, multi-stage retail authorizations? monday.com CRM is built for the way F&B actually sells, and it integrates with Salesforce if needed." |
| "Our trade promo management is handled by our TPM system" | "For enterprise TPM, that makes sense. But how well does it connect to your pipeline, account plans, and field activity? Most teams end up running a shadow system in spreadsheets. monday.com bridges that gap." |
| "Our reps won't adopt another tool" | "That's exactly why we focus on low-friction input — mobile forms that take 30 seconds, Sidekick AI that lets reps update by typing naturally. The adoption barrier is lower than any traditional CRM." |
| "We need industry-specific functionality you don't have" | "monday.com's flexibility is the feature. Instead of paying for a rigid industry-specific tool that never quite fits, you build exactly what you need — and change it when your business changes. Let me show you a working F&B pipeline in 10 minutes." |
| "Our data is in too many systems to consolidate" | "We integrate with 200+ tools natively, plus mondayDB gives you a structured data layer that connects everything. Most F&B companies start with one workflow — say, trade promotions — and expand from there." |
| "We're a small sales team, we don't need all this" | "Small teams actually benefit most — you don't have dedicated sales ops, so you need a tool that automates what a 3-person ops team would do. AI agents handle the admin so your reps focus on selling." |

## Proof Points
*(To be populated with customer references)*
- [F&B manufacturer that improved trade promotion ROI tracking]
- [CPG company that consolidated broker management into monday.com]
- [Beverage brand that accelerated new product launches]
- [Food distributor that improved sales team visibility and forecasting]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
