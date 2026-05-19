class Human:
    def __init__(self, num_heart):
        self.nose = 1
        self.eyes = 2
        self.heart = num_heart

    def m1(self):
        print("I am a human")


class Male:
    def __init__(self, name):
        self.name = name

    def m2(self):
        print("I am a male")


class Boy(Male, Human):
    def __init__(self, name, num_heart, language):
        Male.__init__(self, name)
        Human.__init__(self, num_heart)
        self.language = language

    def m3(self):
        print("I am a boy")

    def display(self):
        print(f"my name is {self.name} and my language is {self.language}")


b1 = Boy("jack", 1, "python")
#b1.m2()
#b1.m1()
#print(b1.nose)
#print(b1.eyes)
#b1.display()

print(b1.heart)
print(b1.name)
print(b1.language)


