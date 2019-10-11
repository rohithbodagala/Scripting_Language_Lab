def AgeConvert(a):
    a= a.split("-")
    age = 2019 - int(num[2])
    if int(num[1])>10:
        age = age - 1
    print(age)
print("Enter the date of birth")
a=input();
AgeConvert(a)
