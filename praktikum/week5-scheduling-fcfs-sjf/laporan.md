
# Laporan Praktikum Minggu [5]
Topik: [Penjadwalan CPU – FCFS dan SJF]

---

## Identitas
- **Nama**  : [Andri Dwi Yuliyanto]  
- **NIM**   : [250202976]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> 1. Menghitung waiting time dan turnaround time untuk algoritma FCFS dan SJF.
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.


---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
Penjadwalan CPU adalah mekanisme sistem operasi untuk menentukan urutan eksekusi proses agar penggunaan prosesor efisien dan adil. Tujuannya untuk meminimalkan waktu tunggu (waiting time) dan waktu penyelesaian (turnaround time) setiap proses. Dua algoritma dasar yang umum digunakan adalah FCFS dan SJF.
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
 1. **Siapkan Data Proses**
   Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):
   | Proses | Burst Time | Arrival Time |
   |:--:|:--:|:--:|
   | P1 | 6 | 0 |
   | P2 | 8 | 1 |
   | P3 | 7 | 2 |
   | P4 | 3 | 3 |

 2. **Eksperimen 1 – FCFS (First Come First Served)**
   - Urutkan proses berdasarkan *Arrival Time*.  
   - Hitung nilai berikut untuk tiap proses:
     ```
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
     ```
   - Hitung rata-rata Waiting Time dan Turnaround Time.  
   - Buat Gantt Chart sederhana:  
     ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
     ```

 3. **Eksperimen 2 – SJF (Shortest Job First)**
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).  
   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.  
   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS | ... | ... | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF | ... | ... | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

 4. **Eksperimen 3 – Visualisasi Spreadsheet (Opsional)**
   - Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
     - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
     - Gunakan formula dasar penjumlahan/subtraksi.
   - Screenshot hasil perhitungan dan simpan di:
     ```
     praktikum/week5-scheduling-fcfs-sjf/screenshots/
     ```

 5. **Analisis**
   - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
   - Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
   - Tambahkan kesimpulan singkat di akhir laporan.


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
Membuat tabel FCFS yang diperintahkan
Membuat tabel SJF yang diperintahkan
Bandingkan antara FCFS dan SJF
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/FCFS%20DAN%20SJF%20(1).png)
![Screenshot hasil](screenshots/FCFS%20DAN%20SJF%20(2).png)

---
## Tugas

# Eksperiment 1
| Proses | Arrival |	Burst | Start | Finish | Waiting Time (WT) | Turnaround Time (TAT) |
|--------|---------|-------|-------|--------|-------------------|-----------------------|
| P1 |	0 |	6 |	0 | 6 |	0 | 6 |
| P2 |	1 |	8 |	6 | 14 |	5 | 13 |
| P3 |	2 |	7 |	14 | 21 | 12 | 19 |
| P4 |	3 |	3 |	21 | 24 | 18 |	21 |
| Total | ... | ... | ... | ... | 35 | 59 |
| Average | ... | ... | ... | ... | 8.75 | 14.75 |

Grant 
| P1 | P2 | P3 | P4 |
0 6 14 21 24

# Eksperiment 2
| Proses | Arrival |	Burst |	Start |	Finish |	Waiting Time (WT) | Turnaround Time (TAT) |
|--------|---------|-------|--------|---------|-------------------|-----------------------|
| P1 | 0 |	6 | 0 | 6 |	0 | 6 |
| P4 | 3 |	3 | 6 | 9 |	3 | 6 |
| P3 | 2 |	7 | 9 | 16 | 7 | 14 |
| P2 | 1 | 8 | 16 | 24 | 15 |	23 |
| Total | ... | ... | ... | ... | 45 | 59 |
| Average | ... | ... | ... | ... | 6.25 | 12.25 |

# PERBANDINGAN ANTARA SJF DAN FCFS
| Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
|------------|------------------|----------------------|------------|-------------|
| FCFS | 8.75 | 14.75 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
| SJF | 6.25 | 12.25 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

# Analisis
 - Analisis Perbandingan
 Berdasarkan perhitungan pada eksperimen sebelumnya, perbandingan rata-rata waktu sebagai berikut:
 Average Waiting Time (WT): FCFS = 8.75, SJF = 6.25.
 Average Turnaround Time (TAT): FCFS = 14.75, SJF = 12.25.
 Dari angka di atas terlihat bahwa SJF memberikan rata-rata WT dan TAT yang lebih kecil dibandingkan FCFS pada skenario data proses yang diberikan.
 - Kapan SJF lebih unggul dan kapan FCFS lebih cocok
 SJF lebih unggul ketika:
 Mayoritas proses memiliki durasi eksekusi yang pendek atau ada banyak pekerjaan kecil; SJF memproses yang singkat terlebih dahulu sehingga mengurangi waktu tunggu rata-rata.
 Sistem bersifat batch atau non-interaktif di mana estimasi burst time dapat dipercaya.
 Tujuan utama adalah meminimalkan rata-rata waktu tunggu/turnaround.
 FCFS lebih cocok ketika:
 Keadilan berdasarkan urutan kedatangan penting (mis. antrian layanan yang harus dilayani sesuai urutan).
 Sistem interaktif atau real-time yang memerlukan prediktabilitas dan sederhana dalam implementasi.
 Estimasi burst time tidak dapat diandalkan atau tidak tersedia.



---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
SJF menghasilkan waktu tunggu dan waktu penyelesaian rata-rata yang lebih rendah dibanding FCFS. FCFS lebih sederhana dan adil, sedangkan SJF lebih efisien untuk proses pendek. Secara umum, SJF lebih unggul dalam efisiensi, sementara FCFS lebih baik dalam kesederhanaan dan keadilan.
---

## Quiz
1. [Apa perbedaan utama antara FCFS dan SJF? singkat saja]  
   **Jawaban:Perbedaan utamanya, FCFS menjalankan proses berdasarkan urutan kedatangan, sedangkan SJF menjalankan proses dengan waktu eksekusi paling singkat terlebih dahulu.**  
2. [Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?]  
   **Jawaban:Karena SJF memprioritaskan proses dengan waktu eksekusi paling singkat, sehingga proses cepat selesai lebih dulu dan mengurangi waktu tunggu total bagi semua proses.**  
3. [Apa kelemahan SJF jika diterapkan pada sistem interaktif?]  
   **Jawaban:Kelemahan SJF pada sistem interaktif adalah proses yang lama bisa terus tertunda (starvation) karena selalu kalah prioritas dari proses yang lebih pendek, dan sulit memperkirakan waktu eksekusi setiap proses secara akurat.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
