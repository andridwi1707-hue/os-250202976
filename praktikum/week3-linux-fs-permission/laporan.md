
# Laporan Praktikum Minggu [3]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : [Andri Dwi Yuliyanto]  
- **NIM**   : [250202976]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> 1. Memahami cara menggunakan perintah dasar Linux untuk mengelola file dan direktori.
2. Mempelajari konsep permission dan ownership dalam sistem file Linux.
3. Mengetahui cara mengatur keamanan dan hak akses file menggunakan perintah chmod dan chown.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
 Seluruh data dalam Linux disimpan dalam file dan direktori. File adalah tempat penyimpanan data, sementara direktori digunakan untuk mengelompokkan file. File dan direktori diatur dan disusun menggunakan perintah-perintah dasar seperti ls, cd, cp, mv, rm, dan mkdir. Selain itu, Linux juga menerapkan permission dan ownership pada file agar tidak sembarang orang bisa membaca, menulis, atau menjalankan sebuah file. Peraturan tersebut dapat diubah menggunakan perintah chmod dan chown untuk permission kepemilikan, sehingga data akan terlindungi dari pihak-pihak yang tidak bertanggungjawab.
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
 - Gunakan Linux (Ubuntu/WSL)
 -  Pasukan perintah yang ditugaskan
2. Perintah yang dijalankan.  
pwd
ls -l
cd /tmp
ls -a
cat /etc/passwd | head -n 5
echo "Hello <NAME><NIM>" > percobaan.txt
ls -l percobaan.txt
chmod 600 percobaan.txt
ls -l percobaan.txt
sudo chown root percobaan.txt
ls -l percobaan.txt
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.
Git add . 
git commit -m "pesan"
git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
pwd
ls -l
cd /tmp
ls -a
cat /etc/passwd | head -n 5
echo "Hello <NAME><NIM>" > percobaan.txt
ls -l percobaan.txt
chmod 600 percobaan.txt
ls -l percobaan.txt
sudo chown root percobaan.txt
ls -l percobaan.txt

# Penjelassan
1. Perintah 1
pwd (print working directory)
👉Menampilkan posisi atau direktori tempat kita sedang berada sekarang.
Contoh hasil: /home/andridwi1707

ls -l
 Melihat isi folder dengan tampilan detail (izin, pemilik, ukuran, dan waktu).
Misalnya muncul:

-rw-r--r-- 1 user user 123 Okt 24 10:00 file.txt


Artinya file itu bisa dibaca semua orang, tapi cuma pemilik yang bisa ubah.

cd /tmp
 Pindah ke folder /tmp, yaitu tempat file sementara disimpan oleh sistem.

ls -a
 Menampilkan semua isi folder, termasuk file yang tersembunyi (nama diawali dengan titik .).
2. Perintah 2
echo "Hello <NAME><NIM>" > percobaan.txt
Perintah ini digunakan untuk membuat file baru bernama percobaan.txt dan menuliskan teks “Hello <NAME><NIM>” ke dalamnya.
Jika file dengan nama yang sama sudah ada, maka isinya akan diganti dengan teks baru tersebut.

ls -l percobaan.txt
Perintah ini menampilkan informasi detail mengenai file percobaan.txt, seperti jenis file, izin akses (permission), pemilik (owner), grup, ukuran, dan waktu terakhir file diubah.

chmod 600 percobaan.txt
Perintah ini digunakan untuk mengubah izin akses file.
Nilai 600 berarti:

Pemilik file memiliki izin untuk membaca (read) dan menulis (write).

Pengguna lain tidak memiliki izin apa pun terhadap file tersebut.
Dengan demikian, file menjadi bersifat privat dan hanya dapat diakses oleh pemiliknya.

ls -l percobaan.txt
Perintah ini dijalankan kembali untuk memverifikasi bahwa perubahan izin akses (permission) pada file telah berhasil diterapkan.
3. Perintah 3
sudo chown root percobaan.txt
Perintah ini digunakan untuk mengubah kepemilikan (ownership) file percobaan.txt menjadi milik pengguna root.

sudo berarti menjalankan perintah dengan hak akses administrator (superuser).

chown merupakan singkatan dari change owner, yaitu perintah untuk mengganti pemilik suatu file atau direktori.

root adalah pengguna tertinggi dalam sistem Linux yang memiliki hak penuh terhadap semua file dan konfigurasi sistem.

Setelah perintah ini dijalankan, file percobaan.txt tidak lagi dimiliki oleh pengguna biasa, melainkan oleh pengguna root.

ls -l percobaan.txt
Perintah ini digunakan untuk menampilkan informasi detail tentang file percobaan.txt setelah kepemilikannya diubah.
Hasilnya akan menunjukkan bahwa kolom pemilik (owner) telah berubah menjadi root
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/fs%20permission%20(1).png)
![Screenshot hasil](screenshots/fs%20permission%20(2).png)

---

## Analisis
- Jelaskan makna hasil percobaan. 
 Makna dari percobaan tadi adalah untuk memahami cara mengelola file di Linux, khususnya dalam hal pembuatan file, pengaturan izin (permission), dan perubahan kepemilikan (ownership). Melalui percobaan tersebut, kita belajar bagaimana membuat file baru, memberi izin akses hanya kepada pemilik, serta mengubah pemilik file menjadi pengguna root agar file lebih aman dan terkontrol. 
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS). 
 Percobaan ini menunjukkan bagaimana perintah Linux bekerja melalui kernel menggunakan system call. Kernel bertugas mengatur akses ke file dan sumber daya sistem. Saat pengguna menjalankan perintah seperti chmod atau chown, shell menerjemahkannya menjadi system call yang diproses oleh kernel. Hal ini menggambarkan hubungan antara pengguna, shell, dan kernel dalam arsitektur sistem operasi. 
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
 Linux mengatur izin file lewat perintah terminal, sedangkan Windows lewat tampilan grafis. Linux memakai struktur root (/), sementara Windows memakai drive (C:).

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
- Sistem permission di Linux mengatur siapa yang boleh menuli,menjalankan, dan mengubah file.
- Setiap perintah yang dijalankan melibatkan kerja kernel untuk mengatur akses dan keamanan file.
---

## Quiz
1. [Apa fungsi dari perintah chmod?]  
   **Jawaban:MEngubah izin akses pada file direktori dalam sistem Linux,pengguna dapat membaca,menulis atau menjalankan file tersebut.**  
2. [Apa arti dari kode permission rwxr-xr--]  
   **Jawaban:Kode rwxr-xr-- berarti pemilik dapat membaca, menulis, dan menjalankan file, grup hanya dapat membaca dan menjalankan, sedangkan pengguna lain hanya dapat membaca.v**  
3. [Jelaskan perbedaan antara chown dan chmod]  
   **Jawaban:Perintah chown digunakan untuk mengubah pemilik (owner) atau grup dari sebuah file atau direktori, sedangkan chmod digunakan untuk mengubah izin akses (permission) file atau direktori, seperti hak untuk membaca, menulis, atau menjalankan.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
* Menjalankan perintah yang ditugaskan pada versi cloud agar meminimalisir masalah pada laptop pribadi
- Bagaimana cara Anda mengatasinya? 
* Bertanya kepada teman,menggunakan analogi agar dapat muda dipahami


---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
