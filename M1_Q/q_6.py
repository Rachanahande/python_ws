
'''6. Write a program to accept a number from the user, then display reverse of given number'''
def reverse_num(num):
    rev = 0
    while num != 0:
        rev= rev * 10 + num %10
        num//= 10
    return rev

num = int(input("enter a number"))
rev = reverse_num(num)
print(f" reverse of {num} is {rev}")