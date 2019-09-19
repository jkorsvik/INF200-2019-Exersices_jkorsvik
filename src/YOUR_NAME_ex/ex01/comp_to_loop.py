def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n=10):
    squares = []
    for k in range(n):
        if k % 3 == 1:
            squares.append(k**2)

if __name__ == '__main__':
    if squares_by_loop(10) != squares_by_comp(10):
        print('ERROR!')
    else:
        print('No Error')
