# s1 = float(input("enter first score: "))
# s2 = float(input("enter first score: "))
# s3 = float(input("enter first score: "))
# s4 = float(input("enter first score: "))
# s5 = float(input("enter first score: "))

# ave = (s1 + s2 + s3 + s4+ s5) / 5
# print("your average is", ave)
# if ave >= 90:
#     print("A")
# elif ave >= 80 and ave < 90:
#     print("B")
# else:
#     print("C")


# x = int(input("enter a number: "))
# y = int(input("enter a number: "))
# z = int(input("enter a number: "))

# greatest = x
# if y > greatest:
#     greatest = y
# if z > greatest:
#     greatest = z
    
# print("biggest is", greatest)

std1 = input("enter student's name: ")
sc1 = input("enter student's score: ")
std2 = input("enter student's name: ")
sc2 = input("enter student's score: ")
std3 = input("enter student's name: ")
sc3 = input("enter student's score: ")

greatest_score = sc1
best_student = std1
if sc2 > greatest_score:
    greatest_score = sc2
    best_student = std2
if sc3 > greatest_score:
    greatest_score = sc3
    best_student = std3
    
print("best student is", best_student, "best score is", greatest_score)