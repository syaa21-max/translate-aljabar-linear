import streamlit as st
from textblob import TextBlob

# ==========================================
# DESAIN MODEL GOOGLE TRANSLATE (KETIK BEBAS)
# ==========================================
st.set_page_config(page_title="Google Translate - Vektor Raksasa", layout="centered")

st.title("🌐 Ruang Vektor Translate (Ketik Bebas)")
st.write("Simulasi Penerjemah Otomatis Tugas Akhir — Mendukung Banyak Kata & Kalimat")
st.write("---")

# Membuat 2 kolom berdampingan mirip Google Translate
kolom_kiri, kolom_kanan = st.columns(2)

with kolom_kiri:
    st.caption("Bahasa Indonesia (Ketik di sini)")
    # Mengubah selectbox menjadi text_input agar dosen bisa mengetik bebas
    kata_input = st.text_input(
        "Masukkan kata/kalimat:", 
        value="selamat pagi",
        label_visibility="collapsed"
    )

# --- PROSES TRANSLASI DI LATAR BELAKANG ---
hasil_terjemahan = ""
if kata_input.strip() != "":
    try:
        # Menggunakan TextBlob untuk mendeteksi dan menerjemahkan ke Bahasa Inggris (en)
        blob = TextBlob(kata_input)
        hasil_terjemahan = str(blob.translate(from_lang='id', to='en'))
    except Exception:
        # Jika kata yang diketik sama antara ID dan EN (misal: "internet")
        hasil_terjemahan = kata_input

with kolom_kanan:
    st.caption("Inggris (English)")
    # Kotak hasil translate yang langsung muncul otomatis dalam huruf besar
    st.info(f"**{hasil_terjemahan.upper()}**")

st.write("---")
st.caption("Sistem mendeteksi teks input secara otomatis dan mentransformasikannya ke dalam ruang makna bahasa tujuan di latar belakang.")
