import streamlit as st
def page_3():
    st.title("Halaman 3")
    st.write('Menampilkan Halaman dari file MD (MarkDown)')
    
    with open('file page 3.md', 'r') as file:
        isi_teks = file.read()
    st.markdown(isi_teks)
    
