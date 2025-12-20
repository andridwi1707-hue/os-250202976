
# Laporan Praktikum Minggu [9]
Topik: [Simulasi Algoritma Penjadwalan CPU]

---

## Identitas
- **Nama**  : [Andri Dwi Yuliyanto]  
- **NIM**   : [50202976]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.  
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.  
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.  
4. Menjelaskan hasil simulasi secara tertulis.  
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.


---

## Dasar Teori
Penjadwalan CPU (CPU Scheduling) merupakan mekanisme pada sistem operasi untuk menentukan urutan eksekusi proses yang siap menggunakan CPU, dengan tujuan meningkatkan efisiensi pemakaian prosesor dan kinerja sistem secara keseluruhan. Salah satu algoritma penjadwalan paling dasar adalah First Come First Served (FCFS), yaitu algoritma non-preemptive yang mengeksekusi proses berdasarkan urutan kedatangan (arrival time). Proses yang datang lebih dahulu akan dieksekusi terlebih dahulu hingga selesai tanpa interupsi.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**

   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
# FCFS Scheduling Simulation

processes = [
    ("P1", 0, 6),
    ("P2", 1, 8),
    ("P3", 2, 7),
    ("P4", 3, 3)
]

current_time = 0
results = []

for process in processes:
    pid, arrival, burst = process

    if current_time < arrival:
        current_time = arrival

    start_time = current_time
    waiting_time = start_time - arrival
    turnaround_time = waiting_time + burst
    finish_time = start_time + burst

    current_time = finish_time

    results.append([
        pid, arrival, burst,
        waiting_time, turnaround_time
    ])

# Output tabel
print("Proses | Arrival | Burst | Waiting | Turnaround")
print("-" * 45)
for r in results:
    print(f"{r[0]:<6} | {r[1]:<7} | {r[2]:<5} | {r[3]:<7} | {r[4]:<10}")

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/Screenshot%202025-12-20%20215104.png)

---

## Analisis
1. Alur Program
Program membaca data proses (arrival time dan burst time), lalu mengeksekusi proses satu per satu sesuai urutan kedatangan menggunakan algoritma FCFS. Setiap proses dihitung waktu tunggunya (waiting time) dan waktu penyelesaiannya (turnaround time), kemudian hasilnya ditampilkan dalam tabel.

2. Perbandingan Simulasi dan Perhitungan Manual
Hasil simulasi sama dengan perhitungan manual, baik urutan proses maupun nilai waiting time dan turnaround time, sehingga implementasi algoritma dinyatakan benar.

3. Kelebihan dan Keterbatasan Simulasi
Kelebihan simulasi adalah sederhana, akurat, dan mengurangi kesalahan perhitungan manual. Keterbatasannya, simulasi tidak mempertimbangkan preemption, prioritas proses, dan kondisi sistem nyata seperti context switching.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. Simulasi CPU scheduling dengan algoritma FCFS dapat membantu memahami konsep waiting time dan turnaround time secara lebih jelas dan terstruktur.

2. Hasil simulasi sesuai dengan perhitungan manual, sehingga membuktikan bahwa algoritma telah diimplementasikan dengan benar.

3. Praktik ini menunjukkan bahwa FCFS sederhana dan mudah diterapkan, namun kurang efisien untuk sistem dengan proses berdurasi panjang.
---

## Quiz
1. [Mengapa simulasi diperlukan untuk menguji algoritma scheduling?]  
   **Jawaban:Simulasi diperlukan untuk memastikan algoritma scheduling bekerja sesuai teori, memudahkan perbandingan dengan perhitungan manual, serta memungkinkan pengujian berbagai skenario tanpa risiko pada sistem nyata.**  
2. [Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?]  
   **Jawaban:Pada dataset besar, perhitungan manual lebih lambat dan rawan kesalahan, sedangkan simulasi tetap cepat, konsisten, dan akurat.**  
3. [Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.]  
   **Jawaban:Algoritma FCFS lebih mudah diimplementasikan karena proses dieksekusi langsung berdasarkan urutan kedatangan tanpa perlu perhitungan tambahan atau pengurutan burst time. Struktur logikanya sederhana sehingga mudah dipahami dan dikodekan.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
Memahami materi.
- Bagaimana cara Anda mengatasinya?  
menggunakan analogi

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
