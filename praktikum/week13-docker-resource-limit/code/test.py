# test.py
import time

data = []
i = 0

print("Program uji resource dimulai...")

try:
    while True:
        # Komputasi berulang (CPU)
        x = i * i * i

        # Alokasi memori bertahap
        data.append("X" * 10_000)  # ~10 KB
        i += 1

        if i % 1000 == 0:
            print(f"Iterasi: {i}, Perkiraan memori terpakai: {len(data)*10} KB")

        time.sleep(0.01)
except MemoryError:
    print("MemoryError: Memori tidak mencukupi")
