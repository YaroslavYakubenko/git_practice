# i = 1
# n = int(input('Enter number: '))
# while i <= n:
#     print('Hello')
#     i = i + 1

# i = 'kodak'
# # print(i)
# # print(type(i))
# n = list(i)
# # print(n)
# # print(type(n))
# n.reverse()
# # n = str(n)
# print(type(n))
# print(n)
# print((''.join(n)))

# def is_palindrome(s):
#     i = list(s)
#     i.reverse()
#     print(''.join(i))
#     print(i == s)
# print(is_palindrome('ni'))

# a = 5
# # print(type(a))
# if isinstance(a, int) == True != False:
#     print('ok')
# else:
#     print('not')
# # print(isinstance(a, str))

# a = [3, 4, 5]
# print(type(a))
# print(a[0])
# print((a[0])**2+(a[1])**2==(a[2])**2)

# a = [5, 2, -3]
# # i = []
# for i in a:
#     i = []
#     i = a * -1
#     print(i)

# a = range(1, 6, 3)
# print(float(573/3))
# print(788-216+1)

# family_1 = input('Write names: ')
# family_2 = input('Write names: ')
# if family_1 > family_2:
#     print(family_1)
# elif family_1 == family_2:
#     print('Equal')
# elif family_1 < family_2:
#     print(family_2)

# d = {'num1': 35, 'num2': 15, 'num3': 50}
# print(sum(d.values()))


# set1 = [1, 5, 4, 3, 1, 5, 7, 3]
# print(set1)
# print(type(set1))
# print(set(set1))

def person(**kwargs):
    return kwargs
print(person(name= 'John', last_name= 'Smith', age= 35, position= 'web developer'))


def person(**kwargs):
    for key, value in kwargs.items():
        return "{0}: {1}".format(key,value)


print(person(name='John', last_name='Smith', age=35, position='web developer'))

# from functools import *
# my_list = [20, -3, 15, 2, -1, -21]
# my_list = reduce(lambda x, y: x*y, my_list)
# print(my_list)

# from calc import *
# print(plus(5, 4))
# print(minus(10, 5))
# print(dell(9, 3))
# print(double(5, 4))