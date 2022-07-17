##### DICTIONARY



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

# a = 10
# count = 0

# while a > 0:
#     print(a)
#     a-=1
#     count += 1
#     if count == 3:
#         break


# first_name = "Chidiebere"
# # print(len(first_name))
# # print(first_name[20])

# count = 0
# while count < len(first_name):
#     print(first_name[count])
#     count += 1

# prefixes = 'JKLMNOPQ'

# count = 0
# suffix = 'ack'
# for i in prefixes:
#     if prefixes[count] == "Q" or prefixes[count] == "O":
#         print(f"{prefixes[count]}u{suffix}")
#     else:
#         print(prefixes[count] + suffix)
#     count +=1

text = "learning backend with django in Univelcity has been eye opening \
so i am really grateful for the opportunity but it seems like its going \
to ba a long road, i hope when i am donr, i can related well to all things\
and be a better person"
# print(text)
# print("\n")

long_text = """This planet has - or rather had - a problem, which was 
this: most of the people living on it were unhappy for pretty much
of the time. Many solutions were suggested for this problem, but
most of these were largely concerned with the movements of small
green pieces of paper, which is odd because on the whole it wasn't
the small green pieces of paper that were unhappy"""
# print(long_text)

sample_text = "Another example"
# print(len(sample_text))
# print("\n")
# print(sample_text[0:-8])
# sample_text[3] = 5  #you cannot reassign  a cahracter in astring to abother thing cos string are immutable 
# print(sample_text)
# word = "bazinga"
# print(word[2:])
# word2 = word.upper()
# print(word2)
# word3 = word2.lower()
# print(word3)

pray = "        prayer is the key        "
pray1 = "this has trailing right space          "
pray2 = "        prayer is the key. this has trailinf left space"
print(pray.strip())
print(pray1.rstrip())
print(pray2.lstrip())








