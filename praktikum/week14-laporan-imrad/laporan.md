
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : [Nama Mahasiswa]  
- **NIM**   : [NIM Mahasiswa]  
- **Kelas** : [Kelas]

---

# week14-laporan-imrad

> **Editor**: Visual Studio Code  
> **Format**: Markdown (`.md`)  
> **Topik**: Docker Resource Limit (CPU & Memori)

---

## Pendahuluan (Introduction)

Docker merupakan teknologi container yang memungkinkan aplikasi berjalan secara terisolasi dengan penggunaan sumber daya yang efisien (Merkel, 2014). Namun, container yang berjalan tanpa batasan dapat mengonsumsi CPU dan memori secara berlebihan sehingga menurunkan performa sistem host. Oleh karena itu, Docker menyediakan mekanisme pembatasan sumber daya (*resource limit*) untuk mengontrol penggunaan CPU dan memori pada setiap container (Pahl, 2015).

**Tujuan Praktikum**:

* Menguji dampak pembatasan CPU dan memori pada Docker container.
* Mengamati perbedaan penggunaan sumber daya sebelum dan sesudah diberi limit.
* Menilai pengaruh resource limit terhadap stabilitas sistem host.

---

## Metode (Methods)

### Lingkungan Uji

* **Host OS** : Windows 10
* **Tools**   : Docker Desktop, Visual Studio Code
* **Image**   : Python (alpine)
* **Hardware**: Laptop dengan RAM 4 GB

### Kode Program Uji

```python
# stress_test.py
import time

data = []
while True:
    data.append('A' * 10**6)
    time.sleep(0.1)
```

### Langkah Eksperimen

1. Membuat file program uji menggunakan VS Code.
2. Menulis `Dockerfile` dan melakukan *build image*.
3. Menjalankan container tanpa batasan resource.
4. Menjalankan container dengan limit CPU dan memori.
5. Memantau penggunaan resource menggunakan perintah berikut:

```bash
docker stats
```

### Parameter Uji

* **CPU**   : 0.5 core
* **Memori**: 512 MB

### Cara Pengukuran

Pengukuran dilakukan dengan mencatat nilai CPU (%) dan penggunaan memori (MB) yang ditampilkan oleh perintah `docker stats`.

---

## Hasil (Results)

### Tabel Hasil Pengujian

**Tabel 1. Penggunaan CPU dan Memori Docker Container**

| Kondisi Container | CPU (%) | Memori (MB) |
| ----------------- | ------- | ----------- |
| Tanpa Limit       | > 80%   | > 800 MB    |
| Dengan Limit      | < 50%   | ± 450 MB    |

### Bukti Eksekusi

![Screenshot hasil](screenshots/Screenshot%202026-01-07%20152800.png)


### Ringkasan Temuan

1. Container tanpa limit menggunakan CPU dan memori secara agresif.
2. Penerapan limit membuat penggunaan resource lebih terkendali.
3.  Sistem host menjadi lebih stabil.

---

## Pembahasan (Discussion)

Hasil praktikum menunjukkan bahwa fitur *resource limiting* pada Docker bekerja sesuai teori containerization, yaitu dengan memanfaatkan *control groups (cgroups)* untuk membatasi alokasi CPU dan memori (Merkel, 2014; Pahl, 2015). Keterbatasan utama pada praktikum ini adalah spesifikasi laptop dengan RAM hanya 4 GB, sehingga proses pengujian tidak dapat dijalankan dalam skala besar dan performa container relatif lambat.

---

## Kesimpulan

* Pembatasan CPU dan memori pada Docker container dapat diterapkan secara efektif.
* Resource limit membantu menjaga stabilitas sistem host.
* Keterbatasan perangkat keras mempengaruhi hasil eksperimen.

---
## Quiz
1. [Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?]  
   **Jawaban:Format IMRAD membuat laporan praktikum lebih ilmiah dan mudah dievaluasi karena menyajikan isi secara sistematis, jelas, dan sesuai alur metode ilmiah. Setiap bagian memudahkan dosen menilai tujuan, metode, hasil, dan pembahasan secara terpisah dan objektif.**  
2. [Apa perbedaan antara bagian Hasil dan Pembahasan?]  
   **Jawaban:Hasil menyajikan data atau temuan eksperimen secara objektif (tabel, grafik, angka) tanpa interpretasi, sedangkan Pembahasan menjelaskan makna hasil tersebut, mengaitkannya dengan teori, serta membahas keterbatasan dan penyebabnya.**  
3. [Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?]  
   **Jawaban:Sitasi dan daftar pustaka penting karena menunjukkan dasar teori yang digunakan, menjaga kejujuran akademik (menghindari plagiarisme), serta memudahkan pembaca menelusuri dan memverifikasi sumber rujukan, sehingga laporan praktikum lebih kredibel dan ilmiah.**  
---

## Daftar Pustaka

1. Merkel, D. (2014). *Docker: Lightweight Linux Containers for Consistent Development and Deployment*. Linux Journal.
2. Pahl, C. (2015). *Containerization and the PaaS Cloud*. IEEE Cloud Computing.
