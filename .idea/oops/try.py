a = 5
b =0
# if we have any doubt on our code so we wirte it in the try block beacuse if there is an error so it will not we show and execute but except block is imp;
try:
    print(a/b)
    # Except block are execute when we get error
except:
    print(a+b)
# Finally: Finally block execute every time if we have any error or we don't have any error 
finally:
    print('finally statement')
