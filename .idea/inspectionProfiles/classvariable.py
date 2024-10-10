class car:
    wheel=5
    def __init__(self):
        self.mil=12
        self.name="BMW"
c1=car()   
c2=car()
# car.wheel=16
c1.mil=7
print(c1.name,c1.mil,c1.wheel)

print(c2.name,c2.mil,c1.wheel)