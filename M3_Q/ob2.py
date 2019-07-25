from bmw import Car
car1= Car("ka01234,5")
car1= Car("ka01234,5")
car1= Car("ka01234,5")
car1.start()
car2.start()
car3.start()
car1.change_gear()
car2.change_gear()
car1.change_gear()

lst= [car1,car2,car3,car4,car5]

for car in lst:
    car.showinfo()
c=len(list(filter(lambda x:x.is_started and x.c_gear == 0)))
print(c)