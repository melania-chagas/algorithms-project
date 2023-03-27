def is_palindrome_recursive(word, low_index, high_index):
    if not word or word[low_index] != word[high_index]:
        return False
    elif (len(word) == 1) or high_index <= low_index:
        return True
    else:
        low_index += 1
        high_index -= 1

    return is_palindrome_recursive(word, low_index, high_index)
