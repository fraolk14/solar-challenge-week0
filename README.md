# ☀️ Solar Energy Data Analysis — Benin, Sierra Leone, and Togo

This repository contains an end-to-end data analysis project focused on evaluating solar energy potential across three West African countries: **Benin**, **Sierra Leone**, and **Togo**.

---

## 📘 Project Overview
MoonLight Energy Solutions aims to identify high-potential regions for solar farm installations to enhance sustainability and operational efficiency.  
As part of this challenge, we perform:
- Data cleaning and preprocessing.
- Exploratory Data Analysis (EDA).
- Cross-country comparison and visualization.
- Interactive dashboard development using Streamlit.

----

## 🗂️ Project Structure

```
solar-challenge-week0/
├── app/
│   ├── main.py          # Streamlit dashboard for visualization
│   ├── utils.py         # Helper functions (data loading & plotting)
├── data/
│   ├── raw/
│   │   ├── benin-malanville.csv
│   │   ├── sierraleone-bumbuna.csv
│   │   └── togo-dapaong_qc.csv
│   ├── benin_clean.csv
│   ├── sierra_clean.csv
│   └── togo_clean.csv
├── notebooks/
│   ├── clean_benin.ipynb
│   ├── clean_sierra.ipynb
│   ├── clean_togo.ipynb
│   ├── explore_benin.ipynb
│   ├── explore_sierra.ipynb
│   ├── explore_togo.ipynb
│   └── compare_countries.ipynb
├── scripts/
│   └── README.md
├── requirements.txt
└── README.md
```

---

## ⚙️ Task 1: Data Cleaning

**Objective:** Prepare and clean raw solar irradiance datasets for each country.

**Branch:** `data-cleaning`  
**Notebook:** `notebooks/clean_<country>.ipynb`

### Steps:
1. Import and inspect datasets.
2. Handle missing values and convert timestamp columns.
3. Detect and remove outliers using Z-scores.
4. Rename and format key columns (`GHI`, `DNI`, `DHI`, `Tamb`, `RH`).
5. Export cleaned data to `/data/` directory (excluded in `.gitignore`).

---

## 📊 Task 2: Exploratory Data Analysis (EDA)

**Objective:** Explore solar irradiance patterns per country to understand potential.

**Branch:** `eda-<country>`  
**Notebook:** `notebooks/<country>_eda.ipynb`

### Steps:
- Generate descriptive statistics (`df.describe()` and `df.isna().sum()`).
- Visualize irradiance trends (GHI, DNI, DHI vs time).
- Identify correlations between variables (e.g., `RH` vs `Tamb`).
- Analyze the impact of panel cleaning and wind variations.
- Create bubble charts, histograms, and heatmaps.

---

## 🌍 Task 3: Cross-Country Comparison

**Objective:** Compare Benin, Sierra Leone, and Togo to identify high-potential solar regions.

**Branch:** `compare-countries`  
**Notebook:** `compare_countries.ipynb`

### Steps:
1. Load cleaned datasets for all countries.
2. Create summary tables (mean, median, std for GHI, DNI, DHI).
3. Visualize using boxplots and bar charts.
4. Perform ANOVA test for GHI differences across countries.
5. Summarize key insights:
   - Benin: Highest average GHI, good consistency.
   - Sierra Leone: More variability due to humidity.
   - Togo: Stable but lower irradiance overall.

---

## 💡 Task 4 (Bonus): Interactive Streamlit Dashboard

**Branch:** `dashboard-dev`  
**Files:** `app/main.py`, `app/utils.py`

### Features:
- Country selection dropdown (Benin, Sierra Leone, Togo).
- Boxplots for GHI and DNI comparison.
- Summary statistics table.
- Dynamic visualizations using Seaborn and Matplotlib.

### Example Commands
```bash
# Run Streamlit app
cd app
streamlit run main.py
```

Ensure your working directory allows `app/utils.py` to find `../data/...`.  
If not, adjust `DATA_DIR` in `utils.py` accordingly.

---

## 🧰 Tools and Technologies

| Category | Tools Used |
|-----------|-------------|
| IDE | Visual Studio Code |
| Version Control | Git, GitHub |
| Programming Language | Python 3.x |
| Data Analysis | Pandas, NumPy, SciPy |
| Visualization | Matplotlib, Seaborn |
| Dashboard | Streamlit |
| Statistical Tests | ANOVA, Kruskal–Wallis |

---

## 🧾 Git Workflow

| Task | Branch | Description |
|------|---------|-------------|
| Task 1 | `data-cleaning` | Data preprocessing and cleaning |
| Task 2 | `eda-<country>` | Exploratory data analysis |
| Task 3 | `compare-countries` | Multi-country statistical comparison |
| Task 4 | `dashboard-dev` | Streamlit app for visualization |

### Example Commands
```bash
# Create a new branch for EDA
git checkout -b eda-benin

# Commit changes
git add .
git commit -m "feat: added EDA notebook for Benin"

# Push to GitHub
git push origin eda-benin
```

---

## 📈 Key Insights Summary

| Country | Avg GHI | Variability | Solar Potential |
|----------|----------|--------------|-----------------|
| **Benin** | High | Moderate | ⭐⭐⭐⭐ |
| **Sierra Leone** | Moderate | High | ⭐⭐⭐ |
| **Togo** | Steady | Low | ⭐⭐⭐⭐ |

**Conclusion:**  
Benin and Togo demonstrate promising solar conditions with consistent irradiance patterns. Sierra Leone shows potential but with higher variability due to humidity.

---

## 🕓 Project Duration
**05 Nov - 12 Nov 2025**

**Author:** Fraol Kuma (@fraolk14)  
**Institution:** 10 Academy — Artificial Intelligence Mastery Challenge  
**Challenge:** *Solar Data Discovery: Week 0*  
**Generated on:** 12 November 2025
