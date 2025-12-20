
# Laporan Praktikum Minggu [11]
Topik: [Simulasi dan Deteksi Deadlock]

---

## Identitas
- **Nama**  : [Andri Dwi Yuliyanto]  
- **NIM**   : [250202976]  
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
 Deadlock dalam sistem operasi adalah kondisi ketika dua atau lebih proses saling menunggu sumber daya yang sedang dipegang proses lain sehingga tidak ada satu pun proses yang dapat melanjutkan eksekusi. Deteksi deadlock dilakukan dengan menganalisis hubungan ketergantungan antara proses dan resource, salah satunya menggunakan wait-for graph yang merepresentasikan proses sebagai simpul dan hubungan tunggu sebagai sisi. Jika pada graf tersebut terbentuk siklus, maka sistem berada dalam kondisi deadlock. Secara teori, deadlock hanya dapat terjadi apabila empat kondisi terpenuhi secara bersamaan, yaitu mutual exclusion, hold and wait, no preemption, dan circular wait. Pendekatan deteksi deadlock bertujuan mengidentifikasi kondisi ini agar sistem dapat mengambil tindakan pemulihan yang tepat.
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
# Data proses: (Allocation, Request)
processes = {
    "P1": ("R1", "R2"),
    "P2": ("R2", "R3"),
    "P3": ("R3", "R1")
}

# Resource -> pemilik proses
owner = {alloc: p for p, (alloc, _) in processes.items()}

# Bangun Wait-For Graph
wfg = {}
for p, (_, req) in processes.items():
    if req in owner:
        wfg[p] = owner[req]

visited, stack, deadlock = set(), set(), set()

def dfs(p):
    if p in stack:
        deadlock.update(stack)
        return
    if p in visited:
        return
    visited.add(p)
    stack.add(p)
    if p in wfg:
        dfs(wfg[p])
    stack.remove(p)

for p in wfg:
    dfs(p)

# Output
if deadlock:
    print("Sistem DEADLOCK")
    print("Proses terlibat:", deadlock)
else:
    print("Tidak terjadi deadlock")

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
  |:------:|:----------:|:-------:|:--------:|
  | P1     | R1         | R2      | Deadlock |
  | P2     | R2         | R3      | Deadlock |
  | P3     | R3         | R1      | Deadlock |
3. **Narasi Hasil Analisis**
Berdasarkan hasil simulasi dan analisis manual, sistem berada dalam kondisi deadlock. Setiap proses memegang satu resource dan menunggu resource lain yang sedang dipegang oleh proses berbeda, sehingga membentuk circular wait. Karena resource bersifat eksklusif, tidak dapat diambil paksa, dan setiap proses menahan resource sambil menunggu resource lain, maka keempat kondisi deadlock terpenuhi. Akibatnya, tidak ada proses yang dapat melanjutkan eksekusi.
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/Screenshot%202025-12-20%20235014.png)

---

## Analisis
Hasil praktik menunjukkan bahwa sistem mengalami deadlock karena terdapat siklus ketergantungan antar proses, di mana setiap proses menahan satu resource dan menunggu resource lain yang dipegang proses lain. Deteksi program dan analisis manual memberikan hasil yang sama, sehingga membuktikan bahwa kondisi deadlock terjadi sesuai dengan teori.
---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. Terjadi siklus ketergantungan antar proses sehingga sistem berada dalam kondisi deadlock.
2. Semua proses saling menunggu resource yang sedang dipegang proses lain.
3. Hasil simulasi program sesuai dengan analisis teori deadlock.
---

## Quiz
1. [Apa perbedaan antara deadlock prevention, avoidance, dan detection?]  
   **Jawaban:Deadlock prevention mencegah sejak awal, avoidance menghindari dengan alokasi aman, dan detection mendeteksi lalu memulihkan setelah terjadi.**  
2. [Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?]  
   **Jawaban:Deteksi deadlock tetap diperlukan karena tidak semua sistem dapat mencegah atau menghindari deadlock tanpa mengorbankan efisiensi, sehingga deadlock dibiarkan terjadi dan kemudian dideteksi agar sistem dapat melakukan pemulihan dan tetap berjalan normal.**  
3. [Apa kelebihan dan kekurangan pendekatan deteksi deadlock?]  
   **Jawaban:Kelebihannya lebih efisien dan fleksibel, sedangkan kekurangannya deadlock baru ditangani setelah terjadi dan memerlukan proses pemulihan.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
Memahami materi yang begitu membingungkan  
- Bagaimana cara Anda mengatasinya?  
Menggunakan analogi agar mudah dipahami
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
