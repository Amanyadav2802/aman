f=open("jaishreeram.jpg",'rb')
f1=open('mypic.jpg','wb')
for i in f:
    f1.write(i)