import streamlit as st
import urllib.request
import urllib.parse
import json

# Set halaman web agar rapi dan responsif
st.set_page_config(page_title="Penerjemah Ruang Vektor", layout="wide")

st.title("🌐 Ruang Vektor Translate")
st.write("Aplikasi Penerjemah Otomatis — Tugas Akhir Aljabar Linear Terapan")
st.write("---")

# Menggunakan session state agar pilihan bahasa bisa diingat dan ditukar dengan lancar
if 'bahasa_asal' not in st.session_state:
    st.session_state.bahasa_asal = "Indonesia"

# Tombol untuk menukar arah bahasa secara instan (Fitur Google Translate)
if st.button("🔄 Tukar Arah Bahasa"):
    if st.session_state.bahasa_asal == "Indonesia":
        st.session_state.bahasa_asal = "Inggris"
    else:
        st.session_state.bahasa_asal = "Indonesia"

# Menentukan komponen bahasa berdasarkan pilihan saat ini
if st.session_state.bahasa_asal == "Indonesia":
    label_asal = "Indonesia"
    label_tujuan = "Inggris"
    sl = "id"
    tl = "en"
    contoh_teks = "Selamat pagi, mari belajar Aljabar Linear bersama."
else:
    label_asal = "Inggris"
    label_tujuan = "Indonesia"
    sl = "en"
    tl = "id"
    contoh_teks = "Good morning, let's learn Linear Algebra together."

# Membuat 2 kolom besar untuk kotak ketik teks berdampingan
kolom_input, kolom_output = st.columns(2)

with kolom_input:
    st.markdown(f"### 📥 Bahasa Asal: **{label_asal}**")
    teks_input = st.text_area(
        "Ketik kata atau kalimat di sini:", 
        value=contoh_teks,
        height=150,
        key="input_area"
    )

# --- PROSES MESIN TRANSLASI DI LATAR BELAKANG ---
hasil_translate = ""
if teks_input.strip() != "":
    try:
        # Menggunakan API Google Translate resmi versi publik (Gratis, Cepat & Akurat)
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={sl}&tl={tl}&dt=t&q={urllib.parse.quote(teks_input)}"
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req).read().decode("utf-8")
        
        data_json = json.loads(response)
        
        # Menggabungkan seluruh teks hasil terjemahan jika kalimatnya panjang
        hasil_translate = "".join([part[0] for part in data_json[0] if part[0] is not None])
    except Exception as e:
        hasil_translate = f"Gagal tersambung ke server: {str(e)}"

with kolom_output:
    st.markdown(f"### 📤 Hasil Terjemahan: **{label_tujuan}**")
    # Tampilan kotak output hasil terjemahan yang elegan
    st.success(hasil_translate if hasil_translate else "Menunggu teks...")

st.write("---")
st.caption("Sistem ini bekerja dengan mentransformasikan representasi string teks ke dalam ruang semantik bahasa target secara otomatis.")
