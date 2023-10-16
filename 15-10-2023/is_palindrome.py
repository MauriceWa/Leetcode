class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

def isPalindrome2(x):
    if x < 0:
        return False

    list_numbers = []
    variable_number = x
    while variable_number > 0:
        divide = variable_number % 10
        list_numbers.append(divide)
        variable_number //= 10

    left_list = 0
    right_list = len(list_numbers) - 1
    while left_list < right_list:
        if list_numbers[left_list] != list_numbers[right_list]:
            return False
        left_list += 1
        right_list -= 1
    return True




print(isPalindrome2(12))

def isPalindrome3(x):
    # Als x negatief is, is het geen palindroom
    if x < 0:
        return False

    list_numbers = []
    variable_number = x

    while variable_number > 0:
        divide = variable_number % 10
        list_numbers.append(divide)
        variable_number //= 10

    left_list = 0
    right_list = len(list_numbers) - 1

    while left_list < right_list:
        if list_numbers[left_list] != list_numbers[right_list]:
            return False

    return True


