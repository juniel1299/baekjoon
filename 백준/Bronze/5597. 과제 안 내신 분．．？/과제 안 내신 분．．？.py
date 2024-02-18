student_list = [i for i in range(1,31)]

for _ in range (28):
    student = int(input())
    student_list.remove(student)

print(min(student_list))
print(max(student_list))

