import streamlit as st
import views.views as views

SELECTION = ""

st.set_page_config(
    page_title="Dashboard Metode Mencari Akar",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Dashboard Metode Mencari Akar")

with st.sidebar:
    st.title("Menu")
    SELECTION = st.selectbox(
        "Pilih Metode",
        ("Homepage", "Bisection", "Regula Falsi", "Iterasi Sederhana", "Newton Raphson", "Secant")
    )

with st.container():
    if SELECTION == "Homepage":
        views.display_home()
    elif SELECTION == "Bisection":
        views.display_bisection()
    elif SELECTION == "Regula Falsi":
        views.display_regula_falsi()
    elif SELECTION == "Iterasi Sederhana":
        views.display_iterasi_sederhana()
    elif SELECTION == "Newton Raphson":
        views.display_newton_raphson()
    elif SELECTION == "Secant":
        views.display_secant()