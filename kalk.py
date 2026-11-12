def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    if b == 0:
        raise ValueError("tidak dapat membagi dengan nol")
    return a / b
