def solution(n):
    bin_n = bin(n)
    cnt_one = bin_n.count('1')

    num = n + 1
    while True:
        bin_num = bin(num)
        if cnt_one == bin_num.count('1'):
            break
        num += 1

    return num