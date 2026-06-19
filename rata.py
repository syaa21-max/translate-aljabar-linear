import streamlit as st
import urllib.request
import urllib.parse
import json

# Set konfigurasi halaman web
st.set_page_config(page_title="Penerjemah Ruang Vektor", layout="wide")

st.title("🌐 Ruang Vektor Translate (Instan)")
st.write("Aplikasi Penerjemah Otomatis — Tugas Akhir Aljabar Linear Terapan")
st.write("---")

# Menggunakan session state agar pilihan bahasa bisa diingat dengan lancar
if 'bahasa_asal' not in st.session_state:
    st.session_state.bahasa_asal = "Indonesia"

# Baris Pilihan Arah Bahasa menggunakan selectbox otomatis
pilihan = st.selectbox(
    "Arah Terjemahan Bahasa:",
    ["Indonesia ke Inggris", "Inggris ke Indonesia"],
    index=0 if st.session_state.bahasa_asal == "Indonesia" else 1
)

# Set kode bahasa berdasarkan selectbox
if pilihan == "Indonesia ke Inggris":
    label_asal = "Indonesia"
    label_tujuan = "Inggris"
    sl = "id"
    tl = "en"
else:
    label_asal = "Inggris"
    label_tujuan = "Indonesia"
    sl = "en"
    tl = "id"

st.write("")

# Membuat 2 kolom besar berdampingan
kolom_input, kolom_output = st.columns(2)

with kolom_input:
    st.markdown(f"### 📥 Dari: **{label_asal}**")
    # Menggunakan text_input (bukan text_area) agar deteksi ketikan jauh lebih sensitif dan instan
    teks_input = st.text_input(
        "Ketik teks di bawah ini:", 
        value="",
        placeholder="Ketik kata yang ingin diterjemahkan langsung...",
        key="teks_asal_baru"
    )

# --- PROSES TRANSLASI LANGSUNG DI LATAR BELAKANG ---
hasil_translate = ""
if teks_input.strip() != "":
    try:
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={sl}&tl={tl}&dt=t&q={urllib.parse.quote(teks_input)}"
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req).read().decode("utf-8")
        
        data_json = json.loads(response)
        hasil_translate = "".join([part[0] for part in data_json[0] if part[0] is not None])
    except Exception:
        hasil_translate = "Sedang menerjemahkan..."

with kolom_output:
    st.markdown(f"### 📤 Ke: **{label_tujuan}**")
    if teks_input.strip() != "":
        st.success(hasil_translate)
    else:
        st.info("Hasil terjemahan otomatis muncul di sini saat Anda mengetik...")

st.write("---")
st.caption("Sistem mentransformasikan representasi teks ke dalam ruang bahasa target secara otomatis.")
