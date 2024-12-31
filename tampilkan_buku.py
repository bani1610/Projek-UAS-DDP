import streamlit as st
import pandas as pd

class Buku:
    def __init__(self, judul, penulis, stok=1):
        self.judul = judul
        self.penulis = penulis
        self.stok = stok
        self.status = "Tersedia" if stok > 0 else "Tidak Tersedia"

class dftPeminjam:
    def __init__(self, daftar_buku, peminjam):
        self.daftar_buku = daftar_buku
        self.peminjam = peminjam

    def proses(self):
        st.header("Daftar Buku")
        buku_df = pd.DataFrame([{
            "Judul": buku.judul, 
            "Penulis": buku.penulis, 
            "Stok": buku.stok,
            "Status": "Tersedia" if buku.stok > 0 else "Tidak Tersedia"
        } for buku in self.daftar_buku
        ])
        buku_df.index += 1  # Start index from 1
        st.table(buku_df)

        st.header("Daftar Peminjam")
        if self.peminjam:
            peminjam_df = pd.DataFrame(list(self.peminjam.items()), columns=["Nama", "Buku"])
            peminjam_df.index += 1  # Start index from 1
            st.table(peminjam_df)
        else:
            st.info("Belum ada peminjam")