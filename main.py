import streamlit as st
from tambah_buku import TambahBuku
from tampilkan_buku import dftPeminjam, Buku
from pinjam_buku import PinjamBuku
from kembalikan_buku import KembalikanBuku
import about 

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://wallpapercave.com/wp/wp7713574.jpg");
        background-size: cover;
    }

    div.streamlit-expanderContent {
        background-color: rgba(0, 0, 0);
        padding: 10px;
        border-radius: 10px;
    }
    .st-emotion-cache-qcpnpn {
        border-radius: 1rem;
        padding: calc(-1px + 1rem);
        background-color:rgba(0,0,1);
        color: white;
    }
    .st-emotion-cache-4brx5n{
        text-align: center;
        color: white;
    }

    .st-emotion-cache-zuelfj{
        background-color:rgba(0,0,0);
        border-radius: 1rem;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# Inisialisasi objek
if 'daftar_buku' not in st.session_state:
    st.session_state.daftar_buku = [
        Buku("Gigi naga", "Dave Revoy", 2),
        Buku("Bukan Pengikutmu Yang Sempurna", "Annisa Ihsani", 2),
        Buku("Cinta Yang Jatuh Bersama Hujan", "Puput Fitria", 5),
        Buku("Buku Pintar", "Puput Fitria", 4)
    ]

if 'peminjam' not in st.session_state:
    st.session_state.peminjam = {}

# Streamlit UI
st.title("Sistem Peminjaman Buku")

menu = st.sidebar.selectbox("Menu", ["about","Daftar Buku dan Peminjam", "Pinjam Buku", "Kembalikan Buku", "Tambah Buku"])

if menu == "Daftar Buku dan Peminjam":
    dftbuku_peminjam = dftPeminjam(st.session_state.daftar_buku, st.session_state.peminjam)
    dftbuku_peminjam.proses()

elif menu == "Pinjam Buku":
    pinjam_buku = PinjamBuku(st.session_state.daftar_buku, st.session_state.peminjam)
    pinjam_buku.proses()

elif menu == "Kembalikan Buku":
    kembalikan_buku = KembalikanBuku(st.session_state.daftar_buku, st.session_state.peminjam)
    kembalikan_buku.proses()

elif menu == "Tambah Buku":
    tambah_buku = TambahBuku(st.session_state.daftar_buku)
    tambah_buku.proses()

elif menu == "about":
    about.tampilkan_informasi()

