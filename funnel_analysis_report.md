# Marketing Funnel Analysis: Visitor → Customer

**Period:** July 2025 – June 2026 (12 months) · **Business type:** B2B SaaS (simulated data) · **Funnel:** Visitor → Lead → MQL → SQL → Customer

---

## 1. Executive Summary

Across 7 acquisition channels and ~810K visitors, the funnel converted **2,310 customers** (0.29% visitor-to-customer rate) and **$9.6M in revenue** against **$663K in spend** (14.5x blended ROAS). The funnel is healthy in the middle (Lead→MQL and MQL→SQL both exceed 38%) but leaks heavily at the very top and bottom: **94.8% of visitors never submit a lead form**, and **72.6% of Sales-Qualified Leads never close**. Two channels — Referral and Email — punch far above their weight on lead quality, while Content Syndication produced zero customers despite being the second most expensive channel.

## 2. Overall Funnel

| Stage | Count | % of Visitors |
|---|---:|---:|
| Visitors | 809,623 | 100% |
| Leads | 42,043 | 5.2% |
| MQLs | 21,867 | 2.7% |
| SQLs | 8,422 | 1.0% |
| Customers | 2,310 | 0.3% |

![Overall Funnel](../charts/01_overall_funnel.png)

**Stage-to-stage conversion rates:**

| Transition | Conversion Rate | Drop-off |
|---|---:|---:|
| Visitor → Lead | 5.19% | **94.8%** ⚠️ largest leak |
| Lead → MQL | 52.01% | 48.0% |
| MQL → SQL | 38.51% | 61.5% |
| SQL → Customer | 27.43% | **72.6%** second-largest leak |

![Stage Conversion Rates](../charts/02_stage_conversion_rates.png)

## 3. Where Users Are Dropping Off

- **Visitor → Lead is the single biggest leak in the funnel.** Only about 1 in 19 visitors ever fills out a form. Because every downstream stage is a percentage of this number, even a modest improvement here (e.g., 5.2% → 6.5% conversion) would flow through to roughly 25% more customers with no change to spend.
- **SQL → Customer is the second-largest leak**, and it's the one stage largely outside marketing's direct control — it reflects sales follow-up, deal qualification, and closing effectiveness rather than traffic quality.
- Lead → MQL and MQL → SQL are comparatively healthy (52% and 38%), suggesting the lead-scoring and initial qualification process is working reasonably well once someone converts.

![Monthly Trend](../charts/06_monthly_trend.png)

Traffic and conversion both show mild seasonality, peaking around December and again in June, with a dip in Q1 (Jan–Mar) — worth checking against typical B2B budget-cycle patterns.

## 4. Channel Performance

| Channel | Visitors | Leads | Customers | Lead→Customer | CAC | ROAS |
|---|---:|---:|---:|---:|---:|---:|
| Organic Search | 241,969 | 10,398 | 642 | 6.2% | $0 (unpaid) | — |
| Referral | 49,948 | 4,560 | 570 | **12.5%** | $0 (unpaid) | — |
| Email | 80,799 | 6,836 | 563 | 8.2% | $7 | 575x |
| Paid Search | 121,706 | 7,818 | 273 | 3.5% | $933 | 4.5x |
| Direct | 89,150 | 5,200 | 211 | 4.1% | $0 (unpaid) | — |
| Paid Social | 160,469 | 5,656 | 51 | **0.9%** ⚠️ | $3,444 | 1.2x |
| Content Syndication | 65,582 | 1,575 | 0 | **0.0%** ⚠️ | — | 0x |

![Customers by Channel](../charts/03_customers_by_channel.png)
![Lead Quality by Channel](../charts/04_lead_quality_by_channel.png)
![CAC by Channel](../charts/05_cac_by_channel.png)

**Key takeaways:**
- **Referral and Email are the highest-quality channels by far** — both convert leads to customers at 2–4x the rate of paid channels, and both cost next to nothing per acquisition.
- **Organic Search is the largest single source of customers** (642) thanks to sheer volume, even though its lead quality is only middling (6.2%).
- **Paid Social is the weakest paid channel**: high spend, high lead volume, but the lowest lead-to-customer rate (0.9%) and the highest CAC ($3,444) of any channel that produced customers.
- **Content Syndication is the clearest candidate to cut or rebuild.** It has the highest cost-per-lead ($145) and converted zero SQLs into customers all year.

## 5. Recommendations

1. **Attack the Visitor→Lead leak first.** This is the largest drop in the funnel by a wide margin. Test shorter forms, clearer above-the-fold CTAs, and exit-intent offers on top-traffic landing pages (start with Organic Search and Paid Search pages, since they carry the most volume).
2. **Reallocate budget away from Content Syndication toward Referral and Email.** Content Syndication spent ~$229K for zero customers this year. Even a partial shift of that budget into a referral incentive program or expanded email nurture sequences would likely produce a materially better return.
3. **Formalize a referral program.** Referral already converts best (12.5% lead→customer) at zero acquisition cost — it's currently underinvested relative to its performance. A structured customer/partner referral incentive could scale volume without diluting quality.
4. **Re-target or pause underperforming Paid Social campaigns.** At $3,444 CAC against a ~$4,200 average deal size, Paid Social is barely profitable before accounting for fulfillment and support costs. Tighten audience targeting or shift that budget to Paid Search, which converts roughly 4x better.
5. **Investigate the SQL→Customer stage with the sales team.** This is a sales-process question, not a marketing one: review response times, qualification criteria, and objection patterns to understand why nearly 3 in 4 sales-qualified leads aren't closing.

## 6. Methodology & Caveats

This analysis uses a **simulated dataset** (`data/funnel_data.csv`) generated to reflect realistic B2B SaaS funnel dynamics — channel-level conversion rates, seasonality, and cost structures were modeled on typical industry benchmarks rather than pulled from a live source. The approach (stage-by-stage conversion tracking, channel comparison on CAC/ROAS/lead quality, and drop-off identification) is directly transferable to real Google Analytics, HubSpot, Salesforce, or CRM exports — swap in real data at `data/funnel_data.csv` with the same column structure and every chart and metric in this report will recompute correctly.
