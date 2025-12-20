
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul top"]

---

## Identitas
- **Nama**  : [Andri Dwi Yuliyanto]  
- **NIM**   : [NIM Mahasiswa]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Membuat program sederhana untuk mendeteksi deadlock.  
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.  
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.  
4. Memberikan interpretasi hasil uji secara logis dan sistematis.  
5. Menyusun laporan praktikum sesuai format yang ditentukan.
---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---
# Tugas
1. **Implementasi Algoritma Deteksi Deadlock**
 ```
 # Dataset: proses -> (resource yang dipegang, resource yang diminta)
 processes = {
    "P1": ("R1", "R2"),
    "P2": ("R2", "R3"),
    "P3": ("R3", "R1")
 }

 # Membangun Wait-For Graph
 wait_for = {}
 for p1, (_, req) in processes.items():
    for p2, (alloc, _) in processes.items():
        if req == alloc:
            wait_for[p1] = p2

 # Deteksi siklus (deadlock)
 visited = set()
 def detect_cycle(p):
    if p in visited:
        return True
    visited.add(p)
    if p in wait_for:
        return detect_cycle(wait_for[p])
    return False

 deadlock = detect_cycle("P1")

 # Output hasil
 print("Deadlock terjadi:" if deadlock else "Tidak terjadi deadlock")
 print("Proses yang terlibat:", list(visited))

 ```
2. **Tabel Hasil Analisis**
 | Proses | Allocation | Request | Status   |
 | ------ | ---------- | ------- | -------- |
 | P1     | R1         | R2      | Deadlock |
 | P2     | R2         | R3      | Deadlock |
 | P3     | R3         | R1      | Deadlock |

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

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
