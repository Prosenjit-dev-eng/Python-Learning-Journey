class Laptop:#duck
    def build(self):
        print("Laptop builds")
class Desktop:#crow
    def build(self):
        print("Desktop builds")

class Aliens:
    def code(self, machine : Laptop):
        print("Alien builds")
        machine.build()

asus_rog = Laptop()
beast = Desktop()

pro = Aliens()
pro.code(beast)#see machine is a laptop object but still it can call Desktop's build
# bcz it's same same => duck