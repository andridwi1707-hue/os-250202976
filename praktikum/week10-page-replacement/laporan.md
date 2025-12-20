
# Laporan Praktikum Minggu [10]
Topik: [Manajemen Memori – Page Replacement FIFO & LRU]

---

## Identitas
- **Nama**  : [Andri Dwi Yuliyanto]  
- **NIM**   : [250202976]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah *page fault*.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.


---

## Dasar Teori
Penggantian halaman (page replacement) merupakan mekanisme dalam sistem operasi yang digunakan untuk menentukan halaman mana yang harus dikeluarkan dari memori utama ketika memori penuh dan halaman baru perlu dimuat. Tujuannya adalah meminimalkan terjadinya page fault, yaitu kondisi ketika halaman yang dibutuhkan proses tidak tersedia di memori. Algoritma FIFO (First In First Out) mengganti halaman yang pertama kali masuk ke memori tanpa mempertimbangkan apakah halaman tersebut masih sering digunakan, sehingga bersifat sederhana namun kurang adaptif terhadap pola akses. Sebaliknya, algoritma LRU (Least Recently Used) mengganti halaman yang paling lama tidak digunakan dengan asumsi bahwa halaman yang baru saja dipakai memiliki peluang lebih besar untuk digunakan kembali, sehingga secara umum lebih efisien dalam menurunkan jumlah page fault meskipun memerlukan overhead pencatatan riwayat akses.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan *reference string* berikut sebagai contoh:
   ```
   7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
   ```
   Jumlah frame memori: **3 frame**.

2. **Implementasi FIFO**

   - Simulasikan penggantian halaman menggunakan algoritma FIFO.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

3. **Implementasi LRU**

   - Simulasikan penggantian halaman menggunakan algoritma LRU.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

4. **Eksekusi & Validasi**

   - Jalankan program untuk FIFO dan LRU.
   - Pastikan hasil simulasi logis dan konsisten.
   - Simpan screenshot hasil eksekusi.

5. **Analisis Perbandingan**

   Buat tabel perbandingan seperti berikut:

   | Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | ... | ... |
   | LRU | ... | ... |


   - Jelaskan mengapa jumlah *page fault* bisa berbeda.
   - Analisis algoritma mana yang lebih efisien dan alasannya.

6. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash

reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3



def simulate_fifo(reference, frame_size):
    frames = []
    page_fault = 0
    result = []

    for page in reference:
        if page in frames:
            status = "Hit"
        else:
            status = "Fault"
            page_fault += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)

        result.append((page, frames.copy(), status))

    return page_fault, result



def simulate_lru(reference, frame_size):
    frames = []
    page_fault = 0
    last_used = {}
    result = []

    for time, page in enumerate(reference):
        if page in frames:
            status = "Hit"
        else:
            status = "Fault"
            page_fault += 1

            if len(frames) < frame_size:
                frames.append(page)
            else:
                # Cari halaman yang paling lama tidak digunakan
                lru_page = min(frames, key=lambda p: last_used[p])
                frames[frames.index(lru_page)] = page

        last_used[page] = time
        result.append((page, frames.copy(), status))

    return page_fault, result



fifo_fault, fifo_result = simulate_fifo(reference_string, frame_size)
lru_fault, lru_result = simulate_lru(reference_string, frame_size)



def print_result(title, data, faults):
    print(f"\n{title}")
    print("Page\tFrame\t\tStatus")
    print("-" * 30)
    for page, frame, status in data:
        print(f"{page}\t{frame}\t{status}")
    print(f"Total Page Fault = {faults}")


print_result("FIFO Simulation", fifo_result, fifo_fault)
print_result("LRU Simulation", lru_result, lru_fault)

```

---
## Tugas
1. **Implementasi FIFO**
 
 | Referensi | Frame (setelah eksekusi) | Hit/Fault        |
 | --------- | ------------------------ | ---------------- |
 | 7         | 7 - -                    | Fault            |
 | 0         | 7 0 -                    | Fault            |
 | 1         | 7 0 1                    | Fault            |
 | 2         | 2 0 1                    | Fault (7 keluar) |
 | 0         | 2 0 1                    | **Hit**          |
 | 3         | 2 3 1                    | Fault (0 keluar) |
 | 0         | 2 3 0                    | Fault (1 keluar) |
 | 4         | 4 3 0                    | Fault (2 keluar) |
 | 2         | 4 2 0                    | Fault (3 keluar) |
 | 3         | 4 2 3                    | Fault (0 keluar) |
 | 0         | 0 2 3                    | Fault (4 keluar) |
 | 3         | 0 2 3                    | **Hit**          |
 | 2         | 0 2 3                    | **Hit**          |
 Hasil FIFO:
 Page Fault = 10
 Page Hit = 3
2. **Implementasi LRU**
 
 | Referensi | Frame (setelah eksekusi) | Hit/Fault                     |
 | --------- | ------------------------ | ----------------------------- |
 | 7         | 7 - -                    | Fault                         |
 | 0         | 7 0 -                    | Fault                         |
 | 1         | 7 0 1                    | Fault                         |
 | 2         | 2 0 1                    | Fault (7 paling lama dipakai) |
 | 0         | 2 0 1                    | **Hit**                       |
 | 3         | 2 0 3                    | Fault (1 paling lama dipakai) |
 | 0         | 2 0 3                    | **Hit**                       |
 | 4         | 4 0 3                    | Fault (2 paling lama dipakai) |
 | 2         | 4 0 2                    | Fault (3 paling lama dipakai) |
 | 3         | 4 3 2                    | Fault (0 paling lama dipakai) |
 | 0         | 0 3 2                    | Fault (4 paling lama dipakai) |
 | 3         | 0 3 2                    | **Hit**                       |
 | 2         | 0 3 2                    | **Hit**                       |
 Hasil LRU:
 Page Fault = 9
 Page Hit = 4
3. **Analisis Perbandingan**
 | Algoritma | Jumlah Page Fault | Keterangan                                                  |
 | --------- | ----------------- | ----------------------------------------------------------- |
 | FIFO      | 10                | Sederhana, tidak adaptif terhadap pola akses                |
 | LRU       | 9                 | Lebih adaptif, mempertahankan halaman yang sering digunakan |
 Analisis Perbedaan Page Fault:
 Mengapa jumlahnya berbeda?
 - FIFO hanya melihat urutan masuk
 - LRU melihat pola penggunaan aktual
 - Pada reference string ini, beberapa halaman seperti 0, 2, dan 3 sering digunakan kembali → LRU lebih “cerdas”   mempertahankannya
 Algoritma paling efisien:
 LRU lebih efisien, karena:
 - Page fault lebih sedikit
 - Lebih sesuai dengan prinsip locality of reference
Mendekati perilaku optimal (OPT), walau lebih kompleks diimplementasikan
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/Screenshot%202025-12-20%20223307.png)

---

## Analisis
Berdasarkan hasil praktik simulasi, algoritma FIFO menghasilkan 10 page fault sedangkan LRU menghasilkan 9 page fault. Perbedaan ini terjadi karena FIFO hanya mempertimbangkan urutan kedatangan halaman tanpa melihat frekuensi atau waktu penggunaan, sehingga dapat mengganti halaman yang masih sering dipakai. Sebaliknya, LRU mempertahankan halaman yang baru digunakan sehingga lebih sesuai dengan pola akses memori, membuatnya lebih efisien pada dataset uji.eda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. Algoritma LRU menghasilkan jumlah page fault lebih sedikit dibanding FIFO pada hasil praktik.
2. FIFO lebih sederhana tetapi kurang efisien karena tidak mempertimbangkan pola penggunaan halaman.
3. LRU lebih efektif dalam pengelolaan memori karena sesuai dengan prinsip locality of reference.
---

## Quiz
1. [Apa perbedaan utama FIFO dan LRU?]  
   **Jawaban:FIFO mengganti halaman yang paling awal masuk ke memori, sedangkan LRU mengganti halaman yang paling lama tidak digunakan.**  
2. [Mengapa FIFO dapat menghasilkan Belady’s Anomaly?]  
   **Jawaban:Karena FIFO tidak mempertimbangkan pola penggunaan halaman, sehingga penambahan jumlah frame justru bisa membuat halaman penting terbuang dan jumlah page fault meningkat (Belady’s Anomaly).**  
3. [Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?]  
   **Jawaban:Karena LRU mempertahankan halaman yang baru saja digunakan, sehingga lebih sesuai dengan prinsip locality of reference dan biasanya menghasilkan page fault lebih sedikit dibanding FIFO.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
Memahami materi
- Bagaimana cara Anda mengatasinya?  
Belajar menggunakan analogi agar mudah dipahami
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
