#9-1
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name =restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print('Название ресторана: '+self.restaurant_name)
        print('Тип кухни '+self.restaurant_name+': ' + self.cuisine_type)
    def open_resturant(self):
        print(self.restaurant_name + ' открыт')
    def set_number_served(self,number_served):
        self.number_served = number_served
    def increment_number_served(self,number):
        self.number_served += number
my_restaurant = Restaurant('Кашка монашки','православная')
my_restaurant.describe_restaurant()
my_restaurant.open_resturant()
#9-2
names_restaurants = {'Вкусная курица':'традиционная',
                     'Горький ниньдзя':'восточная',
                     'Перчик':'острая'}

for rest,cuis in names_restaurants.items():
    r =  Restaurant(rest,cuis)
    #r.describe_restaurant()
#9-3
class User():
    def __init__(self,first_name,last_name,years, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.years = years
        self.profession = profession
        self.login_attempts = 0
    def describe_user(self):
        print('Пользователь: %s %s \nВозраст: %s \nПроффесия: %s'
              %(self.first_name.title(),self.last_name.title(),self.years,self.profession))
    def greet_user(self):
        print('Добро пожаловать ' + self.first_name.title() + ' ' + self.last_name.title())
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

Dimon = User('дмитрий','дроздов','26','инженер')
Grisha =User('григорий','иванов','42','водитель')
Tolik = User('анатолий','лукьянов','14','интернет эксперт')

Dimon.greet_user()
Dimon.describe_user()
Grisha.greet_user()
Grisha.describe_user()
Tolik.greet_user()
Tolik.describe_user()

#9-4
restaurant = Restaurant('курочка','восточная')
print('Количество поситителей: ' + str(restaurant.number_served))
restaurant.number_served = 12
print('Количество поситителей: ' + str(restaurant.number_served))
restaurant.set_number_served(20)
print('Количество поситителей: ' + str(restaurant.number_served))
restaurant.increment_number_served(20)
print('Количество поситителей: ' + str(restaurant.number_served))

#9-5
Dimon = User('дмитрий','дроздов','26','инженер')
Dimon.increment_login_attempts()
Dimon.increment_login_attempts()
Dimon.increment_login_attempts()
Dimon.increment_login_attempts()
print(Dimon.login_attempts)
Dimon.reset_login_attempts()
print(Dimon.login_attempts)

#9-6
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['Шоколадное','Клубничное']
    def print_flavors(self):
        for flavor in self.flavors:
            print(flavor)
ice_stand = IceCreamStand('Морж','Мороженное')
ice_stand.print_flavors()