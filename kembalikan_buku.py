import streamlit as st

class KembalikanBuku:
    def __init__(self, daftar_buku, peminjam):
        self.daftar_buku = daftar_buku
        self.peminjam = peminjam

    def proses(self):
            with st.form("Kembalikan"):
                st.header("Kembalikan Buku")
                nama = st.text_input("Nama Peminjam")
                
                if st.form_submit_button("Kembalikan"):
                    if nama in self.peminjam:
                        judul = self.peminjam.pop(nama)
                        
                        for buku in self.daftar_buku:
                            if buku.judul == judul:
                                buku.stok += 1
                                st.success(f"{judul} berhasil dikembalikan.")
                                break 
                        
                    else:
                        st.error(f"Tidak ada pinjaman atas nama {nama}.")