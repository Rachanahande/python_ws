''' 3.	Write a program to accept 2 different numbers from the user and print all the prime numbers between these 2 numbers.'''
a=int(input("enter starting number"))
b=int(input("enter ending number"))
for i in range(a,b+1):
    is_prime = True
    if i < 2 :
        is_prime =False
    else:
        for j in range(2,i//2+1):
            if i % j == 0:
                is_prime = False
                break
    if is_prime:
       print(i)