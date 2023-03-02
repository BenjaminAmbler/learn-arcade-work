import random
class Dog():
    def __init__(self, p_name="",p_age=0):
        self.age = 0
        self.name = p_name
        self.weight = 0

    def bark(self):
        brk_str = "Woof! "
        print(self.name + " says: " + brk_str)

    def sit(self):
        if random.choice([1,2]) == 2:
            print(self.name,' sits obediently')
        else:
            print(self.name," gets no treats today.")

def main():
    done = False
    dog_list = []
    dog = Dog("Fido", 5)
    dog_list.append(dog)
    dog = Dog("Fifi", 13)
    dog_list.append(dog)
    dog = Dog("Frufru", 21)
    dog_list.append(dog)
    dog = Dog("Max", 2)
    dog_list.append(dog)

    print("Is Fido really dog 0?",dog_list[0].name)
    print("Who is dog 3?", dog_list[3].name)

    while not done:
        curr_dog = random.choice(dog_list)
        brk = input("Do you want " + curr_dog.name + " to bark? ").lower()
        if brk == 'q':
            break
        elif brk == 'y':
            curr_dog.bark()
        st = input("Do you want " + curr_dog.name + " to sit? ").lower()
        if st == 'y':
            curr_dog.sit()


if __name__ == "__main__":
    main()