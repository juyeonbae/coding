def solution(a, b):
    m = [31,29,31,30,31,30,31,31,30,31,30,31]
    d = ['FRI','SAT','SUN','MON','TUE','WED','THU']

    n = sum(m[:a-1]) + b
    return d[n % 7 - 1]