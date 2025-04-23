import streamlit as st
import controllers.methods as methods

def display_bisection():
    st.subheader("Metode Bisection")
    st.write("Metode Bisection adalah metode numerik untuk mencari akar dari fungsi dengan cara membagi interval menjadi dua bagian dan memilih bagian yang mengandung akar.")
    
    # Input for function
    func = st.text_input("Masukkan fungsi (dalam x):", "x**2 - 4")
    
    # Input for interval
    a = st.number_input("Masukkan nilai a:", value=0.0)
    b = st.number_input("Masukkan nilai b:", value=5.0)
    
    # Input for error tolerance
    e = st.number_input("Masukkan toleransi kesalahan (e):", value=0.01)
    
    hasil = st.empty()
    
    if st.button("Hitung"):
        result = methods.biseksi(a, b, func, e)
        hasil.write(f"Hasil Akar : {result}")
        
def display_regula_falsi():
    st.subheader("Metode Regula Falsi")
    st.write("Metode Regula Falsi adalah metode numerik untuk mencari akar dari fungsi dengan cara menggunakan garis lurus antara dua titik pada grafik fungsi.")
    
    # Input for function
    f_x = st.text_input("Masukkan fungsi (dalam x):", "x**2 - 4")
    
    # Input for interval
    a = st.number_input("Masukkan nilai a:", value=0.0)
    b = st.number_input("Masukkan nilai b:", value=5.0)
    
    # Input for error tolerance
    e = st.number_input("Masukkan toleransi kesalahan (e):", value=0.01)
    
    hasil = st.empty()
    
    if st.button("Hitung"):
        result = methods.regula_falsi(a, b, f_x, e)
        hasil.write(f"Hasil Akar : {result}")
        
def display_iterasi_sederhana():
    st.subheader("Metode Iterasi Sederhana")
    st.write("Metode Iterasi Sederhana adalah metode numerik untuk mencari akar dari fungsi dengan cara menggunakan iterasi.")
    
    st.markdown(
        """
            #### ***Permasalahan : x^2 - 2x - 3 =0***
        """
    )
    
    st.write("Ada 3 kemungkinan yang dapat digunakan untuk menyelesaikan permasalahan di atas, yaitu:")
    st.markdown(
        """
            - x = sqrt(2x + 3)
            - x = 3 / (x - 2)
            - x = (x^2 - 3) / 2
        """
    )
    
    x_initial = st.number_input("Masukkan nilai x awal:", value=0.0)
    max_iter = st.number_input("Masukkan jumlah iterasi maksimum:", value=100)
    e = st.number_input("Masukkan toleransi kesalahan (e):", value=0.01)
    
    cols = st.empty()
    
    if st.button("Hitung"):
        col1, col2, col3 = cols.columns(3)
        
        with col1:
            result1 = methods.iterasi_sederhana(x_initial, "sqrt(2*x + 3)", e, max_iter)
            col1.metric(f"Hasil Akar (x = sqrt(2x + 3))", result1, border=True)
        with col2:
            result2 = methods.iterasi_sederhana(x_initial, "3 / (x - 2)", e, max_iter)
            col2.metric(f"Hasil Akar (x = 3 / (x - 2))", result2, border=True)
        with col3:
            result3 = methods.iterasi_sederhana(x_initial, "(x**2 - 3) / 2", e, max_iter)
            col3.metric(f"Hasil Akar (x = (x^2 - 3) / 2)", result3, border=True)

def display_newton_raphson():
    pass

def display_secant():
    pass