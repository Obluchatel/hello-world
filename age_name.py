def ask_for_name():
    name = raw_input("What is your name: ")
    return name

def ask_for_age():
    age = raw_input("What is your age: ")
    return age

def age_name (name, age):
    print ("Hello " + (name) +  "! " + "Your age is " + (age).__str__() + "!")

age_name(ask_for_name(), ask_for_age())
