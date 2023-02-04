# You are given list of numbers separated by spaces.
# Write a function filter_prime which will take list of
# numbers as an agrument and returns only prime numbers from the list.

def filter_prime(arr):
    primes = []
    for i in arr:
        if i < 2:
            continue
        else:
            flag = True
            for j in range(2, i // 2 + 1):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                primes.append(i)
    return primes


if __name__ == "__main__":
    print(filter_prime([1, 8, 4, 5, 7, 9, 5]))


# def filter_prime(x):
#     c = ""
#     ok = True
#     if x == 1:
#         ok = False
#     else:
#         for i in range(2, x):
#             if x % i == 0:
#                 ok = False
#                 break
#             else:
#                 ok = True
#     if ok == True:
#         c += str(x)
#     else:
#         return ""
#     print(c)
#
# s = input()
# n = s.split()
# for p in n:
#     filter_prime(int(p))