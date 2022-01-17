def diamond(size, design):
    import warnings
    if size % 2 == 0:
        warnings.warn('Enter Odd Number')
    mid = int(size / 2)
    for i in range(size):
        if (i <= mid):
            for j in range(mid - i):
                print(' ', end='')
            for k in range(2 * (i + 1) - 1):
                print(design, end='')
            print()
        else:
            for j in range(i - mid):
                print(' ', end='')
            for k in range(2 * (size - i) - 1):
                print(design, end='')
            print()


def Rtriangle(size, design):
    for i in range(5):
        for j in range(i + 1):
            print(design, end='')
        print()


def Ltriangle(size, design):
    for i in range(size):
        for j in range(size - i - 1):  # j space
            print(' ', end='')
        for k in range(i + 1):
            print(design, end='')
        print()


def triangle(size, design):
    x = ' '
    design = design + x
    k = size - 1
    for i in range(0, size):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print(design, end="")
        print("\r")
