# 🇸🇪 Swedish Road Safety Dashboard

[![Streamlit App](https://img.shields.io/badge/Live_Demo-Streamlit-red?logo=streamlit)](REPLACE_WITH_YOUR_STREAMLIT_URL)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-green?logo=pandas)](https://pandas.pydata.org)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive_Charts-purple?logo=plotly)](https://plotly.com)

An interactive data dashboard analysing **5 years of official Swedish road accident statistics (2020–2024)** from Transport Analysis (Trafa), combined with a **65-year fatality trend (1960–2024)** tracking Sweden's Vision Zero progress.

> 🔗 **[View Live Dashboard](https://swedish-road-safety-dashboard-n.streamlit.app/)**

---

## 📌 Project Motivation

Sweden's **Vision Zero** policy, launched in 1997, aims to eliminate all road fatalities and serious injuries. This dashboard tracks progress toward that goal using official government statistics, making the data accessible and interactive for anyone interested in road safety trends.

This project was developed alongside crash safety research at **Chalmers University of Technology**, where I work with large-scale accident datasets to study injury severity and road safety outcomes.

---

## 📊 Dashboard Features

| Tab | What it shows |
|-----|--------------|
| 📊 Overview | KPI cards, long-term trend (1960–2024), Vision Zero progress, year comparison |
| 🕐 When? | Monthly patterns, weekday analysis, hourly breakdown — compare two years |
| 📍 Where? | Accident rankings by Swedish county, top 5 counties, trend over time |
| 👥 Who? | Fatalities by road user type, donut charts, year comparison |

### 🎛️ Interactive Filters
- **Focus Year** — select any year from 2020–2024
- **Compare With** — compare two years side by side across all charts
- **Trend Range** — adjust the historical trend from 1960–2024
- **Injury Severity** — filter by Fatal, Severe, Slight or All
- **Road User** — filter Who tab by Car Driver, Cyclist, Pedestrian, Motorcycle or Moped

---

## 🔍 Key Findings

- 📉 Road fatalities in Sweden dropped **over 70% since 1990** — Vision Zero is working
- ☀️ **Summer months (May–August)** consistently show the highest accident rates
- 📆 **Friday and Saturday** are the most dangerous days of the week
- 🕓 **Afternoon rush hour (14:00–18:00)** has the highest accident concentration
- 🚗 **Car drivers** account for the largest share of fatalities
- 🚴 **Cyclists and pedestrians** are the most vulnerable road users despite lower numbers

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Core language |
| **pandas** | Data cleaning and transformation |
| **Plotly** | Interactive charts |
| **Streamlit** | Dashboard framework |
| **openpyxl** | Reading official .xlsx files |
| **Jupyter Notebook** | Data exploration and cleaning |

---

## 📁 Project Structure
```
swedish-road-safety-dashboard/
│
├── app.py                    ← Streamlit dashboard (4 tabs)
├── requirements.txt          ← Python dependencies
├── README.md
│
├── Data/
│   └── Processed/            ← Clean CSVs used by dashboard
│       ├── trend.csv         ← Fatalities 1960–2024
│       ├── by_month.csv      ← Accidents by month
│       ├── by_day.csv        ← Accidents by weekday
│       ├── by_hour.csv       ← Accidents by hour
│       ├── by_county.csv     ← Accidents by Swedish county
│       └── by_road_users.csv ← Fatalities by road user type
│
└── Notebooks/
    └── 01_data_cleaning.ipynb ← Full data exploration and cleaning
```

---

## 🚀 Run Locally
```bash
# 1. Clone the repo
git clone https://github.com/hafssalimama-alt/swedish-road-safety-dashboard
cd swedish-road-safety-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the dashboard
streamlit run app.py
```

---

## 📂 Data Source

Official statistics from **Transport Analysis (Trafa)**, Sweden's government transport authority.

🔗 [https://www.trafa.se/en/road-traffic/road-traffic-injuries/](https://www.trafa.se/en/road-traffic/road-traffic-injuries/)

Files used: `vagtrafikskador-2020` through `vagtrafikskador-2024` (.xlsx format)

Each file contains 32 sheets with detailed breakdowns by:
- Month, weekday and hour
- Swedish county (21 counties)
- Road user type
- Injury severity
- Age and gender

---

## 👩‍💻 Author

**Hafsa Limama** · Data Analyst · Gothenburg, Sweden

🔗 [LinkedIn](https://www.linkedin.com/in/hafsa-limama-036939279)
🐙 [GitHub](https://github.com/hafssalimama-alt)

---

## 🎯 Future Improvements

- Add age and gender breakdown analysis
- Include population-adjusted accident rates per county
- Add predictive modelling for accident risk
- Expand dataset to include pre-2020 detailed data)**

---

## 📌 Project Motivation

Sweden's **Vision Zero** policy, launched in 1997, aims to eliminate all road fatalities and serious injuries. This dashboard tracks progress toward that goal using official government statistics, making the data accessible and interactive for anyone interested in road safety trends.

This project was developed alongside crash safety research at **Chalmers University of Technology**, where I work with large-scale accident datasets to study injury severity and road safety outcomes.

---

## 📊 Dashboard Features

| Tab | What it shows |
|-----|--------------|
| 📊 Overview | KPI cards, long-term trend (1960–2024), Vision Zero progress, year comparison |
| 🕐 When? | Monthly patterns, weekday analysis, hourly breakdown — compare two years |
| 📍 Where? | Accident rankings by Swedish county, top 5 counties, trend over time |
| 👥 Who? | Fatalities by road user type, donut charts, year comparison |

### 🎛️ Interactive Filters
- **Focus Year** — select any year from 2020–2024
- **Compare With** — compare two years side by side across all charts
- **Trend Range** — adjust the historical trend from 1960–2024
- **Injury Severity** — filter by Fatal, Severe, Slight or All
- **Road User** — filter Who tab by Car Driver, Cyclist, Pedestrian, Motorcycle or Moped

---

## 🔍 Key Findings

- 📉 Road fatalities in Sweden dropped **over 70% since 1990** — Vision Zero is working
- ☀️ **Summer months (May–August)** consistently show the highest accident rates
- 📆 **Friday and Saturday** are the most dangerous days of the week
- 🕓 **Afternoon rush hour (14:00–18:00)** has the highest accident concentration
- 🚗 **Car drivers** account for the largest share of fatalities
- 🚴 **Cyclists and pedestrians** are the most vulnerable road users despite lower numbers

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Core language |
| **pandas** | Data cleaning and transformation |
| **Plotly** | Interactive charts |
| **Streamlit** | Dashboard framework |
| **openpyxl** | Reading official .xlsx files |
| **Jupyter Notebook** | Data exploration and cleaning |

---

## 📁 Project Structure
```
swedish-road-safety-dashboard/
│
├── app.py                    ← Streamlit dashboard (4 tabs)
├── requirements.txt          ← Python dependencies
├── README.md
│
├── Data/
│   └── Processed/            ← Clean CSVs used by dashboard
│       ├── trend.csv         ← Fatalities 1960–2024
│       ├── by_month.csv      ← Accidents by month
│       ├── by_day.csv        ← Accidents by weekday
│       ├── by_hour.csv       ← Accidents by hour
│       ├── by_county.csv     ← Accidents by Swedish county
│       └── by_road_users.csv ← Fatalities by road user type
│
└── Notebooks/
    └── 01_data_cleaning.ipynb ← Full data exploration and cleaning
```

---

## 🚀 Run Locally
```bash
# 1. Clone the repo
git clone https://github.com/hafssalimama-alt/swedish-road-safety-dashboard
cd swedish-road-safety-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the dashboard
streamlit run app.py
```

---

## 📂 Data Source

Official statistics from **Transport Analysis (Trafa)**, Sweden's government transport authority.

🔗 [https://www.trafa.se/en/road-traffic/road-traffic-injuries/](https://www.trafa.se/en/road-traffic/road-traffic-injuries/)

Files used: `vagtrafikskador-2020` through `vagtrafikskador-2024` (.xlsx format)

Each file contains 32 sheets with detailed breakdowns by:
- Month, weekday and hour
- Swedish county (21 counties)
- Road user type
- Injury severity
- Age and gender

---

## 👩‍💻 Author

**Hafsa Limama** · Data Analyst · Gothenburg, Sweden

🔗 [LinkedIn](https://www.linkedin.com/in/hafsa-limama-036939279)
🐙 [GitHub](https://github.com/hafssalimama-alt)

---

## 🎯 Future Improvements

- Add age and gender breakdown analysis
- Include population-adjusted accident rates per county
- Add predictive modelling for accident risk
- Expand dataset to include pre-2020 detailed data)**

---

## 📌 Project Motivation

Sweden's **Vision Zero** policy, launched in 1997, aims to eliminate all road fatalities and serious injuries. This dashboard tracks progress toward that goal using official government statistics, making the data accessible and interactive for anyone interested in road safety trends.

This project was developed alongside crash safety research at **Chalmers University of Technology**, where I work with large-scale accident datasets to study injury severity and road safety outcomes.

---

## 📊 Dashboard Features

| Tab | What it shows |
|-----|--------------|
| 📊 Overview | KPI cards, long-term trend (1960–2024), Vision Zero progress, year comparison |
| 🕐 When? | Monthly patterns, weekday analysis, hourly breakdown — compare two years |
| 📍 Where? | Accident rankings by Swedish county, top 5 counties, trend over time |
| 👥 Who? | Fatalities by road user type, donut charts, year comparison |

### 🎛️ Interactive Filters
- **Focus Year** — select any year from 2020–2024
- **Compare With** — compare two years side by side across all charts
- **Trend Range** — adjust the historical trend from 1960–2024
- **Injury Severity** — filter by Fatal, Severe, Slight or All
- **Road User** — filter Who tab by Car Driver, Cyclist, Pedestrian, Motorcycle or Moped

---

## 🔍 Key Findings

- 📉 Road fatalities in Sweden dropped **over 70% since 1990** — Vision Zero is working
- ☀️ **Summer months (May–August)** consistently show the highest accident rates
- 📆 **Friday and Saturday** are the most dangerous days of the week
- 🕓 **Afternoon rush hour (14:00–18:00)** has the highest accident concentration
- 🚗 **Car drivers** account for the largest share of fatalities
- 🚴 **Cyclists and pedestrians** are the most vulnerable road users despite lower numbers

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Core language |
| **pandas** | Data cleaning and transformation |
| **Plotly** | Interactive charts |
| **Streamlit** | Dashboard framework |
| **openpyxl** | Reading official .xlsx files |
| **Jupyter Notebook** | Data exploration and cleaning |

---

## 📁 Project Structure
```
swedish-road-safety-dashboard/
│
├── app.py                    ← Streamlit dashboard (4 tabs)
├── requirements.txt          ← Python dependencies
├── README.md
│
├── Data/
│   └── Processed/            ← Clean CSVs used by dashboard
│       ├── trend.csv         ← Fatalities 1960–2024
│       ├── by_month.csv      ← Accidents by month
│       ├── by_day.csv        ← Accidents by weekday
│       ├── by_hour.csv       ← Accidents by hour
│       ├── by_county.csv     ← Accidents by Swedish county
│       └── by_road_users.csv ← Fatalities by road user type
│
└── Notebooks/
    └── 01_data_cleaning.ipynb ← Full data exploration and cleaning
```

---

## 🚀 Run Locally
```bash
# 1. Clone the repo
git clone https://github.com/hafssalimama-alt/swedish-road-safety-dashboard
cd swedish-road-safety-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the dashboard
streamlit run app.py
```

---

## 📂 Data Source

Official statistics from **Transport Analysis (Trafa)**, Sweden's government transport authority.

🔗 [https://www.trafa.se/en/road-traffic/road-traffic-injuries/](https://www.trafa.se/en/road-traffic/road-traffic-injuries/)

Files used: `vagtrafikskador-2020` through `vagtrafikskador-2024` (.xlsx format)

Each file contains 32 sheets with detailed breakdowns by:
- Month, weekday and hour
- Swedish county (21 counties)
- Road user type
- Injury severity
- Age and gender

---

## 👩‍💻 Author

**Hafsa Limama** · Data Analyst · Gothenburg, Sweden

🔗 [LinkedIn](https://www.linkedin.com/in/hafsa-limama-036939279)
🐙 [GitHub](https://github.com/hafssalimama-alt)

---

## 🎯 Future Improvements

- Add age and gender breakdown analysis
- Include population-adjusted accident rates per county
- Add predictive modelling for accident risk
- Expand dataset to include pre-2020 detailed data
