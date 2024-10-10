class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram = ram

    def config(self):
        print("Hello this is the config",self.cpu,self.ram)
com1 = Computer('i3',64)
com2 = Computer('Riyzen 3',16
)
com1.config()
com2.config()