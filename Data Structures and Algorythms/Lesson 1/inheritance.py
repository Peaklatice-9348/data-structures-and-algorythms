class Car:
    def __init__(self,brand,model,fuel,color):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self,newcolor):
        self.color = newcolor
    
    def show_car(self):
        print('Car-{}-{}, Fuel Type-{}, Color-{}'.format(self.brand,self.model,self.fuel,self.color))
    
class SUV(Car):
    def __init__(self,brand,model,fuel,color,transmission,turbo):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        self.color = color
        Car.__init__(self,brand,model,fuel,color)
        self.transmission = transmission
        self.turbo = turbo
    
    def show_car(self):
        print('Car-{}-{}, Fuel Type-{}, Color-{}, Tranmission-{}, Turbo(True/False)-{}'.format(self.brand,self.model,self.fuel,self.color,self.transmission,self.turbo))

audiQ3 = SUV('Audi','Q3','Deisel','White','Automatic',True)
print(audiQ3.get_color())
audiQ3.set_color('red')
print(audiQ3.show_car())

toyotaG7 = SUV('Toyota','G7','Electric','Grey','Automatic',True)
print(toyotaG7.get_color())
toyotaG7.set_color('Black')
print(toyotaG7.show_car())

        
