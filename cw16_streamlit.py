import streamlit as st
from PIL import Image

st.title("My Resume")
st.header("Jacob Boetig")

st.divider()

col1, col2 = st.columns((4,5))

with col1:
    st.markdown("**About Me**")
    st.text("I am a computer scientist, a student, and a lover of boardgames.")

with col2:
    image = Image.open('captain_america.jpg')
    st.image(image, width=200)

st.divider()

col3, col4, col5 = st.columns((4,5))
with col3:
    st.markdown("**Work Experience**")
    st.text("I have work experince as a entraprenuor and as both a sacker and slicer.")

with col4:
    st.markdown("**Projects**")
    st.text("My projects are coding a library app and calculus homework.")

with col5:
    st.markdown("**Hobbies**")
    st.text("My hobbies are boardgames and reading books.")


