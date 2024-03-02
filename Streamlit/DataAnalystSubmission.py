import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
st.title('Belajar Analisis Data')
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://scontent.cdninstagram.com/v/t51.2885-15/299994437_3880401438909035_6323677938800735950_n.webp?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDgweDEzNTAuc2RyIn0&_nc_ht=scontent.cdninstagram.com&_nc_cat=111&_nc_ohc=h2JKNW5WEfAAX-A88FC&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MjkwODk3MzI5ODg3NzM0NzQ4Mg%3D%3D.2-ccb7-5&oh=00_AfAQEx3jCEeFPsxCzqIyHAhFmSrgMXMD_VBRFh1oZSBoIQ&oe=65E64313&_nc_sid=10d13b")

col1, col2, col3 = st.columns(3)
 
with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")

with st.container():
    st.write("Inside the container")
    
    x = np.random.normal(15, 5, 250)
 
    fig, ax = plt.subplots()
    ax.hist(x=x, bins=15)
    st.pyplot(fig) 
 
st.write("Outside the container")
with st.expander("See explanation"):
    st.write(
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
        sunt in culpa qui officia deserunt mollit anim id est laborum.
        """
    )