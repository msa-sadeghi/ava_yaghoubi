# print("1" + "3")

# name = input("enter a name: ")
# course_name = input("enter a course: ")

# # message = name + " " + "welcome to " + course_name + " class"

# print(f"{name} welcome to {course_name} class")

# name = input("enter a name: ")
# for x in name:
#     print(x, end=" ")

# print("a", "v", "a", sep="*", end=" ")  
# print("benita") 

# numbers = "123456789"
# calc the sum of digits in numbers with for loop
# res = 0
# for d in numbers:
#     res += int(d) * 2
# print(res)

# names = ["ramin", "artin", "sara","benita", "ava","roze"]
# for n in names:
#     print("hello", n)
# c = 0
# for n in names:
#     # if n[len(n)-1] == "n":
#     if n[-1] == "n":
#         c += 1
# print(c)
# چند تا از اسم ها دو تا 
# a
# دارند
        
        
   
# names = ["ramin", "artin", "sara","benita", "ava","roze"]

# x = 0  #    تعداد اسم هایی که دوتا آ  دارند

# for n in names:  #    می خواهیم تک تک اسم ها را بررسی کنیم
#     s = 0  #   تعداد آ ها را در هر اسم مشخص می کند
#     for c in n:  #    هر اسم چند کاراکتر دارد 
#         if c == "a": #   آیا کاراکتر   آ   می باشد؟
#             s += 1  #   تعداد   آ   ها را   برای آن اسم یکی اضافه
#     if s == 2:  #   آیا   تعداد    آ   های آن اسم  2  می باشد؟
#         x += 1  #   یکی به تعداد اسم هایی که دوتا  آ دارند اضافه کن
# print(x)
        

# names = ["ramin", "artin", "sara","benita", "ava","roze", "javad"]
# x = 0
# for n in names:
#     if n.count("a") == 2:
#         x += 1
# print(x)
import math      
        
print(5 / 2)
print(5 // 2)
print(5 % 2)
print(5 ** 2)

print(math.sqrt(4))


print(1,2,3,4,5,6,7,8,9, sep="===", end="#########")
print("hello", "friends", "how", "are", "you today?", sep="******")