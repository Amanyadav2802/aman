class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        m3=Student(m1,m2)
        return m3
s1=Student(32,12)
s2=Student(54,32)
s3=s1+s2
print(s3.m1,s3.m2)
    