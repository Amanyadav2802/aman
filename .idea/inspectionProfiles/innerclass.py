class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.rollno)
        # its inner class and we defind its variabble  in outer class
    class laptop:
        def __init__(self):
            self.brand='Lenovo'
            self.ram=16
            self.cpu='i7'
           
        
s1=student("Aman",3)
s2=student("Karan",2)

s1.show()
s2.show()  
print(s1.lap.cpu)
# second way you can create object of inner class outside the outer class proviede you usee outer class name to call it.
lap1=student.laptop()
print(lap1.ram)