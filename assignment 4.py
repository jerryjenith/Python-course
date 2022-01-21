def commant():
    name=input("enter your name")
    age=int(input("enter your age"))
    address=input("enter your address")
    qualification=input("enter your Qua")
    marks=float(input("enter your marks"))
    print(f"my name is {name} I am  {age} years old I am from {address} i have done {qualification} with {marks} percent")
commant()

def my_assignment():
    thisdict =	{
      "name": "tom",
      "address": "US",
      "year": 2022
    }
    for x in thisdict:
      print(thisdict[x])
my_assignment()

def come(name,address,year):
    print(f"my name is {name} I am from {address} i have done {year} ")
come('tom','US',2022)

def com():
    num = range(1,7)
    final=list(num)
    print(final)
com()

