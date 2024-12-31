import streamlit as st

def tampilkan_informasi():
    # Menampilkan judul informasi
    st.header("Informasi Aplikasi & Tim")

    st.subheader("Tim Pengembang")
    st.write("""
    - **Ketua Tim**: Sholahuddin Robbani
    - **Anggota Tim**: Nathania Belva Zerlina
    - **Anggota Tim**: Fatimah Az Zakiyah
    - **Anggota Tim**: Muhammad Adrian Rafif
    
    """)
    # Menjelaskan sistem perhitungan
    st.subheader("Simulasi Sistem Peminjaman Buku")

    st.write("""
    Aplikasi **Sistem Peminjaman Buku** memudahkan anda dalam meminjam buku dan mendata buku apa saja yang ada, aplikasi ini menggunakan sistem perhitungan yang sederhana. Peminjam dapat memilih buku yang ingin,
    

    ### 1. Tampilkan Buku dan buku yang dipinjam
    - **Tampilkan Buku**: Ini berfungsi untuk menampilkan buku yang ada di aplikasi.
    - **buku yang dipinjam**: Ini berfungsi untuk melihat buku yang telah dipinjam oleh pengguna aplikasi.

    ### 2. Pinjam Buku

    - **Pinjam Buku** pinjam buku.
    - **Nama peminjam** ini berfungsi untuk mengetahui siapa saja yang telah meminjam buku.
    - **Buku yang dipinjam** ini berfungsi untuk mengetahui buku apa saja yang telah dipinjam oleh pengguna

    ### 3. kembalikan buku
    - **kembalikan buku** ini berfungsi untuk mengembalikan buku yang sudah dipinjam

    ### 4. Tambah buku
    - **Tambah buku** ini berfungsi untuk menambahkan buku baru ke dalam aplikasi.
    """)

    # Menampilkan informasi tentang tim pengembang
