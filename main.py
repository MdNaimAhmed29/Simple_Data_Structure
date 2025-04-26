"""
Data Structure
-list[]
    -mutable
    -ordered
    -most used
    -allow duplicates
    -heterogeneous
    -dynamic size
    -append()
    -insert()
    -extend()
    -remove()
    -pop()
    -clear()
    -sort()
    -reverse()
    -index()
    -count()
    -loop
    -len()
------------------------------------------------------------
tuples()
    -immutable
    -ordered
    -allow duplicates
    -heterogeneous
    -Fixed size
    -index()
    -count()
    -loop
    -len()

-------------------------------------------------------------

Set{}
    -unordered
    -mutable
    -dynamic size
    -not allowed duplicates
    -heterogeneous
    -add()
    -update()
    -remove()
    -pop()
    -clear()
    -union()
    -intersection()
    -difference()
    -issubset()
    -issuperset()

-----------------------------------------------------------

dictonary/object/map-almost used everywhere{}
    -keys()
    -values()
    -finding each value for the respective key
    -items()
    -copy()
    -update()
    -pop()
    -clear()
    -len()
    -update()
    -get()

---------------------------------------------------------

jSON -javascript object notation-Uses
    -common interchange format
    -python, js, dart, java
    -back end to front end(B2C)
    -back end to back end(B2B)
    -rest API development
    -rest API implement
    -payment gateway
    -sms API
 **object to json string conversion->json.dumps()
 **json string to object conversion->json.loads()

"""


#list

fruits = ["apple", "banana", "cherry", "orange"]
fruits.pop()
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.remove("cherry")
fruits.append("Mango")
fruits.insert(0, "cherry")

print(fruits)
print(fruits.pop())
print(fruits.index("cherry"))
print(fruits.count("banana"))
print(len(fruits))

for fruit in fruits:
    print(fruit)

#Tuples
cities = ("Dhaka", "Mirpur", "Savar")
print(cities.index("Dhaka"))
print(cities.count("Dhaka"))
print(len(cities))

for city in cities:
    print(city)

#sets

country = {"bangladesh", "pakistan", "china"}
city = {"manikganj", "rajshahi", "kushtia"}

res = country.union(city)
print(res)

res2 = country.intersection(city)
print(res2)

res3 = country.difference(city)
print(res3)

res4 = country.issubset(city)
print(res4)

res5 = country.issuperset(city)
print(res5)

country.add("America")
print(country)

country.update(["A", "B"])
print(country)

country.pop()
print(country)

#map/dictonary

adlof_hitler = {
    "Name": "Adlof Hitler",
    "Age": 56,
    "Country": "Germany",
    "Occupation": "President",
    "Gender": "Male",
}
print(adlof_hitler)
print(adlof_hitler.keys())
print(adlof_hitler.values())
print(adlof_hitler.items())
print(adlof_hitler.copy())
print(adlof_hitler.pop('Gender'))
print(len(adlof_hitler))
print(adlof_hitler['Name'])
print(adlof_hitler.get('Age'))
adlof_hitler.update(
    {
        "Age": 76,
        "Country": "USA",
    }
)
print(adlof_hitler)


#JSON-javascript object notation

import json

adlof_hitlerJSON = json.dumps(adlof_hitler, indent=4)
print(adlof_hitlerJSON)

ahobject = json.loads(adlof_hitlerJSON)
print(ahobject)

peoples = [
    {"name" : "A", "age" : 24},
    {"name" : "B", "age" : 25},
    {"name" : "C", "age" : 26},
    {"name" : "D", "age" : 27},
    {"name" : "E", "age" : 28},
    {"name" : "F", "age" : 29},
    {"name" : "G", "age" : 30},
]

peoplesJSONArray = json.dumps(peoples, indent=4)
print(peoplesJSONArray)