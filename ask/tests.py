from django.test import TestCase

# Create your tests here.
dict = {}

list = [12,5,6,7,8,5,3]


for i in list:
    dict[len(dict)] = i

for i in dict.keys():
    print(dict[i])


print(dict)