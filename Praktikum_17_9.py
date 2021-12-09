def binary_search(num, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if num[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < num[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(num, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(num, element, middle + 1, right)


num = list(map(int, input("Введите целые числа через пробел:").split()))
print(sorted(num))
element = int(input("Введите любое число из полученного списка : "))
element_index = binary_search(num, element, 0, len(num))
#print(element_index)
