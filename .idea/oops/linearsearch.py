pos = -1
def hey(list,n):
    i=0
    while i<len(list):
        if list[i]==n:

           if list[i]==n: 
            globals()['pos']=i
            return True
        i=i+1
    return False
list=[2,5,6,7,5,4,5,7,9]
n=int(input('Enter the number that you want to search'))
if hey(list,n):
    print("found at",pos+0)
else:
    print('Not found')