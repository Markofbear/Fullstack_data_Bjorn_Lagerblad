import streamlit as st  # Make sure to import streamlit
from frontend.kpi import ContentKPI, GeographyKPI, OSKPI, ExposureKPI 
from frontend.graphs import ViewsTrend

content_kpi = ContentKPI()
views_graph = ViewsTrend()
geography_kpi = GeographyKPI()
os_kpi = OSKPI()
exposure_kpi = ExposureKPI()


def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")
    
    # Display KPIs
    content_kpi.display_content()
    geography_kpi.display_geography()
    os_kpi.display_os()
    exposure_kpi.display_exposure()  # Add this line to display exposure KPIs
    views_graph.display_plot()

if __name__ == "__main__":
    layout()
