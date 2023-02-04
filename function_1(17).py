def count_rab_che(head, leg):
    sum = 0
    for i in range(100):
        for j in range(100):
            if i + j == head and 2*i + 4*j == leg:
                ind1 = i
                ind2 = j
    return ind1, ind2

print(count_rab_che(35, 94))