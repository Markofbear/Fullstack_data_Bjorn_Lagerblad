import streamlit as st
from frontend.kpi import ContentKPI, GeographyKPI, OSKPI, ExposureKPI 
from frontend.graphs import ViewsTrend
import os

def load_css(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("styles.css")

content_kpi = ContentKPI()
views_graph = ViewsTrend()
geography_kpi = GeographyKPI()
os_kpi = OSKPI()
exposure_kpi = ExposureKPI()

def layout():
    st.markdown("# The Data-Driven YouTuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")
    
    content_kpi.display_content()
    views_graph.display_plot() 
    geography_kpi.display_geography()
    os_kpi.display_os()
    exposure_kpi.display_exposure()  

if __name__ == "__main__":
    layout()
