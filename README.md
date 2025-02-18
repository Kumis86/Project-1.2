# Quiz Game dengan Proteksi Password

Proyek ini adalah sebuah **game kuis sederhana** yang dibangun menggunakan Python. Game ini memungkinkan pemain untuk menjawab pertanyaan-pertanyaan yang disimpan dalam file teks. Selain itu, proyek ini juga dilengkapi dengan **sistem proteksi password** untuk mengamankan fitur-fitur yang berhubungan dengan manipulasi data, seperti menambah, mengedit, atau menghapus pertanyaan.

---

## Fitur Utama

1. **Main Quiz**:
   - Pemain dapat menjawab pertanyaan-pertanyaan yang tersedia.
   - Skor pemain akan ditampilkan di akhir game.

2. **Lihat Pertanyaan**:
   - Menampilkan semua pertanyaan dan jawaban yang tersimpan di dalam file.

3. **Tambah Pertanyaan**:
   - Menambahkan pertanyaan baru ke dalam file.
   - **Proteksi Password**: Hanya user yang mengetahui password yang bisa menambah pertanyaan.

4. **Edit Pertanyaan**:
   - Mengubah pertanyaan atau jawaban yang sudah ada.
   - **Proteksi Password**: Hanya user yang mengetahui password yang bisa mengedit pertanyaan.

5. **Hapus Pertanyaan**:
   - Menghapus pertanyaan dari file.
   - **Proteksi Password**: Hanya user yang mengetahui password yang bisa menghapus pertanyaan.

6. **Proteksi Password**:
   - Setiap kali user mencoba mengakses fitur yang berhubungan dengan manipulasi data (tambah, edit, hapus), program akan meminta password terlebih dahulu.
   - Password default: `admin123` (dapat diubah di dalam kode program).

---

## Cara Menggunakan

1. **Clone Repository**:
   ```bash
   git clone https://github.com/Kumis86/Poject-1.2.git
