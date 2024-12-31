import streamlit as st
class PinjamBuku:
    def __init__(self, daftar_buku, peminjam):
        self.daftar_buku = daftar_buku
        self.peminjam = peminjam

    def proses(self):
        with st.form('Pinjam Buku'):
            st.header("Pinjam Buku")
            nama = st.text_input("Nama Peminjam")
            judul = st.text_input("Judul Buku yang Ingin Dipinjam")
        
            if st.form_submit_button("Pinjam"):
                if nama and judul:
                    buku_dipinjam = False
                
                    for buku in self.daftar_buku:
                        if buku.judul == judul and buku.stok > 0:
                            buku.stok -= 1
                            self.peminjam[nama] = judul
                            st.session_state.peminjam[nama] = judul  
                            st.success(f"{judul} berhasil dipinjam oleh {nama}.")
                            buku_dipinjam = True
                            break
                    
                    if not buku_dipinjam:
                        st.error(f"Maaf, buku {judul} tidak tersedia.")
                else:
                    st.error("Masukkan nama dan judul buku.")