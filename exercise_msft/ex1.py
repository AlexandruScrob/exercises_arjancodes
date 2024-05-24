def solution(A):
    n = len(A)
    i = n - 1
    result = -1
    maximal = 0
    k = 0
    while i >= 0:
        if A[i] == 1:
            k = k + 1
            if k >= maximal:
                maximal = k
                result = i
        else:
            k = 0
        i = i - 1
    if A[0] == 1 and k + 1 > maximal:
        result = 0
    return result


ex_1 = [0, 1, 1, 1, 0, 1, 1, 1, 0, 1]
ex_2 = [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]

if __name__ == "__main__":
    print(solution(ex_2))
