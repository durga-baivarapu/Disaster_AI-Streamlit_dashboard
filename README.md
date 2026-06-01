# Disaster_AI-Streamlit_dashboard

Disaster_AI is an interactive Streamlit dashboard that combines cleaned USGS earthquake event data with machine-learning hazard scoring to compute event and regional priority indices.

The app delivers key decision support for emergency response by showing:

- event-level hazard KPIs
- priority-index distribution plots
- top-risk regional rankings
- predicted casualties and rescue task estimates

It is designed for local deployment, easy customization, and rapid inspection of earthquake risk intelligence.

## Features

- Interactive magnitude range filtering
- Dynamic KPI summary cards
- Histogram of priority index risk distribution
- Ranked top 10 high-priority regions table
- Bar chart visualization of region priority scores
- Easy-to-run Streamlit dashboard for disaster planning

## Installation

1. Create and activate a virtual environment:

   Windows (PowerShell):
   ```powershell
   python -m venv menv
   & "menv\Scripts\python.exe" -m pip install --upgrade pip
   & "menv\Scripts\python.exe" -m pip install -r req.txt
   ```

   macOS / Linux:
   ```bash
   python3 -m venv menv
   source menv/bin/activate
   pip install --upgrade pip
   pip install -r req.txt
   ```

2. Run the dashboard:

   ```powershell
   & "menv\Scripts\python.exe" -m streamlit run app.py
   ```

## Data

The dashboard loads the cleaned datasets from the `outputs/` folder:

- `hazard_scores_cleaned.csv`
- `regional_demand_cleaned.csv`

> Tip: Update `app.py` to use relative paths if you move the project to another location.

## Project Structure

- `app.py` — Streamlit application file
- `req.txt` — dependency requirements
- `Dataset/` — raw earthquake input data files
- `outputs/` — cleaned CSV files used by the dashboard
- `menv/` — virtual environment folder (ignored by `.gitignore`)

## Notes

- Keep `menv/` out of the repository; it is already excluded in `.gitignore`.
- If you want to publish this to GitHub, create a repository and push the project from your local folder.

## License

This project is provided as-is. Add a `LICENSE` file if you want to publish under a specific license.

