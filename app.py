import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Swedish Road Safety Dashboard",
    page_icon="🚦",
    layout="wide",
)

# ── COLORS ───────────────────────────────────────────────────────────────────
ACCENT = "#2D6A8F"
RED    = "#C0392B"
ORANGE = "#E67E22"
GREEN  = "#27AE60"
GRAY   = "#95A5A6"

# ── LOAD DATA ────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    trend  = pd.read_csv("Data/Processed/trend.csv")
    months = pd.read_csv("Data/Processed/by_month.csv")
    days   = pd.read_csv("Data/Processed/by_day.csv")
    hours  = pd.read_csv("Data/Processed/by_hour.csv")
    county = pd.read_csv("Data/Processed/by_county.csv")
    users  = pd.read_csv("Data/Processed/by_road_users.csv")
    return trend, months, days, hours, county, users

trend, months, days, hours, county, users = load_data()

# ── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("🛣️ Filters")
    st.markdown("---")

    st.markdown("**📅 Year Selection**")
    selected_year = st.selectbox(
        "Focus Year",
        options=[2024, 2023, 2022, 2021, 2020],
        index=0
    )
    compare_year = st.selectbox(
        "Compare With",
        options=[2023, 2022, 2021, 2020, 2024],
        index=0
    )

    st.markdown("---")
    st.markdown("**📈 Trend Chart Range**")
    trend_range = st.slider(
        "Years",
        min_value=1960,
        max_value=2024,
        value=(1960, 2024)
    )

    st.markdown("---")
    st.markdown("**🏥 Injury Severity**")
    severity = st.selectbox(
        "Filter by Severity",
        options=["All", "Fatal", "Severe", "Slight"]
    )

    st.markdown("---")
    st.caption("Data: Transport Analysis (Trafa)")
    st.caption("Built by Hafsa Limama · Gothenburg")

# ── SEVERITY MAPPING ─────────────────────────────────────────────────────────
if severity == "Fatal":
    accident_col   = "fatal_accidents"
    severity_label = "Fatal"
elif severity == "Severe":
    accident_col   = "severe_accidents"
    severity_label = "Severe"
elif severity == "Slight":
    accident_col   = "slight_accidents"
    severity_label = "Slight"
else:
    accident_col   = "total_accidents"
    severity_label = "All"

# ── ROAD USER MAPPING ────────────────────────────────────────────────────────
user_map = {
    "Car Driver":  "car_driver",
    "Cyclist":     "cyclist",
    "Pedestrian":  "pedestrian",
    "Motorcycle":  "motorcycle",
    "Moped":       "moped",
}

# ── TITLE ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="
    background-image: url('https://assets.qz.com/media/a554f3b516c867346e42656531e2b5fa.jpg');
    background-size: cover;
    background-position: center;
    padding: 25px 20px;
    border-radius: 12px;
    margin-bottom: 20px;
">
    <div style="
        background-color: rgba(0,0,0,0.5);
        padding: 15px 25px;
        border-radius: 10px;
        display: inline-block;
    ">
        <h1 style="color: white; margin:0; font-size: 1.6em;">🇸🇪 Swedish Road Safety Dashboard</h1>
        <p style="color: #DDDDDD; margin:8px 0 0 0; font-size: 1.1em;">
            Official accident statistics · Focus year: <b>{selected_year}</b> · Source: Trafa
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# ── TABS ─────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview",
    "🕐 When?",
    "📍 Where?",
    "👥 Who?",
])

# ════════════════════════════════════════════════════════════════════════════
# TAB 1 — OVERVIEW
# ════════════════════════════════════════════════════════════════════════════
with tab1:
    st.header(f"📊 Overview — {selected_year} vs {compare_year}")

    yr      = trend[trend["year"] == selected_year].iloc[0]
    yr_prev = trend[trend["year"] == selected_year - 1]
    yr_cmp  = trend[trend["year"] == compare_year].iloc[0]

    def get_delta(current, prev_df, col):
        if prev_df.empty: return None
        prev = prev_df.iloc[0][col]
        return f"{((current - prev) / prev * 100):+.1f}% vs {selected_year - 1}"

    # ── KPI CARDS ────────────────────────────────────────────────────────────
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("💥 Total Accidents",
                  int(yr[accident_col]),
                  get_delta(yr[accident_col], yr_prev, accident_col),
                  delta_color="inverse")
    with col2:
        st.metric("☠️ Fatalities",
                  int(yr["killed"]) if severity in ["All", "Fatal"] else "—",
                  get_delta(yr["killed"], yr_prev, "killed") if severity in ["All", "Fatal"] else None,
                  delta_color="inverse")
    with col3:
        st.metric("🚑 Severely Injured",
                  int(yr["severely_injured"]) if severity in ["All", "Severe"] else "—",
                  get_delta(yr["severely_injured"], yr_prev, "severely_injured") if severity in ["All", "Severe"] else None,
                  delta_color="inverse")
    with col4:
        st.metric("🩹 Slightly Injured",
                  int(yr["slightly_injured"]) if severity in ["All", "Slight"] else "—",
                  get_delta(yr["slightly_injured"], yr_prev, "slightly_injured") if severity in ["All", "Slight"] else None,
                  delta_color="inverse")

    st.caption("""
    ℹ️ **Note:** Total Accidents = number of crash events.
    Injured figures = number of people hurt (multiple people can be injured in one accident,
    so injured counts may exceed total accidents).
    """)
    st.markdown("---")

    # ── COMPARE TWO YEARS ────────────────────────────────────────────────────
    st.subheader(f"📊 {selected_year} vs {compare_year} — Side by Side")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        diff = int(yr[accident_col]) - int(yr_cmp[accident_col])
        st.metric("💥 Accidents",
                  int(yr[accident_col]),
                  f"{diff:+d} vs {compare_year}",
                  delta_color="inverse")
    with c2:
        diff = int(yr["killed"]) - int(yr_cmp["killed"])
        st.metric("☠️ Fatalities",
                  int(yr["killed"]),
                  f"{diff:+d} vs {compare_year}",
                  delta_color="inverse")
    with c3:
        diff = int(yr["severely_injured"]) - int(yr_cmp["severely_injured"])
        st.metric("🚑 Severely Injured",
                  int(yr["severely_injured"]),
                  f"{diff:+d} vs {compare_year}",
                  delta_color="inverse")
    with c4:
        diff = int(yr["slightly_injured"]) - int(yr_cmp["slightly_injured"])
        st.metric("🩹 Slightly Injured",
                  int(yr["slightly_injured"]),
                  f"{diff:+d} vs {compare_year}",
                  delta_color="inverse")
    st.markdown("---")

    # ── TREND CHART ──────────────────────────────────────────────────────────
    df_range = trend[
        (trend["year"] >= trend_range[0]) &
        (trend["year"] <= trend_range[1])
    ]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_range["year"], y=df_range["killed"],
        mode="lines+markers", name="Fatalities",
        line=dict(color=RED, width=2.5), marker=dict(size=5)))
    fig.add_trace(go.Scatter(
        x=df_range["year"], y=df_range["severely_injured"],
        mode="lines+markers", name="Severely Injured",
        line=dict(color=ORANGE, width=2), marker=dict(size=4)))
    fig.add_trace(go.Scatter(
        x=df_range["year"], y=df_range[accident_col],
        mode="lines+markers", name=f"Accidents ({severity_label})",
        line=dict(color=GRAY, width=1.5, dash="dot"), marker=dict(size=3)))
    fig.add_vline(x=selected_year, line_dash="dash",
                  line_color=ACCENT, opacity=0.7,
                  annotation_text=f"Focus: {selected_year}")
    fig.add_vline(x=compare_year, line_dash="dot",
                  line_color=GREEN, opacity=0.7,
                  annotation_text=f"Compare: {compare_year}")
    fig.update_layout(
        title=f"Road Safety Trend ({trend_range[0]}–{trend_range[1]})",
        xaxis_title="Year", yaxis_title="Count",
        plot_bgcolor="white", paper_bgcolor="white",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
    )
    st.plotly_chart(fig, use_container_width=True)

    # ── VISION ZERO ──────────────────────────────────────────────────────────
    st.markdown("---")
    st.subheader("🎯 Vision Zero Progress")
    baseline  = trend[trend["year"] == 1990]["killed"].values[0]
    latest    = int(yr["killed"])
    reduction = (1 - latest / baseline) * 100
    st.markdown(f"""
    Sweden's **Vision Zero** policy launched in **1997** with the goal of
    zero road fatalities.
    - 📌 **1990 baseline:** {int(baseline):,} fatalities
    - 📌 **{selected_year}:** {latest:,} fatalities
    - ✅ **Reduction:** {reduction:.1f}% since 1990
    """)

    progress_df = trend[
        (trend["year"] >= 1990) &
        (trend["year"] <= 2024)
    ][["year", "killed"]].dropna()

    fig3 = px.bar(progress_df, x="year", y="killed",
                  color="killed",
                  color_continuous_scale=[[0, GREEN], [0.5, ORANGE], [1, RED]],
                  title="Annual Fatalities Since Vision Zero (1997)",
                  labels={"killed": "Fatalities", "year": "Year"})
    fig3.add_vline(x=1997, line_dash="dash", line_color=ACCENT,
                   annotation_text="Vision Zero launch 1997")
    fig3.add_vline(x=selected_year, line_dash="dot", line_color=ACCENT,
                   annotation_text=f"{selected_year}")
    fig3.update_layout(plot_bgcolor="white", paper_bgcolor="white",
                       coloraxis_showscale=False)
    st.plotly_chart(fig3, use_container_width=True)


# ════════════════════════════════════════════════════════════════════════════
# TAB 2 — WHEN?
# ════════════════════════════════════════════════════════════════════════════
with tab2:
    st.header("🕐 When Do Accidents Happen?")

    yr_months     = months[months["year"] == selected_year].sort_values("month_n")
    yr_months_cmp = months[months["year"] == compare_year].sort_values("month_n")
    yr_days       = days[days["year"] == selected_year].sort_values("day_n")
    yr_days_cmp   = days[days["year"] == compare_year].sort_values("day_n")
    yr_hours      = hours[hours["year"] == selected_year].copy()
    yr_hours_cmp  = hours[hours["year"] == compare_year].copy()

    col1, col2 = st.columns(2)
    with col1:
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=yr_months["month"], y=yr_months["accidents"],
            name=str(selected_year), marker_color=ACCENT))
        fig.add_trace(go.Bar(
            x=yr_months_cmp["month"], y=yr_months_cmp["accidents"],
            name=str(compare_year), marker_color=ORANGE, opacity=0.7))
        fig.update_layout(
            title="Accidents by Month",
            xaxis_title="Month", yaxis_title="Accidents",
            plot_bgcolor="white", paper_bgcolor="white",
            barmode="group", xaxis_tickangle=-30,
            legend=dict(orientation="h"))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        day_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        yr_days["day"] = pd.Categorical(yr_days["day"], categories=day_order, ordered=True)
        yr_days_cmp["day"] = pd.Categorical(yr_days_cmp["day"], categories=day_order, ordered=True)
        yr_days     = yr_days.sort_values("day")
        yr_days_cmp = yr_days_cmp.sort_values("day")

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=yr_days["day"], y=yr_days["accidents"],
            name=str(selected_year), marker_color=ACCENT))
        fig.add_trace(go.Bar(
            x=yr_days_cmp["day"], y=yr_days_cmp["accidents"],
            name=str(compare_year), marker_color=ORANGE, opacity=0.7))
        fig.update_layout(
            title="Accidents by Day of Week",
            xaxis_title="Day", yaxis_title="Accidents",
            plot_bgcolor="white", paper_bgcolor="white",
            barmode="group",
            legend=dict(orientation="h"))
        st.plotly_chart(fig, use_container_width=True)

    yr_hours["hour_start"]     = yr_hours["hour_slot"].str.extract(r"(\d+):").astype(int)
    yr_hours_cmp["hour_start"] = yr_hours_cmp["hour_slot"].str.extract(r"(\d+):").astype(int)
    yr_hours     = yr_hours.sort_values("hour_start")
    yr_hours_cmp = yr_hours_cmp.sort_values("hour_start")

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=yr_hours["hour_slot"], y=yr_hours["accidents"],
        name=str(selected_year), marker_color=ACCENT))
    fig.add_trace(go.Bar(
        x=yr_hours_cmp["hour_slot"], y=yr_hours_cmp["accidents"],
        name=str(compare_year), marker_color=ORANGE, opacity=0.7))
    fig.update_layout(
        title="Accidents by Hour of Day",
        xaxis_title="Time", yaxis_title="Accidents",
        plot_bgcolor="white", paper_bgcolor="white",
        barmode="group",
        legend=dict(orientation="h"))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("📅 All Years Comparison")
    fig = px.line(months.sort_values(["year","month_n"]),
                  x="month", y="accidents", color="year",
                  title="Monthly Accidents — All Years",
                  labels={"accidents":"Accidents","month":"Month"},
                  color_discrete_map={
                      2020: "#E74C3C",
                      2021: "#E67E22",
                      2022: "#F1C40F",
                      2023: "#27AE60",
                      2024: "#2D6A8F",
                  })
    fig.update_layout(plot_bgcolor="white", paper_bgcolor="white",
                      xaxis_tickangle=-30)
    st.plotly_chart(fig, use_container_width=True)


# ════════════════════════════════════════════════════════════════════════════
# TAB 3 — WHERE?
# ════════════════════════════════════════════════════════════════════════════
with tab3:
    st.header("📍 Where in Sweden?")

    yr_county     = county[county["year"] == selected_year].dropna(subset=["total_accidents"])
    yr_county_cmp = county[county["year"] == compare_year].dropna(subset=["total_accidents"])
    yr_county     = yr_county.sort_values("total_accidents", ascending=True)
    yr_county_cmp = yr_county_cmp.sort_values("total_accidents", ascending=True)

    col1, col2 = st.columns([3, 2])

    with col1:
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=yr_county["total_accidents"], y=yr_county["county"],
            orientation="h", name=str(selected_year),
            marker_color=ACCENT))
        fig.add_trace(go.Bar(
            x=yr_county_cmp["total_accidents"], y=yr_county_cmp["county"],
            orientation="h", name=str(compare_year),
            marker_color=ORANGE, opacity=0.7))
        fig.update_layout(
            title=f"Accidents by County — {selected_year} vs {compare_year}",
            xaxis_title="Accidents", yaxis_title="County",
            plot_bgcolor="white", paper_bgcolor="white",
            barmode="group", height=600,
            legend=dict(orientation="h"))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader(f"Top 5 Counties — {selected_year}")
        top5 = yr_county.sort_values("total_accidents", ascending=False).head(5)
        for _, row in top5.iterrows():
            name = row["county"].replace(" län", "")
            is_vg = "Västra Götaland" in row["county"]
            st.markdown(f"""
            **{"📍 " if is_vg else ""}{name}**
            - Accidents: **{int(row["total_accidents"])}**
            - Fatalities: **{int(row["killed"]) if not pd.isna(row["killed"]) else "N/A"}**
            {"*← Gothenburg's county*" if is_vg else ""}
            ---
            """)

    st.markdown("---")
    st.subheader("📈 County Trends Over Time")
    top_counties = county.groupby("county")["total_accidents"].sum().nlargest(6).index.tolist()
    df_top = county[county["county"].isin(top_counties)]
    fig = px.line(df_top, x="year", y="total_accidents", color="county",
                  title="Top 6 Counties — Accident Trend",
                  labels={"total_accidents":"Accidents","year":"Year"},
                  markers=True)
    fig.add_vline(x=selected_year, line_dash="dash", line_color=ACCENT,
                  annotation_text=str(selected_year))
    fig.add_vline(x=compare_year, line_dash="dot", line_color=ORANGE,
                  annotation_text=str(compare_year))
    fig.update_layout(plot_bgcolor="white", paper_bgcolor="white",
                      legend=dict(orientation="h", yanchor="bottom", y=1.02))
    st.plotly_chart(fig, use_container_width=True)


# ════════════════════════════════════════════════════════════════════════════
# TAB 4 — WHO?
# ════════════════════════════════════════════════════════════════════════════
with tab4:
    st.header("👥 Who Gets Hurt?")

    # Road user filter — inside Who tab only
    road_user = st.selectbox(
        "🔍 Filter by Road User",
        options=["All", "Car Driver", "Cyclist", "Pedestrian", "Motorcycle", "Moped"]
    )
    st.markdown("---")

    yr_users     = users[users["year"] == selected_year].iloc[0]
    yr_users_cmp = users[users["year"] == compare_year].iloc[0]

    labels = ["Car Driver","Car Passenger","Motorcycle","Moped","Cyclist","Pedestrian","Other"]
    cols   = ["car_driver","car_passenger","motorcycle","moped","cyclist","pedestrian","other"]

    values     = [yr_users.get(c, 0) for c in cols]
    values_cmp = [yr_users_cmp.get(c, 0) for c in cols]
    values     = [v if not pd.isna(v) else 0 for v in values]
    values_cmp = [v if not pd.isna(v) else 0 for v in values_cmp]

    # ── ROAD USER FILTER ─────────────────────────────────────────────────────
    if road_user != "All":
        st.subheader(f"🔍 Filtered: {road_user} — {selected_year} vs {compare_year}")
        col = user_map[road_user]
        filtered = users[["year", col]].copy()
        filtered.columns = ["year", "killed"]

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=filtered["year"], y=filtered["killed"],
            marker_color=[RED if y == selected_year else ORANGE for y in filtered["year"]],
            text=filtered["killed"], textposition="outside"))
        fig.update_layout(
            title=f"Fatalities — {road_user} (All Years)",
            xaxis_title="Year", yaxis_title="Fatalities",
            plot_bgcolor="white", paper_bgcolor="white")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("---")

    # ── DONUT CHARTS SIDE BY SIDE ────────────────────────────────────────────
    col1, col2 = st.columns(2)

    with col1:
        fig = go.Figure(go.Pie(
            labels=labels, values=values, hole=0.45,
            marker_colors=[ACCENT,"#5499C7",ORANGE,"#F0B27A",GREEN,"#A9DFBF",GRAY]))
        fig.update_layout(
            title=f"Fatalities by Road User — {selected_year}",
            annotations=[dict(text=f"{int(sum(values))}<br>total",
                              x=0.5, y=0.5, font_size=14, showarrow=False)])
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = go.Figure(go.Pie(
            labels=labels, values=values_cmp, hole=0.45,
            marker_colors=[ACCENT,"#5499C7",ORANGE,"#F0B27A",GREEN,"#A9DFBF",GRAY]))
        fig.update_layout(
            title=f"Fatalities by Road User — {compare_year}",
            annotations=[dict(text=f"{int(sum(values_cmp))}<br>total",
                              x=0.5, y=0.5, font_size=14, showarrow=False)])
        st.plotly_chart(fig, use_container_width=True)

    # ── TREND LINE ───────────────────────────────────────────────────────────
    user_long = users.melt(
        id_vars="year",
        value_vars=["car_driver","car_passenger","motorcycle","cyclist","pedestrian"],
        var_name="user_type", value_name="killed")
    user_long["user_type"] = user_long["user_type"].str.replace("_"," ").str.title()

    if road_user != "All":
        user_long = user_long[user_long["user_type"] == road_user]

    fig = px.line(user_long, x="year", y="killed", color="user_type",
                  markers=True,
                  title="Fatalities by Road User — Trend",
                  labels={"killed":"Fatalities","year":"Year","user_type":"Road User"})
    fig.add_vline(x=selected_year, line_dash="dash", line_color=ACCENT,
                  annotation_text=str(selected_year))
    fig.add_vline(x=compare_year, line_dash="dot", line_color=ORANGE,
                  annotation_text=str(compare_year))
    fig.update_layout(plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig, use_container_width=True)

    # ── KEY INSIGHTS ─────────────────────────────────────────────────────────
    st.markdown("---")
    st.subheader("💡 Key Insights")
    c1, c2, c3 = st.columns(3)
    total = sum(values)
    with c1:
        pct = round(yr_users.get("cyclist", 0) / total * 100, 1) if total > 0 else 0
        st.info(f"🚴 **Cyclists** represent **{pct}%** of fatalities in {selected_year}.")
    with c2:
        ped = int(yr_users.get("pedestrian", 0))
        st.warning(f"🚶 **{ped} pedestrians** killed in {selected_year}.")
    with c3:
        car = yr_users.get("car_driver", 0) + yr_users.get("car_passenger", 0)
        pct2 = round(car / total * 100, 1) if total > 0 else 0
        st.success(f"🚗 **Car occupants** make up **{pct2}%** of fatalities.")

# ── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#999; font-size:12px'>
    Data: <a href='https://www.trafa.se' target='_blank'>Transport Analysis (Trafa)</a> — Official Statistics of Sweden |
    Built by <b>Hafsa Limama</b> · Data Analyst · Gothenburg |
    Research at <b>Chalmers University of Technology</b>
</div>
""", unsafe_allow_html=True)