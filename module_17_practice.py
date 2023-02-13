# a = list(map(int, input().split()))

s = [9,9,8,7,5,3,6,2,1,4,5,6,8,9,22]
def sliyanie(a, b):
    c = []
    i = j = 0  # указатели на элементы
    # пока указатели не вышли за границы
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    # добавляем хвосты
    while i < len(a):
        c.append(a[i])
        i += 1
    if j < len(b):
        c = c + b[j:]
    return c

def sort(s):  # "разделяй"
    if len(s) == 1:  # если кусок массива равен 1
        return s  # выходим из рекурсии
    seredina = len(s) // 2  # ищем середину
    left = sort(s[:seredina])  # рекурсивно делим левую часть
    rigth = sort(s[seredina:])  # и правую
    return sliyanie(left, rigth)  # выполняем слияние
print(sort(s))

def binary_search(array, element, left, right,):
    global c
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)
element = int(input())-1
array = sort(s)
print(binary_search(array, element, 0, 15))