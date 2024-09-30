import streamlit as st  # Make sure to import streamlit
from frontend.kpi import ContentKPI, GeographyKPI, OSKPI
from frontend.graphs import ViewsTrend

# Initialize the KPI classes
content_kpi = ContentKPI()
geography_kpi = GeographyKPI()
os_kpi = OSKPI()
views_graph = ViewsTrend()

def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")
    
    # Display KPIs
    content_kpi.display_content()
    geography_kpi.display_geography()
    os_kpi.display_os()
    views_graph.display_plot()

if __name__ == "__main__":
    layout()
