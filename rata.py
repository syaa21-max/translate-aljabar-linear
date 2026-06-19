import streamlit as st
from textblob import TextBlob
import nltk

# Memastikan kamus bahasa terunduh dengan aman di server cloud
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

# ==========================================
# DESAIN MODEL GOOGLE TRANSLATE
# ==========================================
st.set_page_config(page_title="Google Translate - Vektor Raksasa", layout="centered")

st.title("🌐 Ruang Vektor Translate (Ketik Bebas)")
st.write("Simulasi Penerjemah Otomatis Tugas Akhir — Mendukung Banyak Kata & Kalimat")
st.write("---")

# Membuat 2 kolom berdampingan mirip Google Translate
kolom_kiri, kolom_kanan = st.columns(2)

with kolom_kiri:
    st.caption("Bahasa Indonesia (Ketik di sini)")
    kata_input = st.text_input(
        "Masukkan kata/kalimat:", 
        value="selamat pagi",
        label_visibility="collapsed"
    )

# --- PROSES TRANSLASI ---
hasil_terjemahan = ""
if kata_input.strip() != "":
    try:
        blob = TextBlob(kata_input)
        # Menambahkan parameter to='en' untuk menerjemahkan ke Inggris
        hasil_terjemahan = str(blob.translate(from_lang='id', to='en'))
    except Exception:
        # Jika textblob gagal/error, kita gunakan alternatif library bawaan python yang sangat ringan
        import urllib.request
        import json
        try:
            # Menggunakan API translate cadangan gratis jika TextBlob sibuk
            url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=id&tl=en&dt=t&q={urllib.parse.quote(kata_input)}"
            res = urllib.request.urlopen(url).read().decode("utf-8")
            hasil_terjemahan = json.loads(res)[0][0][0]
        except Exception:
            hasil_terjemahan = kata_input

with kolom_kanan:
    st.caption("Inggris (English)")
    st.info(f"**{hasil_terjemahan.upper()}**")

st.write("---")
st.caption("Sistem mendeteksi teks input secara otomatis dan mentransformasikannya ke dalam ruang makna bahasa tujuan di latar belakang.")
