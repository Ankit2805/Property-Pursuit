students = ('stu1','stu2','stu3','stu1')
a = list(students)
a[1] = "stu4"
students = tuple(a)
print(students)
print(type(students))
print(len(students))