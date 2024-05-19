option = int(input("Введите 1 для ввода из консоли / введите 2 для работы с файлом\n"))
if option == 1:
    n = int(input("Укажите кол-во элементов: "))
    if n != 0:
        array = [i for i in map(int, input("Введите элементы через пробел: ").split())]
else:
    path = input("Укажите путь к файлу: ")
    with open(path, "r") as file:
        array = [int(i) for i in file.read().split()]
        n = array[0]
        array = array[1:]


def merge(p_n, n, p_m, m):
    start = p_n
    end = m
    for i in range(end - start + 1):
        if p_n != n + 1 and p_m != m + 1:
            if array[p_n] >= array[p_m]:
                res_array.append(array[p_m])
                p_m += 1
            else:
                res_array.append(array[p_n])
                p_n += 1
        elif p_n == n + 1 and p_m != m + 1:
            res_array.append(array[p_m])
            p_m += 1
        else:
            res_array.append(array[p_n])
            p_n += 1
    array[start:end + 1] = res_array
    res_array.clear()


def merge_sort(start, end):
    half = start + (end - start) // 2
    if half - start > 0:
        merge_sort(start, half)
    if end - half > 0:
        merge_sort(half + 1, end)
    merge(start, half, half + 1, end)


if n != 0:
    res_array = []
    merge_sort(0, n - 1)
    print(" ".join(map(str, array)))
