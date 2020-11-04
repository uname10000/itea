class Vehicle:
    def __init__(self, weight, number_of_seats):
        self.weight = weight
        self.number_of_seats = number_of_seats
        self.wheels = 4

    def get_weight(self):
        return self.weight

    def get_number_of_seats(self):
        return self.number_of_seats

    def get_number_of_wheels(self):
        return self.wheels

    def drive(self):
        print('Vehicle drive')

    def stop(self):
        print('Vehicle stop')


class FreightCar(Vehicle):
    def drive(self):
        print('Freight Car drive')

    def stop(self):
        print('Freight Car stop')


class Car(Vehicle):
    def drive(self):
        print('Car drive')

    def stop(self):
        print('Car stop')


f_car = FreightCar(20, 2)
car = Car(2, 5)

f_car.drive()
f_car.stop()
print(f'Freight car weight is: {f_car.get_weight()}')
print(f'Freight car number of seats is: {f_car.get_number_of_seats()}')
print(f'Freight car number of seats is: {f_car.get_number_of_wheels()}')

print("-"*40)

car.drive()
car.stop()
print(f'Car weight is: {car.get_weight()}')
print(f'Car number of seats is: {car.get_number_of_seats()}')
print(f'Car number of seats is: {car.get_number_of_wheels()}')
