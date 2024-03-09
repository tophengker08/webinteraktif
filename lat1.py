import streamlit as st
from page1 import page_1
from page2 import page_2
from page3 import page_3
from kalkulatorsegitiga import kalkulatorsegitiga
from testimoni import testimoni
from image1 import main

# import pandas as pd

# st.write("coding club 2024")
# df = pd.DataFrame({
#     'No' : [1,2,3,4],
#     'Nama' : ['Timothy','Vino','Aqda','Randy'],
#     'Nilai' : [98, 90, 92, 93]
# })

# df



PAGES = {
    "Home" : page_1,
    "Tontonan" : page_2,
    "Contoh" : page_3,
    "Kalkulatorsegitiga" : kalkulatorsegitiga,
    "Testimoni" : testimoni,
    "Convert Foto" : main
    }
    
st.sidebar.image("foto image.jpg", width=300)
page = st.sidebar.radio("Halaman", list(PAGES.keys()))
PAGES[page]()

