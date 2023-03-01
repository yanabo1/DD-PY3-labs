def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    :param brackets_row: Входная строка для проверки
    :return: True # TODO реализовать проверку скобочной группы

    stack = []
    brackets_map = {")": "(", "}": "{", "]": "["} #

    for bracket in brackets_row:
    if bracket in brackets_map.values():
    stack.append(bracket)
    elif bracket in brackets_map.keys():
    if not stack:
    return False
    elif stack[-1] == brackets_map[bracket]:
    stack.pop()
    else:
    return False
    return not stack

 if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
