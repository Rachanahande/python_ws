def armstrong_num(num):
    num_1 = num
    res=0
    while num!=0:
        r = num%10
        res =res +r**3
        num=num//10
    return num_1==res
input_num = int(input("enter the number "))
if(armstrong_num(input_num)):
    print(f"given no {input_num} is armstrong number")
else:
    print(f"given no {input_num} is not an armstrong no")