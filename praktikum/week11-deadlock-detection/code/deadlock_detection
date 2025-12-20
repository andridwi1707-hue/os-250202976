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
