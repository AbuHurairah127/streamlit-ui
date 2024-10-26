import streamlit as st

st.header("Buttons")

# Regular buttons
st.button("Hello World", type="secondary")
unsustained_output = st.button("Check Output")
st.write(unsustained_output)

# Set session state key only when button is clicked
if st.button("Check output 2 of sustained button"):
    st.session_state = "Button 2 clicked!"
    # st.write(st.session_state["button1"])
if st.button("Check output 3 of sustained button"):
    st.session_state = False
    # st.write(st.session_state["button1"])

st.button("Reset", type="primary")

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

# Print the current session state
st.write("Current Session State:")
st.write(st.session_state)
