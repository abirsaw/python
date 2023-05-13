from abc import ABC,abstractmethod
class car():
    def show(self):
        print("Every car has 4 wheel")
    @abstractmethod
    def speed(self):
        pass
class maruti(car):
    def speed(self):
        print("speed is 100 km/h")
class suzuki(car):
    def speed(sef):
        print("speed is 70 km/h")
        
obj=maruti()
obj.show()
obj.speed()

obj=suzuki()
obj.show()
obj.speed()