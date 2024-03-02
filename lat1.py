import streamlit as st
import pandas as pd

st.write("coding club 2024")
df = pd.DataFrame({
    'No' : [1,2,3,4],
    'Nama' : ['Timothy','Vino','Aqda','Randy'],
    'Nilai' : [98, 90, 92, 93]
})

df
