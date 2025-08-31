def sum_core(m, l, c):
    soma = 0

    for i in range(1, l):
        for j in range(1, c):
            soma += m[i] [j]

    return soma

matriz = [
    [68, 86, 50, 42, 84, 98, 75],
    [15, 83, 10, 16, 14, 99, 58],
    [30, 68, 78, 44, 70, 25, 31],
    [69, 53, 17, 87, 55, 83, 15],
    [20, 70, 78, 61, 65, 16, 26]
]

print(sum_core(matriz, 5, 7))

