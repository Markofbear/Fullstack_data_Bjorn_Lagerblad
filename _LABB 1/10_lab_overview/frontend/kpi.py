import streamlit as st
import plotly.express as px
import pycountry
from utils.query_database import QueryDatabase

# Klassen för "KPIer för videor"
class ContentKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time;").df

    def display_content(self):
        df = self._content 
        st.markdown("## KPIer för videor") # Första rubriken

        # dictionary för KPI
        kpis = {
            "videor": len(df),  
            "visade timmar": df["Visningstid_timmar"].sum(),  
            "prenumeranter": df["Prenumeranter"].sum(), 
            "exponeringar": df["Exponeringar"].sum(), 
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col: 
                st.metric(kpi, round(kpis[kpi]))  # Rundar av värdet
        st.dataframe(df)  


class DeviceKPI:
    pass


# Konverterar ISO-2 landskoder till ISO-3
def convert_iso2_to_iso3(iso2):
    try:
        return pycountry.countries.get(alpha_2=iso2).alpha_3
    except AttributeError:
        return None


# Klass för min Geography KPI
class GeographyKPI:
    def __init__(self) -> None:
        # Hämtar information från databasen, fungerade endast med en sum här istället för direkt till marts
        self._geography = QueryDatabase("SELECT * FROM marts.geography_summary;").df

    def display_geography(self):
        df = self._geography  # Sparar

        st.markdown("## Geografiska KPIer") 

        total_views = df["Total visningar"].sum()  # Beräkning/summering av totala visningar
        df["percent_of_total"] = (df["Total visningar"] / total_views) * 100  # Beräkna procentandel av total

        st.metric("Totala visningar", total_views)  
        st.metric("Antal länder", len(df))  

        # Döper om kolumnerna
        df_display = df.rename(columns={
            "country_code": "Land",  
            "Total visningar": "Totala visningar",  
            "percent_of_total": "Procent av totalt"  
        })

        # Lägger till ISO-3
        df_display["ISO-3"] = df_display["Land"].apply(convert_iso2_to_iso3)

        st.dataframe(df_display[['Land', 'Totala visningar', 'Procent av totalt']])  

        # Skapar choropleth
        fig = px.choropleth(
            df_display,
            locations="ISO-3",  
            locationmode="ISO-3",  
            color="Totala visningar",  # FÄrg baserat på totala visningar
            hover_name="Land",  # Landsnamn vid hover av pekare
            color_continuous_scale=px.colors.sequential.Plasma,  # Färgskala
            labels={"Totala visningar": "Totala visningar"},  
            title="Totala visningar per Land" 
        )

        st.plotly_chart(fig) 


class OSKPI:
    def __init__(self) -> None:
        self._os = QueryDatabase("SELECT * FROM marts.os;").df

    def display_os(self):
        df = self._os 
        
        st.markdown("## Operativsystem")

        os_options = df["Operativsystem"].unique()  # Unika os
        selected_os = st.selectbox("Välj Operativsystem", options=os_options)  # Dropdown för val av os

        if selected_os:
            os_info = df[df["Operativsystem"] == selected_os].iloc[0]  

            st.write(f"**Operativsystem:** {os_info['Operativsystem']}")
            st.write(f"**Totalt antal visningar:** {os_info['Genomsnitt visningar']}")
            st.write(f"**Genomsnittlig visningstid:** {os_info['Genomsnittliga visningar']}")
            st.write(f"**Procent av totalt:** {os_info['Procent av totalt']}%")

        kpis = {
            "Antal operativsystem": len(df),  # Antal olika os
            "Totalt antal visningar": df["Genomsnitt visningar"].sum(),  
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col: 
                st.metric(kpi, round(kpis[kpi])) 

        df_display = df.rename(columns={
            "Genomsnitt visningar": "Totalt antal visningar",  
            "Genomsnittliga visningar": "Genomsnittlig visningstid",
            "Procent av totalt": "Procent av totalt"
        })

        st.dataframe(df_display)  

        # stapeldiagram
        fig = px.bar(
            df_display,
            x="Operativsystem", 
            y="Totalt antal visningar", 
            title="Totala visningar per Operativsystem",  
            labels={"Operativsystem": "Operativsystem", "Totalt antal visningar": "Visningar"}, 
            color="Procent av totalt"  
        )

        # transparence på staplarna
        fig.for_each_trace(lambda t: t.update(marker=dict(opacity=0.5) if t.name != selected_os else dict(opacity=1)))

        st.plotly_chart(fig) 


class ExposureKPI:
    def __init__(self) -> None:
        self._exposure = QueryDatabase("SELECT * FROM marts.exposure;").df 

    def display_exposure(self):
        df = self._exposure  

        st.markdown("## Exponeringar KPI")  

        total_exposures = df["Exponeringar"].sum() 
        average_click_rate = df["Klickfrekvens"].mean()

        kpis = {
                "Totala exponeringar": total_exposures, 
                "Genomsnittlig klickfrekvens": average_click_rate,
            }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
                with col: 
                    st.metric(kpi, round(kpis[kpi], 2))

        st.dataframe(df[['Exponeringar', 'Klickfrekvens']]) 





