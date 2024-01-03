wheels_count = int(input("Введіть кількість коліс "))
sits = int(input("Введіть кількість місць "))
guns_count = int(input("Введіть кількість зброї "))

class Banderomobil:
    cars_count=0
    def __init__(self, wheels_count_param, sits_param, guns_count_param):
       Banderomobil.cars_count+=1
       self.wheels_count=wheels_count_param
       self.sits=sits_param
       self.guns_count=guns_count_param
    def print_info(self):
       w1=self.wheels_count
       s1=self.sits
       g1=self.guns_count
       print("Бандеромобіль на {k1} колесах, призначений для {k2} людей і {k3} стволів".format(k1=w1, k2=s1, k3=g1))

car1 = Banderomobil(wheels_count, sits, guns_count )
car1.print_info()
print(car1.cars_count)

car2 = Banderomobil(wheels_count+1, sits+1, guns_count+1 )
car2.print_info()
print(car2.cars_count)

print('hello')
        

