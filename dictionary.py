# data = {1:"Aman",2:"Age",3:23}
# print(data)
# # if we don't have any value so we can fatch like this
# newdata=data.get(5,"no value")
# print(newdata)


# how to add data and value from the list
# keys = ('aman','karan','jatin')
# values = ('python','java','js')
# data = dict(zip(keys,values))
# # how to add new data in a dictionary
# data['monika']="cs"
# print(data)
# # how to delete data from a dictionary
# del data['aman']
# print(data)

# we can store dictionary under a dictionary and list under the dictionary\

dictionary = {1:'aman',2:'karan','python':['vs','pycharm'],'java':{'jse':'netbeans','jee':'netclips'}}

newdata=dictionary['python'][1]
print(newdata)
data=dictionary['java']['jse']
print(data)