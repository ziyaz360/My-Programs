#step 1
n=int(input("Enter no of students"))
students=[]
for _ in range(n):
    name=input("Enter your name:")
    grade=float(input("Enter your grade:"))
    students.append((name,grade))
print(students)

#step 2
grades=[grade for grade in students]
print(grades)

