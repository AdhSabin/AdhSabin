def check_palindrome(value):
    rev = value[::-1]
    if rev==value:
        return True
    else:
        return False
print(check_palindrome('data'))            