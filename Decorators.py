# def div(a,b):
#     print(a/b)

# def s_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner
# div = s_div(div)
# div(6,24),

from modules import *
a = 41
b= 5
c = sub(a,b)
print(c)