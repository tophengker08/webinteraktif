import streamlit as st 
def kalkulatorsegitiga():
    st.title('Kalkulator Hitung Segitiga')
    panjang = st.number_input("Masukan Nilai Panjang", 0)
    lebar = st.number_input("masukan Nilai Lebar", 0)
    hitung = st.button("Hitung Luas")
    
    if hitung:
        luas = panjang * lebar /2
        st.success(f"Luas Segitiga adalah={luas}")
    