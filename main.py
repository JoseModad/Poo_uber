from car import Car
from account import Account

if __name__ == '__main__':
    
    car = Car('KJH897', Account('Marcos Torres', 'PKI347'))   
    print(vars(car))
    print(vars(car.driver))
    
    car2 = Car('MKL372', Account('Antonio Rios', 'MKL372'))    
    print(vars(car2))
    print(vars(car2.driver))
  