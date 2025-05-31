import streamlit as st
import controllers.methods as methods
import numpy as np

from sympy import sympify
from pandas import DataFrame

def display_home():
    # Judul Utama Aplikasi
    st.markdown("---")

    # Pendahuluan dan Deskripsi Dashboard
    st.markdown(
        """
        Selamat datang di **Dashboard Interaktif Metode Pencarian Akar**!

        Dashboard ini dirancang untuk membantu Anda memahami, memvisualisasikan, dan membandingkan 
        berbagai metode numerik yang umum digunakan untuk menemukan akar dari suatu fungsi matematika. 
        Anda dapat memasukkan fungsi Anda sendiri, mengatur parameter awal, dan melihat bagaimana setiap 
        metode bekerja langkah demi langkah.

        Proyek ini merupakan bagian dari pemenuhan tugas akhir mata kuliah **Rekayasa Komputasional** (Semester 6) 
        di Jurusan Informatika, Fakultas Teknologi Industri, Universitas Gunadarma.
        """
    )
    st.markdown("---")

    # Informasi Tim Pengembang (dapat dibuat lebih ringkas dengan expander)
    with st.expander("🎓 Tim Pengembang (Kelompok 1 Rekayasa Komputasional)", expanded=False):
        st.markdown(
            """
            Dashboard ini dikembangkan oleh:
            * **Muhamad Raka Pratama** (NPM: `50422956`)
            * **Muhammad Bintang Alifiansyah** (NPM: `51422001`)
            * **Muhammad Bukhori** (NPM: `51422002`)
            * **Bahrul Ilmi Surachman** (NPM: `50422318`)
            * **Muhammad Azhar Iskandar** (NPM: `50422937`)
            """
        )
    
    st.markdown("---")

    # Deskripsi Metode yang Digunakan
    st.header("🔍 Metode Pencarian Akar yang Diimplementasikan")
    st.markdown(
        """
        Dalam dashboard ini, Anda akan menemukan implementasi dari beberapa metode pencarian akar fundamental, 
        yang dikelompokkan menjadi dua kategori utama:
        """
    )

    # Menggunakan kolom untuk tampilan yang lebih rapi
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Metode Tertutup")
        st.markdown(
            """
            Metode dalam kategori ini memerlukan interval awal $[a, b]$ yang dipastikan mengapit akar (yaitu, $f(a)$ dan $f(b)$ memiliki tanda yang berlawanan). Metode ini umumnya konvergen secara pasti menuju akar.
            - **Metode Bagi Dua (Bisection Method)**
            - **Metode Regula Falsi (False Position Method)**
            """
        )

    with col2:
        st.subheader("Metode Terbuka")
        st.markdown(
            """
            Metode dalam kategori ini biasanya menggunakan satu atau dua tebakan awal, tetapi tidak mensyaratkan tebakan tersebut mengapit akar. Metode ini bisa konvergen lebih cepat, namun konvergensinya tidak selalu dijamin.
            - **Metode Newton-Raphson**
            - **Metode Secant**
            """
        )
    
    st.markdown("---")

    # Petunjuk Penggunaan Dashboard
    st.info(
        """
        💡 **Panduan Penggunaan:**
        Untuk memulai, silakan pilih salah satu metode numerik dari menu _sidebar_ di sebelah kiri. 
        Anda kemudian dapat memasukkan fungsi matematika, parameter awal yang diperlukan, dan toleransi kesalahan 
        untuk melihat proses iterasi, hasil akar yang ditemukan, serta visualisasi grafisnya.
        """,
        icon="ℹ️"
    )
    
    st.markdown("---")
    
    # Tautan Tambahan (misalnya ke repositori GitHub jika ada, atau tautan dashboard yang sudah di-deploy)
    st.subheader("🔗 Tautan Terkait")
    link_dashboard = "https://github.com/RakaPratama8/dashboard-metode-pencarian-akar" 
    st.markdown(f"Anda dapat mengakses repository github kami di : [RakaPratama8/dashboard-metode-pencarian-akar]({link_dashboard})")
    # Jika Anda memiliki repositori GitHub publik:
    # st.markdown("Lihat kode sumber proyek ini di [GitHub](URL_GITHUB_ANDA)")

    st.markdown("<br><hr><br>", unsafe_allow_html=True) # Sedikit spasi dan garis di bagian bawah
    st.caption("© 2025 - Proyek Rekayasa Komputasional | Jurusan Informatika | Universitas Gunadarma")



def display_bisection():
    st.subheader("Metode Bagi Dua")
    st.write("Metode Bagi Dua adalah metode numerik untuk mencari akar dari fungsi dengan cara membagi interval menjadi dua bagian dan memilih bagian yang mengandung akar.")
    
    # Input for function
    func = st.text_input("Masukkan fungsi (dalam x):", "x**2 - 4")
    
    # Input for interval
    a = st.text_input("Masukkan nilai a:", value="0.0")
    a = np.float64(a)
    b = st.text_input("Masukkan nilai b:", value="5.0")
    b = np.float64(b)
    
    # Input for error tolerance
    e = st.text_input("Masukkan toleransi kesalahan (e):", value="0.01")
    e = np.float64(e)
    
    hasil = st.empty()
    disp_datas = st.empty()
    
    if st.button("Hitung"):
        result, datas = methods.biseksi(a, b, func, e)
        hasil.write(f"Hasil Akar : {result}")
        df_datas = DataFrame(datas, columns=["a", "c", "b", "f(a)", "f(c)", "f(b)", "lebar"])
        disp_datas.dataframe(df_datas, use_container_width=True)
        
def display_regula_falsi():
    st.subheader("Metode Regula Falsi")
    st.write("Metode Regula Falsi adalah metode numerik untuk mencari akar dari fungsi dengan cara menggunakan garis lurus antara dua titik pada grafik fungsi.")
    
    # Input for function
    f_x = st.text_input("Masukkan fungsi (dalam x):", "x**2 - 4")
    
    # Input for interval
    a = st.text_input("Masukkan nilai a:", value="0.0")
    a = np.float64(a)
    b = st.text_input("Masukkan nilai b:", value="5.0")
    b = np.float64(b)
    
    # Input for error tolerance
    e = st.text_input("Masukkan toleransi kesalahan (e):", value="0.01")
    e = np.float64(e)
    
    hasil = st.empty()
    disp_datas = st.empty()
    
    if st.button("Hitung"):
        result, datas = methods.regula_falsi(a, b, f_x, e)
        hasil.write(f"Hasil Akar : {result}")
        df_datas = DataFrame(datas, columns=["a", "c", "b", "f(a)", "f(b)", "f(c)", "e"])
        disp_datas.dataframe(df_datas, use_container_width=True)
        
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
    
    x_initial = st.text_input("Masukkan nilai x awal:", value="0.0")
    x_initial = np.float64(x_initial)
    max_iter = st.number_input("Masukkan jumlah iterasi maksimum:", value=100)
    e = st.text_input("Masukkan toleransi kesalahan (e):", value="0.01")
    e = np.float64(e)
    
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
    st.subheader("Metode Newton Raphson")
    st.write("Metode Newton Raphson adalah metode numerik untuk mencari akar dari fungsi dengan cara menggunakan turunan fungsi.")
    
    # Input for function
    f_x = st.text_input("Masukkan fungsi (dalam x):", "x - exp(-x)")
    f_x = sympify(f_x)
    
    # Input for initial guess
    x0 = st.text_input("Masukkan nilai x awal:", value="0.0")
    x0 = np.float64(x0)
    
    # Input for error tolerance
    e = st.text_input("Masukkan toleransi kesalahan (e):", value="0.00001")
    e = np.float64(e)
    
    hasil = st.empty()
    disp_datas = st.empty()
    
    if st.button("Hitung"):
        result, datas = methods.newton_raphson(x0, f_x, e)
        hasil.write(f"Hasil Akar : {result}")
        
        df_datas = DataFrame(datas, columns=["x_r", "f(x)", "f'(x)", "x_r+1", "e"])
        disp_datas.dataframe(df_datas, use_container_width=True)

def display_secant():
    st.subheader("Metode Secant")
    st.write("Metode Secant adalah metode numerik untuk mencari akar dari fungsi dengan cara menggunakan dua titik pada grafik fungsi.")
    
    # Input for function
    f_x = st.text_input("Masukkan fungsi (dalam x):", "x - exp(-x)")
    
    # Input for initial guesses
    x0 = st.text_input("Masukkan nilai x0:", value="0.0")
    x0 = np.float64(x0)
    x1 = st.text_input("Masukkan nilai x1:", value="5.0")
    x1 = np.float64(x1)
    
    # Input for error tolerance
    e = st.text_input("Masukkan toleransi kesalahan (e):", value="0.01")
    e = np.float64(e)
    
    hasil = st.empty()
    disp_data = st.empty()
    
    if st.button("Hitung"):
        result, datas = methods.secant(x0, x1, f_x, e)
        hasil.write(f"Hasil Akar : {result}")
        
        df_datas = DataFrame(datas, columns=["x_r-1", "x_r", "f(x_r-1)", "f(x_r)", "x_r+1", "e"])
        disp_data.dataframe(df_datas, use_container_width=True)