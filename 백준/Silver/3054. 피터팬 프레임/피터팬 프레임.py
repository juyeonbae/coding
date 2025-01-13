word = input()
n = len(word)
result = [''] * 5

for i in range(n):
    is_wendy = (i + 1) % 3 == 0
    prev_wendy = (i % 3 == 0) and i > 0

    if i > 0:
        for j in range(5):
            result[j] = result[j][:-1]

    if is_wendy:
        frame = ['..*..',
                 '.*.*.',
                 '*.' + word[i] + '.*',
                 '.*.*.',
                 '..*..']
    else:
        frame = ['..#..',
                 '.#.#.',
                 '#.' + word[i] + '.#',
                 '.#.#.',
                 '..#..']

    if prev_wendy:
        frame[2] = frame[2].replace('#', '*', 1)

    for j in range(5):
        result[j] += frame[j]

for line in result:
    print(line)