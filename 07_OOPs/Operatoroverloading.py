class Account:
    def __init__(self,name, balance):
        self.name = name
        self.balance = balance
    def __str__(self):
        #Though __str__ ia method of Object class
        return f'{self.name} : {self.balance}'
    
user1 = Account('Pro', 1000)
user2 = Account('Say', 500)
print(user1.__str__())
