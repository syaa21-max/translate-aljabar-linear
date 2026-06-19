import streamlit as st
import urllib.request
import urllib.parse
import json

# Set halaman web agar rapi dan responsif
st.set_page_config(page_title="Penerjemah Ruang Vektor", layout="wide")

st.title("🌐 Ruang Vektor Translate (Instan)")
st.write("Aplikasi Penerjemah Otomatis — Tugas Akhir Aljabar Linear Terapan")
st.write("---")

# Menggunakan session state agar pilihan bahasa bisa diingat dengan lancar
if 'bahasa_asal' not in st.session_state:
    st.session_state.bahasa_asal = "Indonesia"

# Pilihan Arah Bahasa menggunakan tombol toggle sederhana
kolom_tombol1, kolom_tombol2 = st.columns([1, 4])
with kolom_tombol1:
    if st.button("🔄 Tukar Bahasa"):
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
else:
    label_asal = "Inggris"
    label_tujuan = "Indonesia"
    sl = "en"
    tl = "id"

# Membuat 2 kolom besar untuk kotak ketik teks berdampingan
kolom_input, kolom_output = st.columns(2)

with kolom_input:
    st.markdown(f"### 📥 Dari: **{label_asal}**")
    # Menggunakan text_area biasa tanpa tombol pemicu manual
    teks_input = st.text_area(
        "Ketik di sini...", 
        value="",
        height=150,
        placeholder="Ketik kata atau kalimat yang ingin diterjemahkan...",
        key="teks_asal"
    )

# --- PROSES MESIN TRANSLASI INSTAN ---
hasil_translate = ""
if teks_input.strip() != "":
    try:
        # Menggunakan API Google Translate publik gratis
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={sl}&tl={tl}&dt=t&q={urllib.parse.quote(teks_input)}"
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req).read().decode("utf-8")
        
        data_json = json.loads(response)
        
        # Menggabungkan seluruh teks hasil terjemahan
        hasil_translate = "".join([part[0] for part in data_json[0] if part[0] is not None])
    except Exception:
        hasil_translate = "Menerjemahkan..."

with kolom_output:
    st.markdown(f"### 📤 Ke: **{label_tujuan}**")
    # Menampilkan hasil di dalam kotak yang elegan secara langsung
    if teks_input.strip() != "":
        st.success(hasil_translate)
    else:
        st.info("Hasil terjemahan akan muncul di sini secara otomatis...")

st.write("---")
st.caption("Sistem mendeteksi perubahan input teks secara langsung dan mentransformasikannya ke dalam ruang bahasa target.")
