# x = [17.25 , 18 , 19 , 19.42 , 19.5 , 20 ]
# x.sort()
# print(x)
# x.sort(reverse=True)
# print(x)


# متغیر = ["a", "b", "e", "c"]
# متغیر.sort()
# print(متغیر)
# متغیر.sort(reverse=True)
# print(متغیر)

# print(ord("a"))
# print(ord("b"))
# print(ord("c"))
# print(ord("e"))


# a = {
#     "benita" : "basket",
#     "ava" : "tennis",
#     "artin" : "football"
# }

# print(a["benita"])
# print(a["ava"])
# print(a["artin"])
# print(list(a.keys()))
# print(list(a.values()))
# print(list(a.items()))
all_students = []
# for i in range(1_000_000):
#     student = {}
#     name = input("enter a name:> ")
#     family = input("enter a family:> ")
#     age = int(input("enter a age:> "))
#     student["esm"] = name
#     student["family"] = family
#     student["sen"] = age
#     all_students.append(student)


# z = {
#     1 : "a",
#     2 : "b"
# }

# z[3] = "c"
# z.update({4 : "d"})
# z.update({5 : "e", 6 : "f"})
# print(z)


# z = {
#     1 : "a",
#     2 : "b"
# }

# z.pop(1)
# del z[2]
# print(z)
# for key, val in z.items():
#     if val == "b":
#         z.pop(key)
#         break
        
# print(z)
# friends = {}

# n1 = input("enter the name: ")
# a1 = int(input("enter the age: "))
# friends[n1] = a1
# n2 = input("enter the name: ")
# a2 = int(input("enter the age: "))
# friends.update({n2:a2})
# print(friends)


# students = {}
# n1 = input("enter student's name: ")
# c1 = int(input("enter student's class number: "))
# students[n1] = c1
# n2 = input("enter student's name: ")
# c2 = int(input("enter student's class number: "))
# students.update({n2 : c2})

# print(students)

students_scores = {
    "benita" : 100,
    "ava" : 100
    }

if students_scores["ava"] > 90:
    print("ava")
if students_scores["benita"] > 90:
    print("benita")