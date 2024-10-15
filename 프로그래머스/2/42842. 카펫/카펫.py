def solution(brown, yellow):
    total = brown + yellow
    for i in range(3, int(total**0.5)+1):
        if total % i == 0:
            if ((total//i) - 2) * (i-2) == yellow:
                return [max(total//i,i), min(total//i,i)]