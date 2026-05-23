import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================
st.set_page_config(
    page_title="Dashboard Manajemen Perikanan",
    page_icon="🚢",
    layout="wide"
)

# =====================================================
# BACA DATA CSV
# =====================================================
operasional = pd.read_csv("DT operasional kapal.csv")
finansial = pd.read_csv("DT finansial kapal.csv")
integrasi = pd.read_csv("Data integrasi.csv")

# =====================================================
# RAPIKAN TIPE DATA
# =====================================================
integrasi["Tanggal Berangkat"] = pd.to_datetime(
    integrasi["Tanggal Berangkat"],
    errors="coerce"
)

operasional["Tanggal Berangkat"] = pd.to_datetime(
    operasional["Tanggal Berangkat"],
    errors="coerce"
)

integrasi["Bulan"] = integrasi["Tanggal Berangkat"].dt.strftime("%b %Y")
operasional["Bulan"] = operasional["Tanggal Berangkat"].dt.strftime("%b %Y")

# =====================================================
# FUNGSI FORMAT ANGKA
# =====================================================
def angka(x):
    try:
        return f"{x:,.0f}".replace(",", ".")
    except:
        return x

def rupiah(x):
    try:
        return "Rp " + f"{x:,.0f}".replace(",", ".")
    except:
        return x

# =====================================================
# CSS DASHBOARD
# =====================================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #06101f, #0b1324, #111827);
    color: white;
}

section[data-testid="stSidebar"] {
    background:
        radial-gradient(circle at 50% 0%, rgba(59,130,246,0.30), transparent 30%),
        linear-gradient(180deg, #020617, #071827, #020617);
    border-right: 1px solid rgba(96,165,250,0.35);
}

h1, h2, h3, h4, h5, h6, p, label {
    color: white !important;
}

@keyframes fadeUp {
    from {opacity: 0; transform: translateY(25px);}
    to {opacity: 1; transform: translateY(0);}
}

@keyframes glow {
    0% {box-shadow: 0 0 12px rgba(59,130,246,0.25);}
    50% {box-shadow: 0 0 30px rgba(59,130,246,0.55);}
    100% {box-shadow: 0 0 12px rgba(59,130,246,0.25);}
}

@keyframes boatFloat {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
    100% { transform: translateY(0px); }
}

@keyframes waveMove {
    0% { background-position-x: 0px; }
    100% { background-position-x: 100px; }
}

.hero {
    padding: 28px;
    border-radius: 25px;
    background: linear-gradient(135deg, rgba(30,64,175,0.50), rgba(15,23,42,0.95));
    border: 1px solid #1e3a8a;
    animation: fadeUp 0.8s ease;
}

.card {
    padding: 22px;
    border-radius: 22px;
    border: 1px solid #1e293b;
    animation: fadeUp 0.8s ease;
}

.card:hover {
    animation: glow 2s infinite;
}

.card-blue {background: linear-gradient(135deg, #1d4ed8, #0f172a);}
.card-green {background: linear-gradient(135deg, #0f766e, #0f172a);}
.card-purple {background: linear-gradient(135deg, #6d28d9, #0f172a);}
.card-orange {background: linear-gradient(135deg, #ea580c, #0f172a);}

.metric-title {
    font-size: 14px;
    color: #bfdbfe;
    font-weight: 700;
}

.metric-value {
    font-size: 34px;
    font-weight: 900;
    margin-top: 8px;
    word-break: break-word;
}

.metric-note {
    font-size: 13px;
    color: #dbeafe;
    margin-top: 8px;
}

.box {
    padding: 22px;
    border-radius: 22px;
    background: rgba(15, 23, 42, 0.94);
    border: 1px solid #1e293b;
    box-shadow: 0 8px 28px rgba(0,0,0,0.30);
    animation: fadeUp 0.9s ease;
}

.sidebar-box {
    padding: 18px;
    border-radius: 24px;
    background: linear-gradient(145deg, rgba(37,99,235,0.45), rgba(15,23,42,0.95));
    border: 1px solid rgba(147,197,253,0.35);
    box-shadow: 0 0 20px rgba(59,130,246,0.30);
    margin-bottom: 18px;
}

.azza-profile {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 18px;
}

.azza-avatar {
    width: 46px;
    height: 46px;
    border-radius: 16px;
    background: linear-gradient(135deg, #38bdf8, #2563eb, #7c3aed);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 900;
    font-size: 18px;
}

.azza-name {
    font-size: 18px;
    font-weight: 900;
    margin: 0;
}

.azza-role {
    font-size: 12px;
    color: #bfdbfe !important;
    margin: 0;
}

.boat-icon {
    text-align: center;
    font-size: 58px;
    animation: boatFloat 3s ease-in-out infinite;
}

.wave {
    height: 16px;
    margin: 0 12px 14px 12px;
    border-radius: 999px;
    background: repeating-linear-gradient(
        90deg,
        #60a5fa 0px,
        #60a5fa 14px,
        #1e40af 14px,
        #1e40af 28px
    );
    animation: waveMove 3s linear infinite;
}

.sidebar-title {
    font-size: 26px;
    font-weight: 900;
    margin: 0;
}

.sidebar-subtitle {
    font-size: 13px;
    color: #bfdbfe !important;
    margin-top: 5px;
}

.sidebar-badge {
    display: inline-block;
    padding: 8px 13px;
    margin-top: 10px;
    border-radius: 999px;
    background: rgba(59,130,246,0.22);
    color: #dbeafe;
    font-size: 12px;
    font-weight: 800;
}

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR AMAN + KAPAL ANIMASI
# =====================================================

st.sidebar.markdown("""
<style>
@keyframes kapalGerak {
    0% { transform: translateX(-8px) translateY(0px); }
    50% { transform: translateX(8px) translateY(-8px); }
    100% { transform: translateX(-8px) translateY(0px); }
}

@keyframes ombakGerak {
    0% { letter-spacing: 2px; opacity: 0.5; }
    50% { letter-spacing: 6px; opacity: 1; }
    100% { letter-spacing: 2px; opacity: 0.5; }
}

.kapal-animasi {
    font-size: 70px;
    text-align: center;
    animation: kapalGerak 3s ease-in-out infinite;
    margin-bottom: -10px;
}

.ombak-animasi {
    text-align: center;
    color: #38bdf8;
    font-size: 22px;
    animation: ombakGerak 2s ease-in-out infinite;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown(
    """
    <div class="kapal-animasi">🚢</div>
    <div class="ombak-animasi">≈≈≈≈≈</div>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("PERIKANAN")
st.sidebar.subheader("Azza")
st.sidebar.caption("Dashboard Creator")

st.sidebar.success("🌊 Live Data System")
st.sidebar.info("🐟 Smart Fisheries Monitoring")

st.sidebar.markdown("---")

st.sidebar.metric(
    label="🚢 Total Kapal Terpantau",
    value=integrasi["Nama Kapal"].nunique()
)

st.sidebar.metric(
    label="📍 Total Trip",
    value=integrasi["trip id"].nunique()
)

st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "📌 Menu Navigasi",
    [
        "Dashboard Utama",
        "Data Operasional",
        "Data Finansial",
        "Data Integrasi"
    ]
)

st.sidebar.markdown("---")
st.sidebar.subheader("🔎 Filter Data")

pilih_kapal = st.sidebar.multiselect(
    "🚢 Pilih Kapal",
    sorted(integrasi["Nama Kapal"].dropna().unique()),
    default=sorted(integrasi["Nama Kapal"].dropna().unique())
)

data_filter = integrasi[integrasi["Nama Kapal"].isin(pilih_kapal)]

search = st.sidebar.text_input(
    "🔍 Cari Data",
    placeholder="Contoh: TRP001 / nama kapal"
)

if search:
    data_filter = data_filter[
        data_filter.astype(str)
        .apply(lambda x: x.str.contains(search, case=False, na=False))
        .any(axis=1)
    ]

# =====================================================
# HEADER DASHBOARD
# =====================================================
st.markdown("""
<style>
.header-box {
    padding: 28px;
    border-radius: 25px;
    background: linear-gradient(135deg, rgba(30,64,175,0.75), rgba(15,23,42,0.98));
    border: 1px solid #1e3a8a;
    box-shadow: 0 0 28px rgba(37,99,235,0.35);
    margin-bottom: 24px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="header-box">
    <h1 style="font-size:42px; margin-bottom:10px;">
        🚢 Dashboard Manajemen Perikanan
    </h1>
    <p style="font-size:17px;">
        Visualisasi data operasional kapal, konsumsi BBM, hasil tangkapan, dan pendapatan perikanan.
    </p>
    <p style="font-size:14px; color:#bfdbfe;">
        Terakhir diperbarui: {datetime.now().strftime("%d %B %Y %H:%M WIB")}
    </p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# DASHBOARD UTAMA
# =====================================================
if menu == "Dashboard Utama":

    total_produksi = data_filter["Berat Tangkapan (kg)"].sum()
    total_pendapatan = data_filter["Total Pendapatan (IDR)"].sum()
    total_bbm = data_filter["bbm_liter"].sum()
    jumlah_trip = data_filter["trip id"].nunique()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="card card-blue">
            <div class="metric-title">TOTAL TANGKAPAN</div>
            <div class="metric-value">{angka(total_produksi)} Kg</div>
            <div class="metric-note">hasil tangkapan kapal</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="card card-green">
            <div class="metric-title">TOTAL PENDAPATAN</div>
            <div class="metric-value">{rupiah(total_pendapatan)}</div>
            <div class="metric-note">pendapatan keseluruhan</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="card card-purple">
            <div class="metric-title">TOTAL BBM</div>
            <div class="metric-value">{angka(total_bbm)} Liter</div>
            <div class="metric-note">konsumsi bahan bakar</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="card card-orange">
            <div class="metric-title">JUMLAH TRIP</div>
            <div class="metric-value">{angka(jumlah_trip)}</div>
            <div class="metric-note">total perjalanan kapal</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    kiri, kanan = st.columns(2)

    with kiri:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader("🐟 Produksi Hasil Tangkapan per Kapal")

        produksi_kapal = (
            data_filter.groupby("Nama Kapal")["Berat Tangkapan (kg)"]
            .sum()
            .reset_index()
            .sort_values("Berat Tangkapan (kg)", ascending=False)
        )

        fig1 = px.bar(
            produksi_kapal,
            x="Nama Kapal",
            y="Berat Tangkapan (kg)",
            color="Nama Kapal",
            text="Berat Tangkapan (kg)",
            template="plotly_dark"
        )

        fig1.update_layout(
            height=430,
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Nama Kapal",
            yaxis_title="Berat Tangkapan (kg)"
        )

        st.plotly_chart(fig1, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with kanan:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader("💰 Distribusi Pendapatan per Kapal")

        pendapatan_kapal = (
            data_filter.groupby("Nama Kapal")["Total Pendapatan (IDR)"]
            .sum()
            .reset_index()
            .sort_values("Total Pendapatan (IDR)", ascending=False)
        )

        fig2 = px.pie(
            pendapatan_kapal,
            names="Nama Kapal",
            values="Total Pendapatan (IDR)",
            hole=0.55,
            template="plotly_dark"
        )

        fig2.update_layout(
            height=430,
            paper_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    kiri2, kanan2 = st.columns(2)

    with kiri2:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader("⛽ Konsumsi BBM per Kapal")

        bbm_kapal = (
            data_filter.groupby("Nama Kapal")["bbm_liter"]
            .sum()
            .reset_index()
            .sort_values("bbm_liter", ascending=False)
        )

        fig3 = px.bar(
            bbm_kapal,
            x="bbm_liter",
            y="Nama Kapal",
            orientation="h",
            text="bbm_liter",
            template="plotly_dark"
        )

        fig3.update_layout(
            height=430,
            yaxis=dict(autorange="reversed"),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis_title="BBM Liter",
            yaxis_title="Nama Kapal"
        )

        st.plotly_chart(fig3, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with kanan2:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader("📈 Tren Tangkapan Berdasarkan Tanggal")

        tren = (
            data_filter.groupby("Tanggal Berangkat")["Berat Tangkapan (kg)"]
            .sum()
            .reset_index()
            .sort_values("Tanggal Berangkat")
        )

        fig4 = px.area(
            tren,
            x="Tanggal Berangkat",
            y="Berat Tangkapan (kg)",
            markers=True,
            template="plotly_dark"
        )

        fig4.update_traces(
            line=dict(width=4),
            marker=dict(size=8),
            fill="tozeroy"
        )

        fig4.update_layout(
            height=430,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Tanggal Berangkat",
            yaxis_title="Berat Tangkapan (kg)"
        )

        st.plotly_chart(fig4, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    b1, b2, b3 = st.columns(3)

    with b1:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader("🏆 Top 5 Kapal Tangkapan Tertinggi")
        top5 = produksi_kapal.head(5)
        st.dataframe(top5, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with b2:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader("🚢 Ringkasan Operasional")
        st.metric("Jumlah Data Operasional", len(operasional))
        st.metric("Jumlah Kapal", data_filter["Nama Kapal"].nunique())
        st.metric("Rata-rata BBM", f"{angka(data_filter['bbm_liter'].mean())} Liter")
        st.markdown("</div>", unsafe_allow_html=True)

    with b3:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader("💰 Ringkasan Finansial")
        st.metric("Jumlah Data Finansial", len(finansial))
        st.metric("Rata-rata Pendapatan", rupiah(data_filter["Total Pendapatan (IDR)"].mean()))
        st.metric("Harga BBM Rata-rata", rupiah(data_filter["harga_per_liter"].mean()))
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.subheader("📋 Data Integrasi Perikanan")
    st.dataframe(data_filter, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    csv = data_filter.to_csv(index=False)

    st.download_button(
        label="⬇️ Download Data Integrasi CSV",
        data=csv,
        file_name="data_integrasi_perikanan.csv",
        mime="text/csv"
    )

elif menu == "Data Operasional":
    st.header("🚢 Data Operasional Kapal")
    st.dataframe(operasional, use_container_width=True)

    csv = operasional.to_csv(index=False)
    st.download_button("⬇️ Download Data Operasional", csv, "data_operasional.csv", "text/csv")

elif menu == "Data Finansial":
    st.header("💰 Data Finansial Kapal")
    st.dataframe(finansial, use_container_width=True)

    fig = px.bar(
        finansial,
        x="ID_Kapal",
        y="Total Pendapatan (IDR)",
        text="Total Pendapatan (IDR)",
        template="plotly_dark"
    )

    fig.update_layout(
        height=450,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

    csv = finansial.to_csv(index=False)
    st.download_button("⬇️ Download Data Finansial", csv, "data_finansial.csv", "text/csv")

elif menu == "Data Integrasi":
    st.header("🐟 Data Integrasi Perikanan")
    st.dataframe(integrasi, use_container_width=True)

    csv = integrasi.to_csv(index=False)
    st.download_button("⬇️ Download Data Integrasi", csv, "data_integrasi.csv", "text/csv")

st.markdown("---")
st.markdown(
    '<div class="footer">Dashboard Praktikum Perikanan Menggunakan Python, Streamlit, dan Plotly ❤️</div>',
    unsafe_allow_html=True
)