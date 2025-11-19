
# Laporan Praktikum Minggu [7]
Topik: ["Sinkronisasi Proses dan Masalah Deadlock"]

---

## Identitas
- **Nama**  : [Andri Dwi Yuliyanto]  
- **NIM**   : [250202976]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> 1. Mengidentifikasi empat kondisi penyebab deadlock (*mutual exclusion, hold and wait, no preemption, circular wait*).  
2. Menjelaskan mekanisme sinkronisasi menggunakan *semaphore* atau *monitor*.  
3. Menganalisis dan memberikan solusi untuk kasus deadlock.  
4. Berkolaborasi dalam tim untuk menyusun laporan analisis.  
5. Menyajikan hasil studi kasus secara sistematis.  


---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
1. Race Condition – Terjadi ketika dua atau lebih proses mengakses data bersama secara bersamaan sehingga hasilnya bergantung pada urutan eksekusi.
2. Critical Section – Bagian kode yang mengakses data bersama dan harus dijalankan secara eksklusif untuk mencegah konflik.
3. Mekanisme Sinkronisasi – Tools seperti semaphore, mutex, dan monitor digunakan untuk mengatur akses terkoordinasi ke sumber daya bersama.
4. Kondisi Deadlock – Deadlock muncul saat empat syarat Coffman terpenuhi: mutual exclusion, hold and wait, no preemption, dan circular wait.
Sumber:
Silberschatz, Galvin, Gagne — Operating System Concepts
Stallings — Operating Systems: Internals and Design Principles

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan. 
1. Persiapan Tim
   - Bentuk kelompok beranggotakan 3–4 orang.  
   - Tentukan ketua dan pembagian tugas (analisis, implementasi, dokumentasi).

2. Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)
   - Implementasikan versi sederhana dari masalah *Dining Philosophers* tanpa mekanisme pencegahan deadlock.  
   - Contoh pseudocode:
     ```text
     while true:
       think()
       pick_left_fork()
       pick_right_fork()
       eat()
       put_left_fork()
       put_right_fork()
     ```
   - Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).  
   - Identifikasi kapan dan mengapa deadlock terjadi.

3. Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)
   - Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:
     - Menggunakan *semaphore (mutex)* untuk mengontrol akses.
     - Membatasi jumlah filosof yang dapat makan bersamaan (max 4).  
     - Mengatur urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).  
   - Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.

4. Eksperimen 3 – Analisis Deadlock
   - Jelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut dipecahkan pada versi fixed.  
   - Sajikan hasil analisis dalam tabel seperti contoh berikut:

     | Kondisi Deadlock | Terjadi di Versi Deadlock | Solusi di Versi Fixed |
     |------------------|---------------------------|------------------------|
     | Mutual Exclusion | Ya (satu garpu hanya satu proses) | Gunakan semaphore untuk kontrol akses |
     | Hold and Wait | Ya | Hindari proses menahan lebih dari satu sumber daya |
     | No Preemption | Ya | Tidak ada mekanisme pelepasan paksa |
     | Circular Wait | Ya | Ubah urutan pengambilan sumber daya |

5. Eksperimen 4 – Dokumentasi
   - Simpan semua diagram, screenshot simulasi, dan hasil diskusi di:
     ```
     praktikum/week7-concurrency-deadlock/screenshots/
     ```
   - Tuliskan laporan kelompok di `laporan.md` (format IMRaD singkat: *Pendahuluan, Metode, Hasil, Analisis, Diskusi*).

6. Commit & Push
   ```bash
   git add .
   git commit -m "Minggu 7 - Sinkronisasi Proses & Deadlock"
   git push origin main
   ``` 


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
import threading
import time

N = 5  # jumlah filosof (1 sampai 5)
forks = [threading.Semaphore(1) for _ in range(N)]
max_dining = threading.Semaphore(N - 1)  # maksimal 4 filosof makan bersamaan

def philosopher(i):
    name = f"Filosof {i+1}"  # tampilkan Filosof 1–5
    while True:
        print(f"{name} sedang berpikir...")
        time.sleep(1)

        max_dining.acquire()

        if i == N - 1:
            # Filosof terakhir (Filosof 5) ambil garpu kanan dulu
            forks[(i + 1) % N].acquire()
            forks[i].acquire()
        else:
            # Filosof lain ambil garpu kiri dulu
            forks[i].acquire()
            forks[(i + 1) % N].acquire()

        print(f"{name} mulai makan...")
        time.sleep(2)

        # selesai makan, letakkan garpu
        forks[i].release()
        forks[(i + 1) % N].release()
        max_dining.release()

        print(f"{name} selesai makan.")

# buat thread untuk setiap filosof
threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/dokumentasi.jpeg)
![Screenshot hasil](screenshots/diskusi%20kelompok.png)

---

## Analisis
Ketua          : Andri Dwi Yuliyanto (250202976)

Implementasi   : Andri Dwi Yuliyanto (250202976)

Analisis       : Rafi Nurul Fauzan (250202961)

Dokumentasi    : Muhammad Fajri Abdullah (250202979)


Analisis Versi Deadlock dan Versi Fixed Dining Philosophers

Versi Deadlock

1. Filosof selalu ambil garpu kiri lalu garpu kanan.
2. Jika semua filosof ambil garpu kiri secara bersamaan, mereka akan tunggu garpu kanan yang sedang dipegang oleh filosofi lain.Terjadi circular wait dan semua stuck (deadlock).
3. Tidak ada filosof yang dapat makan karena saling tunggu.

Versi Fixed (Bebas Deadlock)

1. Gunakan mekanisme sinkronisasi, misalnya semaphore atau mutex.
2. Dibatasi jumlah filosof yang boleh makan bersama, misal maksimal 4 dari 5 filosofi.
3. Filosof terakhir ambil garpu dengan urutan terbalik (kanan dulu, baru kiri) untuk cegah circular wait.
4. Filosof hanya ambil garpu jika kedua garpu tersedia. 
5. Deadlock dicegah karena setidaknya satu filosof dapat makan dan melepaskan garpu sehingga siklus berjalan.



Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)

Pseudocode Deadlock Version

```pseudo
while true:
    think()
    pick_left_fork()
    pick_right_fork()
    eat()
    put_left_fork()
    put_right_fork()
```

Analisis Deadlock
Deadlock terjadi saat semua filosofi ambil garpu kiri mereka tapi menunggu garpu kanan yang sedang dipegang filosof lain. Maka semua filosofi stuck saling tunggu garpu satu sama lain, tidak ada yang bisa makan, lalu jadilah kondisi deadlock.



Eksperimen 2 – Versi Fixed (Menggunakan Semaphore)


Modifikasi Pseudocode

```pseudo
semaphore max_dining = 4

while true:
    think()
    wait(max_dining)           # Batasi max filosof yang makan bersamaan
    if id_filosof == N:        # Filosof terakhir mengambil garpu secara terbalik
        pick_right_fork()
        pick_left_fork()
    else:
        pick_left_fork()
        pick_right_fork()
    eat()
    put_left_fork()
    put_right_fork()
    signal(max_dining)
```

Analisis hasil:
- Maksimal 4 filosof makan bersamaan, cegah semuanya ambil garpu dan tunggu.
- Filosof terakhir ubah urutan pengambilan garpu, lalu hilangkan circular wait.
- Dengan semaphore, mutual exclusion tetap terjaga.
- Deadlock tidak terjadi karena semua empat kondisi deadlock dicegah.


Eksperimen 3 – Analisis Deadlock dalam Tabel

| Kondisi Deadlock     | Terjadi di Versi Deadlock | Solusi di Versi Fixed                                              |
|----------------------|---------------------------|-------------------------------------------------------------------|
| Mutual Exclusion      | Ya                        | Gunakan semaphore untuk mengontrol akses garpu                    |
| Hold and Wait        | Ya                        | Batasi jumlah filosof yang makan bersamaan (semaphore max_dining)|
| No Preemption        | Ya                        | Filosof melepaskan garpu secara sukarela setelah makan            |
| Circular Wait        | Ya                        | Filosof terakhir mengambil garpu secara terbalik                  |

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. Kasus para filsuf yang sedang makan menunjukkan betapa sulitnya menjaga keteraturan saat beberapa proses harus berbagi sumber daya yang jumlahnya terbatas. Tanpa pengaturan akses yang tepat, sistem dapat berhenti bekerja karena saling menunggu.


2. Situasi deadlock muncul ketika setiap filsuf sudah memegang satu garpu, tetapi garpu pasangannya tidak tersedia, sehingga seluruh aktivitas terhenti karena semua pihak saling menanti.


3. Untuk menghindari kondisi tersebut, dapat digunakan mekanisme pengendali seperti semaphore atau mutex, membatasi jumlah filsuf yang diizinkan makan pada saat yang sama, atau mengubah pola pengambilan garpu agar siklus saling menunggu tidak terbentuk.


---

## Quiz
1. [Sebutkan empat kondisi utama penyebab deadlock.]  
   **Jawaban:1. Mutual Exclusion – Sumber daya hanya bisa digunakan oleh satu proses pada satu waktu. 2. Hold and Wait – Proses sudah memegang sebagian sumber daya dan menunggu sumber daya lain.3. No Preemption – Sumber daya yang sedang digunakan tidak bisa diambil paksa dari proses.4. Circular Wait – Terjadi rantai proses yang saling menunggu sumber daya satu sama lain secara melingkar.**  
2. [Mengapa sinkronisasi diperlukan dalam sistem operasi?]  
   **Jawaban:Sinkronisasi diperlukan untuk mencegah konflik antarproses, menjaga konsistensi data, dan memastikan eksekusi berjalan tertib.**  
3. [Jelaskan perbedaan antara semaphore dan monitor.]  
   **Jawaban:Semaphore adalah mekanisme sinkronisasi berbasis counter yang mengontrol akses ke sumber daya melalui operasi wait dan signal, dan penggunaannya harus diatur secara manual oleh programmer. Monitor adalah mekanisme sinkronisasi tingkat lebih tinggi yang menyediakan penguncian otomatis dan condition variables, sehingga koordinasi antarproses lebih terstruktur dan lebih mudah digunakan.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
 kerja sama tim 
- Bagaimana cara Anda mengatasinya?  
 saling komunikasi dan berbagi ilmu

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
