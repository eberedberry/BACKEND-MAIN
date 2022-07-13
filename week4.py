##### DICTIONARY
from numpy import sort


data = {
    "name" : "desmond",
    "course": "Backend",
    "scores" : [10,7,5,9],
    "address" : {"str_num":2,
                "str_name": "Montegomery rd",
                "city" : "Yaba"
                }
}

subject = {("girl", "young"): "bestfriend",

         } ##USING A TUUPLE AS KEY

sister = "meme" #change the variABLE NAME WITH A FUNCTION



# print(data["name"])
# data["name"] = "Chidi"  #changing the value of the name
# print(data["name"])
# print(data["address"]["city"])
# print(max(data["scores"]))
# print(sum(data["scores"])) 
# print(sum(data["scores"])/len(data["scores"]))

# print(subject[("girl", "young")])
# print(data["boy"]) #### this key gives key error cos the key (boy) doesn't exist

### GET METHOD
# print(data.get("boy"))   ###key doesn't exist
# print(data.get("name"))
# print(data.get("boy", "Key doesn't exist"))
# print(data.get("name", "Key doesn't exist"))

# print(data.keys())
# print(data.values())
# print(data.items())
# print(data.pop("name"))
# print(data.pop())  ###if you dont put a key it gives error

# print(data.keys())
# data["first_name"] = data.pop("name") #when you pop data it gives the name which u assign to a new key
# print(data)


###GIVEN THIS DICTIONARY WRITE A PROGRAM TO SORT IS DICTIONARY USING THE VALUES IN DESCENDING
data2 = {"5": 8,
        "3": 10,
        "4":2,
        "9" : 3,
        "2": 7,
        "0" : 5
        }

# new_data = sorted(data2.values())
# print(new_data)


# sorted_data = sorted(data2.items(), key = lambda x: x[1], reverse = True )  ##how is key related to sorted
# print(sorted_data)
# print(dict(sorted_data))



# sorted_data = sorted(data2.items(), key = lambda x: x[0],reverse = True )
# print(sorted_data)

# students = ['Smith', 'John', 'chichi', 'Grace']
# marks = [89, 53, 92, 86, 90, 89]

# students_list = list(zip(students, marks))
# print(students_list)

# students_dict = dict(zip(students, marks))
# print(students_dict)

# students_tuple = tuple(zip(students, marks))
# print(students_tuple)

sample_data = {"V":"S001",
            "VI":"S002",
            "VII":"S001",
            "VIII":"S005",
            "VIV":"S005",
            "VV":"S009",
            "VVI":"S007"
            }

# print(set(sample_data.values()))  ##to get unique values

# while True:
#     data = int(input("> "))
#     print(data)
#     if data == 5:
#         break

a = 10
count = 0

while a > 0:
    print(a)
    a-=1
    count += 1
    if count == 3:
        break









