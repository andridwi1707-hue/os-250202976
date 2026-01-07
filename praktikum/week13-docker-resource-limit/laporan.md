
# Laporan Praktikum Minggu [13]
Topik: ["Docker Resource Limit"]

---

## Identitas
- **Nama**  : [Andri Dwi Yuliyanto]  
- **NIM**   : [250202976]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> 1. Membuat **Dockerfile sederhana** untuk menjalankan aplikasi/skrip.
2. Menjalankan container dengan **pembatasan resource** (CPU dan memori).
3. Mengamati dampak pembatasan resource melalui output program dan monitoring sederhana.
---

## Dasar Teori
>Docker adalah platform containerization yang digunakan untuk menjalankan aplikasi dalam lingkungan terisolasi yang disebut container. Docker memungkinkan pengelolaan resource seperti CPU dan memori melalui mekanisme pembatasan resource sehingga penggunaan sistem dapat dikontrol dengan baik. Pembatasan ini penting untuk menjaga kestabilan sistem dan memastikan aplikasi berjalan sesuai alokasi resource yang ditentukan.
---

## Langkah Praktikum
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```FROM python:3.10-alpine
WORKDIR /app
COPY code/test.py .
CMD ["python","test.py"]
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/docker%20(1).png)
![Screenshot hasil](screenshots/docker%20(2).png)
![Screenshot hasil](screenshots/docker%20(3).png)
![Screenshot hasil](screenshots/docker%20(4).png)
![Screenshot hasil](screenshots/docker%20(5).png)
![Screenshot hasil](screenshots/docker%20(6).png)
![Screenshot hasil](screenshots/docker%20(7).png)
![Screenshot hasil](screenshots/Screenshot%202026-01-07%20152800.png)
---

## Analisis
1. Pengujian Tanpa Batasan Resource
Program uji resource berhasil dijalankan tanpa batasan CPU dan memori. Selama pengujian, program menunjukkan peningkatan penggunaan memori secara bertahap, yang ditandai dengan bertambahnya jumlah iterasi dan estimasi memori terpakai. Proses berjalan cukup lama dan dihentikan pada tahap tertentu setelah penggunaan resource meningkat signifikan.
2. Pada pengujian tanpa batasan resource 
container memiliki keleluasaan dalam menggunakan CPU dan memori sehingga proses berjalan lebih cepat. Sebaliknya, saat diberikan batasan resource, performa container menurun dan proses berjalan lebih lambat, menandakan bahwa pembatasan resource oleh Docker berjalan dengan efektif.
3. Monitoring Resource Container
Monitoring penggunaan resource dilakukan menggunakan perintah docker stats. Hasil pengamatan menunjukkan bahwa container menggunakan CPU sekitar 2–3% dan memori antara 448 MB hingga 562 MB dari total memori yang tersedia sebesar 1.553 GB. Hal ini menunjukkan bahwa aplikasi di dalam container secara aktif menggunakan resource, dan Docker mampu memonitor serta mengelola penggunaan resource tersebut secara real-time.
---

## Kesimpulan
Docker mampu menjalankan dan membatasi penggunaan resource CPU dan memori pada container secara efektif. Pemberian batasan resource berpengaruh langsung terhadap performa aplikasi, sehingga manajemen resource menjadi penting untuk menjaga kestabilan sistem.Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Mengapa container perlu dibatasi CPU dan memori?]  
   **Jawaban:Untuk mencegah penggunaan resource berlebihan dan menjaga kestabilan sistem.**  
2. [Apa perbedaan VM dan container dalam konteks isolasi resource?]  
   **Jawaban:VM mengisolasi resource melalui sistem operasi tersendiri, sedangkan container berbagi kernel host dan mengisolasi resource secara lebih ringan melalui pembatasan CPU dan memori.**  
3. [Apa dampak limit memori terhadap aplikasi yang boros memori?]  
   **Jawaban:Aplikasi akan melambat atau dihentikan ketika penggunaan memori melebihi batas yang ditentukan.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
Keterbatasan spesifikasi Laptop saya menjadi salah satu kendala,singkatnya Laptop kentang.
- Bagaimana cara Anda mengatasinya?  
Bersyukur

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
