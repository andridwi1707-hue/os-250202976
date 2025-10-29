
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : [Nama Mahasiswa]  
- **NIM**   : [NIM Mahasiswa]  
- **Kelas** : [Kelas]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> - Membuat dan mengatur proses (process management).
- Mengelola user, group, serta hak akses pengguna.
- Menampilkan, menghentikan, dan mengontrol proses yang sedang berjalan.
- Menghubungkan konsep user management dengan keamanan sistem operasi.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
Manajemen proses di Linux berkaitan dengan pengaturan jalannya program (proses) oleh sistem operasi, termasuk pembuatan, penjadwalan, dan penghentian proses. Setiap proses memiliki PID (Process ID) dan dapat dilihat atau dikendalikan menggunakan perintah seperti ps, top, kill, dan nice.
Manajemen user mengatur hak akses dan identitas pengguna dalam sistem. Setiap user memiliki UID (User ID) dan GID (Group ID) yang menentukan izin terhadap file atau proses. Pengaturan user dilakukan dengan perintah seperti useradd, passwd, usermod, dan deluser.
Tujuannya adalah menjaga keamanan, pembagian sumber daya, dan kestabilan sistem.
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
whoami
id
groups
sudo adduser praktikan
sudo passwd praktikan
ps aux | head -10
top -n 1
sleep 1000 &
ps aux | grep sleep
kill <PID>
pstree -p | head -20
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
Setiap perintah yang dijalankan di Linux akan memicu terbentuknya proses tersendiri yang memiliki identitas unik berupa PID (Process ID).
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
Ketika kita menjalankan perintah di terminal, sistem mengirimkan instruksi tersebut ke kernel melalui mekanisme system call. Selanjutnya, kernel bertanggung jawab untuk mengeksekusi serta mengatur jalannya proses hingga selesai sesuai instruksi pengguna.
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
Manajemen proses dan pengguna di Linux umumnya dilakukan melalui antarmuka berbasis teks di terminal menggunakan perintah seperti ps, top, atau kill, yang memberi akses penuh untuk memantau dan mengatur proses secara langsung. Sebaliknya, di Windows, pengelolaan proses lebih sering dilakukan lewat tampilan grafis seperti Task Manager atau lewat Command Prompt dengan perintah seperti tasklist, namun dengan kontrol yang lebih terbatas dibandingkan Linux.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. Linux memiliki sistem identitas dan izin akses yang terorganisir, sehingga keamanan dan pengendalian proses lebih terjamin.
2. Kernel berfungsi sebagai penghubung utama antara pengguna dan perangkat keras melalui system call.
3. Dibandingkan dengan Windows, sistem Linux lebih terbuka dan fleksibel dalam melakukan pemantauan serta pengaturan proses secara langsung.

---
---
## Tugas
1. Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.
```
whoami → menampilkan user aktif
id → info UID, GID, grup user
groups → daftar grup user
sudo adduser praktikan → buat user baru “praktikan”
sudo passwd praktikan → ubah/setel password user
ps aux | head -10 → lihat 10 proses awal
top -n 1 → tampilkan proses aktif sekali
sleep 1000 & → jalankan proses di background
ps aux | grep sleep → cari proses “sleep”
kill <PID> → hentikan proses
pstree -p | head -20 → tampilkan 20 baris awal pohon proses
```
2. Gambarkan hierarki proses dalam bentuk diagram pohon pstree di laporan.
```bash
bash(1)-+-dockerd(207)-+-containerd(234)-+-{containerd}(243)
        |              |                 |-{containerd}(244)
        |              |                 |-{containerd}(245)
        |              |                 |-{containerd}(246)
        |              |                 |-{containerd}(257)
        |              |                 |-{containerd}(260)
        |              |                 `-{containerd}(261)
        |              |-{dockerd}(213)
        |              |-{dockerd}(214)
        |              |-{dockerd}(215)
        |              |-{dockerd}(216)
        |              |-{dockerd}(231)
        |              |-{dockerd}(232)
        |              |-{dockerd}(262)
        |              |-{dockerd}(263)
        |              `-{dockerd}(463)
        |-logger(25)
        |-python(24)-+-editor-proxy(247)-+-runuser(467)---sh(468)---node(481)-+-node(3394)-+-node(3414)-+-{node}(3415)
        |            |                   |                                    |            |            |-{node}(3416)
        |            |                   |                                    |            |            |-{node}(3417)
```
---
## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
