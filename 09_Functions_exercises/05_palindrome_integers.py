def check__if_palindrome(el):
    if el == el[::-1]:
        return True
    return False


nums_as_string = input().split(", ")

for num_as_str in nums_as_string:
    is_palindrome = check__if_palindrome(num_as_str)
    if is_palindrome:
        print(True)
    else:
        print(False)

# def check__if_palindrome(el):
#     if el == el[::-1]:
#         return True
#     return False
#
#
# nums_as_string = input().split(", ")
#
# for num_as_str in nums_as_string:
#     print(check__if_palindrome(num_as_str))
