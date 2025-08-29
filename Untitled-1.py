# num=input("enter a number")
# print("you entered"+num)
# print("you entered",num)

# number1="2"
# number3=int(number1)
# number2=5
# print(type(number1))
# print(type(number3))
# sum=number3+number2

# print(sum)

# name="himal"
# number=str(2)

# print(name+number)
# print(name,number)

# name="himal basnet"
# # print(name.replace("basnet","analyst"))
# print("H" in name)

# print(5==2)
# print(5>=2)

# num=5
# num+=2
# numb%=2
# print(num)
# print(numb)


# age=22
# if age>=18:
#     print("you are an adult")
# elif age>12 and age<18:
#     print("you are a teen")
# else:
#     print("you are a kid")

# print("thank you")  


# num=range(5)
# print(num)
# print(range(5))


# marks=int(input("Enter your marks"))

# if marks>=90:
#     grade="A"
# elif marks>=80 and marks<90:
#     grade="B"
# elif marks>=70 and marks<80:
#     grade="c"
# else:
#     grade="D"

# print("Your grade is",grade)


# student=["himal","Butwal",95]
# print(student)
# student[2]="kapil"
# print(student)


# marks=[5,8,1,3,9]
# print(marks.append(7))
# print(marks.sort())
# print(marks)


# marks=[3,1,5,2]
# marks.remove(5)
# marks.pop()
# print(marks)


# tup=(1,5,3,2,7,4)
# print(type(tup))
# print(tup.count(3))


# movie1=input("enter movie1 name")
# movie2=input("enter movie2 name")
# movie3=input("enter movie3 name")

# movies=[]
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)


# list=[1,2,1]

# copyList=list.copy()
# copyList.reverse()

# if list==copyList:
#     print("Palindrome")
# else:
#     print("NOT Palindrome")


# dict={
#     "name":"himal",
#     "cgpa":3.25,
#     "marks":[97,95,98]
# }

# print(type(dict))
# print(dict["name"])
# print(dict["cgpa"],dict["marks"])


# student={
#     "name":"Himal",
#     "score":{
#         "math":98,
#         "chem":95,
#         "phy":97
#     }
# }

# print(type(student))
# print(student["score"]["math"])


# student={
#     "name":"Himal",
#     "score":{
#         "math":98,
#         "chem":95,
#         "phy":97
#     }
# }

# print(list(student.keys()))
# print(student.items())
# print(student.get("score2"))
# print(student["score2"])
# student.update({"city":"butwal"})
# print(student)

# dict={}
# print(type(dict))


# set={1}
# set=set(1,2)
# print(type(set))


# collectiom=set()

# collectiom.add(1)
# collectiom.add(1)
# collectiom.add(5)
# collectiom.add((2,9,6))
# collectiom.add("himal")

# collectiom.pop()
# # collectiom.clear()
# # print(type(collectiom))

# print(collectiom)
# print(len(collectiom))


# subject=set()
# subject.add("python")
# subject.add("java")
# subject.add("c++")
# subject.add("python")
# subject.add("js")
# subject.add("java")
# subject.add("python")
# subject.add("python")
# subject.add("java")
# subject.add("c++")
# subject.add("c")

# print(type(subject))
# print(subject)
# print("total class is",len(subject))


values={
    ("int",9),
    ("float",9.0),
}

print(list(values))