import streamlit as st
if "shared" not in st.session_state:
   st.session_state["shared"] = True

st.set_page_config(
    page_title="Heart Rate Predictions by Adriana Machado",
    page_icon="🚲",
)

st.markdown("### Homepage and README")
st.sidebar.header("Homepage and README")

st.title("Welcome to Adriana Machado's Cycling Predictions Project!")