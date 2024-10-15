# x = input("enter three numbers: ")
# x = x.split(" ")
# res = int(x[0]) + int(x[1]) + int(x[2])
# print(res)


# res = 0
# for i in x:
#     res += int(i)
# print(res)

# a = ["ali", "sara", "abtin"]

# for i in a:
#     for j in i:
#         print(j, end=" ")
#     print()
    
# print("hello")

# def my_function(name, family):
#     # return "welcome" + " " + name + " " + family
#     return f"welcome {name} {family}"

# print(my_function("ava", "yaghoubi"))
# print(my_function("nikan", "ariaei"))
# print(my_function(family="rezaeifar", name="benita"))


# def is_prime(number):
#     res = True
#     for x in range(2, number):
#         if number % x == 0:
#             res = False
#             break
#     return res
# for i in range(2, 100):
#     if is_prime(i):
#         print(i)
# import random
# nums = []
# for i in range(10):
#     x = random.randint(1,1000)
#     nums.append(x)  
# print(nums)
# print(min(nums))
# print(max(nums))

# nums = [random.randint(1,1000) for i in range(10)]
# print(nums)
# print(min(nums))
# print(max(nums))


students = ["benita","ava", "radman", "nikan", "amirmohammad", "sara"]

def my_function(names):
    count = 0
    for n in names:
        if len(n) > 5:
            count += 1
            
    return count

print(my_function(students))

def func(names):
    count = 0
    for n in names:
        if "e" in n:
            count += 1
            
    return count
print(func(students))