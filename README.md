# Marketing Funnel & Lead Conversion Analysis

Analysis of a B2B SaaS marketing funnel (Visitor → Lead → MQL → SQL → Customer) across 7 acquisition channels over 12 months. Built to identify where users drop off, which channels bring high-quality (not just high-volume) leads, and what to fix first.

**[View the live interactive dashboard →](dashboard/index.html)**

![Funnel Overview](charts/01_overall_funnel.png)

## Project Structure

```
funnel_project/
├── data/
│   ├── generate_data.py       # Simulates the raw funnel dataset
│   ├── funnel_data.csv        # Funnel data by month × channel × campaign
│   └── channel_summary.csv    # Aggregated channel-level metrics
├── notebooks/
│   └── analysis.py            # Full funnel + channel + trend analysis, generates all charts
├── charts/                    # PNG exports of every chart (used in the report)
├── dashboard/
│   ├── index.html             # Self-contained interactive dashboard (Chart.js)
│   └── data.json              # Aggregated data powering the dashboard
└── report/
    └── funnel_analysis_report.md   # Full written analysis, insights, and recommendations
```

## Key Findings

- **809,623 visitors → 2,310 customers** (0.29% overall conversion), $9.6M revenue on $663K spend (**14.5x blended ROAS**).
- **Biggest leak: Visitor → Lead (94.8% drop-off).** This single stage matters more than any other — every downstream improvement is multiplied by it.
- **Referral and Email are the highest-quality channels** (12.5% and 8.2% lead→customer rate) at near-zero cost, while **Paid Social is the weakest** (0.9% lead→customer, $3,444 CAC).
- **Content Syndication produced zero customers** despite being the second-most expensive channel — the clearest budget reallocation opportunity.

Full breakdown, charts, and 5 prioritized recommendations: **[report/funnel_analysis_report.md](report/funnel_analysis_report.md)**

## How This Was Built

1. **Data:** `data/generate_data.py` simulates realistic funnel data — channel-specific conversion rates, seasonality, and spend, based on typical B2B SaaS benchmarks. Swap in a real GA4/HubSpot/CRM export with the same columns (`month, channel, campaign, visitors, leads, mqls, sqls, customers, spend_usd, revenue_usd`) to re-run this analysis on live data.
2. **Analysis:** `notebooks/analysis.py` (pandas + matplotlib) computes stage-to-stage conversion, drop-off rates, channel-level CAC/ROAS/lead quality, and monthly trends, and exports all charts.
3. **Dashboard:** `dashboard/index.html` is a single self-contained HTML file (Chart.js via CDN) — no build step, just open it in a browser or host it on GitHub Pages.

## Tools Used

- **Python** (pandas, numpy, matplotlib) — data simulation and funnel/channel analysis
- **Chart.js** — interactive dashboard
- Approach is directly portable to **Power BI**, **Tableau**, or **Jupyter Notebook** if preferred

## Run It Yourself

```bash
pip install pandas numpy matplotlib
python data/generate_data.py     # regenerate the dataset
python notebooks/analysis.py     # rerun the analysis + regenerate charts
```

Then open `dashboard/index.html` directly in a browser.

---

*This project was completed as part of the Future Interns Data Analytics program.*
