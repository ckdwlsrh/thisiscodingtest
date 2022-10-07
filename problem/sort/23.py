
N = int(input())

students = []
for _ in range(N):
    name, ko, en, math = input().split()
    students.append([name,int(ko),int(en),int(math)])

students.sort(key=lambda k:(-k[1],k[2],-k[3],k[0]))

for student in students:
    print(student[0])