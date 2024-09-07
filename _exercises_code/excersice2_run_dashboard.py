import subprocess
from pathlib import Path

if __name__ == "__main__":
    dashboard_path = Path(__file__).parent / "exercise2_streamlit_dashboard.py"
    subprocess.run(f"streamlit run {dashboard_path}", shell=True)