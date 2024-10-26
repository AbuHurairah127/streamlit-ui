import streamlit as st

if "xyz" not in st.session_state:
    st.session_state["xyz"] = "Abu Hurairah is testing streamlit"


st.write(st.session_state.xyz)