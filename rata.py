import streamlit as st
import numpy as np
import pandas as pd

# 1. DATABASE KOSAKATA (RUANG VEKTOR)
dataset = {
    'buku': np.array([0.90, 0.05, 0.05]),
    'pria': np.array([0.10, 0.95, 0.10]),
    'wanita': np.array([0.10, 0.02, 0.10]),
    'lari': np.array([0.05, 0.50, 0.95]),
    'book': np.array([0.88, 0.06, 0.04]),
    'man': np.array([0.11, 0.92, 0.08]),
    'woman': np.array([0.08, 0.03, 0.09]),
    'run': np.array([0.06, 0.48, 0.92])
}
kandidat_en = ['book', 'man', 'woman', 'run']

# 2. DESAIN ANTARMUKA WEB
st.title("🌐 Sistem Penerjemah Ruang Vektor")
st.write("Aplikasi Simulasi Aljabar Linear Terapan — Tugas Akhir")
st.write("---")

kata_input = st.selectbox("Pilih Kata Bahasa Indonesia yang Ingin Diterjemahkan:", ['buku', 'pria', 'wanita', 'lari'])

if st.button("Terjemahkan Kata"):
    v_sumber = dataset[kata_input]
    st.info(f"📍 Koordinat Vektor Asal ({kata_input}): {list(v_sumber)}")
    
    hasil_data = []
    for k in kandidat_en:
        v_kand = dataset[k]
        cos_sim = np.dot(v_sumber, v_kand) / (np.linalg.norm(v_sumber) * np.linalg.norm(v_kand))
        eucl_dist = np.linalg.norm(v_sumber - v_kand)
        
        hasil_data.append({
            "Kandidat Kata (EN)": k, 
            "Cosine Similarity": round(cos_sim, 4), 
            "Jarak Euclidean": round(eucl_dist, 4)
        })
    
    df = pd.DataFrame(hasil_data)
    st.write("### 📊 Tabel Perbandingan Nilai:")
    st.dataframe(df, use_container_width=True)
    
    pemenang = df.loc[df['Cosine Similarity'].idxmax()]['Kandidat Kata (EN)']
    st.write("---")
    st.success(f"💡 **Keputusan Sistem:** Kata **'{kata_input}'** cocok diterjemahkan menjadi **'{pemenang.upper()}'**")
