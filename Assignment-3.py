#Write a program to find whether the string is palindrome or not.

def isPalindrome(s):
    return s == s[::-1]
  
  
# Driver code
s = input("Enter String:")
ans = isPalindrome(s)
  
if ans:
    print("Yes")
else:
    print("No")
