import streamlit as st
from utils.query_database import QueryDatabase

class ContentKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time;").df

    def display_content(self):
        df = self._content
        st.markdown("## KPIer för videor")
        st.markdown("Nedan visas KPIer för totalt antal")

        kpis = {
            "videor": len(df),
            "visade timmar": df["Visningstid_timmar"].sum(),
            "prenumeranter": df["Prenumeranter"].sum(),
            "exponeringar": df["Exponeringar"].sum(),
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col: 
                st.metric(kpi, round(kpis[kpi]))
        st.dataframe(df)

# create more KPIs here
class DeviceKPI:
    pass 


class GeographyKPI:
    def __init__(self) -> None:
        self._geography = QueryDatabase("SELECT * FROM marts.geography_summary;").df

    def display_geography(self):
        df = self._geography 
        st.markdown("## Info över länder")

        kpis = {
            "antal länder": len(df),
            "totalt antal visningar": df["Total visningar"].sum(),
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col:
                st.metric(kpi, round(kpis[kpi]))

        df_display = df.rename(columns={
            "country_code": "Landskod",
            "percent_of_total": "Antal i procent"
        })

        st.dataframe(df_display)

class OSKPI:
    def __init__(self) -> None:
        self._os = QueryDatabase("SELECT * FROM marts.os;").df

    def display_os(self):
        df = self._os
        st.markdown("## KPIer för Operativsystem")
        st.markdown("Nedan visas KPIer för operativsystem")

        kpis = {
            "antal operativsystem": len(df),
            "totalt antal visningar": df["sum_visningar"].sum(),
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col: 
                st.metric(kpi, round(kpis[kpi]))

        st.dataframe(df)