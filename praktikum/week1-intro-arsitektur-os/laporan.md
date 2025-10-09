
# Laporan Praktikum Minggu [1]
Topik: Laporan Arstiketur OS

---

## Identitas
- **Nama**  : [Andri Dwi Yuliyanto]  
- **NIM**   : [250202976]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Mampu menjelaskan sistem operasi dalam arsitektur komputer 
2. Memahami peran setiap sistem operasi dalam arsitektur komputer 
3. Mengenali komponen utama OS (kernel,system call,device driver dll.)
4. Membuat diagram sederhana tentang arsitektur OS menggunakan Draw.io


---

## Dasar Teori
Dengan mempelajari tentang materi tersebut,kita dapat memahami bahwa di dalam sistem komputer terdapat sistem-sistem yang menjalankan setiap program yang kita perintahkan/gunakan 
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
- Buat akun GitHub dan berikan nama kalian.
- Fork akun GitHub kalian ke GitHub pengajar atau dosen kalian.
- Install VSCode,Ubuntu, dan GitBash
- clone Git dengan mengklik clone
- buat folder-klik kanan lalu pilih Git Bash Here
- Untuk memngatur Git kalian,ketikkan git --global user.name "username GitHub Kalian"- git --global user.name "akun email kalian"
- ketik " git clone "url yang disalin"
- untuk push ke GitHubnya buka terminal dan ketikkan "git add .- git commit -m "pesan kalian"- git push origin main"
- install Ubuntu di Microsoft Store (Windows 10/11)
- Tunggu hingga penginstallan selesai
- Lalu cari WSL lewat CMD
- ketikkan username dan password kalian 
- Setelah itu ketik sesuai yang ditugaskan dosen/pengajar.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
inux cs-890654789635-default 6.6.105+ #1 SMP PREEMPT_DYNAMIC Tue Sep 23 09:51:10 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
lsmod | head
Module                  Size  Used by
ip6table_nat           12288  1
xt_set                 20480  0
ip_set                 53248  1 xt_set
netlink_diag           12288  0
iptable_nat            12288  1
xt_nat                 12288  6
xt_mark                12288  1
veth                   36864  0
nft_limit              16384  1
dmesg | head
[    0.000000] Linux version 6.6.105+ (builder@9fdf8d957a16) (Chromium OS 17.0_pre498229-r33 clang version 17.0.0 (/var/cache/chromeos-cache/distfiles/egit-src/external/github.com/llvm/llvm-project 14f0776550b5a49e1c42f49a00213f7f3fa047bf), LLD 17.0.0) #1 SMP PREEMPT_DYNAMIC Tue Sep 23 09:51:10 UTC 2025
[    0.000000] Command line: BOOT_IMAGE=/syslinux/vmlinuz.A init=/usr/lib/systemd/systemd rootwait ro noresume loglevel=7 console=tty1 console=ttyS0,115200 security=apparmor virtio_net.napi_tx=1 nmi_watchdog=0 csm.disabled=1 loadpin.exclude=kernel-module,firmware modules-load=loadpin_trigger firmware_class.path=/var/lib/nvidia/firmware module.sig_enforce=1 dm_verity.error_behavior=3 dm_verity.max_bios=-1 dm_verity.dev_wait=1 i915.modeset=1 cros_efi root=/dev/dm-0 "dm-mod.create=vroot,,,ro,0 4077568 verity 0 PARTUUID=33380AF5-AE20-B145-804B-0FA44521AF7F PARTUUID=33380AF5-AE20-B145-804B-0FA44521AF7F 4096 4096 509696 509696 sha256 369788617d53fa637bc7245ad62cd9be0900ebff78243ea69cff567792de4f74 9698505fe0b51565e3fe4f68ee69838dc0b0bb6143fd9784fdff1e7fdc76d530"
[    0.000000] BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x0000000000000fff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000001000-0x0000000000054fff] usable
[    0.000000] BIOS-e820: [mem 0x0000000000055000-0x000000000005ffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000060000-0x0000000000097fff] usable
[    0.000000] BIOS-e820: [mem 0x0000000000098000-0x000000000009ffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x00000000bd221fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000bd222000-0x00000000bd223fff] ACPI data
```


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/Screenshot 2025-10-06 174215.png)
![Screenshot hasil](screenshots/Screenshot 2025-10-06 code.png)
---

## Analisis
- Jelaskan makna hasil percobaan.  
1. uname -a
Memberikan informasi sistem kernel yang digunakan 
- Kernel yang digunakan (Linux)
- Versi Linux (6.6.105+)
- cs-890654789635-default = Nama host (komputer/server).
- x86_64 = Arsitektur 64-bit.
2.  lsmod | head
Perintah lsmod | head menampilkan modul-modul yang aktif
- Jaringan (IPv4 & IPv6)
- Firewall (iptables/nftables)
- Virtualisasi jaringan (veth)
- Keamanan & kontrol trafik
3. dmesg | head 
Menampilkan log awal saat dinyalakan 
- Info versi kernel
- Opsi boot
- Alokasi memori dari BIOS
Log ini sangat penting untuk diagnosis awal dan mendeteksi masalah dalam perangkat keras.
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Fungsi Kernel: Kernel adalah inti sistem operasi yang menghubungkan perangkat lunak dan perangkat keras. Fungsinya meliputi mengatur proses, memori, perangkat keras, sistem file, dan menjaga keamanan sistem.
- system call: jembatan yang menghubungkan antara user dan juga kernel untuk meminta akses seperti mengakses file,membuat proses dll.
- Arsitektur OS: Arsitektur sistem operasi adalah struktur internal OS yang mengatur kerja dan interaksi antar komponennya. Jenisnya antara lain monolithic, microkernel, layered, dan modular, masing-masing dengan kelebihan dalam kecepatan, keamanan, atau fleksibilitas. Tujuannya agar OS bekerja efisien, aman, dan mudah dikelola.
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
Linux dan Windows adalah dua sistem operasi dengan perbedaan utama pada sifat, penggunaan, dan arsitektur. Linux bersifat open source, lebih aman, dan banyak digunakan di server serta pengembangan. Sementara Windows bersifat proprietary, lebih ramah pengguna, dan dominan di komputer pribadi dan kantor. Linux menggunakan struktur file berbasis direktori root ("/"), sedangkan Windows menggunakan sistem drive (C:, D:). Dari sisi keamanan, Linux lebih ketat dalam manajemen izin, sementara Windows lebih rentan terhadap malware.

---

## Kesimpulan
Linux memiliki beberapa keuntungan, antara lain bersifat open source dan gratis, sehingga dapat digunakan dan dimodifikasi tanpa biaya. Sistem ini juga dikenal aman, stabil, dan ringan, membuatnya cocok untuk server maupun perangkat dengan spesifikasi rendah. Selain itu, Linux memiliki komunitas pengguna yang besar, sehingga dukungan dan dokumentasi mudah ditemukan.

---

## Quiz
1. [Sebutkan 3 fungsi utama Sistem Operasi]  
   **Jawaban:Memanajemen Proses,Memanajemen Memori,Memanajemen I/O**  
2. [Jelaskan perbedaan antara kernel mode da juga user mode]  
   **Jawaban:Kernel mode adalah mode dengan akses penuh ke sistem, digunakan oleh inti sistem operasi. User mode memiliki akses terbatas dan digunakan oleh aplikasi, untuk menjaga keamanan dan tidak merusak sistem.**  
3. [Sebutkan contoh OS dengan arsitektur monolithic dan mikrokernel]  
   **Jawaban:Monolithic Kernel:Linux, MS-DOS, Unix - Microkernel:Minix, QNX, L4, GNU Hurd**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
**Memahami sistem GitHub yang kompleks untuk seseorang yang awam terhadap ilmu komputer seperti saya.**  
- Bagaimana cara Anda mengatasinya? 
**Mencari tutorial dan mempelajarinya lebih lanjut, walaupun belum 100% memahami.** 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
