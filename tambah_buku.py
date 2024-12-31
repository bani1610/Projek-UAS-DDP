import streamlit as st
from tampilkan_buku import Buku

class TambahBuku:
    def __init__(self, daftar_buku):
        self.daftar_buku = daftar_buku

    def proses(self):
        with st.form("Tambah Buku"):
            st.header("Tambah Buku")
            judul = st.text_input("Judul Buku")
            penulis = st.text_input("Penulis Buku")
            stok = st.number_input("Jumlah Stok", min_value=1, value=1)

            if st.form_submit_button("Tambah"):
                if judul and penulis:
                    buku = Buku(judul, penulis, stok)
                    st.session_state.daftar_buku.append(buku)
                    st.success(f"Buku {judul} oleh {penulis} dengan stok {stok} berhasil ditambahkan.")
                else:
                    st.error("Masukkan judul dan penulis buku.")