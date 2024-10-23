def move(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"Move top disk from {from_rod} to {to_rod}")
        return
    move(n - 1, from_rod, aux_rod, to_rod)
    move(1, from_rod, to_rod, aux_rod)
    move(n - 1, aux_rod, to_rod, from_rod)

if __name__ == "__main__":
    n = 3
    move(n,"A","C","B")