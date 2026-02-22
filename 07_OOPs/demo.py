class Computer:
    #__init__, it's used to initialise , not the constructor
    # cpu,ram,ssd=> These are called instance variable
    brand = "Telusko"#Class variable
    def __init__(self,cpu,ram,ssd):
        print("Initialised")
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd
    def config(self):
        print("Config: ",self.cpu,self.ram,self.ssd)
    @classmethod
    def info(cls):#we can write any type of variable name instead of cls
        return cls.brand
    @staticmethod
    #when a function is not related to class or instance method , we use static methos
    def gb2byte(gb):
        return gb * (1024**3)
        
comp1 = Computer("i9","24 GB", "2 TB")
comp2 = Computer("i7","16 GB", "1 TB")

comp1.config() 
comp2.config()
print(Computer.info())# printing class variable
print(Computer.gb2byte(16))