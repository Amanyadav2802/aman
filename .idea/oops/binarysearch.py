pos = -1
def hey(list,n):

    l=0
    u=len(list)-1
    while l<=u:
        mid=(u+l)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
    
list=[2,5,6,7,5,4,5,7,9]
n=int(input('Enter the number that you want to search'))
if hey(list,n):
    print("found at",pos+0)
else:
    print('Not found')