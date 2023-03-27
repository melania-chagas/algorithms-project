def quick_sort(lista):
    # https://chat.openai.com/chat
    # prompt: "algoritmo de ordenação, em python, que tenha \
    # complexidade diferente de O(n²)""

    if len(lista) <= 1:
        return lista

    pivo = lista[0]
    iguais = [x for x in lista if x == pivo]
    menores = [x for x in lista if x < pivo]
    maiores = [x for x in lista if x > pivo]

    return quick_sort(menores) + iguais + quick_sort(maiores)


def is_anagram(first_string, second_string):
    letters_first_string = []
    letters_second_string = []

    for letter in first_string:
        letters_first_string.append(letter.lower())

    for letter in second_string:
        letters_second_string.append(letter.lower())

    sorted_list_first_string = quick_sort(letters_first_string)
    sorted_list_second_string = quick_sort(letters_second_string)

    if sorted_list_first_string == sorted_list_second_string and \
        first_string != '' and \
            second_string != '':
        return (
            ''.join(sorted_list_first_string),
            ''.join(sorted_list_second_string),
            True
            )
    else:
        return (
            ''.join(sorted_list_first_string),
            ''.join(sorted_list_second_string),
            False
            )


# print(is_anagram('casa', 'saca'))
