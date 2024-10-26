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
st.text_input("Favorite movie?")

text_contents = '''This is some text'''
st.download_button("Download some text", text_contents)


import streamlit as st

with open("pic.png", "rb") as file:
    btn = st.download_button(
        label="Download image",
        data=file,
        file_name="pic.png",
        mime="image/png",
    )
    import streamlit as st

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("faces")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")