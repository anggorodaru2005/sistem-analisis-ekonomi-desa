
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Ekonomi Desa Cerme",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 Sistem Analisis dan Prediksi Ekonomi Desa")
st.subheader("Kecamatan Cerme, Kabupaten Gresik")

st.info("Status proyek: Dalam tahap pengembangan (On Progress)")

st.markdown("""
Sistem ini dikembangkan untuk membantu memahami kondisi dan potensi
ekonomi desa melalui analisis data serta pengembangan model prediksi.
""")

st.divider()

st.header("Tujuan Proyek")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📊 Analisis Data
    - Mengidentifikasi indikator ekonomi desa.
    - Mengeksplorasi data yang tersedia.
    - Membandingkan kondisi ekonomi antarwilayah.
    """)

with col2:
    st.markdown("""
    ### 🔮 Pengembangan Prediksi
    - Menentukan target prediksi berdasarkan data.
    - Mengembangkan dan mengevaluasi model.
    - Menyusun rekomendasi berbasis hasil analisis.
    """)

st.divider()

st.header("Tahapan Pengembangan")

tahapan = [
    "Identifikasi sumber dan pengumpulan data",
    "Pembersihan serta eksplorasi data",
    "Analisis indikator ekonomi desa",
    "Pengembangan dan evaluasi model prediksi",
    "Pembuatan dashboard dan rekomendasi"
]

for i, tahap in enumerate(tahapan, start=1):
    st.write(f"**{i}.** {tahap}")

st.divider()

st.header("Sumber Data")

st.write("""
Data akan dikumpulkan dari sumber yang relevan dan dapat
dipertanggungjawabkan, seperti publikasi BPS dan data pemerintah desa
jika tersedia. Analisis dan prediksi akan dilakukan setelah data
diperiksa kualitas serta kelengkapannya.
""")

st.warning(
    "Dashboard ini masih berupa prototipe. "
    "Belum ada hasil analisis atau prediksi ekonomi yang ditampilkan."
)

st.caption(
    f"Terakhir dijalankan: {datetime.now().strftime('%d-%m-%Y')} "
    "| Proyek akademik dalam tahap pengembangan."
)
