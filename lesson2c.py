# python dictionary 
person={
    "firstname" : "Martha",
    "lastname" : "Kwamboka",
    "age" : 18,
    "colors":["purple" , "yellow"],
    "salary": 5000000
}
# show output
print(person)
# print age
print(person["age"])
# print salary
print(person["salary"])

# add new key value
person["passport"] ="275244ff"
# show output
print(person)
# change age to 56
person["age"]=56
# show output
print(person)
# delete lastname
del person["lastname"]
# show output
print(person)