def sort(s):  # ПРИНИМАЕМ список
    if len(s) == 1:  # если массив равен 1
        return s  # выходим из рекурсии возвращаем массив
    seredina = len(s) // 2  # ищем середину массива
    left = sort(s[:seredina])  # рекурсивно делим левую часть
    rigth = sort(s[seredina:])  # и правую
    return sliyanie(left, rigth)  # выполняем слияние


def sliyanie(a, b):  # принимаем по 2 элемента
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


def binary_search(array, element, left, right):
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


try:
    a = list(map(float, input('Введите числа через пробел: ').split())) #Вводим последовательность

    element = float(input('Введите любое число: '))  #Вводим число

    if a and element:   # если введенные данные присутствуют
        print('Вы ввели список', a)
        array = sort(a)
        print('Отсортированный список:', *array)
        if element <= array[0] or element > array[-1]:  # Условие что введенное число меньше или равно минимальному или больше максимального
            print('Нарушены условия поиска. Введенное число меньше или равно минимальному или больше максимального')
        else:
            array_el = sliyanie(array, [element])  # добовляем введенное число в отсортированную последовательность
            ellement_in_array = binary_search(array_el, element, 0,
                                              len(array) - 1)  # узнаем номер позиции введенного элемента в последовательности
            print('Номер позиции элемента, который меньше введенного пользователем числа:', ellement_in_array - 1,
                  '. Следующее за ним число:', array_el[ellement_in_array + 1])
    else:
        print('Повторите ввод чисел')
except ValueError as e:  # ловим ошибку при введении посторонних символов
    print('Повторите ввод чисел через пробел!')
