class Cat:
    name = ""
    age = 0
    fur_color = ""
    breed = ""

    def eat(self):
        print("Cat is eating!")

    def sleep(self):
        print("Cat is sleeping!")


# creating objects
tom = Cat()
snow = Cat()
tom.name = "Tom"
tom.age = 3
tom.fur_color = "grey"
tom.breed = "City cat"

snow.name = "Snowbell"
snow.age = 5
snow.fur_color = "white"
snow.breed = "Persion"

# calling methods
tom.eat()
snow.sleep()
tom.sleep()

# displaying attributes
print(tom.name, tom.age, tom.fur_color, tom.breed)
print(snow.name, tom.age, tom.fur_color,snow.breed)