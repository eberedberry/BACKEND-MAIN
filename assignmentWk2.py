import math

### NO 1

num1 = int(input("Please input First number :"))
num2 = int(input("Please input Second number :"))
num3 = int(input("Please input Third number :"))
sum1 = num1 + num2 + num3
ave = float(sum1) /3
print("The average is {}".format(ave))



##### NO 2.
sentence = input("Please input a Sentence :")
sentence = sentence.split(maxsplit=1)
rest_sentence = (sentence[1])
first_word = sentence[0].upper()
new_sentence = "{} {}".format(first_word, rest_sentence)
print(new_sentence)

### OR NO 2
user = input("enter your sentences: ")
a = user.split()
a[0] = a[0].upper()
print(" ".join(a)) #USE SPACE TO JOIN THEM TOGETHER 



### NO 3
txt = "I am learning python"
x = txt.replace("I", "you")
print(x)



###NO 4
text = "I hope you had fun today in class"
result = text.count("a")
print(result)



### NO 5
def check_fermat(a, b, c, n):
    calc = math.pow(a,n) + math.pow(b,n) 
    result = math.pow(c,n)
    if (calc == result) and (n > 2):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work")

check_fermat(3,4,5,1)
check_fermat(3,4,5,2)
check_fermat(3,4,5,3)




#### NO 6
def get_data():
    a = int(input("please input a :"))
    b = int(input("please input b :"))
    c = int(input("please input c :"))
    n = int(input("please input n :"))

# def check_fermat(a, b, c, n):
#     calc = math.pow(a,n) + math.pow(b,n) 
#     result = math.pow(c,n)
#     if (calc == result) and (n > 2):
#         print("Holy smokes, Fermat was wrong!")
#     else:
#         print("No, that doesn’t work")

    check_fermat(a,b,c,n)

get_data()




