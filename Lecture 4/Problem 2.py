def checkPalindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False

num = int(input())

for k in range(1, num):
    if checkPalindrome(str(k)):
        print(k)
