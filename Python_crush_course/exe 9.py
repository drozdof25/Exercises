class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name =restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print('Название ресторана: '+self.restaurant_name)
        print('Тип кухни '+self.restaurant_name+': ' + self.cuisine_type)
    def open_resturant(self):
        print(self.restaurant_name + ' открыт')

my_restaurant = Restaurant('Кашка монашки','православная')
my_restaurant.describe_restaurant()
my_restaurant.open_resturant()
names_restaurants = {'Вкусная курица':'традиционная',
                     'Горький ниньдзя':'восточная',
                     'Перчик':'острая'}

for rest,cuis in names_restaurants.items():
    r =  Restaurant(rest,cuis)
    r.describe_restaurant()

class User():
    def __init__(self,first_name,last_name,years, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.years = years
        self.profession = profession
    def describe_user(self):
        print('Пользователь: %s %s \nВозраст: %s \nПроффесия: %s'
              %(self.first_name.title(),self.last_name.title(),self.years,self.profession))
    def greet_user(self):
        print('Добро пожаловать ' + self.first_name.title() + ' ' + self.last_name.title())

Dimon = User('дмитрий','дроздов','26','инженер')
Grisha =User('григорий','иванов','42','водитель')
Tolik = User('анатолий','лукьянов','14','интернет эксперт')

Dimon.greet_user()
Dimon.describe_user()
Grisha.greet_user()
Grisha.describe_user()
Tolik.greet_user()
Tolik.describe_user()