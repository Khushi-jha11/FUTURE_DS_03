"""
Marketing Funnel Analysis
Stages: Visitor -> Lead -> MQL -> SQL -> Customer
"""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.edgecolor": "#444444",
    "axes.grid": True,
    "grid.color": "#e6e6e6",
    "font.size": 11,
})

df = pd.read_csv("/home/claude/funnel_project/data/funnel_data.csv")
STAGES = ["visitors", "leads", "mqls", "sqls", "customers"]
STAGE_LABELS = ["Visitors", "Leads", "MQLs", "SQLs", "Customers"]
OUT = "/home/claude/funnel_project/charts"

# ---------------------------------------------------------------
# 1. OVERALL FUNNEL
# ---------------------------------------------------------------
totals = df[STAGES + ["spend_usd", "revenue_usd"]].sum()
overall_rates = {
    "Visitor -> Lead": totals["leads"] / totals["visitors"],
    "Lead -> MQL": totals["mqls"] / totals["leads"],
    "MQL -> SQL": totals["sqls"] / totals["mqls"],
    "SQL -> Customer": totals["customers"] / totals["sqls"],
    "Visitor -> Customer (overall)": totals["customers"] / totals["visitors"],
}

print("=" * 60)
print("OVERALL FUNNEL TOTALS (12 months)")
print("=" * 60)
for s, l in zip(STAGES, STAGE_LABELS):
    print(f"{l:12s}: {int(totals[s]):>10,}")
print(f"{'Spend':12s}: ${totals['spend_usd']:>12,.0f}")
print(f"{'Revenue':12s}: ${totals['revenue_usd']:>12,.0f}")
print(f"{'ROAS':12s}: {totals['revenue_usd']/totals['spend_usd']:.2f}x")
print()
print("STAGE-TO-STAGE CONVERSION RATES")
for k, v in overall_rates.items():
    print(f"  {k:32s}: {v*100:5.2f}%")

# Funnel (waterfall) chart
fig, ax = plt.subplots(figsize=(8, 5.5))
values = [totals[s] for s in STAGES]
colors = ["#2E5EAA", "#3E7CB1", "#5FA8D3", "#8ECAE6", "#FFB703"]
bars = ax.barh(STAGE_LABELS[::-1], values[::-1], color=colors[::-1])
for bar, val, lbl in zip(bars, values[::-1], STAGE_LABELS[::-1]):
    pct = val / values[0] * 100
    ax.text(bar.get_width() + values[0]*0.01, bar.get_y() + bar.get_height()/2,
            f"{int(val):,}  ({pct:.1f}% of visitors)", va="center", fontsize=10)
ax.set_title("Marketing Funnel: Visitors → Customers (Jul 2025–Jun 2026)", fontsize=13, fontweight="bold")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
ax.set_xlim(0, values[0]*1.35)
plt.tight_layout()
plt.savefig(f"{OUT}/01_overall_funnel.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# 2. STAGE-TO-STAGE CONVERSION RATE CHART
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 4.5))
labels = list(overall_rates.keys())[:-1]
vals = [overall_rates[k]*100 for k in labels]
bars = ax.bar(labels, vals, color=["#2E5EAA","#3E7CB1","#5FA8D3","#FFB703"])
for bar, v in zip(bars, vals):
    ax.text(bar.get_x()+bar.get_width()/2, v+0.5, f"{v:.1f}%", ha="center", fontweight="bold")
ax.set_ylabel("Conversion Rate (%)")
ax.set_title("Stage-to-Stage Conversion Rates", fontsize=13, fontweight="bold")
plt.xticks(rotation=15, ha="right")
plt.tight_layout()
plt.savefig(f"{OUT}/02_stage_conversion_rates.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# 3. CHANNEL COMPARISON
# ---------------------------------------------------------------
ch = df.groupby("channel")[STAGES + ["spend_usd", "revenue_usd"]].sum().reset_index()
ch["v2l"] = ch["leads"] / ch["visitors"]
ch["l2cust"] = ch["customers"] / ch["leads"]
ch["v2cust"] = ch["customers"] / ch["visitors"]
import numpy as np
ch["cpl"] = ch["spend_usd"] / ch["leads"].replace(0, np.nan)          # cost per lead
ch["cac"] = ch["spend_usd"] / ch["customers"].replace(0, np.nan)       # cost per acquired customer
ch["roas"] = ch["revenue_usd"] / ch["spend_usd"].replace(0, np.nan)
ch = ch.sort_values("customers", ascending=False)

print("\n" + "=" * 60)
print("CHANNEL PERFORMANCE SUMMARY")
print("=" * 60)
print(ch[["channel","visitors","leads","customers","v2l","l2cust","cac","roas"]]
      .assign(v2l=lambda d: (d.v2l*100).round(1), l2cust=lambda d: (d.l2cust*100).round(1),
              cac=lambda d: d.cac.round(0), roas=lambda d: d.roas.round(2))
      .to_string(index=False))
ch.to_csv("/home/claude/funnel_project/data/channel_summary.csv", index=False)

# Chart: customers + lead-to-customer rate by channel
fig, ax1 = plt.subplots(figsize=(9, 5.5))
order = ch.sort_values("customers", ascending=True)
ax1.barh(order["channel"], order["customers"], color="#2E5EAA", label="Customers Won")
ax1.set_xlabel("Customers Won (12 mo)")
for i, (c, v) in enumerate(zip(order["channel"], order["customers"])):
    ax1.text(v + 5, i, f"{int(v)}", va="center")
ax1.set_title("Customers Won by Channel", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig(f"{OUT}/03_customers_by_channel.png", dpi=150)
plt.close()

# Chart: Lead->Customer conversion rate (quality) by channel
fig, ax = plt.subplots(figsize=(9, 5.5))
order2 = ch.sort_values("l2cust", ascending=True)
bars = ax.barh(order2["channel"], order2["l2cust"]*100, color="#FFB703")
for i, v in enumerate(order2["l2cust"]*100):
    ax.text(v + 0.1, i, f"{v:.1f}%", va="center")
ax.set_xlabel("Lead → Customer Conversion Rate (%)")
ax.set_title("Lead Quality by Channel (Lead → Customer Rate)", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig(f"{OUT}/04_lead_quality_by_channel.png", dpi=150)
plt.close()

# Chart: CAC by channel (paid channels only, spend > 0)
paid = ch[ch["spend_usd"] > 0].sort_values("cac")
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(paid["channel"], paid["cac"], color="#8ECAE6")
for bar, v in zip(bars, paid["cac"]):
    ax.text(bar.get_x()+bar.get_width()/2, v+10, f"${v:,.0f}", ha="center", fontweight="bold")
ax.axhline(4200*0.3, color="red", linestyle="--", linewidth=1, label="Healthy CAC threshold (~30% of $4,200 deal)")
ax.set_ylabel("Customer Acquisition Cost (USD)")
ax.set_title("CAC by Channel (Paid Channels)", fontsize=13, fontweight="bold")
plt.xticks(rotation=20, ha="right")
ax.legend()
plt.tight_layout()
plt.savefig(f"{OUT}/05_cac_by_channel.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# 4. TREND OVER TIME (overall conversion + volume)
# ---------------------------------------------------------------
mo = df.groupby("month")[STAGES].sum().reset_index()
mo["v2cust"] = mo["customers"] / mo["visitors"] * 100

fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.bar(mo["month"], mo["visitors"], color="#D7E3F4", label="Visitors")
ax1.set_ylabel("Visitors")
ax1.tick_params(axis='x', rotation=45)
ax2 = ax1.twinx()
ax2.plot(mo["month"], mo["v2cust"], color="#E63946", marker="o", linewidth=2, label="Visitor→Customer %")
ax2.set_ylabel("Visitor → Customer Conversion (%)")
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1+lines2, labels1+labels2, loc="upper left")
ax1.set_title("Monthly Traffic Volume vs. Overall Conversion Rate", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig(f"{OUT}/06_monthly_trend.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# 5. BIGGEST DROP-OFF STAGE IDENTIFICATION
# ---------------------------------------------------------------
dropoffs = {
    "Visitor -> Lead": 1 - overall_rates["Visitor -> Lead"],
    "Lead -> MQL": 1 - overall_rates["Lead -> MQL"],
    "MQL -> SQL": 1 - overall_rates["MQL -> SQL"],
    "SQL -> Customer": 1 - overall_rates["SQL -> Customer"],
}
biggest = max(dropoffs, key=dropoffs.get)
print("\n" + "=" * 60)
print("DROP-OFF ANALYSIS")
print("=" * 60)
for k, v in dropoffs.items():
    print(f"  {k:20s}: {v*100:5.1f}% drop-off")
print(f"\n  Biggest drop-off stage: {biggest} ({dropoffs[biggest]*100:.1f}% lost)")

print("\nAll charts saved to:", OUT)
