
# Laporan Praktikum Minggu [4]
Topik: [Manajemen Proses dan User di Linux]

---

## Identitas
- **Nama**  : [Andri Dwi Yuliyanto]  
- **NIM**   : []  
- **Kelas** : [1IKRB]

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
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.
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
![Screenshot hasil](screenshots/proses%20user%20(1).png)
![Screenshot hasil](screenshots/proses%20user%20(2).png)
![Screenshot hasil](screenshots/proses%20user%20(3).png)

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
tree = """
bash(1)
 ├─dockerd(207)
 │   ├─containerd(234)
 │   │   ├─{containerd}(243)
 │   │   ├─{containerd}(244)
 │   │   └─{containerd}(261)
 │   ├─{dockerd}(213)
 │   └─{dockerd}(463)
 ├─logger(25)
 └─python(24)
     └─editor-proxy(247)
         └─runuser(467)
             └─sh(468)
                 └─node(481)
                     └─node(3394)
                         └─node(3414)
"""
print(tree)

```
3. Jelaskan hubungan antara user management dan keamanan sistem Linux.
User management berhubungan langsung dengan keamanan sistem Linux karena pengaturan user dan izin akses menentukan siapa yang boleh menjalankan atau mengubah file, sehingga mencegah penyalahgunaan dan melindungi sistem dari akses tidak sah.
---
## Quiz
1. [Apa fungsi dari proses init atau systemd dalam sistem Linux ?]  
   **Jawaban:Mengelola dan menjalankan proses utama saat booting serta mengatur layanan sistem.**  
2. [Apa perbedaan antara kill dan killall ?]  
   **Jawaban:kill menghentikan proses berdasarkan PID, sedangkan killall menghentikan semua proses dengan nama program yang sama.**  
3. [Mengapa user root memiliki hak istimewa di sistem Linux ?]  
   **Jawaban:Karena root adalah administrator utama yang memiliki akses penuh untuk mengubah, menghapus, atau mengatur semua file dan proses di sistem.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
Menjalankan perintah yang ditugaskan pada versi cloud agar meminimalisir masalah pada laptop pribadi 
- Bagaimana cara Anda mengatasinya?  
Bertanya kepada teman,menggunakan analogi agar dapat muda dipahami

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
