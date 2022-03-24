# from User import *
#
#
# class Restaurant():
#
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(self.restaurant_name+'\n'+self.cuisine_type)
#
#     def open_restaurant(self):
#         print("In operation")
#
#     def set_number_served(self,number):
#         self.number_served = number
#
#     def increment_number_served(self,numbers):
#         self.number_served += numbers
#
# my_restaurant = Restaurant("haidlai","huoguo")
# print(my_restaurant.number_served)
# my_restaurant.set_number_served(980)
# print(my_restaurant.number_served)
# my_restaurant.increment_number_served(200)
# print(my_restaurant.number_served)
# my_restaurant.increment_number_served(200)
# print(my_restaurant.number_served)
# my_restaurant.increment_number_served(200)
# print(my_restaurant.number_served)


# def city_country(city_s,country_s):
#     citycountry = city_s + "," + country_s
#     return citycountry.title()
#
# def make_pizza(*toppings):
#     for topping in toppings:
#         print(topping)
#
#
# make_pizza('dawdaw','dawdczd','aczc','wdjo12')
# BJ = True
# while BJ:
#     city_s = input("city: ")
#     if city_s == 'q':
#         break
#     country_s = input("country: ")
#     if country_s == 'q':
#         break
    # make_pizza(city_s,country_s)
    # print('"'+city_country(city_s,country_s)+'"')

# class A:
#     def __init__(self):
#         self.n = 2
#
#     def add(self, m):
#         print('self is {0} @A.add'.format(self))
#         self.n += m


# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.n = 3
#
#     def add(self, m):
#         print('self is {0} @B.add'.format(self))
#         super().add(m)
#         self.n += 3
#
# class C(A):
#     def __init__(self):
#         super().__init__()
#         self.n = 4
#
#     def add(self, m):
#         print('self is {0} @C.add'.format(self))
#         super().add(m)
#         self.n += 4
#
#
# class D(B, C):
#     def __init__(self):
#         super().__init__()
#         self.n = 5
#
#     def add(self, m):
#         print('self is {0} @D.add'.format(self))
#         super().add(m)
#         self.n += 5
#
#
# d = D()
# d.add(2)
# print(d.n)
# var = D.__mro__
# print(var)

# with open('E:\Python-project\python_workstation\snmp\command.txt','r',encoding='utf-8') as comm:
#     lines = comm.read()
#     word = lines.split()
#     num_word = len(word)
#     print(num_word)

import json
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def greet_user():
# 问候用户， 并指出其名字
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
    greet_user()