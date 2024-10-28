# import streamlit as st

# # Headings
# st.title("Main Heading")
# st.header("Subheading")
# st.subheader("Another Subheading")

# # Paragraph
# st.write("This is a paragraph in Streamlit. You can use `st.write()` to add text, markdown, and even HTML if necessary.")

# -----------------------------------
# ## Example 2
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 5), columns=(["Width","Height","Depth","Weight","radius"])
)

st.table(df)






# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: red !important;
        color: blue;
    }
    </style>
    """, unsafe_allow_html=True)

# Content
st.title("Styled Streamlit App")
st.write("This text should appear in blue with a red background.")
x=st.text_input("Favorite movie?")
st.write(x)
text_contents = '''This is some text'''
st.download_button("Download some text", text_contents)


import streamlit as st

with open("pic.png", "rb") as file:
    btn = st.download_button(
        label="Download image",
        data=file,
        file_name="AbuHurairah.png",
        mime="image/png",
    )

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

# st.feedback("faces")


a=st.number_input("Enter first number:")
st.session_state["firstNo"] = a
b=st.number_input("Enter 2nd number:")
st.session_state["scndNo"] = b

if st.button("Add two no."):
    st.session_state["Ans"] = a+b
    st.write(st.session_state.Ans)
if st.button("Subtract two no."):
    st.session_state["Ans"] = a-b
    st.write(st.session_state.Ans)
if st.button("Multiply two no."):
    st.session_state["Ans"] = a*b
    st.write(st.session_state.Ans)